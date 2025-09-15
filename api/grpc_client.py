import grpc
import os
import logging
from service.protos.notes_pb2_grpc import NoteServiceStub
from dotenv import load_dotenv

load_dotenv(override=True)
logger = logging.getLogger(__name__)


async def get_notes_grpc_client() -> NoteServiceStub:
    logger.info(f"Start grpc client on {os.environ["RPC_HOST"]}:50051")
    channel = grpc.aio.insecure_channel(f"{os.environ["RPC_HOST"]}:50051")
    client = NoteServiceStub(channel)
    return client
