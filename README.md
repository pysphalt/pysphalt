[![Documentation Status](https://readthedocs.org/projects/pysphalt/badge/?version=latest)](https://pysphalt.readthedocs.io/en/latest/?badge=latest)
[![pypi](https://img.shields.io/pypi/v/pysphalt.svg)](https://pypi.python.org/pypi/pysphalt)
[![versions](https://img.shields.io/pypi/pyversions/pysphalt.svg)](https://github.com/pysphalt/pysphalt)
[![license](https://img.shields.io/github/license/pysphalt/pysphalt.svg)](https://github.com/pysphalt/pysphalt/blob/main/LICENSE)
<h1 align="center">Pysphalt</h1>

Library of machine learning models for Brazilian asphalt material data.

-   [Installation](#installation)
-   [Local Quickstart](#local-quickstart)
    -   [1. Install dependencies](#1-install-dependencies)
-   [Building Docs](#building-docs)
-   [Deploy to PyPi](#deploy-to-pypi)

## Installation

```shell
pip install pysphalt
```
## Local Quickstart

The fastest way to get Pysphalt up and running locally for development.

### 1. Install dependencies

There are three things to install

1. Conda
3. Python libraries
4. Pre-commit hooks

Create a new miniconda environment.

```shell
conda create -n pysphalt python=3.10
conda activate pysphalt
```

Install all python libraries. Libraries related to development are kept separate, in `requirements-dev.txt`. Make sure to add any dependencies you introduce into these files!

```shell
pip install -r requirements.txt -r requirements-dev.txt
```

Install `pre-commit` and spin it up:

```shell
pre-commit install
pre-commit
```

⚠️ Whenever you work on this codebase, **remember to activate the conda environment:**

```shell
conda activate pysphalt
```

## Building Docs

```shell
cd docs
make html
```

You can access the generated docs on `docs/build/html/index.html`


## Deploy to PyPi

Deploys to PyPi are managed automatically by Github Actions. To upload a new version of the library, just bump the version field on `pyproject.toml` and push a new tag to `main`.
The Action to publish a new version to PyPi will be triggered by the pushing the tag.
