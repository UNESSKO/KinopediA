from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import Category, Genre, Movie, Shots, Persone, Rating, Star, Reviews

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 0
    readonly_fields = ("name", "email", "movie", "parent")


class ShotsInLine(admin.TabularInline):
    model = Shots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [ShotsInLine, ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    form = MovieAdminForm
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("poster", ("get_image", "description"),)
        }),
        (None, {
            "fields": (("country", "year", "world_premiere"),)
        }),
        (None, {
            "fields": (("directors", "actors", "genres", "category"),)
        }),
        ("Money", {
            "classes": ("collapse",),
            "fields": (("budget", "fess_in_usa", "fess_in_world"),)
        }),
        (None, {
            "fields": (("url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="90" height="120"')

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей было обновлено"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей было обновлено"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Постер"


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "name", "parent", "email")
    readonly_fields = ("name", "email", "movie", "parent")


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    list_display = ("name", "url")


@admin.register(Persone)
class PersoneAdmin(TranslationAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "movie", "ip")


@admin.register(Shots)
class ShotsAdmin(TranslationAdmin):
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Genre)
# admin.site.register(Movie)
# admin.site.register(Shots)
# admin.site.register(Persone)
# admin.site.register(Rating)
admin.site.register(Star)
# admin.site.register(Reviews)

admin.site.site_title = "KinopediA"
admin.site.site_header = "KinopediA"
