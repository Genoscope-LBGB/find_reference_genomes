import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="find_reference_genomes",
    version="1.0.0",
    author="bistace",
    author_email="bistace@genoscope.cns.fr",
    description="find_reference_genomes is a rdbioseq tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "find_reference_genomes=find_reference_genomes.command_line:main",
        ],
    },
)
