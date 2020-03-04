from rdflib import Graph



def test_basic_sparql_star():
    g = Graph()
    res = g.query('''SELECT * WHERE {
<<?s ?p ?o>> ?p2 ?o2 . 
}''')
