#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'requests>=2.28',
    'colorama>=0.4',
]

test_requirements = ['pytest>=3', ]

setup(
    author="Andrew Lowe",
    author_email='andrew@lostways.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="CLI tool to ping websites and return their HTTP code.",
    entry_points={
        'console_scripts': [
            'uptimer=uptimer_cli.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='uptimer_cli',
    name='uptimer_cli',
    packages=find_packages(include=['uptimer_cli', 'uptimer_cli.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lostways/uptimer_cli',
    version='0.1.0',
    zip_safe=False,
)
