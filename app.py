import asyncio
import tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ],
    template_path="templates",
    static_path="static",
    autoreload = True,
    )

async def main():
    app = make_app()
    app.listen(8888)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

if __name__ == "__main__":
    asyncio.run(main())