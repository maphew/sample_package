from setuptools import find_packages
from setuptools import setup

setup(
    author="William",
    author_email="williamjamir@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Sample Package",
    entry_points={
        "console_scripts": [
            "sample_package=sample_package.cli:main",
        ]
    },
    install_requires=["CLick >= 6.0"],
    license="MIT license",
    long_description=" ",
    include_package_data=True,
    name="sample-package",
    packages=find_packages(include=["sample_package"]),
    url="https://github.com/williamjamir/sample-package",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    zip_safe=False,
)
