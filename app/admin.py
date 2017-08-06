from django.contrib import admin
from app.models import State, StateCapital, City



#class StateCapitalInline(admin.TabularInline):
    #model = StateCapital.state.through


class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation",)
    search_fields = ["name"]
    #inlines = [StateCapitalInline]



class StateCapitalAdmin(admin.ModelAdmin):
    list_display = ("name", "population")
    search_fields = ["name"]

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "county", "state")
    search_fields = ['name']



# Register your models here.

admin.site.register(State, StateAdmin)
admin.site.register(StateCapital, StateCapitalAdmin)
admin.site.register(City, CityAdmin)


