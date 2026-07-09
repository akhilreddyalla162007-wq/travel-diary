from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),

    path('home/', views.home, name='home'),

    path('login/', views.login_page, name='login'),

    path('register/', views.register_page, name='register'),

    path('logout/', views.logout_page, name='logout'),

    path('add-trip/', views.add_trip, name='add_trip'),

    path('explore/', views.explore, name='explore'),

    path('my_trips/', views.my_trips, name='my_trips'),
    
    path('trip/<int:id>/', views.trip_details, name='trip_details'),

    path('edit-trip/<int:id>/', views.edit_trip, name='edit_trip'),

    path('delete-trip/<int:id>/', views.delete_trip, name='delete_trip'),

    path('trip/<int:id>/', views.trip_details, name='trip_details'),

    path('view-trip/<int:id>/',views.view_trip,name='view_trip'),
    

]