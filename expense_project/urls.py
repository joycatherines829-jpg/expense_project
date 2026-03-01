from django.contrib import admin
from django.urls import path
from tracker.views import home, delete_expense, edit_expense

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('delete/<int:id>/', delete_expense, name='delete'),
    path('edit/<int:id>/', edit_expense, name='edit'),
]