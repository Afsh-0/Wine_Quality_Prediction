#to access src file and tells Python: This project is a package, here is 
#its name, version, and where the code lives.”

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Wine_quality"
AUTHOR_USER_NAME = "Afsh-0"
SRC_REPO = "Wine-Quality"
AUTHOR_EMAIL = "248272946+Afsh-0@users.noreply.github.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ML app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
    "pandas",
    "notebook",
    "numpy",
    "scikit-learn",
    "matplotlib",
    "python-box==6.0.2",
    "pyYAML",
    "tqdm",
    "ensure==1.0.2",
    "joblib",
    "types-pyYAML",
    "Flask",
    "Flask-Cors"
    ],
    python_requires=">=3.10",
)