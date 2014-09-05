from django.contrib import admin
from ldap_groups.models import LDAPGroup
from ldap_groups.views import ldap_search
from django.conf.urls import *

class LDAPGroupAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(LDAPGroupAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^ldap_search/$', self.admin_site.admin_view(ldap_search)),
        )
        
        return my_urls + urls

admin.site.register(LDAPGroup, LDAPGroupAdmin)
