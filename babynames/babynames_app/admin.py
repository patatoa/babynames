from django.contrib import admin
from babynames_app.models import FirstName, LastName, FullName,\
    Country, Gender, NameInfo


class LastNameAdmin(admin.TabularInline):
    model = LastName


class FirstNameInlineAdmin(admin.TabularInline):
    model = FullName.first


class NameInfoInline(admin.TabularInline):
    model = NameInfo


class FullNameInline(admin.TabularInline):
    model = FullName


class FirstNameAdmin(admin.ModelAdmin):
    inlines = [
        FullNameInline,
        NameInfoInline,
    ]


class FullNameAdmin(admin.ModelAdmin):
    inlines = [
        NameInfoInline,
        LastNameAdmin,
    ]
    exclude = ("rank",)
#class FullNameAdmin(admin.ModelAdmin):
#	inlines = [
#			FirstNameAdmin,
#			]


admin.site.register(FirstName, FirstNameAdmin)
admin.site.register(FullName)
admin.site.register(Country)
admin.site.register(Gender)
