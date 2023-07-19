from django.forms import ModelForm
from django import forms
from Task.models import Addproduct, Addmove

class ProductForm(forms.ModelForm):
    class Meta:
        model = Addproduct
        fields = ('pname','name', 'place')

class MoveForm(forms.ModelForm):
    class Meta:
        model = Addmove
        fields = ('mpname','orgin','destiny','qty')