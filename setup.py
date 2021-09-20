from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in clientx_custom_app/__init__.py
from clientx_custom_app import __version__ as version

setup(
	name="clientx_custom_app",
	version=version,
	description="Custom app for client",
	author="Aptitudetech",
	author_email="info@aptitudetech.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
