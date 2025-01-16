
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

dependencies = [
    'flask',
    'click',
    'Flask',  
    # 'sqlite3',
    # 'mysql-connector-python',
    # 'psycopg2',
    # 'pymongo',
]

setup(
    name='flask-wiz',
    version='1.9.4',
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
