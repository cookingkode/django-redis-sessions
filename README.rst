django-redis-sessions
=======================
Redis database backend for your sessions; with support for Redis cluster

.. image:: https://travis-ci.org/martinrusev/django-redis-sessions.svg?branch=master
    :target: https://travis-ci.org/martinrusev/django-redis-sessions



------------
Installation
------------

1. Install deps
clone from https://github.com/Grokzen/redis-py-cluster
and run ``python setup.py install``

2. Install package
Run ``python setup.py install``,


2. Set ``redis_sessions.session`` as your session engine, like so::

    SESSION_ENGINE = 'redis_sessions.session'

3. Optional settings::

    # This defines the nodes in the redis cluster
    SESSION_REDIS_NODES =  [{"host": "127.0.0.1", "port": "30001"},
                                {"host": "127.0.0.1", "port": "30002"},
                                {"host": "127.0.0.1", "port": "30003"},
                                {"host": "127.0.0.1", "port": "30004"},
                                {"host": "127.0.0.1", "port": "30005"},
                                {"host": "127.0.0.1", "port": "30006"},
                                ]




4. Tests::

    $ pip install django nose redis
    # Make sure you have redis running on localhost:6379
    $ nosetests
