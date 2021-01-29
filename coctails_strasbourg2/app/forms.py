from django import forms
from django.contrib.auth.forms import AuthenticationForm

from app.models import Cocktail


class CocktailForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = ('title', 'description', 'content')

    title = forms.CharField(
        label="Titre", max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        label="Description", max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    content = forms.CharField(
        label="Contenu", max_length=2000,
        widget=forms.Textarea(attrs={"class": "form-control"})
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        if '<' in title:
            self.add_error(
                "title", "Only alphanum characters -or spaces) !"
                           )
        return title

    def clean(self):
        title = self.cleaned_data['title']
        description = self.cleaned_data['description']
        if title == description:
            self.add_error(
                None, "Title shoud be different from description!"
            )
        return self.cleaned_data
