
Code for the blog [Python Essentials for Data Engineers](https://www.startdataengineering.com/post/python-for-de/)
<!-- vim-markdown-toc GFM -->

* [Python Essentials for Data Engineers](#python-essentials-for-data-engineers)
    * [Setup](#setup)
        * [Codespaces](#codespaces)
        * [Local](#local)
    * [Run code](#run-code)

<!-- vim-markdown-toc -->

# Python Essentials for Data Engineers 

## Setup 

### Codespaces 

**Prerequisites**:

1. [GitHub Account](https://github.com/)

Click on the button below to clone this repo and start a Jupyter notebook to practice code in the blog post.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/josephmachado/python_essentials_for_data_engineers)

Give the machine a few minutes to start up, then run the following commands.

```bash 
uv sync 
uv run juptyer lab
```

> [!CAUTION]
> Do not forget to turn off your CodeSpaces machine when you are done

### Local 

**Prerequisites**:

1. [Git](https://git-scm.com/install/)
2. [uv](https://docs.astral.sh/uv/getting-started/installation/)

On your terminal, clone the repo and start notebook server.

```bash 
git clone https://github.com/josephmachado/python_essentials_for_data_engineers.git
cd python_essentials_for_data_engineers
uv sync 
uv run jupyter lab
```

## Run code 

Follow along with code using the [workshop notebook](./notebooks/workshop.ipynb).

Fully working code and solutions are available at [solutions notebook](./notebooks/solutions.ipynb)

