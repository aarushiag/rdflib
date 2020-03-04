from rdflib import Graph


def test_basic_sparql_star_subject():
    g = Graph()
    res = g.query('''SELECT * WHERE {
<< ?s ?p ?o >> ?p2 ?o2 . 
}''')


def test_basic_sparql_star_object():
    g = Graph()
    res = g.query('''SELECT * WHERE {
?s ?p << ?s2 ?p2 ?o2 >> . 
}''')

def test_basic_sparql():
    g = Graph()
    res = g.query('''SELECT * WHERE {
    ?s ?p ?o . 
    }''')


def test_bind_sparql_star():
    g = Graph()
    res = g.query('''SELECT * WHERE { BIND(<< ?s2 ?p2 ?o2 >> AS ?b) }''')