from django.contrib import admin
from babynames_app.models import FirstName, LastName, FullName, Country, Gender


class FirstNameAdmin(admin.ModelAdmin):
	exclude = ('rank',)
	list_display = ('firstName','gender',)

	
#class FirstNameAdmin(admin.TabularInline):
#	model = FirstName
#	exclude = ('rank',)
#	list_display = ('firstName','gender',)
#
#
#class FullNameAdmin(admin.ModelAdmin):
#	inlines = [
#			FirstNameAdmin,
#			]


admin.site.register(FirstName, FirstNameAdmin)
admin.site.register(FullName)#, FullNameAdmin)
admin.site.register(Country)
admin.site.register(Gender)
