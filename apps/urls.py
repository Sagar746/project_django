from django.urls import path
from .views import home_view,add_publication,add_book,edit_book,edit_publication

app_name='app'

urlpatterns=[
	path('home/',home_view, name='home'),
	path('addpublication/',add_publication,name='add_publication'),
	path('addbook/',add_book,name='add_book'),
	path('editbook/<int:book_id>/',edit_book,name='edit_book'),
	path('editpublication/<int:publication_id>/',edit_publication,name='edit_publication'),

]