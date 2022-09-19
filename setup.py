from setuptools import setup
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = f.read().splitlines()

with open(path.join(here, 'requirements-dev.txt'), encoding='utf-8') as f:
    requires_dev = f.read().splitlines()

setup(
    name='pywavesurfer',
    packages=['pywavesurfer'],
    version='0.0.8',
    description="Python package for reading WaveSurfer data files",
    long_description=long_description,
    author='Adam L. Taylor, Boaz Mohar',
    author_email='taylora@janelia.hhmi.org, boazmohar@gmail.com',
    url='https://github.com/JaneliaSciComp/PyWaveSurfer',
    download_url='https://github.com/JaneliaSciComp/PyWaveSurfer/archive/v0.0.8.tar.gz',
    classifiers=['Development Status :: 3 - Alpha',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 'Programming Language :: Python :: 3.10',
                 ],
    install_requires=requires,
    extras_require={
        'dev': requires_dev,
    },
)
