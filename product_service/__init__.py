from product_service.config import settings
import asyncio
from fastapi import FastAPI
from logging import getLogger

logger = getLogger(__name__)

class ProductService:
    app = None

    @classmethod
    def create_app(cls):
        app = FastAPI()
        cls.app = app
        logger.info('APP Created!!')
        return cls.app