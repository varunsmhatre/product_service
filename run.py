from product_service import settings, ProductService
from uvicorn import Server, Config
from entrypoint import Main

app = ProductService.create_app()

def run_app():
    loop = Main.get_app_event_loop()
    loop.run_until_complete(Server(
        Config(app=app, host='0.0.0.0', loop=loop, port=int(settings.PORT))
    ).serve())