from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery,Banner
import admin_thumbnails
from django.utils.html import format_html

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

class BannerImage(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html ("<img src='{}'width='40' style='border-radius:50px;'/>".format(object.photo.url))   
    thumbnail.short_description="photo"

    list_display=('thumbnail','created_date','Title')
    list_display_links=('thumbnail','created_date','Title')

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
admin.site.register(Banner,BannerImage)
