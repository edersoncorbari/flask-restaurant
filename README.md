# Full-Stack-Menu-Project

Simple web-application based on Python (version3) with Flask Microframework. Used for studies with the framework. It simplementes the list of restaurants.

![screenshot](https://raw.github.com/edersoncorbari/flask-restaurant/master/screenshot.png)


## Dependencies

**VirtualBox**

https://www.virtualbox.org/

**Vagrant**

https://www.vagrantup.com/

**SQL Alchemy**

http://www.sqlalchemy.org/

**Flask**

http://flask.pocoo.org/

**dicttoxml**

https://pypi.python.org/pypi/dicttoxml

## Setup

Set up VirtualBox and Vagrant to create your own server. With Vagrant installed, run:

```
$ vagrant up
$ vagrant ssh
$ cd <SYNCED PATH TO REPOSITORY>
```

## Run

Run the web app using command:


```
$ python app.py
```

The app runs on port `5000`:

```
http://0.0.0.0:5000/
```

## API Endpoints

Available in JSON and XML at the following endpoints:

List all restaurants:

```
http://0.0.0.0:5000/restaurants/json
http://0.0.0.0:5000/restaurants/xml
```

List all menu items for a given RESTAURANT_ID:

```
http://0.0.0.0:5000/restaurants/<RESTAURANT_ID>/menu/json
http://0.0.0.0:5000/restaurants/<RESTAURANT_ID>/menu/xml
```

List a single menu item:

```
http://0.0.0.0:5000/restaurants/<RESTAURANT_ID>/menu/<ITEM_ID>/json
http://0.0.0.0:5000/restaurants/<RESTAURANT_ID>/menu/<ITEM_ID>/xml
```
