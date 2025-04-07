from django import forms
from django.forms import widgets
from .models import CategoryModel, PostModel


class QuillWidget(widgets.Textarea):
    template_name = 'widgets/quill_widget.html'

class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=CategoryModel.objects.all(), empty_label='Кликните ;D' ,label='Категория')

    class Meta:
        model = PostModel
        fields = ['title', 'main_picture', 'content', 'category']
        widgets = {
            'content' : QuillWidget(),
        }