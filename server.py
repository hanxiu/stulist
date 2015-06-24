# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

import reqs
import os.path


handlers = [
    (r"/coulist", reqs.CourseListHandler),
    (r"/couedit/(\d+|new)", reqs.CourseEditHandler),
    (r"/coudel/(\d+)", reqs.CourseDelHandler),
    (r"/", reqs.MainHandler),
]

home_path = os.path.dirname(__file__)

settings = {
    "static_path": os.path.join(home_path, "static"),
    "debug": "true"
}

application = tornado.web.Application(handlers, **settings)

application.listen(8888)

if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
