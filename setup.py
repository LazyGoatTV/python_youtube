from typing import List
from setuptools import setup, find_packages

def parse_requirements(filename) -> List[str]:
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


install_reqs = parse_requirements("requirements.txt")
requirements = [str(ir) for ir in install_reqs]

setup_kwargs = dict(
    name="python_youtube",
    version="0.8.2",
    license="LICENSE",
    platforms="All",
    description="LazyGoat Common Moduls",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.7",
)

setup(**setup_kwargs)
