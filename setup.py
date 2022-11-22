from setuptools import find_packages, setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lazy-sqlalchemy',
    version='1.2.0',
    description='A library to wrap sqlalchemy for lazy load of database.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/masamitsu-murase/lazy-sqlalchemy',
    author='Masamitsu MURASE',
    author_email='masamitsu.murase@gmail.com',
    license='MIT',
    keywords='sqlalchemy',
    packages=find_packages("src"),
    package_dir={"": "src"},
    zip_safe=True,
    python_requires='>=3.7.*, <4',
    install_requires=['SQLAlchemy'],
    extras_require={
        'test': ['coverage', 'flake8', 'mypy', 'sqlalchemy2-stubs'],
        'package': ['wheel', 'twine']
    },
    project_urls={
        'Bug Reports':
        'https://github.com/masamitsu-murase/lazy-sqlalchemy/issues',
        'Source': 'https://github.com/masamitsu-murase/lazy-sqlalchemy',
    },
)
