from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import School
from .models import Diferentials
from .models import Visitation
from .models import Footer

admin.site.unregister(User)
admin.site.unregister(Group)



class SchoolAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("main_website/_css/main.css", )
        }
        js = ("main_website/_js/tiny_edit_form.js",)

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False    

class DiferentialsAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("main_website/_css/main.css", )
        }
        js = ("main_website/_js/tiny_edit_form.js",)
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False     

class VisitationAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("main_website/_css/main.css", )
        }
        js = ("main_website/_js/tiny_edit_form.js",)
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False     

class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False  
    def has_delete_permission(self, request, obj=None):
        return False                   

admin.site.register(School, SchoolAdmin)
admin.site.register(Diferentials, DiferentialsAdmin)
admin.site.register(Visitation, VisitationAdmin)
admin.site.register(Footer, FooterAdmin)

