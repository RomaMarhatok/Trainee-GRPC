import grpc
import logging
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import Annotated
from google.protobuf.json_format import MessageToDict, ParseDict
from service.protos.notes_pb2 import (
    GRPCGetListNoteMessage,
    GRPCGetNoteMessage,
    GRPCCreateNoteMessage,
)
from api.grpc_client import get_notes_grpc_client, NoteServiceStub
from api.schema import POSTCreateNoteRequest
import uuid

note_router = APIRouter(prefix="/notes", tags=["Notes"])

logger = logging.getLogger(__name__)


@note_router.get("/note/{note_uuid}")
async def get_note(
    note_uuid: str, client: Annotated[NoteServiceStub, Depends(get_notes_grpc_client)]
):
    request = GRPCGetNoteMessage(uuididf=note_uuid)
    try:
        grpc_response = await client.get(request=request)
    except grpc.RpcError as e:
        return JSONResponse(
            content={
                "error": {
                    "status_code": e.code().name,
                    "details": e.details(),
                }
            }
        )
    return JSONResponse(content=MessageToDict(grpc_response))


@note_router.post("/create")
async def create_note(
    request: POSTCreateNoteRequest,
    client: Annotated[NoteServiceStub, Depends(get_notes_grpc_client)],
):
    data = request.model_dump()
    data.update({"uuididf": str(uuid.uuid4())})
    message = ParseDict(data, GRPCCreateNoteMessage())
    grpc_response = await client.create(message)
    return JSONResponse(content=MessageToDict(grpc_response))


@note_router.get("/{user_id}")
async def get_notes_list(
    user_id: str, client: Annotated[NoteServiceStub, Depends(get_notes_grpc_client)]
):
    logger.info("Try get notes list from user with UUID:%s", user_id)
    request = GRPCGetListNoteMessage(userUuididf=user_id)
    grpc_message = await client.list(request)
    return JSONResponse(content=MessageToDict(grpc_message))
