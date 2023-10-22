# The-best-places-in-Moscow
Site about the most interesting places in Moscow  
![site.png](static/.gitbook/assets/site.png)

## Environment variables

Some of the project settings come from environment variables. To define them, create a `.env` file next to `manage.py` and write the data there in this format: `VARIABLE=value`.

There are 2 variables available:
- `SECRET_KEY` — project secret key
- `DEBUG` — debug mode. Set `True` to see debug information in case of an error.

## Launch

You will need Python version 3 to run the site.

Download the code from GitHub. Install the package manager:

```sh
pip3 install poetry
```

Install the dependencies:

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

## Load place from json

You can load location from json file:

```commandline
python manage.py load_place <json-url>
```

#### json-file example:

```commandline
{
    "title": "Эйфелева башня в Москве",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/8868d171420b5221f8f50af5e95a7b12.jpeg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/46cb25cf1719bf546c8bbcf1b51ba4f4.jpeg"
    ],
    "description_short": "Вы можете поехать в Париж и отстоять огромную очередь, 
    чтобы посетить главную его достопримечательность — великолепную Эйфелеву башню.
    А можете просто сесть в метро и, не выезжая за пределы МКАД, прикоснуться к точной 
    её копии.",
    "description_long": "<p><strong>Эйфелева башня в Москве</strong> находится 
    недалеко от станции метро «Авиамоторная» на территории одного из производственных
    предприятий — завода «Москабельмет». Соорудили точную копию мировой архитектурной 
    знаменитости сами рабочие этого завода. Высота заводской башни — 15 метров (для 
    справки — высота оригинальной, парижской Эйфелевой башни составляет 324 метра)."
    "coordinates": {
        "lng": "37.71241599999999",
        "lat": "55.74669399999998"
    }
}
```

You can find other JSON files [here](https://github.com/devmanorg/where-to-go-places)
## Project Goals

The code is written for educational purposes - for a course on Python and web development on the [Devman](https://dvmn.org).
