__package__ = "typeIt"

import tornado.ioloop
import tornado.web
import json
import os
import predictor

from platform import system


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("main.html")
        #self.render("main.html")
        self.finish("main")

class searchHandler(tornado.web.RequestHandler):
    def post(self):
        print("search handler")
        body = bytes.decode(self.request.body)
        body = json.loads(body)
        msg = body["msg"]
        if msg != "":
            try:
                test_result = predictor.find_emojis(msg)
                print(test_result)
                result = {"result":test_result}
                result = json.dumps(result)
            except KeyError:
                self.set_status(404)
                result = "no such user id"
        else:
            self.set_status(404)
            result = json.dumps("empy message")
        self.finish(result)
        print('sent result')

settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static")
)


def make_app():
    print("make_app")
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search", searchHandler),
    ], **settings)


if __name__ == "__main__":
    if system() in ["Windows", "Darwin"]:
        port = 8888
    else:
        port = 80
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
