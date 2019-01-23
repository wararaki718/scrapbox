from setuptools import setup

setup(
    name='hello',
    version='1.0.0',
    packages=['hello'],
    package_data={
        'hello': ['base.ipynb']
    },
    install_requires=[
        'papermill'
    ]
)