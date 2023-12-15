# setup.py
from setuptools import setup, find_packages
import pathlib

setup(
    name='uganda_data_python',
    version='0.1.0',
    description='Python library for accessing Uganda Data API',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    author='Katende Nicholas',
    author_email='katznicho@gmail.com.com',
    url='https://github.com/katende/uganda_data_python',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            # Add any command-line scripts here
        ],
    },
)
