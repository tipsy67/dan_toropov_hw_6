from django import forms
from django.db.models import Q
from django.core.exceptions import ValidationError
from catalog.models import ProductVersion, Product, Category


stop_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

class ProductForm(forms.ModelForm):
    # name = forms.CharField(max_length=100, label='Наименование')
    # description = forms.CharField(widget=forms.Textarea(), required=False, label='Описание')
    # price = forms.DecimalField(max_digits=15, decimal_places=2, label='Цена')
    # image = forms.ImageField(required=False, label='Изображение')
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
    #                                   empty_label='Категория не выбрана', required=False)
    class Meta:
        model = Product
        fields = '__all__'

    @staticmethod
    def verify_stop_words(text: str):
        for word in stop_words:
            if word in text.lower():
                raise forms.ValidationError(f'Вы используете запрещенное слово {word}')


    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.verify_stop_words(name)

        return name


    def clean_description(self):
        desc = self.cleaned_data.get('description')
        self.verify_stop_words(desc)

        return desc


class ProductVersionForm(forms.ModelForm):

    class Meta:
        model = ProductVersion
        fields = '__all__'

    def clean_is_active(self):
        is_active = self.cleaned_data['is_active']
        if is_active:
            obj = self.cleaned_data['product']
            flag = obj.versions.filter(Q(is_active=True) & ~Q(pk=self.instance.id)).exists()
            if flag:
                raise ValidationError('Уже есть активная версия для этого продукта')

        return is_active


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

