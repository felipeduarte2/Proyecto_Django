from django.contrib import admin
from myApp.models import Software

# Register your models here.
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('id','nivel', 'nombre', 'define')
    # ordering = ('nombre',)
    # ordering = ('-nivel','nombre')
    # search_fields = ('nombre','define')
    #list_display = ('id','nivel', 'nombre', 'define')
    #list_display_links = ('nombre',)
    #list_editable = ('nombre','define')
    #list_filter = ('nivel',)
    #list_per_page = 4
    #exclude = ('nivel',)
    
admin.site.register(Software,SoftwareAdmin)
admin.site.site_header = "Tecnológicco Nacional de Mexico"
admin.site.index_title = "Tecnológias Python"
admin.site.site_title = "TectNM"
