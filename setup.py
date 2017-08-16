#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
import sys, os
"""
python setup.py register sdist bdist_egg upload
python setup.py register sdist upload -r "https://test.pypi.org/legacy/"
pip install -i https://testpypi.python.org/simple/ defogging
"""

VERSION = '0.1.7'

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
	name='defogging',
    version=VERSION,
    description="Defogging based on Python",
    long_description=readme,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='python image defogging dehaze',
    author='scloudyy',
    author_email='onecloud.shen@gmail.com',
    url='https://github.com/scloudyy/Defogging',
    license='GPL',
    packages=['defogging', 'defogging/core', 'defogging/utils'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'numpy',
        'pillow'
    ],
    entry_points={
        'console_scripts':[
        'defogging = defogging:main'
        ]
    },
)
