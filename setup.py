from __future__ import unicode_literals

import re


from setuptools import find_packages, setup


def read_file(filename):
    with open(filename) as fh:
        return fh.read()


def get_version(filename):
    init_py = read_file(filename)
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", init_py))
    return metadata['version']


setup(
    name='pysiriusxm',
    version=get_version('siriusxm/__init__.py'),
    url='http://siriusxm.mopidy.com/',
    license='Apache License, Version 2.0',
    author='Dallas Brown',
    author_email='dbrown@port21.com',
    description='Python API wrapper for Sirius XM internet radio',
    long_description=read_file('README.rst'),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
    ],
)
