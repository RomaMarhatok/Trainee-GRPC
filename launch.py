import asyncio
from api.main import start_fastapi_server
from service.grpc_server import launch_grpc_server


async def main_func():
    await asyncio.gather(
        launch_grpc_server(),
        start_fastapi_server(),
    )


if __name__ == "__main__":
    try:
        asyncio.run(main_func())
    except RuntimeError:
        loop = asyncio.get_running_loop()
        asyncio.ensure_future(main_func(), loop=loop)
