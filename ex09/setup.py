from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A sample test package'
LONG_DESCRIPTION = 'A sample test package for 42 python piscine'

setup(
    name='ft_package',
    version= VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='pcamaren',
    author_email='pcamaren@student.42.fr',
    license='MIT',
    url='https://github.com/pierinacamarena/python_data_science/ex09/ft_package',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    entry_points={
        'console_scripts': [],
    },
)