import grpc
from service.db.repository import Irepo
from service.db.models import Notes
from service.protos.notes_pb2_grpc import NoteServiceServicer
from service.protos.notes_pb2 import (
    GRPCCreateNoteMessage,
    GRPCNoteMessage,
    GRPCDeleteNoteMessage,
    GRPCGetListNoteMessage,
    GRPCGetNoteMessage,
    GRPCNoteListMessage,
    GRPCUpdateNoteMessage,
)

from google.protobuf.json_format import MessageToDict, ParseDict


class NoteHandler(NoteServiceServicer):
    def __init__(self, repo: Irepo[Notes]):
        self.repo = repo

    async def create(
        self, request: GRPCCreateNoteMessage, context: grpc.aio.ServicerContext
    ) -> GRPCNoteMessage:
        data = MessageToDict(request)
        # data.update({"user_id": data["userUuididf"]})
        # data.pop("userUuididf")
        note = await self.repo.create(data)
        response = ParseDict(note.to_dict(), GRPCNoteMessage())
        return response

    async def get(
        self, request: GRPCGetNoteMessage, context: grpc.aio.ServicerContext
    ) -> GRPCNoteMessage:
        note = await self.repo.get(request.uuididf)
        if note is None:
            await context.abort(
                code=grpc.StatusCode.NOT_FOUND,
                details=f"Model {self.repo._model.__class__.__name__} with UUID {request.uuididf} not found",
            )
            return GRPCGetNoteMessage()
        response = ParseDict(note.to_dict(), GRPCNoteMessage())
        return response

    async def update(
        self, request: GRPCUpdateNoteMessage, context: grpc.aio.ServicerContext
    ) -> GRPCNoteMessage:

        note = await self.repo.get(request.uuididf)
        data_for_update = MessageToDict(request)
        new_note = await self.repo.update(note, data_for_update)
        response = ParseDict(new_note.to_dict(), GRPCNoteMessage())
        return response

    async def delete(
        self, request: GRPCDeleteNoteMessage, context: grpc.aio.ServicerContext
    ) -> GRPCDeleteNoteMessage:
        deleted_uuid = await self.repo.delete(request.uuididf)
        response = GRPCDeleteNoteMessage(uuid=deleted_uuid)
        return response

    async def list(
        self, request: GRPCGetListNoteMessage, context: grpc.aio.ServicerContext
    ) -> GRPCNoteListMessage:
        notes = await self.repo.get_list(request.user_uuididf)
        response = GRPCNoteListMessage(
            notes=[ParseDict(note.to_dict(), GRPCNoteMessage()) for note in notes]
        )
        return response
