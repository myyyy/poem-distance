#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import json
from pymongo import Connection
import gridfs

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print "setting headers!!!"
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

class IndexHandler(BaseHandler):
    def get(self):
        data={"results":[{"gender":"female","name":{"title":"miss","first":"inmaculada","last":"herrero"},"location":{"street":"7936 calle de la democracia","city":"vigo","state":"comunidad valenciana","postcode":89386},"email":"inmaculada.herrero@example.com","login":{"username":"beautifulmouse810","password":"steven","salt":"o7gnbpWG","md5":"be12c9ae1ffa2c4546d87d871ac56575","sha1":"0ff587f11d86ed376c3f19cab4b987519ff99bbb","sha256":"adf4f1c7e619a7a08da6ca593913c000f67df296f0d82d98d58a7bcaf0203bd7"},"dob":"1969-05-11 20:21:33","registered":"2013-05-19 09:38:20","phone":"901-869-091","cell":"666-950-554","id":{"name":"DNI","value":"31648111-I"},"picture":{"large":"https://randomuser.me/api/portraits/women/76.jpg","medium":"https://randomuser.me/api/portraits/med/women/76.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/76.jpg"},"nat":"ES"}],"info":{"seed":"4258edb756a16134","results":1,"page":1,"version":"1.1"}}
        self.write(json.dumps(data))
class gfstest(BaseHandler):
    def get(self):
        db = Connection().test
        fs = gridfs.GridFS(db)
        file_id = fs.put("Hello Word",filename="foo.txt")
        fs.list()
        self.write(dict(data=fs.get(file_id).read()))
settings = {

    'template_path': 'views',
    'static_path': 'static',
    'static_url_prefix': '/static/',
}

application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/gfs", gfstest),


], **settings)

if __name__ == "__main__":
    application.listen(8877)
    tornado.ioloop.IOLoop.instance().start()
