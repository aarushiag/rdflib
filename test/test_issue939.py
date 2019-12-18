from rdflib import Graph, ConjunctiveGraph
import unittest


class TestIssue939(unittest.TestCase):

    def test_issue_939(self):
        test_ttl = """@base <http://purl.org/linkedpolitics/MembersOfParliament_background> .
        @prefix lpv: <vocabulary/> .
        <EUmember_1026>
            a lpv:MemberOfParliament ."""
        g = ConjunctiveGraph()
        g.parse(data=test_ttl, format='turtle')
        assert type(g) is ConjunctiveGraph  # <class 'rdflib.graph.ConjunctiveGraph'>

        g = ConjunctiveGraph()
        x = g.parse(data=test_ttl, format='turtle')
        # The reported would like x to be the ConjunctiveGraph or that type
        assert type(g) is ConjunctiveGraph


if __name__ == "__main__":
    unittest.main()
