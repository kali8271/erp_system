from django.contrib import admin
from .models import Fee, Payment, Scholarship, Fine

admin.site.register(Fee)
admin.site.register(Payment)
admin.site.register(Scholarship)
admin.site.register(Fine)
