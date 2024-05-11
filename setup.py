from setuptools import find_packages
from setuptools import setup


def read_requirements(file_name):
    """Read a requirements file and return a list of its packages."""
    with open(file_name) as f:
        return f.read().splitlines()


# Specify your requirements files
requirements_files = [
    "requirements.txt",
]

# Read and combine requirements from all specified files
combined_requirements = []
for file in requirements_files:
    combined_requirements.extend(read_requirements(file))

combined_requirements = list(set(combined_requirements))

setup(
    name="remote_land_management",
    version="0.0.1",
    description="Python module for handling traditional land managemnt tasks from afar with IoT",
    author="Jeremy Dyer",
    author_email="jdye64@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=combined_requirements,
    classifiers=[],
    python_requires=">=3.10",
)
