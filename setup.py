import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join("rdl_pygments", "__about__.py")) as f:
    v_dict = {}
    exec(f.read(), v_dict)
    version = v_dict['__version__']

setuptools.setup (
    name='pygments-systemrdl',
    version=version,
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
