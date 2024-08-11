from django import forms

from catalog.models import Category


class AddProduct(forms.Form):
    name = forms.CharField(max_length=100, label='Наименование')
    description = forms.CharField(widget=forms.Textarea(), required=False, label='Описание')
    price = forms.DecimalField(max_digits=15, decimal_places=2, label='Цена')
    image = forms.ImageField(required=False, label='Изображение')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      empty_label='Категория не выбрана', required=False)
