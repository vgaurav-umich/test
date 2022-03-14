# Getting Started with Python Project

## First-time installation from Github
1. go to your working directory
2. issue git clone command to clone the repo.
    ```angular2html
    git clone git@umich.github.com:vgaurav-umich/test.git
    ```
3. switch to newly created directory `cd test`
4. open your favorite editor and open the just downloaded project
5. Follow Setup prompts below ...

## Setup
1. No need to add requirements.txt file
2. We will need specific version of mistune package to make it work. 
3. setup.py only needs pipenv, ploomber, and jupyterlab dependencies
4. First use `pip install -e .` command to get setup dependencies installed.
5. Then run `pipenv install -e .` to run all pipenv dependencies 