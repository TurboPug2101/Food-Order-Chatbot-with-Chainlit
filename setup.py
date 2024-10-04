from setuptools import find_packages, setup

setup(
    name = 'Generative AI Project',
    version= '0.0.0',
    author= 'Ishank',
    author_email= 'ishankrajpal@gmail.com',
    packages= find_packages(),
    install_requires = []

)
# Packaging and distributing your Python project refers to the process of preparing your project so that others can easily install and use it.
# Packaging:

# It bundles all your Python code, modules, and resources into a single package (like a .tar.gz or .whl file) so it can be installed.
# This is done through the setup.py script, which defines details like the project name, version, author, and dependencies.
# Distributing:

# Once packaged, you can share your project with others by uploading it to a repository like PyPI (Python Package Index), where users can install it via a command like pip install your_project_name.