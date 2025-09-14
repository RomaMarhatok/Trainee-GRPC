import grpc
from service.protos.notes_pb2_grpc import NoteServiceStub


async def get_notes_grpc_client() -> NoteServiceStub:
    channel = grpc.aio.insecure_channel("localhost:50051")
    client = NoteServiceStub(channel)
    return client
