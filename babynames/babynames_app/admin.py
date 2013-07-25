from django.contrib import admin
from babynames_app.models import FirstName, LastName, FullName, Country, Gender

class FirstNameAdmin(admin.ModelAdmin):
	exclude = ('rank',)
	#list_display = ('FirstName',)


class FullNameAdmin(admin.ModelAdmin):
	list_display = ('FullName')


class GenderAdmin(admin.ModelAdmin):
	list_display = ('Gender')

class CountryAdmin(admin.ModelAdmin):
	list_display = ('Country')


admin.site.register(FirstName, FirstNameAdmin)
admin.site.register(FullName)
admin.site.register(Country)
admin.site.register(Gender)
