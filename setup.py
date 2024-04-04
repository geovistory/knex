from setuptools import setup, find_packages

setup(
    name="knex",
    version="0.0.0",
    author='Gaétan Muck',
    author_email='gaetan.muck@kleiolab.com',
    description='Knowledge Extraction.',
    long_description='Extract Knowledge from raw text an return a graph.',
    packages=find_packages(),
    install_requires=[
        "gmpykit",
    ],
    keywords=['knowledge', 'extraction', 'graph']
)