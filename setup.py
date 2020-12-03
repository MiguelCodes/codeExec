import setuptools

with open("README.md", "r") as fh:
  description = fh.read()

setuptools.setup(
  name = "codeExec", 
  version = "1.0.0",
  author = "nonamed",
  licesne = "MIT",
  description = "A package that executes code without bugs.",
  long_description = description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/MiguelCodes/codeExec",
  packages = setuptools.find_packages(),
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires = '>=3.7',
)