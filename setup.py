from typing import List
from setuptools import setup, find_packages


flag = "-e ."
project_name = "GenAI Recommendation Engine"

def required_packages(filepath:str) -> List[str]:
    requirements = []

    with open(filepath, 'r') as file:
        requirements = file.readlines()
        requirements = [requirement.replace('\n', '') for requirement in requirements]
        file.close()

    if flag in requirements:
        requirements.remove(flag)

    return requirements


setup(
    name=project_name,
    version="0.0.1",
    author="Deepak Saini",
    author_email="deepak170602@gmail.com",
    description="Generative AI Recommendation Engine",
    packages=find_packages(),
    install_requires=required_packages('requirements.txt')
)