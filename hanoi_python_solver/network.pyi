from _typeshed import Incomplete
from typing import Dict, List

class Network:
    edges: Incomplete
    nodes: Incomplete
    neighbors: Incomplete
    def __init__(self) -> None: ...
    @classmethod
    def fromAdjacencyMatrix(cls, file_name: str) -> "Network | None": ...
    def edge_list_size(self) -> int: ...
    @property
    def nodes_list_size(self) -> int: ...
    def changeWeight(self, node_id: str, new_value: float) -> float | None: ...
    def containsNode(self, node_id: str) -> bool: ...
    def add_edge(self, start_node: str, end_node: str, label: float = 1.0) -> int: ...
    def DOT_description(self) -> str: ...
    def dijkstra(self, start_id: str, end_id: str) -> Dict[str, List[str]]: ...
