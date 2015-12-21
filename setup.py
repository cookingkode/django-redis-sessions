from setuptools import setup
import os
from cluster_redis_sessions import __version__

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

packages = ['cluster_redis_sessions']


setup(
    name='django-redis-sessions',
    version=__version__,
    description= "Cluster Redis Session Backend For Django",
    long_description=read("README.rst"),
    keywords='django, sessions,',
    author='Jyotiswarup Raiturkar',
    author_email='jyotisr5@gmail.com',
    url='http://github.com/cookingkode/django-redis-sessions',
    license='BSD',
    packages=packages,
    zip_safe=False,
    install_requires=['redis>=3.0'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
