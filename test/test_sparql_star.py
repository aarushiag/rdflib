from rdflib import Graph
from rdflib.plugins.sparql.parser import VarOrBlankNodeOrIriOrLitOrEmbTP
import  pyparsing
import unittest

class SparqlStarTests(unittest.TestCase):

    @staticmethod
    def test_basic_sparql_star_subject():
        g = Graph()
        res = g.query('''SELECT * WHERE {
    << ?s ?p ?o >> ?p2 ?o2 . 
    }''')

    @staticmethod
    def test_basic_sparql_star_object():
        g = Graph()
        res = g.query('''SELECT * WHERE {
    ?s ?p << ?s2 ?p2 ?o2 >> . 
    }''')

    @staticmethod
    def test_basic_sparql():
        g = Graph()
        res = g.query('''SELECT * WHERE {
        ?s ?p ?o . 
        }''')

    @staticmethod
    def test_bind_sparql_star():
        g = Graph()
        res = g.query('''SELECT * WHERE { BIND(<< ?s2 ?p2 ?o2 >> AS ?b) }''')

    @staticmethod
    def test_parser():
        assert VarOrBlankNodeOrIriOrLitOrEmbTP.matches("<<?s ?p ?o>>")


if __name__ == '__main__':
    unittest.main()