from django.contrib import admin
from babynames_app.models import FirstName, LastName, FullName,\
    Country, Gender, NameInfo


class LastNameAdmin(admin.TabularInline):
    model = LastName


class FirstNameAdmin(admin.TabularInline):
    model = FirstName


class NameAdmin(admin.TabularInline):
    model = NameInfo
    inlines = [
        FirstNameAdmin,
    ]


class FullNameAdmin(admin.ModelAdmin):
    inlines = [
        NameAdmin,
        LastNameAdmin,
    ]
    exclude = ("rank",)
#class FullNameAdmin(admin.ModelAdmin):
#	inlines = [
#			FirstNameAdmin,
#			]


admin.site.register(FirstName)
admin.site.register(FullName, FullNameAdmin)
admin.site.register(Country)
admin.site.register(Gender)
