import ldap
import ldap.filter
from django.conf import settings

import simplejson as json

from django.http import HttpResponse, HttpResponseNotAllowed



LDAP_URL = getattr(settings, 'LDAP_URL', None)
BIND_USER = getattr(settings, 'BIND_USER', None)
NT4_DOMAIN = getattr(settings, 'NT4_DOMAIN', None)
BIND_USER = getattr(settings, 'BIND_USER', None)
BIND_PASSWORD = getattr(settings, 'BIND_PASSWORD', None)
SEARCH_DN = getattr(settings, 'SEARCH_DN', None)
# Use constance settings is available
# But fall back to settings.py
if getattr(settings, 'LDAP_USE_CONSTANCE', False) == True:
    from constance import config
    LDAP_URL = getattr(config, 'LDAP_URL', LDAP_URL)
    BIND_USER = getattr(config, 'BIND_USER', BIND_USER)
    NT4_DOMAIN = getattr(config, 'NT4_DOMAIN', NT4_DOMAIN)
    BIND_USER = getattr(config, 'BIND_USER', BIND_USER)
    BIND_PASSWORD = getattr(config, 'BIND_PASSWORD', BIND_PASSWORD)
    SEARCH_DN = getattr(config, 'SEARCH_DN', SEARCH_DN)

class LDAPSearchResult(object):
    """
    Convenience bag class to help organize the results of an LDAP search.
    """
    def __init__(self, search_result):
        self.dn = search_result[0]
        self.cn = search_result[1]['cn'][0]

def search(canonical_name):
    """
    Searches the LDAP server for all Organizational Units (OUs) whose Canonical
    Name (CN) contains the text argument canonical_name passed into the
    function.
    """
    ldap.set_option(ldap.OPT_REFERRALS,0)
    l = ldap.initialize(LDAP_URL)
    l.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
    binddn = ''
    try:
        binddn = "%s@%s" % (BIND_USER, NT4_DOMAIN)
    except AttributeError:
        binddn = BIND_USER
    l.simple_bind_s(binddn, BIND_PASSWORD)
    base = SEARCH_DN
    scope = ldap.SCOPE_SUBTREE
    retrieve_attributes = ['cn']
    
    filtered_name = ldap.filter.escape_filter_chars(canonical_name)
    filter = 'cn=*%s*' % filtered_name
    
    results = l.search_s(base, scope, filter, retrieve_attributes)
    
    #result_objects = [LDAPSearchResult(result) for result in results]
    result_objects = []
    for result in results:
        if result[0]:
            result_objects.append(LDAPSearchResult(result))
    return result_objects

def ldap_search(request):
    """
    This view provides a JSON response of the Distinguished Names (DNs) returned
    by searching the LDAP server for OU name fragments.  One can search for e.g.
    'django' and retrieve all DNs with 'django' in the Canonical Name (CN).
    """
    if request.method != 'POST':
        return HttpResponseNotAllowed('POST')
    req_cn = None
    if 'req_cn' in request.POST:
        req_cn = request.POST['req_cn']
        results = search(req_cn)
        res_json = json.dumps([res.dn for res in results], ensure_ascii=False)
        
        return HttpResponse(res_json, mimetype='application/json')
