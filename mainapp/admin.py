from django.contrib import admin
from .models import Catagory,Product,ChapaTransaction,Orders,OrderItems,News,CustomerProfile,SubCatagory
admin.site.register(CustomerProfile)
admin.site.register(Catagory)
admin.site.register(Product)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
admin.site.register(Orders, OrderAdmin)
admin.site.register(OrderItems)
admin.site.register(News)
admin.site.register(SubCatagory)
admin.site.register(ChapaTransaction)
# Register your models here.
