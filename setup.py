from setuptools import find_packages, setup

setup(
    name="test",
    packages=find_packages(exclude=('test*','testing*')),
    install_requires=[
    ],
    setup_requires=['jupyterlab', 'ploomber'],
    tests_require=[],

)