from rdflib import Graph
class TestIssue955:
    # This test is for checking bind sparql star query
    def test_issue_bind():
        g = Graph()
        print("##################Testcase-1(Bind)###################")
        g.parse('w3c//turtle//test_issue_955.ttl', format='turtle')
        for row in g.query('''PREFIX owl:<http://www.w3.org/2002/07/owl#>
                            PREFIX prop:<http://www.example.org/pragya/sweb/assignment4/netflix/OwlProperty/>
                            SELECT ?x WHERE{
                            BIND(<<?s ?p ?o>> AS ?x)
                            }'''):
            print(row)
        print("##################Testcase-2(Bind)###################")
        for row in g.query('''PREFIX owl:<http://www.w3.org/2002/07/owl#>
                            PREFIX prop:<http://www.example.org/pragya/sweb/assignment4/netflix/OwlProperty/>
                            SELECT ?x WHERE{
                            BIND(<< << ?s1 ?p1 ?o1 >> ?p2 ?o2 >> AS ?x)
                            }'''):
            print(row)
        print("##################Testcase-3(Bind)###################")
        for row in g.query('''PREFIX owl:<http://www.w3.org/2002/07/owl#>
                            PREFIX prop:<http://www.example.org/pragya/sweb/assignment4/netflix/OwlProperty/>
                            SELECT ?s2 WHERE{
                            BIND(<<?s ?p ?o>> AS ?x)
                            ?x ?s2 ?p2 .
                            }'''):
            print(row)

    def test_issue_recursive_sparql_star():
        # This test is for checking recursive sparql star query
        g = Graph()

        g.parse('w3c//turtle//test_issue_955.ttl', format='turtle')
        print("##################Testcase-1(Recursive)###################")
        for row in g.query('''PREFIX owl:<http://www.w3.org/2002/07/owl#>
                            PREFIX prop:<http://www.example.org/pragya/sweb/assignment4/netflix/OwlProperty/>
                            SELECT ?s1 
                            WHERE{<<?s1 ?p1 ?o1>> ?p2 ?o2.}'''):
            print(row)
        print("##################Testcase-2(Recursive)###################")
        for row in g.query('''PREFIX owl:<http://www.w3.org/2002/07/owl#>
                            PREFIX prop:<http://www.example.org/pragya/sweb/assignment4/netflix/OwlProperty/>
                            SELECT ?s1 
                            WHERE{<<<<?s1 ?p1 ?o1>> ?p2 ?o2>> ?p3 ?o3.}'''):
            print(row)
        print("##################Testcase-3(Recursive)###################")
        for row in g.query('''PREFIX owl:<http://www.w3.org/2002/07/owl#>
                            PREFIX prop:<http://www.example.org/pragya/sweb/assignment4/netflix/OwlProperty/>
                            SELECT ?p3 ?s3
                            WHERE{<<<<?s1 ?p1 ?o1>> ?p2 ?o2>> ?p3 <<?s3 ?p4 ?o3>>.}'''):
            print(row)
        print("##################Testcase-4(Recursive)###################")
        for row in g.query('''PREFIX owl:<http://www.w3.org/2002/07/owl#>
                            PREFIX prop:<http://www.example.org/pragya/sweb/assignment4/netflix/OwlProperty/>
                            SELECT ?s1 
                            WHERE{<<<<?s1 ?p1 ?o1>> ?p2 <<?s2 ?p4 ?o2>>>> ?p3 ?o3.}'''):
            print(row)

if __name__ == '__main__':
    TestIssue955.test_issue_bind()
    TestIssue955.test_issue_recursive_sparql_star()






