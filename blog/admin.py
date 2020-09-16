# blog/admin.py
from adminsortable2.admin import SortableInlineAdminMixin
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
class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = ("id", "title", "category", "status", "post_date", "image")
    readonly_fields = ('image_preview',)
    fieldsets = (
        ('Параметры', {
            "classes": ("collapse"),
            "fields": (("category", "status"),)
        }),
        ("Пост", {
            "fields": (("title",), ("slug",),("image_preview","image"), "content",),

        }),)

    list_display_links = ("title",)
    search_fields = ("title", "category__title")
    list_editable = ("status",)

    inlines = [InlineEditor, PostImageAdmin, ]

    class Meta:
        model = Post

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Thumbnail Preview'
    image_preview.allow_tags = True


admin.site.site_title = "Liza Beta"
admin.site.site_header = "Liza Beta"
