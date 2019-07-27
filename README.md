# Django-Event-Geolocator

Find events based on coordinate location using spatial mapping in postgresql

## Getting Started

Make sure all the prerequisites are installed. 

### Prerequisites

* [PostgresQL](https://www.postgresql.org/download/) - SQL Database
* [Anaconda](https://www.anaconda.com/distribution/) - Conda package manager for data science
* [OSGeo](https://trac.osgeo.org/osgeo4w/) - Binary distribution of a broad set of open source geospatial software for Windows environments

### Installing

Set up a PostgresQL database locally or on a cloud
* [PostgresQL](https://www.postgresql.org/download/)

Install OSGeo on your windows machine
* [OSGeo](https://trac.osgeo.org/osgeo4w/)

Clone this repository

```
  git clone *repo name*
```

Change into project directory

Use conda to install all the python dependencies 

```
  conda env create -f environment.yml
```

Go to *settings.py* file and update the database variables

Make the database migration on your postgres database

```
  python manage.py migrate
```

Run the checks to make sure everything is ok

```
  python manage.py check
```

## Running the tests

Run the test files to make sure that PostgresQL works

```
  python manage.py test
```

## Running self tests

*Get events within the radius of the privided coordinate location, filter results by list count.

*Additional optional parameters may be given: name of event, date of event, type of event.

http://127.0.0.1:8000/event/:lat/:lon/:rad/:count/?name=&date=&eventType=

*Get all the event types or filter by a keyword

http://127.0.0.1:8000/event/type/

http://127.0.0.1:8000/event/type/:eventType

    
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

