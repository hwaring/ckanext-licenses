from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-licenses',
    version=version,
    description="License Manager",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Hayden Waring',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.licenses'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        license_manager=ckanext.licenses.plugin:LicenseClass
    ''',
)
