from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import CustomUser, Expense, Group, Settlement
from .forms import CustomUserCreationForm,CustomUserChangeForm


# Register Expense Model

# class ExpenseAdmin(admin.ModelAdmin):
#     list_display = ('', 'amount', 'group', 'created_at')
#     list_filter = ('group',)
#     search_fields = ('name',)


# Register Group Model

# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_by', 'created_at')
#     search_fields = ('name',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'group', 'created_at')
    list_filter = ('group',)
    search_fields = ('description',)  # Update this line if needed
    
    
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'get_created_by', 'created_at')  # Update this line
    search_fields = ('name',)  # Update this line

    def get_created_by(self, obj):
        return obj.created_by.username

    get_created_by.short_description = 'Created By'
# Register Settlement Model
@admin.register(Settlement)
class SettlementAdmin(admin.ModelAdmin):
    list_display = ('expense_id','payer', 'receiver', 'amount', 'created_at')
    list_filter = ('payer', 'receiver')
    search_fields = ('payer__username', 'receiver__username')


# Customize UserAdmin for Custom User Model
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
        ),
    )


# Register Custom User Model
admin.site.register(CustomUser, CustomUserAdmin)

# # Unregister the default Group model
# admin.site.unregister(Group)
