from setuptools import setup

setup(
    name='tumblrout',
    version='1.0',
    packages=[],
    include_package_data=True,
    scripts=['bin/tumblrout'],

    requires=['termtool', 'httplib2', 'oauth2'],
    install_requires=['termtool', 'httplib2', 'oauth2'],
)
