from django.contrib import admin
from babynames.babynames_app.models import FirstName, LastName

class FirstAdmin(admin.ModelAdmin):
	pass
admin.site.register(FirstName, FirstAdmin)


class LastAdmin(admin.ModelAdmin):
	pass
admin.site.register(LastName, LastAdmin)
