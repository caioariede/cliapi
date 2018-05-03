from setuptools import setup, find_packages

setup(
    name='cliapi',
    version='0.0.1',
    url='https://github.com/caioariede/cliapi.git',
    author='Caio Ariede',
    description='Expose command-line tools around APIs',
    packages=find_packages(),
    install_requires=['bottle>=0.12.13', 'webargs>=2.1.0'],
)
