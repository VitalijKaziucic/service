from django.contrib import admin
from .models import Paslauga, Uzsakymas, UzsakymoEilutes, Automobilis, AutomobilioModelis

# Register your models here.

class UzsakymoEilutesInline(admin.TabularInline):
    model = UzsakymoEilutes
    readonly_fields = ("id", )
    extra = 0

class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ("display_model", "order_date", "amount", "status")
    inlines = [UzsakymoEilutesInline]


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ("display_model", "display_owner", "display_plate", "display_vin")
    list_filter = ("client", "vehicle_id__model")
    search_fields = ("plate", "vin")


    # fieldsets = (
    #     ("General", {"fields": ("id", "vehicle_id",)}),
    #     ("Availability", {"fields": ("vin", "client")})
    # )


admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(AutomobilioModelis)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(UzsakymoEilutes)