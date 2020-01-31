from django import forms
from .models import Publication,Book

# class PublicationForm(forms.Form):
# 	name=forms.CharField()
# 	contact=forms.CharField()
# 	address=forms.CharField()


# class BookForm(forms.Form):
# 	name=forms.CharField()
# 	publication=forms.ModelChoiceField(queryset=Publication.objects.all())


class PublicationForm(forms.ModelForm):

	class Meta:
		model=Publication
		fields=('name','contact','address',)


class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		exclude=('created','modified',)			#### use exclude=('created','modified') not in use