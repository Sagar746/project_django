from django.shortcuts import render,reverse,get_object_or_404,get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book,Publication
from .forms import PublicationForm,BookForm
# Create your views here.

def home_view(request):
	# context={'name':'Smith','age':19,'address':'Kathmandu'}

	book = Book.objects.all()
	publication=get_list_or_404(Publication,active=True)
	return render(request,'home.html',{'booklist':book ,'publist':publication})


def add_publication(request):
	print(request.POST)
	form=PublicationForm(request.POST or None)
	if form.is_valid():
		# print(form.cleaned_data)
		# Publication.objects.create(**form.cleaned_data)
		form.save()				##for meta class
		return HttpResponseRedirect(reverse('app:home'))
	return render(request,'form.html',{'form':form,'model_name':'Publication'})



def add_book(request):
	print(request.POST)
	form=BookForm(request.POST or None)
	if form.is_valid():
		form.save()
		# form=BookForm()
		return HttpResponseRedirect(reverse('app:home'))
	return render(request,'form.html',{'form':form, 'model_name':'Book'})


def edit_book(request,book_id):
	# return HttpResponse('<p> +str(book_id)</p>')
	book=get_object_or_404(Book,pk=book_id)

	form=BookForm(request.POST or None,instance=book)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('app:home'))
	return render(request,'form.html',{'form':form,'model_name':'Book'})



def edit_publication(request,publication_id):
	publication=get_object_or_404(Publication, pk=publication_id)

	form=PublicationForm(request.POST or None,instance=publication)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('app:home'))
	return render(request,'form.html',{'form':form,'model_name':'Publication'})