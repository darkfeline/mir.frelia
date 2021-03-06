#!/usr/bin/env python3

from setuptools import setup

setup(
    name='mir.frelia',
    version='0.1.0',
    description='Static website generator library.',
    long_description='',
    keywords='',
    url='https://github.com/darkfeline/mir.frelia',
    author='Allen Li',
    author_email='darkfeline@felesatra.moe',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ],

    packages=['mir.frelia'],
    install_requires=[
        'mir.monads==0.3.0',
        'PyYAML>=3.12,<4.0',
    ],
)
