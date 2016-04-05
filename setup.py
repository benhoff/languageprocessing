import os
from setuptools import find_packages, setup


# directory = os.path.abspath(os.path.dirname(__file__))
"""
with open(os.path.join(directory, 'README.rst')) as f:
    long_description = f.read()
"""

setup(
    name="languageprocessing",
    version='0.0.1',
    description='Simple language processing with zeromq',
    # long_description=long_description,
    url='https://github.com/benhoff/languageprocessing',
    license='GPL3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
        'Operating System :: OS Independent'],
    author='Ben Hoff',
    author_email='beohoff@gmail.com',
    packages= find_packages(), # exclude=['docs', 'tests']
    entry_points={'languageprocessing.analyzers': ['sentiment = languageprocessing.sentimentanalysis:SentimentAnalysis'
                                                   'parts_of_speech = languageprocessing.partofspeech:PartOfSpeech',
                                                   'parser = languageprocessing.parser:Parser']},

    install_requires=[
        'pluginmanager',
        'pyzmq',
        'textblob',
        'nltk',
        ],

    extras_require={
        'dev': ['flake8']
        },
)
