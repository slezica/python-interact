from distutils.core import setup

setup(
    name     = 'interact',
    version  = '0.2',
    url      = 'https://github.com/slezica/python-interact',

    author       = 'Santiago Lezica',
    author_email = 'slezica89@gmail.com',

    packages = ['interact'],
    license  = 'MIT License',

    description      = 'Immediately start an interactive session',
    long_description = open('README.txt').read()
)
