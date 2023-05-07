import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
    description = description.split("\n")[1]
    print(description)
  
setuptools.setup(
    name="PyneStrap",
    version="0.0.1",
    author="dshaw0004",
    author_email="dipankarshaw692@gmail.com",
    packages=["Card", "IconButton"],
    description="A component library for Pynecone",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/dshaw0004/PyneStrap",
    license='MIT',
    python_requires='>=3.8',
    install_requires=['pynecone']
)