# PyWebPlot

This project is a simple lightweight way of both hosting any matplot plit based graphs (such as seaborn) on
a flask application.

## Overview

This is achived via creating functions that take a pyodbc cursor as a parameter to funcions that returns a [matplotlib figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)

## Installation

First setup a python virual environment

`python -m venv pyenv`

The activate the env
        
`.\pyenv\Scripts\Activate.ps1` (Windows)
`./pyenv/Scripts/activate` (Unix)

