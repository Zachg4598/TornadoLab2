import asyncio
import tornado.web
from userProfiles import UserProfileHandler

def makeApp():
    endpoints = [
        (r"/profile/(\w+)", UserProfileHandler),  
    ]
    app = tornado.web.Application(endpoints)
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()


#final version