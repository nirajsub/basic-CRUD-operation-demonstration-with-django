
from django.db.models import fields
from django.forms import ModelForm
from .models import*

class ProductForm(ModelForm):
    class Meta:
        model= product
        fields = '__all__'