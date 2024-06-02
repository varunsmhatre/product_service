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

# logger.trace("A trace message.")
logger.debug({'a':1, 'b':2})
# logger.info("An info message.")
# logger.success("A success message.")
# logger.warning("A warning message.")
# logger.error("An error message.")
# logger.critical("A critical message.")
