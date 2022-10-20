# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ps_pb2 as ps__pb2


class psStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.publish = channel.unary_unary(
                '/ps.ps/publish',
                request_serializer=ps__pb2.PublishRequest.SerializeToString,
                response_deserializer=ps__pb2.PublishResponse.FromString,
                )
        self.subscribe = channel.unary_unary(
                '/ps.ps/subscribe',
                request_serializer=ps__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=ps__pb2.SubscribeResponse.FromString,
                )


class psServicer(object):
    """Missing associated documentation comment in .proto file."""

    def publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_psServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'publish': grpc.unary_unary_rpc_method_handler(
                    servicer.publish,
                    request_deserializer=ps__pb2.PublishRequest.FromString,
                    response_serializer=ps__pb2.PublishResponse.SerializeToString,
            ),
            'subscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.subscribe,
                    request_deserializer=ps__pb2.SubscribeRequest.FromString,
                    response_serializer=ps__pb2.SubscribeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ps.ps', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ps(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ps.ps/publish',
            ps__pb2.PublishRequest.SerializeToString,
            ps__pb2.PublishResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ps.ps/subscribe',
            ps__pb2.SubscribeRequest.SerializeToString,
            ps__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
