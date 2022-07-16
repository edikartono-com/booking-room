from datetime import date, datetime, timedelta
from django.utils.safestring import mark_safe
from django.views.generic import DetailView, ListView, TemplateView

from dashboard.models import (
    AboutUs, Blog, BlogCategories,
    ContactUs, Facilities, Services
)
from manager.models import AvailableRooms, RoomTypes

class HomePage(TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        room_type = RoomTypes.objects.defer().all()[:3]
        context['room_type'] = room_type

        facility = Facilities.objects.all()
        context['facility'] = facility

        blog = Blog.objects.all()[:3]
        context['our_blog'] = blog
        return context

class RoomAvailableView(TemplateView):
    template_name = 'dashboard/cart/check_availability.html'

    def get_date(self, req_day: date) -> date:
        if req_day:
            year, month = (int(x) for x in req_day.split('-'))
            return date(year, month, day=1)
        return datetime.today()
    
    def next_month(self, obj):
        import calendar
        day_in_month = calendar.monthrange(obj.year, obj.month)[1]
        last = obj.replace(day=day_in_month)
        next_month = last + timedelta(days=1)
        month = str(next_month.year) + '-' + str(next_month.month)
        return month
    
    def prev_month(self, obj):
        first = obj.replace(day=1)
        prev_month = first - timedelta(days=1)
        month = str(prev_month.year) + '-' + str(prev_month.month)
        return month

    def get_context_data(self, *args, **kwargs):
        from manager.calendar import Calendar
        
        d = self.get_date(self.request.GET.get('month', None))
        cal = Calendar(self.request, d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)

        context = super(RoomAvailableView, self).get_context_data(*args, **kwargs)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = self.prev_month(d)
        context['next_month'] = self.next_month(d)

        return context

class CategoryList(ListView):
    template_name = 'dashboard/blog/categories.html'
    paginate_by = 8
    
    def get_queryset(self):
        self.slug = self.kwargs['slug']
        self.queryset = Blog.objects.filter(
            category=self.slug
        )
        return super().get_queryset()
    
    def get_context_data(self, *args, **kwargs):
        context = super(CategoryList, self).get_context_data(*args, **kwargs)
        context['judul'] = "Read Our Blog Category {}".format(self.slug)
        context['for_empty'] = "empty"
        return context

class BlogList(ListView):
    template_name = 'dashboard/blog/categories.html'
    model = Blog
    paginate_by = 8
    extra_context: dict = {
        "judul": "Read Our Blog",
        "for_empty": "no post yet"
    }

class BlogDetail(DetailView):
    template_name = 'dashboard/blog/blog_detail.html'
    model = Blog

    def get_context_data(self, *args, **kwargs):
        from random import sample
        context = super(BlogDetail, self).get_context_data(*args, **kwargs)
        related = self.model.objects.filter(category=self.kwargs['cat']).exclude(slug=self.kwargs['slug'])
        rand_related = sample(list(related), 3)
        context['related'] = rand_related
        return context

class BlogSearch(ListView):
    template_name = 'dashboard/blog/categories.html'
    paginate_by = 8
    
    def get_queryset(self):
        from django.db.models import Q
        self.q = self.request.GET.get('q')
        self.queryset = Blog.objects.defer().filter(
            Q(title__icontains=self.q) | Q(body__icontains=self.q)
        )
        return super().get_queryset()
    
    def get_context_data(self, *args, **kwargs):
        context = super(BlogSearch, self).get_context_data(*args, **kwargs)
        context['judul'] = "Hasil pencarian : {}".format(self.q)
        context['for_empty'] = "{} tidak ditemukan".format(self.q)
        return context

class ServicesList(ListView):
    model = Services
    template_name: str = 'dashboard/blog/services.html'
    paginate_by: int = 6
    extra_context: dict = {
        "judul": "We Offer Services"
    }