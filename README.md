# PyWebPlot

This project is a simple lightweight way of both hosting any matplot plit based graphs (such as seaborn) on
a flask application.

## Overview

This is achived via creating functions that take a pyodbc cursor as a parameter to funcions that returns a [matplotlib figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)

## Installation

Install Python 3.11

Then setup a python virual environment

`python -m venv pyenv`

The activate the env
        
`.\pyenv\Scripts\Activate.ps1` (Windows)

`./pyenv/Scripts/activate` (Unix)

## Database

This app has an MsSQL Server database.

`initdb.sql` has the table creation + population wih some random data.

Connection is managed by environment variables (documented below)

## Environment variables

The dotenv package is used to load env variables from a file.
Simply just make a `.env` file in the project directory with the contents:

        DB_USER='username'
        DB_PASS='password'
        DB_CONN='url here'

