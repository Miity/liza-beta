# blog/admin.py
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Category, Post_Gallery, Inline_Editor


class PostImageAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = Post_Gallery
    extra = 0
    readonly_fields = ('image_preview',)
    fields = ("image_preview", "image")
    classes = ['collapse']

    def image_preview(self, obj):
        return obj.image_preview

class InlineEditor(SortableInlineAdminMixin, admin.StackedInline):
    model = Inline_Editor
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ("id", "title", "slug")
    list_display_links = ("title",)

@admin.register(Post)
class PostAdmin(SortableAdminMixin, admin.ModelAdmin):
    save_on_top = True
    save_as = True

    readonly_fields = ('image_preview',)

    list_display = [
                    "title",
                    "category",
                    "status",
                    "post_date",
                    "my_order",
                    "image_preview",
                    ]
    list_editable = ("status",)
    list_display_links = ("title",)

    fieldsets = (
        ('Параметры', {
            "classes": ("collapse"),
            "fields": (("category", "status"),)
        }),
        ("Пост", {
            "fields": (("title",), ("slug",),("image_preview","image"), "content",),

        }),)

    search_fields = ("title", "category__title")
    inlines = [InlineEditor, PostImageAdmin, ]
    class Meta:
        model = Post

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Thumbnail Preview'
    image_preview.allow_tags = True

admin.site.site_title = "Liza Beta"
admin.site.site_header = "Liza Beta"
