
from distutils.core import setup

setup(
    name='think_stats',
    version='0.1.0',
    author='Lawrence Allan Jones',
    author_email='mrwizard82d1@earthlink.net',
    packages=['think_stats', 'think_stats.test'],
    scripts=['bin/think_stats.py',],
    url='http://pypi.python.org/pypi/think_stats/',
    license='LICENSE.txt',
    description='Useful think_stats stuff.',
    long_description=open('README.txt').read(),
    install_requires=[],
    )
