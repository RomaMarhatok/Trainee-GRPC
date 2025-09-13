import asyncio
import logging
import grpc
from gen import calculator_pb2_grpc, calculator_pb2


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        while True:
            first_number = 0
            second_number = 0
            operation = ""
            first_number = int(input("Input first number: "))
            operation = input("Input operation: ")
            second_number = int(input("Input second number: "))

            response = await stub.calc(
                calculator_pb2.CalculateOperationMessage(
                    first_number=first_number,
                    oper=operation,
                    second_number=second_number,
                )
            )
            print(response)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
