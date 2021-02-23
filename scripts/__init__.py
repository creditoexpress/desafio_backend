import logging
import asyncio

from app.infra.database.seeders.seed import seed_db


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) # TODO: Add the logger to the IOC


def seeder():
    logger.info(' Seeder starting...')
    asyncio.run(seed_db())
    logger.info(' Seedes added to the DB successfully!')


def web_server():
    pass
