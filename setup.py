from setuptools import setup
import os

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="nb_cell_tools",
    author="Tony Hirst",
    author_email="tony.hirst@open.ac.uk",
    url="https://github.com/innovationOUtside/innovationOUtside/nb_cell_tools",
    description="nb_cell_tools -cell tools extension for Jupyter notebooks",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license="MIT License",
    packages=["nb_cell_tools"],
    # version handled via setup.cfg and nb_cell_tools/__init__.py
    include_package_data=True,
    package_data={
    },
    install_requires=[
    ],
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        (
            "share/jupyter/nbextensions/nb_cell_tools",
            [
                "nb_cell_tools/static/index.js",
                "nb_cell_tools/static/jquery.dialogextend.js",
                "nb_cell_tools/static/nb_cell_tools.png",
                "nb_cell_tools/static/nb_cell_tools.yaml",
            ],
        ),
        # like `jupyter nbextension enable --sys-prefix`
        (
            "etc/jupyter/nbconfig/notebook.d",
            ["jupyter-config/nbconfig/notebook.d/nb_cell_tools.json"],
        ),
    ],
)

