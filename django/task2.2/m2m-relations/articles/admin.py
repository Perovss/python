from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = sum([1 for form in self.forms if form.cleaned_data.get('is_main')])
        if count > 1:
            raise ValidationError(f'Ошибка, основной раздел может быть только один!')
        elif count < 1:
            raise ValidationError(f'Ошибка, обязательно должен быть выбран основной раздел!')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image', ]
    list_filter = ['title', 'text', 'published_at', ]
    inlines = [RelationshipInline, ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]
    inlines = [RelationshipInline, ]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['is_main', 'article', 'tag', ]
    list_filter = ['is_main', 'article', 'tag', ]