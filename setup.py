from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

selected_database = ['sqlite','mysql-connector-python',
    'psycopg2',
    'pymongo'  ]

dependencies = [
    'flask',
    'click',
    'sqlite',
    'mysql-connector-python',
    'psycopg2',
    'pymongo',

]

if selected_database == 'sqlite':
    dependencies.append('sqlite')
elif selected_database == 'mysql':
    dependencies.append('mysql-connector-python')
elif selected_database == 'postgresql':
    dependencies.append('psycopg2')
elif selected_database == 'mongodb':
    dependencies.append('pymongo')

setup(
    name='flask-wiz',
    version='1.4',
    author='Krish Soni',
    packages=find_packages(),
    include_package_data=True,
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'flask-wiz=flask_wiz.cli:cli',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
