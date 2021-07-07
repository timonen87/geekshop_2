from django import forms
from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm
from mainapp.models import Product, ProductCategory


class ShopUserRegisterForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'avatar', 'is_active', 'is_staff', 'is_delete')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if 'is_delete' in field_name or 'is_active' in field_name or 'is_staff' in field_name:
                field.widget.attrs['class'] = ''
            else:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''


class ProductEditForm(ShopUserEditForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if 'is_delete' in field_name:
                field.widget.attrs['class'] = ''
            else:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if 'is_delete' in field_name:
                field.widget.attrs['class'] = ''
            else:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''