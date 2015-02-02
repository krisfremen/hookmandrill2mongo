#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import *
from pymongo import MongoClient

application = app = Flask(__name__)
dbhost = "localhost"
dbname = "webhooks"
dbcoll = "mandrill"


@app.route('/', methods=['GET', 'POST'])
def hook():
    try:
        mongo = MongoClient(host=dbhost)
        mandrillhookjson = json.loads(request.form['mandrill_events'])
        for mandrillhook in mandrillhookjson:
            mongo[dbname][dbcoll].insert({"hook": mandrillhook})
        return "OK"
    except Exception, err:
        return str(err)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")