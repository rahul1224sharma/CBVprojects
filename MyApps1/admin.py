from django.contrib import admin
from MyApps1.models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','pages','price']

admin.site.register(Book,BookAdmin)


from MyApps1.models import Company,Employee
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location','ceo']

admin.site.register(Company,CompanyAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','name','salary','company']

admin.site.register(Employee,EmployeeAdmin)