from pathlib import Path

from setuptools import setup, find_packages

from dbt_invoke import version

PARENT_DIR = Path(__file__).parent
README = Path(PARENT_DIR, 'README.md').read_text()

setup(
    name='dbt-invoke',
    version=version.__version__,
    author='Robert Astel, Jennifer Zhan, Vincent Dragonette',
    author_email='rob.astel@gmail.com',
    license='Apache License 2.0',
    description=(
        'dbt-invoke is a CLI for creating, updating, and deleting'
        ' dbt property files.'
    ),
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/Dashlane/dbt-invoke',
    packages=find_packages(),
    install_requires=[
        'invoke>=1.4.1',
        'PyYAML',
    ],
    python_requires='>=3.6.0',
    entry_points={
        'console_scripts': ["dbt-invoke = dbt_invoke.main:program.run"]
    },
)