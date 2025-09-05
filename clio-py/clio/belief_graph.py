
import graphviz

class Node:
    """Represents a single step in the reasoning process."""
    def __init__(self, id, label, data=None):
        self.id = id
        self.label = label
        self.data = data or {}

    def __repr__(self):
        return f"Node(id={self.id}, label={self.label})"

class Edge:
    """Represents the relationship between two nodes in the belief graph."""
    def __init__(self, source, target, label=None):
        self.source = source
        self.target = target
        self.label = label

    def __repr__(self):
        return f"Edge(source={self.source.id}, target={self.target.id}, label={self.label})"

class BeliefGraph:
    """Represents the belief state of the AI."""
    def __init__(self):
        self.nodes = []
        self.edges = []
        self._node_map = {}

    def add_node(self, label, data=None):
        """Adds a new node to the graph."""
        node_id = len(self.nodes)
        node = Node(node_id, label, data)
        self.nodes.append(node)
        self._node_map[node_id] = node
        return node

    def add_edge(self, source, target, label=None):
        """Adds a new edge to the graph."""
        edge = Edge(source, target, label)
        self.edges.append(edge)
        return edge

    def get_node(self, node_id):
        """Returns a node by its ID."""
        return self._node_map.get(node_id)

    def to_graphviz(self):
        """Returns a graphviz.Digraph object for visualization."""
        dot = graphviz.Digraph()
        for node in self.nodes:
            dot.node(str(node.id), node.label)
        for edge in self.edges:
            dot.edge(str(edge.source.id), str(edge.target.id), label=edge.label)
        return dot
