from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'numpy>=1.9.1'
]

setup(
    author="Kamil Czarnogórski",
    description="Python implementation of monte carlo tree search for 2 "
                "players zero-sum game ",
    install_requires=requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='mcts monte carlo tree search',
    name='mctspy',
    python_requires='>=3.5.7',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    url='https://github.com/int8/monte-carlo-tree-search',
    version='0.1.1'
)
