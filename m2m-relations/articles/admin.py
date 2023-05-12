from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_uniq = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                is_main_uniq += 1
        if is_main_uniq > 1:
            raise ValidationError('Главный тег должен быть уникальным.')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    # list_display = ['name', 'is_main']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image', ]
    inlines = [
        ScopeInline,
    ]

