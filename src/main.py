import asyncio
import tornado.web

from userProfiles import UserProfileHandler

def makeApp():
    endpoints = [
        ("/", IndexHandler),
        ("/quote", QuoteHandler),
        (r"/profile/(\w+)", UserProfileHandler),
    ]
    app = tornado.web.Application(endpoints)
    app.listen(8000)
    return app

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Index")

class QuoteHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("random quote")

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()
