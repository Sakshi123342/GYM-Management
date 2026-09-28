from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import MembershipPlan,Service,Trainer,ContactMessage

admin.site.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display=('name','price','duration','is_popular','created_at')
    list_filter=('is_popular',)

admin.site.register(Service)
class ServiceAdmin(admin.ModelAdmin):
     list_display = ('name', 'is_active')
     list_filter = ('is_active',)


admin.site.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display=('name','specialization','experience','is_active')
    list_filter=('is_active')
    # search_fields=('name','specialization')

admin.site.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    ordering = ('-created_at',)