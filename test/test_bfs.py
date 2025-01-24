# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    tiny = graph.Graph('data/tiny_network.adjlist')
    tiny_traverse = tiny.bfs('Martin Kampmann')
    # assert expected number of nodes and all node values unique
    assert len(tiny_traverse)==30 & len(set(tiny_traverse)) == 30 
    assert tiny_traverse[1] in ['33483487','32790644','31806696','31626775','31540829'] # make sure in nodes out from Martin
    assert tiny_traverse[1] == '33483487' # exact expected first node out from Martin
    assert tiny_traverse[29] == 'Charles Chiu' # expected end point from Martin

    # think of test case for divergence from bfs and dfs

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    big = graph.Graph('data/citation_network.adjlist')
    # check for existent path
    big_short = big.bfs('Sergio Baranzini','Martin Kampmann')
    assert len(big_short) == 5
    assert big_short == ['Sergio Baranzini', '30851128', 'Joseph DeRisi', '32972996', 'Martin Kampmann']

    # check for nonexistent path
    big_none = big.bfs('Sergio Baranzini','Reza Abbasi-Asl')
    assert big_none == None

def test_valid_start():
    tiny = graph.Graph('data/tiny_network.adjlist')
    # raise error for nonexistent start node
    with pytest.raises(KeyError):
        tiny.bfs('Sigmund Freud')

def test_valid_end():
    tiny = graph.Graph('data/tiny_network.adjlist')
    # raise error for nonexistent end node
    with pytest.raises(KeyError):
        tiny.bfs('Tony Capra','Sigmund Freud')