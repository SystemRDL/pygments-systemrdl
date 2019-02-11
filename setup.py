import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup (
    name='pygments-systemrdl',
    version="1.0.0",
    author="Alex Mykyta",
    author_email="amykyta3@github.com",
    description="SystemRDL 2.0 lexer extension for Pygments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["pygments"],
    entry_points =
    """
    [pygments.lexers]
    rdllexer = rdl_pygments.rdllexer:SystemRDLLexer
    """,
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    project_urls={
        "Source": "https://github.com/SystemRDL/systemrdl-pygments",
    },
)
