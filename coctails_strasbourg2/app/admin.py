from django.contrib import admin

from app.models import Cocktail, Ingredient, Unit, CocktailIngredientUnit, Tag


class CocktailIngredientUnitInlineAdmin(admin.TabularInline):
    model = CocktailIngredientUnit
    extra = 0


class TagsInlineAdmin(admin.TabularInline):
    model = Tag.cocktails.through
    extra = 0


class CocktailAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    inlines = (CocktailIngredientUnitInlineAdmin, TagsInlineAdmin)


class IngredientAdmin(admin.ModelAdmin):
    search_fields = ("name_singular", "name_plural")


class CocktailIngredientUnitAdmin(admin.ModelAdmin):
    autocomplete_fields = ("cocktail", "ingredient")


admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Unit)
admin.site.register(Tag)
admin.site.register(CocktailIngredientUnit, CocktailIngredientUnitAdmin)
