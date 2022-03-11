import re

from setuptools import setup, find_packages


def get_long_description():
    with open('README.md') as f:
        return re.sub('!\[(.*?)\]\(docs/(.*?)\)',
                      r'![\1](https://github.com/leo-schick/mara-acl-msal/raw/master/docs/\2)', f.read())

setup(
    name='mara-acl-msal',
    version='1.0.0',

    description='ACL implementation for Mara via Microsoft Authentication Library',

    long_description=get_long_description(),
    long_description_content_type='text/markdown',

    url='https://github.com/leo-schick/mara-acl-msal',

    python_requires='>=3.6',

    install_requires=[
        'mara-page>=1.4.0',
        'mara-acl>=2.0.0',
        'msal>=1.17.0'
    ],

    setup_requires=['setuptools_scm'],
    include_package_data=True,

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={}
)