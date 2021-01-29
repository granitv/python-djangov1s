from django.contrib.auth.models import User
from django.db import models


class Cocktail(models.Model):
    title = models.CharField(
        max_length=200, default=None, blank=False, null=True
    )
    description = models.CharField(
        max_length=200, default=None, blank=False, null=True
    )
    content = models.TextField(default=None, blank=False, null=True)

    def detail(self):
        result = self.title or "? no title ?"
        all_tags = self.tags.all()
        if len(all_tags) > 0:
            result += "({})".format(", ".join([str(c.name) or '? no name ?' for c in all_tags]))
        return result

    def __str__(self):
        if self.title is not None:
            return self.title
        return "? no title"


class Tag(models.Model):
    name = models.CharField(
        max_length=200, default=None, blank=False, null=True
    )
    cocktails = models.ManyToManyField(Cocktail,
                                       related_name='tags'
                                       )

    def __str__(self):
        result = self.name or "? no name"
        result += "({})".format(", ".join([str(c) for c in self.cocktails.all()]))
        return result


class Ingredient(models.Model):
    name_singular = models.CharField(
        max_length=200, default=None, blank=False, null=True
    )
    name_plural = models.CharField(
        max_length=200, default=None, blank=False, null=True
    )

    def to_str(self, nb: float):
        return self.name_plural if nb > 1 else self.name_singular

    def __str__(self):
        result = self.name_singular or "? no singular"
        if self.name_plural:
            result = f"{result} / {self.name_plural}"
        return result


class Unit(models.Model):
    name = models.CharField(
        max_length=200, default=None, blank=False, null=True
    )

    def __str__(self):
        if self.name is not None:
            return self.name
        return "? no name"


class CocktailIngredientUnit(models.Model):
    cocktail = models.ForeignKey(
        Cocktail, on_delete=models.CASCADE,
        related_name='c_i_u_s'
    )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, blank=True, null=True
    )
    value = models.FloatField(default=1.0, blank=False, null=True)
    unit_is_displayed = models.BooleanField(
        default=True, blank=False, null=True
    )

    def __str__(self):
        result = f"{self.cocktail} / {self.value} "
        if self.unit_is_displayed:
            result += f"{self.unit} "
        result += f"{self.ingredient.to_str(self.value).lower()}"
        return result
