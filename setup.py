from setuptools import setup, find_packages

version = "2.0"

setup(
    name="ruper_detector",
    version=version,
    description="EITB Irratian Ruper Ordorikaren kantuen detektorea",
    long_description=open("README.rst").read() + "\n" + open("HISTORY.txt").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="ruper eitb music parsing",
    author="Mikel Larreategi",
    author_email="mlarreategi@codesyntax.com",
    url="http://github.com/erral/ruper_detector",
    license="GPLv2",
    python_requires=">=3.6",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        "beautifulsoup4"
    ],
    entry_points={"console_scripts": ["ruper_detector = ruper_detector.ruper:main",]},
)
