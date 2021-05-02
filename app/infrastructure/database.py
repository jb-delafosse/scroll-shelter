import motor.motor_asyncio

DATABASE_URL: str
DATABASE_URL = "mongodb://localhost:27017"
CLIENT = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
