# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re
from pathlib import Path


# get version from __version__ variable in football_club/__init__.py
def get_version():
	init_py = Path("football_club/__init__.py")
	if init_py.exists():
		content = init_py.read_text()
		match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", content, re.M)
		if match:
			return match.group(1)
	return "0.1.0"


setup(
	name="football_club",
	version=get_version(),
	description="Football Club App",
	author="phamos.eu",
	author_email="support@phamos.eu",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[],
)
