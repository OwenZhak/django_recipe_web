from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('recipe_tittle', 'recipe', 'category', 'image')

        widgets = {
            'recipe_tittle': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('recipe_tittle', 'recipe', 'category')

        widgets = {
            'recipe_tittle': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }