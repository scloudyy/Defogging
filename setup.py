#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
import sys, os
"""
打包的用的setup必须引入
"""

VERSION = '0.1.0'

with open('README.md') as f:
    long_description = f.read()

setup(
	name='defogging', # 文件名
    version=VERSION, # 版本(每次更新上传Pypi需要修改)
    description="Defogging based on Python",
    long_description=long_description, # 放README.md文件,方便在Pypi页展示
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='python image defogging dehaze', # 关键字
    author='scloudyy', # 用户名
    author_email='onecloud.shen@gmail.com', # 邮箱
    url='http://www.scloudyy.com/', # github上的地址,别的地址也可以
    license='GPL', # 遵循的协议
    packages=['defogging'], # 发布的包名
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'numpy',
        'pillow'
    ], # 满足的依赖
    entry_points={
        'console_scripts':[
        'defogging = defogging.defogging:main'
        ]
    },
)
