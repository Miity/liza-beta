# blog/admin.py
from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Category, Post_Gallery, Inline_Editor



class PostImageAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Post_Gallery
    extra = 0

class InlineEditor(SortableInlineAdminMixin, admin.StackedInline):
    model = Inline_Editor
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ("id", "title", "slug")
    list_display_links = ("title",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = ("id", "title", "category", "status", "post_date", "image")

    fieldsets = (
        ('Параметры', {
            "classes": ("collapse"),
            "fields": (("category", "status"),)
        }),
        ("Пост", {
            "fields": (("title",), ("slug",),"image", "content",)
        }),)

    list_display_links = ("title",)
    search_fields = ("title", "category__title")
    list_editable = ("status",)

    inlines = [InlineEditor, PostImageAdmin, ]

    class Meta:
        model = Post

admin.site.site_title = "Liza Beta"
admin.site.site_header = "Liza Beta"
