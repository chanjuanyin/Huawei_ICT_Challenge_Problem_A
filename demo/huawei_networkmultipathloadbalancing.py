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

#This class if for rewriting and defining all the classes in message.py
class UserMessage(Message):
    """define SwtichsStatsInfo here or just create another class in this file
    what to do   1.  a controler view of SwitchStatsInfo, including
                        1.1 identifier for controller, maybe put -1
                        1.2 all node remaining buffer, all nodes remaining inbound
                        1.3 and all nodes remaining outbound
                    2.  a normal node view of SwitchStatsInfo including 
                        2.1 identifier for normal nodes, maybe put -2
                        2.2 see class message last five attributes
    """
    pass

class UserSolution(Solution):
    
    def __init__(self, node_id: int, bw_in: int, bw_out: int, size: int, level: int, graph: List[List[int]],
                 nodes_info: List[Tuple[int, int, int, int, int]]):
        super().__init__(node_id, bw_in, bw_out, size, level, graph, nodes_info)
        
        
        
        
        
    #the access node will receive request and divide into messages   
    def add_request_list(self, request_list: List[Request]) -> None:
        # Remember to update your buffer
        pass


    #1. It takes neigbours SwitchStatsInfo
    #2. The method needs to make a decision of which  path to send
    #3. and the simulator will return a message than contains all the successful and fails one
    def ask_round_solution(self, neighbor_info_list: List[SwitchStatsInfo]) -> List[Message]:
        return []


    # 1. take result: List[Tuple[Message, bool]]
    # 2. decode and update it to SwitchStatsInfo
    # 3. 
    def next_round(self, result) -> SwitchStatsInfo:
        # Information communication between node
        
        #cluster controller
        if self.level==4:
            pass
        
        #other nodes
        else:
            pass
            
        return SwitchStatsInfo()

