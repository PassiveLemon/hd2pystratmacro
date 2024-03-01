from setuptools import setup, find_packages

requirements = []
with open("./requirements.txt", "r") as requirements_file:
  requirements = requirements_file.read().splitlines()

setup(
  name="hd2pystratmacro",
  version="0.2.0",
  description="A Python based macro script for Helldivers 2",
  url="http://github.com/passivelemon/hd2pystratmacro/",
  author="PassiveLemon",
  license="GPL3",
  packages=find_packages(),
  install_requires=requirements,
  entry_points={
    'console_scripts': [
      'hd2pystratmacro = hd2pystratmacro.__main__:main'
    ]
  },
  include_package_data=True,
)
