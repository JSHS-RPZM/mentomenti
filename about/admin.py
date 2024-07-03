from django.contrib import admin

# Register your models here.
from about.models import ImageModel

class ImageModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )


admin.site.register(ImageModel, ImageModelAdmin)
