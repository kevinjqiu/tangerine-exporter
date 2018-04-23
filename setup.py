import setuptools
import json


def get_install_requires():
    with open('Pipfile.lock') as f:
        piplock = json.load(f)
    return [
        '{}{}'.format(dep, details['version'])
        for dep, details in piplock['default'].items()
    ]


setuptools.setup(
    name="tangerine_exporter",
    version=open('tangerine_exporter/VERSION').read(),
    url="https://github.com/kevinjqiu/tangerine-exporter",

    author="Kevin J. Qiu",
    author_email="kevin@idempotent.ca",

    description="A Prometheus exporter for metrics of your Tangerine bank accounts.",
    long_description=open('README.md').read(),

    include_package_data=True,

    packages=['tangerine_exporter'],

    install_requires=get_install_requires(),

    entry_points={
        'console_scripts': [
            'tangerine-exporter=tangerine_exporter.main:main'
        ]
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
