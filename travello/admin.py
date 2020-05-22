from django.contrib import admin
from travello.models import contact,passhash,subscribe,bookings,Destination

# Register your models here.
admin.site.register(contact)
admin.site.register(passhash)
admin.site.register(subscribe)
admin.site.register(bookings)
admin.site.register(Destination)


