#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import *
from pymongo import MongoClient

app = Flask(__name__)
dbhost = "localhost"
dbname = "webhooks"
dbcoll = "mandrill"
db = MongoClient(host=dbhost)


@app.route('/', methods=['GET', 'POST'])
def hook():
    mongo = MongoClient()
    mandrillhookjson = json.loads(request.form['mandrill_events'])
    for mandrillhook in mandrillhookjson:
        mongo[dbname][dbcoll].insert({"hook": mandrillhook})
    return ""


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")