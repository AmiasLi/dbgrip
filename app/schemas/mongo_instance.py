from pydantic import BaseModel


class MongoInstance(BaseModel):
    name: str
    host: str
    port: int

    class Config:
        orm_mode = False


class MongoInstanceCreate(MongoInstance):
    username: str
    password: str
    db: str
    auth_source: str
    auth_mechanism: str
    kwargs: dict | None = None

    class Config:
        orm_mode = False


# class MongoInstanceOut(MongoInstance):
#     id: str
