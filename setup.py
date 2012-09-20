from setuptools import setup

setup(
    name='twitterout',
    version='1.0',
    packages=[],
    include_package_data=True,
    scripts=['bin/twitterout'],

    requires=['termtool', 'httplib2', 'oauth2', 'progressbar', 'PrettyTable'],
    install_requires=['termtool', 'httplib2', 'oauth2', 'progressbar', 'PrettyTable'],
)
