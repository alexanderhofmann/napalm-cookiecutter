"""setup.py file."""

import uuid

from setuptools import setup, find_packages
from pip.req import parse_requirements

__author__ = '{{cookiecutter.author}} <{{cookiecutter.author_email}}>'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="{{cookiecutter.package_name}}",
    version="{{cookiecutter.version}}",
    packages=find_packages(),
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    description="{{cookiecutter.short_description}}",
    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/{{cookiecutter.github_owner}}/{{cookiecutter.repo_name}}",
    include_package_data=True,
    install_requires=reqs,
)
