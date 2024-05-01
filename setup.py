from setuptools import find_packages, setup

setup(
    name='bd_schema_plugin',
    version='0.1',
    description='An example NetBox plugin',
    url='https://github.com/jeremystretch/my-example-plugin',
    author='Jeremy Stretch',
    license='Apache 2.0',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
