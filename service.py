import logging
import grpc
import asyncio
from gen import calculator_pb2_grpc, calculator_pb2


class Calculator(calculator_pb2_grpc.CalculatorServicer):
    async def calc(
        self,
        request: calculator_pb2.CalculateOperationMessage,
        context: grpc.aio.ServicerContext,
    ) -> calculator_pb2.CalculatedMessage:
        _accepted_operations = set({"+", "-", "*", "/"})
        result = 0
        if request.oper in _accepted_operations:
            match request.oper:
                case "+":
                    result = request.first_number + request.second_number
                case "-":
                    result = request.first_number - request.second_number
                case "*":
                    result = request.first_number * request.second_number
                case "/":
                    result = request.first_number / request.second_number
        response = calculator_pb2.CalculatedMessage(result=result)
        return response


async def serve() -> None:
    server = grpc.aio.server()
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
