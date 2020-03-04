from rdflib import Graph
from rdflib.namespace import RDF, Namespace
import unittest



class SparqlStarTests(unittest.TestCase):

    def test_basic_sparql_star_subject(self):
        g = Graph()
        g.parse(data="""
        PREFIX ex:<http://example.org/>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        
        ex:subject ex:predicate ex:object .
        ex:reif a rdf:Statement ;
         rdf:subject ex:subject ;
         rdf:predicate ex:predicate ;
         rdf:object ex:object .
        ex:about a ex:reif .
        """, format="ttl")
        res = g.query('''SELECT * WHERE {<< ?s ?p ?o >> ?p2 ?o2 . }''')

        rl = list(res)
        self.assertEqual(4 , len(rl))


    def test_basic_sparql_star_object(self):
        g = Graph()
        g.parse(data="""
        PREFIX ex:<http://example.org/>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        
        ex:subject ex:predicate ex:object .
        ex:reif a rdf:Statement ;
         rdf:subject ex:subject ;
         rdf:predicate ex:predicate ;
         rdf:object ex:object .
        ex:about a ex:reif .
        """, format="ttl")
        res = g.query('''SELECT * WHERE {
    ?s ?p << ?s2 ?p2 ?o2 >> . 
    }''')
        rl = list(res)
        self.assertEqual(1 , len(rl))


    def test_basic_sparql(self):
        g = Graph()
        g.parse(data="""
        PREFIX ex:<http://example.org/>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        ex:subject ex:predicate ex:object .
        ex:reif a rdf:Statement ;
         rdf:subject ex:subject ;
         rdf:predicate ex:predicate ;
         rdf:object ex:object .
     ex:about a ex:reif .
        """, format="ttl")
        res = g.query('''PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        SELECT * WHERE {
        ?s ?p ?o . 
        ?r a rdf:Statement ;
           rdf:subject ?s ;
           rdf:predicate ?p ;
           rdf:object ?o .
        ex:about a ?r.
        }''')
        rl = list(res)
        self.assertEqual(1 , len(rl))

    @staticmethod
    def test_bind_sparql_star():
        g = Graph()
        res = g.query('''SELECT * WHERE { BIND(<< ?s2 ?p2 ?o2 >> AS ?b) }''')

    def test_constant_sparql_star_object(self):
        g = Graph()
        g.parse(data="""
           PREFIX ex:<http://example.org/>
           PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>

           ex:subject ex:predicate ex:object .
           ex:reif a rdf:Statement ;
            rdf:subject ex:subject ;
            rdf:predicate ex:predicate ;
            rdf:object ex:object .
           ex:reif a ex:about .
           """, format="ttl")
        res = g.query('''PREFIX ex:<http://example.org/> SELECT * WHERE {
        << ex:subject ex:predicate ?object >> a ex:about  . 
        }''')
        rl = list(res)
        self.assertEqual(1 , len(rl))

    def test_constant_sparql_object(self):
        g = Graph()
        g.parse(data="""
           PREFIX ex:<http://example.org/>
           PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>

           ex:subject ex:predicate ex:object .
           ex:reif a rdf:Statement ;
            a ex:about ;
            rdf:subject ex:subject ;
            rdf:predicate ex:predicate ;
            rdf:object ex:object .
           
           """, format="ttl")
        res = g.query('''PREFIX ex:<http://example.org/> SELECT * WHERE {
        ex:subject ex:predicate ?object .
        ex:reif a ex:about  ;
        a rdf:Statement ;
        rdf:subject ex:subject ;
        rdf:predicate ex:predicate ;
        rdf:object ?object . 
        }''')
        rl = list(res)
        self.assertEqual(1 , len(rl))
if __name__ == '__main__':
    unittest.main()