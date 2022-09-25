from django.contrib import admin
from .models import Elements
from .models import Tags,purchases
# Register your models here.
admin.site.register(Elements)
admin.site.register(Tags)
admin.site.register(purchases)
