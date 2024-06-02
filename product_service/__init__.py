from product_service.config import settings
import asyncio
from fastapi import FastAPI
from product_service.root_logger import custom_logger


class ProductService:
    app = None

    @classmethod
    def create_app(cls):
        app = FastAPI()
        cls.app = app
        custom_logger.info('APP Created!!')
        return cls.app