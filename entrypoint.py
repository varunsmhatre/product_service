from product_service import settings
import asyncio

class Main:
    _APP_EVENT_LOOP = asyncio.new_event_loop()

    @classmethod
    def get_app_event_loop(cls):
        return cls._APP_EVENT_LOOP
        
    

if __name__ == "__main__":
    if settings.MODE == 'server':
        from run import run_app
        run_app()