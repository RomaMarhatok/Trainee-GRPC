from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import Annotated
from google.protobuf.json_format import MessageToDict
from service.protos.notes_pb2 import GRPCGetListNoteMessage, GRPCGetNoteMessage
from .grpc_client import get_notes_grpc_client, NoteServiceStub

note_router = APIRouter(prefix="/notes", tags=["Notes"])


@note_router.get("/{user_id}")
async def get_notes_list(
    user_id: str, client: Annotated[NoteServiceStub, Depends(get_notes_grpc_client)]
):
    request = GRPCGetListNoteMessage(user_uuid=user_id)
    grpc_message = await client.list(request)
    print(grpc_message)
    return JSONResponse(content=MessageToDict(grpc_message))


@note_router.get("/note/{note_uuid}")
async def get_note(
    note_uuid: str, client: Annotated[NoteServiceStub, Depends(get_notes_grpc_client)]
):
    print("NOTE", type(note_uuid))
    request = GRPCGetNoteMessage(uuid=note_uuid)
    print("REQESUT")
    grpc_message = await client.get(request=request)
    print("GRPC", grpc_message)
    return JSONResponse(content=MessageToDict(grpc_message))
