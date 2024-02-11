from setuptools import setup, find_packages

setup(
    name='flask-wiz',
    version='1.2',
    author='Krish Soni',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'flask-wiz=flask_wiz.cli:cli',
        ],
    },
)
