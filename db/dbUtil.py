# -*- coding: utf-8 -*-
import couchdb
couch = couchdb.Server()

#db = couch.create('test')
db = couch['test']
#doc = {'foo': 'bar'}
#db.save(doc)

for id in db:
    print id