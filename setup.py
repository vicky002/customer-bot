__author__ = 'vikesh'

# this file will be used during our launch
import os
import sys

# check if setuptool exists
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
	longdesc = open("README.md").read()
except:
	longdesc = ''

# Thanks to Kenneth Reitz, I stole the template for this : https://github.com/kennethreitz
setup(
    name='customer-bot',
    version='0.0.1',
    description='An Intelligent bot for online customer support system',
    long_description=longdesc,
    author='Vikesh Tiwari, Siddharth Shekhar and Shaquib Khan',
    author_email='tvicky002@gmail.com',
    url='https://github.com/vicky002/customer-bot',
    packages=packages,
    scripts= ['bin/customer-bot'],
    package_data = {'': ['LICENCE',], '':['']},
    include_package_data=True,
    install_requires=required,
    license='MIT',
    classifiers=(
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ),

)