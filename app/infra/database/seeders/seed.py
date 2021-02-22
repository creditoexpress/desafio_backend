from app.infra.database import Database
from app.infra.database.seeders.fees import seed as fees_seeder
from app.infra.database.seeders.clients import seed as clients_seeder

async def seed_db():
    db = Database()
    collections = db.get_collections()

    print('Executing [ Fees ] Seeder...')
    await fees_seeder(collections['fees'])

    print('Executing [ Clients ] Seeder...')
    await clients_seeder(collections['clients'])
