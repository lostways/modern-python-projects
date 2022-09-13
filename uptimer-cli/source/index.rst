.. Uptimer documentation master file, created by
   sphinx-quickstart on Mon Sep 12 22:39:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Uptimer's documentation!
===================================

Uptimer is a CLI tool to monitor the status of websites.
Specify a list of URLs, and it will return thier HTTP status codes

Quickstart
----------

1. Install poetry (Uptimer uses `poetry ,<https://python-poetry.org/>`)

   $ pip install poetry

2. Instal dependencies

   $ pip install

3. Run uptimer

   $ poetry run uptimer https://urltocheck.url

CLI
---

.. click:: uptimer_cli.uptimer:check
   :prog: uptimer


Useful Links
------------

.. toctree::
   :maxdepth: 2

   api.rst

