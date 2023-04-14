import grpc
import sales_records_pb2
import sales_records_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = sales_records_pb2_grpc.SalesRecordStub(channel)

def print_message():
    response = stub.PingSalesRecords(sales_records_pb2.EmptyMessage())
    return(response.ack)
