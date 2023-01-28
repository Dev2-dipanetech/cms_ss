from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cms_ss/__init__.py
from cms_ss import __version__ as version

setup(
	name="cms_ss",
	version=version,
	description="Contact Management System",
	author="DT Team",
	author_email="dev2@dipanetech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
