from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads a requirements file and returns a list of requirements.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            for line in file:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Warning: requirements.txt not found. No requirements loaded.")
    return requirement_lst

print(get_requirements())

setup(
    name='NetworkSecurities',
    version='0.0.1',
    author='Tanvi Kamath',
    author_email="tanvikamath22@gmail.com",
    packages=find_packages(),  # ✅ fixed
    install_requires=get_requirements()
)
