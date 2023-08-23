from pydantic import BaseModel


class MongoInstance(BaseModel):
    name: str
    host: str | None = None
    host_ip: str
    port: int

    class Config:
        orm_mode = False
