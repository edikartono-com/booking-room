class PagePage:
    def __init__(self, queryset, request):
        self.queryset = queryset
        self.request = request

    def get_per_halaman(self):
        from django.core.paginator import Paginator
        paginator = Paginator(self.queryset, 10)
        page = self.request.GET.get('page')
        activities = paginator.get_page(page)
        return activities