"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'numpy>=1.16.1'
]

setup(
    author="Kamil Czarnogórski",
    description="Python implementation of monte carlo tree search",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='mcts monte carlo tree search',
    name='mctspy',
    packages=find_packages(
        include=['mctspy*']
    ),
    setup_requires=requirements,
    test_suite='tests',
    tests_require=requirements,
    url='https://github.com/int8/monte-carlo-tree-search',
    version='0.1',
    zip_safe=False,
)