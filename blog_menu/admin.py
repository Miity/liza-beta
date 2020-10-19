from django.contrib import admin
from .models import Menu
# Register your models here.

@admin.register(Menu)
class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True

    list_display = ("title", "url")
    list_editable = ("url",)

    fieldsets = (
        ('Параметры', {
            "classes": ("collapse"),
            "fields": (("title", ),("url",),("status",))
        }),
    )