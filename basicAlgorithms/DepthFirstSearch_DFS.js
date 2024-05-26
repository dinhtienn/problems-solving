const Graph = require('../dataStructure/undirectedUnweightedGraph');

Graph.prototype.dfs = function (start) {
  const stack = [start];
  const visited = { [start]: true };
  const results = [];

  let currentVertex;
  while (stack.length) {
    currentVertex = stack.pop();
    results.push(currentVertex);
    this.adjacencyList[currentVertex].forEach((neighbor) => {
      if (!visited[neighbor]) {
        visited[neighbor] = true;
        stack.push(neighbor);
      }
    });
  }

  return results;
};

// test
const graph = new Graph();
graph.addEdge(0, 1);
graph.addEdge(0, 2);
graph.addEdge(1, 2);
graph.addEdge(1, 3);
graph.addEdge(2, 4);
graph.addEdge(3, 4);

console.log(graph);
const search = graph.dfs(0);
console.log(search);
