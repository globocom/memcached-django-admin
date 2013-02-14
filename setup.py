# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from memcached_django_admin import __version__ as Version

setup(
    name=u'memcached-django-admin',
    version=Version,
    description=u"Just a Simple Interface do Expire Memcached Keys",
    long_description=u"""Just a Simple Django Interface do Expire Memcached Keys""",
    keywords='django memcached admin',
    author=u'Victor Pantoja',
    author_email='victor.pantoja@gmail.com',
    url='https://github.com/globocom/memcached-django-admin',
    license='Apache License 2.0',
    classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers'],
    packages=find_packages(),
    package_dir={"memcached_django_admin": "memcached_django_admin"},
    include_package_data=True,

    tests_require=['nose==1.1.2'],
    install_requires=["django==1.4.1"],

)


