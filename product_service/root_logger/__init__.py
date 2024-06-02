import sys
import json
from loguru import logger


def serialize(record):
    subset = {
        "timestamp": str(record["time"]),
        "message": record["message"],
        "level": record["level"].name,
    }
    return json.dumps(subset)


def patching(record):
    record["extra"]["serialized"] = serialize(record)


logger.remove(0)

logger = logger.patch(patching)
logger.add(sys.stderr, format="{extra[serialized]}")

custom_logger = logger