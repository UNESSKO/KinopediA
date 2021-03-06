from modeltranslation.translator import register, TranslationOptions
from .models import Category, Persone, Movie, Genre, Shots


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Persone)
class PersoneTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'description', 'country')


@register(Shots)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')