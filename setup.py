from setuptools import setup, find_packages
import os

LONG_DESCRIPTION = """
============
Django Forum
============

This is a very basic forum application that can plug into any
existing Django installation and use its existing templates,
users, and admin interface.
"""

setup(
    name='django-forum',
    version=version,
    description="django-forum",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='forum,django',
    author='Andrew Choi',
    author_email='andrew@choi.com',
    url='https://github.com/andrewychoi/django-forum',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)

