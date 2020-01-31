from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
	path('login/',views.CustomLogin.as_view(),name='login'),
	path('signup/',views.SignupView.as_view(),name='signup'),
]