from typing import List, Tuple
from solution_common.message import Message, Request, SwitchStatsInfo
from solution_common.solution import Solution

class NodePlaceholder:
    major_id = int

    def __init__(self, buffer_size, incoming_bandwidth, outgoing_bandwidth):
        # Instance attributes
        self.buffer_size = buffer_size
        self.incoming_bandwidth = incoming_bandwidth
        self.outgoing_bandwidth = outgoing_bandwidth

    def display_info(self):
        print(f"Device Info - Buffer Size: {self.buffer_size}, "
              f"Incoming Bandwidth: {self.incoming_bandwidth}, Outgoing Bandwidth: {self.outgoing_bandwidth}")

class UserSolution(Solution):
    
    def __init__(self, node_id: int, bw_in: int, bw_out: int, size: int, level: int, graph: List[List[int]],
                 nodes_info: List[Tuple[int, int, int, int, int]]):
        super().__init__(node_id, bw_in, bw_out, size, level, graph, nodes_info)
        
    def add_request_list(self, request_list: List[Request]) -> None:
        # Remember to update your buffer
        pass

    def ask_round_solution(self, neighbor_info_list: List[SwitchStatsInfo]) -> List[Message]:
        return []

    def next_round(self, result) -> SwitchStatsInfo:
        # Information communication between node
        return SwitchStatsInfo()

