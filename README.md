# The-best-places-in-Moscow
Site about the most interesting places in Moscow  
![site.png](static/.gitbook/assets/site.png)

## Launch

You will need Python version 3 to run the site.

Download the code from GitHub. Install the dependencies:


```sh
pip install poetry
```

```sh
poetry install
```

Create a SQLite database

```sh
python3 manage.py migrate
```

Start the development server

```
python3 manage.py runserver
```
Recommended using [virtualenv/venv](https://docs.python.org/3/library/venv.html)

## Environment variables

Some of the project settings come from environment variables. To define them, create a `.env` file next to `manage.py` and write the data there in this format: `VARIABLE=value`.

There are 2 variables available:
- `SECRET_KEY` — project secret key
- `DEBUG` — debug mode. Set `True` to see debug information in case of an error.

## Project Goals

The code is written for educational purposes - for a course on Python and web development on the [Devman](https://dvmn.org).
