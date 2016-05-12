"""
Networks_tests
"""

import networkx

from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI

# from minicps.utils import setup_func, teardown_func, with_named_setup
from minicps.networks import PLC, DumbSwitch
from minicps.networks import EthLink, build_nx_graph, TopoFromNxGraph

from nose.plugins.skip import SkipTest


def test_build_nx_graph():

    graph = build_nx_graph()

    assert len(graph) == 3, "graph nodes error"

    print
    print 'Graph vertices:', list(graph.nodes())
    print 'Graph edges:', list(graph.edges())


# TODO: currently not working
# @with_named_setup(setup_func, teardown_func)
# @SkipTest
def test_TopoFromNxGraph():

    """Create a Networkx graph and build a mininet topology object."""

    graph = build_nx_graph()

    # Build a test graph
    topo = TopoFromNxGraph(graph)

    net = Mininet(topo=topo, link=TCLink, listenPort=6634)
    net.start()
    CLI(net)
    net.stop()
