# Installation

This fork is not yet well tested. But for the brave just pip install `django-ldap-groups-bsc`

# Settings

- `LDAP_URL` Full url of the ldap server. Example `ldap://example.com:389`
- `LDAP_NT4_DOMAIN`
- `LDAP_BIND_USER`
- `LDAP_BIND_PASSWORD`
- `LDAP_SEARCH_DN`
- `LDAP_USE_CONSTANCE` Defaults to `False`. Used for admin user selectable settings

# LDAP settings in the database

Some uses cases merit storing settings that privileged users edit on the fly. 
This uses django-constance to achieve this. It also makes it possible to 
use with django-tenant-schemas when using the constance database backend.

1. Install django-constance
2. Set `LDAP_USE_CONSTANCE = True`
3. Add these to your `CONSTANCE_CONFIG` settings.
```
'LDAP_URL': ('', 'Ex: ldap://admin.example.com:389'),
'LDAP_NT4_DOMAIN': ('', 'Ex: ADMIN'),
'LDAP_BIND_USER': ('', 'Ex: ldap_user'),
'LDAP_BIND_PASSWORD': ('', 'Bind user\'s password'),
'LDAP_SEARCH_DN': ('', 'DC=admin,DC=example,DC=com'),
```
