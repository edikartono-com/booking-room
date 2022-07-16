from calendar import HTMLCalendar
from datetime import datetime, timedelta
# from django.utils.timezone import datetime
from manager.models import AvailableRooms

class Calendar(HTMLCalendar):
    def __init__(self, request, year=None, month=None):
        self.request = request
        self.year = year
        self.month = month
        self.dat = datetime.today()
        super(Calendar, self).__init__()
    
    def link_cart(self, pid):
        """ membuat link tambah ke basket

        Args:
            pid: id dari room yang available
        
        Returns:
            link produk
        """
        from django.urls import reverse_lazy
        return reverse_lazy('manager:cart_add', kwargs={'product_id': pid})
    
    def formatday(self, day, events) -> str:
        """Menandai hari dengan room yang bisa di booking dan membuat form

        Args: 
            day: hari/tanggal dalam bulan tersebut
            events: room yang tersedia
        
        Returns:
            String
        """

        from django.utils.safestring import mark_safe
        from django.middleware.csrf import get_token
        
        token = get_token(self.request)
        events_per_day = events.filter(booking_date_slot__day=day)
        d = ''
        
        for event in events_per_day:
            d += mark_safe(
                f'''
                    <form method="post" action="{self.link_cart(event.id)}">
                    <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
                    <li>
                        <button type="submit" class="dropdown-item btn btn-primary">
                            <i class="fas fa-luggage-cart"></i> { event.type_available } 
                        </button>
                    </li>
                    </form>
                '''
            )
        
        if day != 0:
            if events_per_day:
                evn = f'''
                        <td>
                        <div class="date dropdown show">
                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">{day}</button>
                            
                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                <ul>{d}</ul>
                            </div>
                            
                        </div>
                        </td>
                        '''
                return evn
            else:
                evn = f'''
                        <td><span class="date btn btn-secondary">{day}</td>
                        '''
                return evn
        return "<td></td>"
    
    def formatweek(self, theweek, events):
        week = ''
        for day, weekday in theweek:
            week += self.formatday(day, events)
        return f'<tr>{week}</tr>'
    
    def formatmonth(self, withyear=True):
        events = AvailableRooms.objects.filter(
            booking_date_slot__year=self.year,
            booking_date_slot__month=self.month,
            booking_date_slot__gte=self.dat
        )

        cal = f"<table class='table'>\n"
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"

        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events)}\n"
        cal += f"</table>"
        return cal