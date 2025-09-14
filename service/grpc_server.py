import grpc
import asyncio
from .protos.notes_pb2_grpc import add_NoteServiceServicer_to_server
from .handler import NoteHandler
from .db.repository import NotesRepository
from .db.session import create_session_factory
from .db.config import DBConfigCreator


async def launch_grpc_server():
    server = grpc.aio.server()
    db_config = DBConfigCreator().get_config()
    repo = NotesRepository(create_session_factory(db_config=db_config))
    add_NoteServiceServicer_to_server(NoteHandler(repo=repo), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)

    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(launch_grpc_server)
