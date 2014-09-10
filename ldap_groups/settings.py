from django.conf import settings


# Ugly code is for legacy settings. We now prefer LDAP_ is always used.
LDAP_URL = getattr(settings, 'LDAP_URL', None)
LDAP_NT4_DOMAIN = getattr(settings, 'LDAP_NT4_DOMAIN', None)
if LDAP_NT4_DOMAIN == None:
    LDAP_NT4_DOMAIN = getattr(settings, 'NT4_DOMAIN', None)
LDAP_BIND_USER = getattr(settings, 'LDAP_BIND_USER', None)
if LDAP_BIND_USER == None:
    LDAP_BIND_USER = getattr(settings, 'BIND_USER', None)
LDAP_BIND_PASSWORD = getattr(settings, 'LDAP_BIND_PASSWORD', None)
if LDAP_BIND_PASSWORD == None:
    LDAP_BIND_PASSWORD = getattr(settings, 'BIND_PASSWORD', None)
LDAP_SEARCH_DN = getattr(settings, 'LDAP_SEARCH_DN', None)
if LDAP_SEARCH_DN == None:
    LDAP_SEARCH_DN = getattr(settings, 'SEARCH_DN', None)


# Use constance settings is available
# But fall back to settings.py
if getattr(settings, 'LDAP_USE_CONSTANCE', False) == True:
    from constance import config
    LDAP_URL = getattr(config, 'LDAP_URL', LDAP_URL)
    LDAP_NT4_DOMAIN = getattr(config, 'LDAP_NT4_DOMAIN', LDAP_NT4_DOMAIN)
    LDAP_BIND_USER = getattr(config, 'LDAP_BIND_USER', LDAP_BIND_USER)
    LDAP_BIND_PASSWORD = getattr(config, 'LDAP_BIND_PASSWORD', LDAP_BIND_PASSWORD)
    LDAP_SEARCH_DN = getattr(config, 'LDAP_SEARCH_DN', LDAP_SEARCH_DN)
