from typing import List, Tuple
from solution_common.message import Message, Request, SwitchStatsInfo
from solution_common.solution import Solution


#this class serves for the node information 101 for each node
class NodePlaceholder:

    def __init__(self, id, level,buffer_size, incoming_bandwidth, outgoing_bandwidth, 
                 remaining_buffer, remaining_inbound, remaining_outbound):
        # Instance attributes
        self.id = id
        self.level=level
        self.buffer_size = buffer_size
        self.incoming_bandwidth = incoming_bandwidth
        self.outgoing_bandwidth = outgoing_bandwidth
        self.remaining_buffer = remaining_buffer
        self.remaining_inbound = remaining_inbound
        self.remaining_outbound = remaining_outbound
        
    #yet to update
    def display_info(self):
        print(f"Device Id : {self.id},"
              f"Device Level : {self.level} "
              f"Device Info - Buffer Size: {self.buffer_size}, "
              f"Incoming Bandwidth: {self.incoming_bandwidth}, Outgoing Bandwidth: {self.outgoing_bandwidth}"
              f"Remaining_Buffer: {self.remaining_buffer}, Remaining_Inbound: {self.remaining_inbound}, Remaining_Outbound: {self.remaining_outbound}")

#Below three classes if for rewriting and defining all the classes in message.py


class UserRequest(Request):
    def __init__(self, source_node_id=0, target_node_id=0, data_size=0, begin_time=0, request_id=0):
        super().__init__(source_node_id, target_node_id, data_size, begin_time, request_id)


"""I think every message should use a Major Id - Minor Id to index it"""
class UserMessage(Message):
    def __init__(self, from_id: int, to_id: int, target_node_id: int, request_id: int, message_id: int,
                 request_begin_time: int):
        super().__init__(from_id, to_id, target_node_id, request_id, message_id, request_begin_time)

class UserSwitchStatsInfo(SwitchStatsInfo):
    """define SwtichsStatsInfo here or just create another class in this file
    what to do   1.  a controler view of SwitchStatsInfo, including
                        1.1 identifier for controller, index -1       bitsize=1
                        1.2 all node remaining buffer                 bitsize=11
                        1.3 all nodes remaining inbound               bitsize=10
                        1.4 and all nodes remaining outbound          bitsize=8
                                                                      total bitsize=30
                                                                      
                    2.  a normal node view of SwitchStatsInfo including 
                        part A what and who have I sent last time slice
                        2.1 identifier for normal nodes, from_node_id                 bitsize=8
                        2.2 where the message will send to, to_node_id                bitsize=8
                        2.3 final destination, target_node_id                         bitsize=8
                        2.4 Request Id(Major Id) that I send last time slice          bitsize=13
                        2.5 Request Size()
                        2.6 Message Id(Minor Id) range that I send last time slice    bitsize=
                        
                        part B My status that is two time slice ago
                        
                        2.x maybe node_info for the first time slice
    """
    def __init__(self,node_id):
        super().__init__()
        self.node_id=node_id
        
    #this is to transform number to binary number, maybe we can put it outside
    def bin_tran(self,number:int):
        if number<0:
            return bin(number)[3:]
        return bin(number)[2:]
    
    #define what will be the SSI like for controller
    def Controller_SSI(self):
        # indentifier
        self.info.append(self.bin_tran(-1))
        # all node remaining buffer
        # task: how to represent remaining buffer

        #self.info.append
        
    def Node_SSI(self,node_id):
        # identifier
        self.info.append(self.bin_tran(self.node_id))
        
class UserSolution(Solution):
    
    def __init__(self, node_id: int, bw_in: int, bw_out: int, size: int, level: int, graph: List[List[int]],
                 nodes_info: List[Tuple[int, int, int, int, int]]):
        super().__init__(node_id, bw_in, bw_out, size, level, graph, nodes_info)
        self.SwitchStatsInfo = UserSwitchStatsInfo(node_id)
        
    #the access node will receive request and divide into messages   
    def add_request_list(self, request_list: List[Request]) -> None:
        # Remember to update your buffer
        pass


    #1. It takes neigbours SwitchStatsInfo (including cluster controller)
    #2. Updates its own SwitchStatsInfo, such as buffer size 
    #3. The method needs to make a decision of which  path to send
    #4. and the simulator will return a message than contains all the successful and fails one
    def ask_round_solution(self, neighbor_info_list: List[SwitchStatsInfo]) -> List[Message]:
        
        
        return []



        
        
    # 1. take result: List[Tuple[Message, bool]]
    # 2. decode and update it to SwitchStatsInfo, the SwicthStatsInfo should be coincides with message
    # 3. return SwitchStatsInfo(including cluster controller)
    def next_round(self, result: List[Tuple[Message, bool]]) -> SwitchStatsInfo:
        #count for success and fail messages
        success, fail = 0,0
        for message_result in result:
            if message_result[1]==True:
                success+=1
            else:
                fail+=1
        
        
                # Information communication between node

        #cluster controller, actually won't get any result
        if self.level==4:
            pass
        
        #other nodes
        else:
            
            
        return SwitchStatsInfo()

