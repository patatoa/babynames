from django.contrib import admin
from babynames_app.models import FirstName, LastName, FullName, Country, Gender


class Choice(admin.ModelAdmin):
	exclude = ('rank',)


class FirstNameInlines(admin.StackedInline):
	model= FirstName 
	extra = 50


class FullNameAdmin(admin.ModelAdmin):
	inlines = [FirstNameInlines]


admin.site.register(FirstName, Choice)
admin.site.register(FullName, FullNameAdmin)
admin.site.register(Country)
admin.site.register(Gender)
