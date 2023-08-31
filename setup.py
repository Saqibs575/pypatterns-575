import os
from typing import List
from pathlib import Path
from setuptools import setup
from setuptools import find_packages


def get_requirements(file_path : str) -> List[str] :
    """
    Read the content of a text file at the specified 'file_path' and return its requirements as a list.

    Parameters:
        file_path (str): The file path of the text file to be read.

    Returns:
        List[str]: A list of requirements extracted from the text file.

    Raises:
        FileNotFoundError: If the specified 'file_path' does not exist.

    Note:
        - The text file should contain requirements, each listed on a separate line.
        - This function reads the file content, splits it by newline character ('\n'),
          and returns a list of requirements.

    Example:
        # Example text file: requirements.txt
        # ------------------------------
        # numpy
        # pandas
        # matplotlib
        # scikit-learn
        # -e .

        requirements_list = get_requirements("requirements.txt")
        print(requirements_list)
        # Output: ['numpy', 'pandas', 'matplotlib', 'scikit-learn']

    Comment:
        The 'get_requirements' function takes a 'file_path' as input, reads the specified
        text file, and returns a list of requirements extracted from that file. It assumes
        that each requirement is listed on a separate line in the text file. The function
        reads the file content using 'open' and 'read' methods, splits it by newline ('\n')
        character to get individual requirements, and then returns the list of requirements.
        If the 'file_path' does not exist, a 'FileNotFoundError' will be raised.
    """

    # Use try block to avoid any error
    try :

        # open requirements.txt as file if exist at given path
        with open(file_path , 'r') as file :

            # Read the file and save requirements in a list
            requirements = file.read().split('\n')

    # If error occured then catch the error
    except Exception as e :

        # Print error to debug and return empty list
        print(e)
        return []

    # finally return a list of requirements excluding last elements if -e in requirements else return full list
    if requirements[-1] == '-e .' :
        return requirements[:-1]
    else :
        return requirements
        
DIR_NAME = Path(__file__).parent
VERSION = '1.0.0'
AUTHOR = 'Saqib Shaikh'
REPO_NAME = 'pypatterns-575'
PROJECT_NAME = 'pypatterns_575'
AUTHOR_USER_NAME = 'Saqibs575'
AUTHOR_EMAIL = 'saquibs575@gmail.com'
LICENSE = 'GNU General Public License v3.0'
LONG_DESCRIPTION = (DIR_NAME / "README.md").read_text()
URL = 'https://github.com/Saqibs575/pypatterns-575'
DESCRIPTION = 'A Python package for creating intricate patterns.'
REQUIREMENTS_FILE_PATH = os.path.join(os.getcwd() , 'requirements.txt')


setup(
    url = URL ,

    author = AUTHOR ,
    
    version = VERSION ,
    
    license = LICENSE ,
    
    name = PROJECT_NAME ,
    
    python_requires = '>=3.6' ,
    
    description = DESCRIPTION ,
    
    packages = find_packages() ,
    
    author_email = AUTHOR_EMAIL ,
    
    long_description = LONG_DESCRIPTION ,
    
    long_description_content_type = 'text/markdown' ,
    
    install_requires = get_requirements(REQUIREMENTS_FILE_PATH) ,
    
    keywords = [
        'patterns', 
        'patterns in python', 
        'star patterns', 
        'pypatterns', 
        'pypatterns-575'
        ] ,

    project_urls = {
        'Source' : URL ,
        'Bug Reports': f'{URL}/issues' ,
    } ,

    classifiers = [
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)" ,
    "Programming Language :: Python :: 3"   ,
    "Programming Language :: Python :: 3.6" ,
    "Programming Language :: Python :: 3.7" ,
    "Programming Language :: Python :: 3.8" ,
    "Programming Language :: Python :: 3.9" ,
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Operating System :: OS Independent"
    ] ,

    platforms = [
        'win32', 'win-amd64', 'win-arm32', 'win-arm64', 'linux-x86', 
        'linux-x86_64', 'linux-armv6l', 'linux-armv7l', 'linux-aarch64', 
        'darwin', 'darwin-arm64', 'any'
    ]
)
