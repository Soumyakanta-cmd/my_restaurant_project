from django import forms
from .models import ItemList,Items,AboutUs
class ItemListForm(forms.ModelForm):
    class Meta:
        model=ItemList
        fields=['Category_name']

class AddItemForm(forms.ModelForm):
    class Meta:
        model=Items
        fields='__all__'

class EditAbout(forms.ModelForm):
                class Meta:
                    model=AboutUs
                    fields=['Description']