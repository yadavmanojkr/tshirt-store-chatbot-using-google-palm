from setuptools import find_packages,setup

setup(
    name='Max T-Shirt',
    version='0.0.1',
    author='manoj yadav',
    author_email='manoj.yadav415@gmail.com',
    install_requires=["langchain","streamlit","python-dotenv","chromadb"],
    packages=find_packages()
)