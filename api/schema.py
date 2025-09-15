from pydantic import BaseModel


class POSTCreateNoteRequest(BaseModel):
    userUuididf: str
    name: str
    message: str


class PUTUpdateNoteRequest(BaseModel):
    uuididf: str
    name: str
    message: str
