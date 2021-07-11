from django.contrib import admin

# Register your models here.
from meetup.models import Files, ResultML


class FilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ResultMLAdmin(admin.ModelAdmin):
    list_display = ('ip_src', 'port_src', 'ip_des', 'port_des', 'classification')
    list_filter = ('classification',)



admin.site.register(Files, FilesAdmin)
admin.site.register(ResultML, ResultMLAdmin)

