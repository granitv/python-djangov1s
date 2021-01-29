from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from app.forms import CocktailForm
from app.models import Cocktail


class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result["last_name"] = "Vrajolli"
        return result


class CocktailListView(generic.ListView):
    template_name = "cocktail_list.html"
    model = Cocktail

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        result['content_title'] = _("Cocktails List")
        return result


class CocktailDetailView(generic.DetailView):
    template_name = "cocktail_detail.html"
    model = Cocktail


class CocktailSearchListView(generic.ListView):
    template_name = "cocktail_list.html"
    model = Cocktail

    def get_queryset(self):
        name = self.kwargs['name']
        return Cocktail.objects.filter(title__icontains=name)

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        name = self.kwargs['name']
        result['title'] = f"Recherche > {name}"
        result['content_title'] = f"Résultat de la recherche : '{name}'"
        return result


class CocktailSearchByIngredientListView(generic.ListView):
    template_name = "cocktail_list.html"
    model = Cocktail

    def get_queryset(self):
        name = self.kwargs['name']
        return Cocktail.objects.filter(
            Q(c_i_u_s__ingredient__name_singular__icontains=name) |
            Q(c_i_u_s__ingredient__name_plural__icontains=name)
        ).distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        name = self.kwargs['name']
        result['title'] = f"Recherche par ingrédient > {name}"
        result['content_title'] = f"Cocktails dont l'un des ingrédient " \
                                  f"contient : '{name}'"
        return result


class MyLoginView(LoginView):
    def get_success_url(self):
        messages.success(self.request, _("Welcome back!"))
        return super().get_success_url()
    template_name = "login.html"


class CocktailCreateView(LoginRequiredMixin, generic.FormView):
    template_name = "cocktail_create.html"
    form_class = CocktailForm
    success_url = reverse_lazy("cocktails_list")

    def form_valid(self, form):
        result = super().form_valid(form)
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        content = form.cleaned_data["content"]
        Cocktail.objects.create(title=title, description=description,
                                content=content
                                )
        return result


class CocktailUpdateView(generic.UpdateView):
    template_name = "cocktail_create.html"
    model = Cocktail
    form_class = CocktailForm
    success_url = reverse_lazy("cocktails_list")

