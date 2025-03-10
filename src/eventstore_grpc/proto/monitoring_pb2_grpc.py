# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from eventstore_grpc.proto import monitoring_pb2 as monitoring__pb2


class MonitoringStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Stats = channel.unary_stream(
                '/event_store.client.monitoring.Monitoring/Stats',
                request_serializer=monitoring__pb2.StatsReq.SerializeToString,
                response_deserializer=monitoring__pb2.StatsResp.FromString,
                )


class MonitoringServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Stats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitoringServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Stats': grpc.unary_stream_rpc_method_handler(
                    servicer.Stats,
                    request_deserializer=monitoring__pb2.StatsReq.FromString,
                    response_serializer=monitoring__pb2.StatsResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'event_store.client.monitoring.Monitoring', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Monitoring(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Stats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/event_store.client.monitoring.Monitoring/Stats',
            monitoring__pb2.StatsReq.SerializeToString,
            monitoring__pb2.StatsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
