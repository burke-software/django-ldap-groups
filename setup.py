from setuptools import setup, find_packages

setup(name='django-ldap-groups-bsc',
      version='0.1.8.4',
      author='Peter Herndon',
      author_email='tpherndon@gmail.com',
      url='http://code.google.com/p/django-ldap-groups/',
      description='A Django app for authenticating and authorizing against LDAP',
      packages=find_packages(),
      include_package_data=True,
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
