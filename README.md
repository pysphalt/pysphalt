[![Documentation Status](https://readthedocs.org/projects/pysphalt/badge/?version=latest)](https://pysphalt.readthedocs.io/en/latest/?badge=latest)
<h1 align="center">Pysphalt</h1>

Library of machine learning models for Brazilian asphalt material data.

-   [Installation](#installation)
-   [Local Quickstart](#local-quickstart)
    -   [1. Install dependencies](#1-install-dependencies)
-   [Building Docs](#building-docs)

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

## Building Docs

```shell
cd docs
make html
```

You can access the generated docs on `docs/build/html/index.html`
