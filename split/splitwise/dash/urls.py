
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dash/', views.dashboard, name='dashboard'),
    path('dash/<int:group_id>/', views.dashboard, name='dashboard_with_group'),
    
    path('create-expense/', views.create_expense, name='create_expense'),
    path('create_group/', views.create_group, name='create_group'),
    path('add_group_member/<int:group_id>/', views.add_group_member, name='add_group_member'),
    # path('add_group_member/<int:group_id>/', views.add_group_member, name='add_group_member'),


    
    path('group_details/<int:group_id>/', views.group_details, name='group_details'),

  
    path('settle_expense/<int:expense_id>/', views.settle_expense, name='settle_expense'),

    
] 