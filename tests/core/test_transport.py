from typing import Union
from unittest.mock import MagicMock
from eventstore_grpc.core import transport
from eventstore_grpc.core.settings import KeepAlive
from eventstore_grpc.core.auth import Auth
import pytest
import importlib.resources
import grpc
from eventstore_grpc import discovery


@pytest.mark.parametrize(
    "hosts",
    ["localhost:2113", ["localhost:2113"], ["localhost:2113", "localhost:2112"]],
)
def test_transport_init(hosts: Union[str, list[str]]) -> None:
    discover = False
    tls = True
    keep_alive = KeepAlive()
    username = "admin"
    password = "changeit"
    root_certificate = importlib.resources.path("tests.fixtures", "ca.crt")
    discovery.discover_endpoint = MagicMock(
        return_value=hosts if isinstance(hosts, str) else hosts[-1]
    )
    auth = Auth(username=username, password=password, root_certificate=root_certificate)
    t = transport.Transport(
        hosts=hosts, discover=discover, tls=tls, keep_alive=keep_alive, auth=auth
    )
    assert t.discover is discover
    assert t.keep_alive is keep_alive
    assert t.tls is tls
    assert t._auth is auth
    assert isinstance(t.target, str)
    assert isinstance(t.channel, grpc.Channel)
    if isinstance(hosts, str):
        assert hosts == t.target
        assert t.multinode_cluster is False
    else:
        assert hosts[-1] == t.target
        if len(hosts) > 1:
            assert t.multinode_cluster is True
        else:
            assert t.multinode_cluster is False
