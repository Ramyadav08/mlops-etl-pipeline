'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    # Read the requirements.txt file and return a list of dependencies
    requirements_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as f:
            lines= f.readlines()
            for line in lines:
                requirement= line.strip()
                # Skip empty lines and comments and -e .
                if requirement and requirement!= '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be installed.")
        
    return requirements_list



setup(
    name='networksecurity',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements(),
    author='Ram Rekha Yadav',
    description='A brief description of your package',
    author_email="ramrekhayadav64@mail.com"
)
                    