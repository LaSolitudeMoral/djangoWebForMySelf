from django import forms
from .models import Category


# формы не связанные с моделью
class NewsForm(forms.Form):
    title = forms.CharField(max_length=150)
    content = forms.CharField()
    is_published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())