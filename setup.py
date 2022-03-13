from setuptools import find_packages, setup

setup(
    name="test",
    packages=find_packages(),
    install_requires=[
    ],
    setup_requires=['ploomber', 'jupyterlab'],
    tests_require=[],

)