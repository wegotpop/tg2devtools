# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os

test_requirements = ['coverage',
                    'nose',
                    'repoze.tm2 >= 1.0a5',
                    'TurboKid >= 1.0.4',
                    'TurboJson >= 1.2.1',
                    'zope.sqlalchemy >= 0.4',
                    'SQLAlchemy >= 0.5',
                    'repoze.what-quickstart >= 1.0.3',
                    'Babel >=0.9.4',
                    'tgext.admin>=0.3.9',
                    'SQLAlchemy >= 0.5',
                    'repoze.what-quickstart >= 1.0.6',
                    'repoze.who==1.0.18'
                    ]

install_requirements = [
                        'TurboGears2 >= 2.2a0',
                        ]

setup(
    name='tg.devtools',
    version="2.2a0",
    description="",
    long_description="""""",
    classifiers=[],
    keywords='turbogears',
    author="TurboGears Team 2008",
    author_email="turbogears@groups.google.com",
    url="www.turbogears.org",
    license="MIT",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires = install_requirements,
    entry_points='''
        [paste.global_paster_command]
        quickstart = devtools.commands.quickstart:QuickstartCommand
        [turbogears2.command]
        quickstart = devtools.commands.quickstart:QuickstartCommand
        [paste.paster_create_template]
        turbogears2=devtools.pastetemplate:TurboGearsTemplate
        tgext=devtools.pastetemplate:TurboGearsExtTemplate
        mongo=devtools.pastetemplate:MongoTemplate
        [turbogears2.template]
        turbogears2=devtools.pastetemplate:TurboGearsTemplate
    ''',
    test_suite='nose.collector',
    tests_require = test_requirements,
)
