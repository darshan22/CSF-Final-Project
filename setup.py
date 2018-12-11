from setuptools import setup

with open("README.md","r") as f:
	long_description = f.read()

setup(name = "NN",
	version = "1.0",
	author = "Darshan Kasat & Shivam Thassu",
	author_email = "darshankasat22@gwu.edu",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/darshan22/CSF-Final-Project",
	packages = setuptools.find_packages(),
	classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",],
)
	
	
