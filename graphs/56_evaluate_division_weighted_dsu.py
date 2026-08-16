class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        equationGraph = self.getEquationGraph(equations, values)
        print(equationGraph)
        queryResults = []
        for query in queries:
            queryResult = self.evaluateQuery(query[0], query[1], equationGraph)
            queryResults.append(queryResult)
        return queryResults
    
    def evaluateQuery(self, startExpression, endExpression, equationGraph):
        if startExpression not in equationGraph or endExpression not in equationGraph:
            return -1
        elif startExpression == endExpression:
            return 1
        elif endExpression in equationGraph[startExpression]:
            return equationGraph[startExpression][endExpression]
        for vertex in equationGraph[startExpression]:
            if equationGraph[startExpression][vertex] == 0:
                continue
            currWeight = equationGraph[startExpression][vertex]
            equationGraph[startExpression][vertex] = 0 # marking visited
            partialResult = self.evaluateQuery(vertex, endExpression, equationGraph)
            equationGraph[startExpression][vertex] = currWeight # marking un visited
            if partialResult == -1:
                continue
            return partialResult * currWeight
        return -1

    
    def getEquationGraph(self, equations, values):
        equationGraph = {}
        valueIndex = 0
        for equation in equations:
            if equation[0] not in equationGraph:
                equationGraph[equation[0]] = {}
            equationGraph[equation[0]][equation[1]] = values[valueIndex]
            if equation[1] not in equationGraph:
                equationGraph[equation[1]] = {}
            equationGraph[equation[1]][equation[0]] = (1/values[valueIndex])
            valueIndex+=1
        return equationGraph
