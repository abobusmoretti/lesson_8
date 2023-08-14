from django.contrib import admin
from .models import Advertisements

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'tittle', 'description', 'price', 'auction', 'created_date', 'updated_date']
    list_filter = ['auction', 'updeted_at']

    actions = ['make_auction_as_false', 'make_auction_as_true']

    @admin.action(description = 'Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description = 'Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction = True)

    fieldsets = (
        ('Общее', {
            'fields' : ('tittle', 'description'),
        }),
        ('Финансы', {
            'fields' : ('price', 'auction'),
            'classes' : ['collapse']
        })
    )

admin.site.register(Advertisements, AdvertisementsAdmin)

# Register your models here.
