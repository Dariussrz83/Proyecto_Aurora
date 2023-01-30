from django.contrib import admin

from cakes.models import Frozen_cakes, Birthday_cakes, Alfajores

@admin.register(Alfajores)
class AfajoresAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','stock')
    list_filter = ('stock',)
    search_fields = ('name',)
   
        
        
@admin.register(Frozen_cakes)
class Frozen_cakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','stock')
    list_filter = ('stock',)
    search_fields = ('name',)

@admin.register(Birthday_cakes)
class Birthday_cakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','stock')
    list_filter = ('stock',)
    search_fields = ('name',)
