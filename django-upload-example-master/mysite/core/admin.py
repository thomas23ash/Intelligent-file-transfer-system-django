from django.contrib import admin

# Register your models here.
from mysite.core.models import Book
from account.models import registermodel
admin.site.register(Book)
admin.site.register(registermodel)