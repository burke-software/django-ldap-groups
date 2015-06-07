#!/usr/bin/env python
from setuptools import setup

setup(name='django-ldap-groups-bsc',
      version='0.1.8',
      author='Peter Herndon',
      author_email='tpherndon@gmail.com',
      url='http://code.google.com/p/django-ldap-groups/',
      description='A Django app for authenticating and authorizing against LDAP',
      packages=['ldap_groups', 'ldap_groups.accounts'],
      package_data={'ldap_groups': ['templates/admin/ldap_groups/ldapgroup/*']},
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 3.4',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP',
          ]

      )
