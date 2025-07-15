from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a requirements file and returns a list of packages.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='brainage_project',
    version='0.0.1',
    author='TAHA BIKKI',
    author_email='tahabikki00@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
