from django import forms
from .models import News, Category
from django.core.exceptions import ValidationError
import re


# формы связанные с моделью
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    # Validator for title textbox
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

# формы не связанные с моделью
# class NewsForm(forms.Form):
#    title = forms.CharField(max_length=150, label='Заголовок',
#                            widget=forms.TextInput(attrs={'class': 'form-control'}))
#    content = forms.CharField(label='Текст статьи', required=False,
#                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
#    is_published = forms.BooleanField(label='Опубликована ли статья?', initial=True, required=False)
#    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Без категории',
#                                     widget=forms.Select(attrs={'class': 'form-control'}))

