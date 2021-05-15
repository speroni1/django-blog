from django.contrib import admin
from polling.models import Poll #pylance doesn't like this but it's correct

# Register your models here.

admin.site.register(Poll)