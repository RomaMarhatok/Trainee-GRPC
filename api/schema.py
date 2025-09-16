from pydantic import BaseModel


class POSTCreateNoteRequest(BaseModel):
    user_uuididf: str
    name: str
    message: str


class PUTUpdateNoteRequest(BaseModel):
    uuididf: str
    name: str
    message: str
