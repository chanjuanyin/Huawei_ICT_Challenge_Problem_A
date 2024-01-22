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

# Finding Neighbour & Paths
class FindReachable:
    def __init__(self, node_id, level, graph, node_info): # neighbors=None):
        self.node_id = node_id
        self.level = level
        self.graph = List[List[int]]
        self.node_info = List[Tuple[int, int, int, int, int]]

        # Check the level of the node and create attributes accordingly
        if self.level == 1:
            self.level_0_reachable = []
            self.level_2_reachable = []
            self.level_3_reachable = []
            
            self.if_I_am_level_1()

        elif self.level == 2:
            self.level_1_reachable = []
            self.level_3_reachable = []
            self.level_0_reachable = []
            
            self.if_I_am_level_2()

        elif self.level == 3:
            self.level_2_reachable = []
            self.level_1_reachable = []
            self.level_0_reachable = []
            
            self.if_I_am_level_3()
            
            
    def if_I_am_level_1(self):
        # Iterate through immediate neighbors
        for i in range(len(self.graph[0])):
            c = self.graph[self.node_id][i]
            if c == 1 and i != self.node_id:
                k = self.node_info[i][1]
                if k == 0:
                    self.level_0_reachable.append(i)
                else:
                    self.level_2_reachable.append(i)
              
        # Iterate through connected nodes at level 2
        for j in self.level_2_reachable:
            for i in range(len(self.graph[0])):
                c = self.graph[j][i]
                if c == 1 and i != j:
                    k = self.node_info[i][1]
                    if k == 3:
                        self.level_3_reachable.append(i)
        
    def if_I_am_level_2(self):
        # Iterate through immediate neighbors
        for i in range(len(self.graph[0])):
            c = self.graph[self.node_id][i]
            if c == 1 and i != self.node_id:
                k = self.node_info[i][1]
                if k == 1:
                    self.level_1_reachable.append(i)
                else:
                    self.level_3_reachable.append(i)
        
        # Iterate through connected nodes at level 1
        for j in self.level_1_reachable:
            for i in range(len(self.graph[0])):
                c = self.graph[j][i]
                if c == 1 and i != j:
                    k = self.node_info[i][1]
                    if k == 0:
                        self.level_0_reachable.append(i)
    
    def if_I_am_level_3(self):
        # Iterate through immediate neighbors
        for i in range(len(self.graph[0])):
            c = self.graph[self.node_id][i]
            if c == 1 and i != self.node_id:
                k = self.node_info[i][1]
                if k == 2:
                    self.level_2_reachable.append(i)
        
        # Iterate through connected nodes at level 2
        for j in self.level_2_reachable:
            for i in range(len(self.graph[0])):
                c = self.graph[j][i]
                if c == 1 and i != j:
                    k = self.node_info[i][1]
                    if k == 1:
                        self.level_1_reachable.append(i)
                        
        # Iterate through connected nodes at level 1
        for j in self.level_1_reachable:
            for i in range(len(self.graph[0])):
                c = self.graph[j][i]
                if c == 1 and i != j:
                    k = self.node_info[i][1]
                    if k == 0:
                        self.level_0_reachable.append(i)
    

#Below three classes if for rewriting and defining all the classes in message.py

class UserRequest:
    def __init__(self, request_id: int, target_node_id: int, request_begin_time: int):
        self.request_id: int = request_id # MajorId
        self.target_node_id: int = target_node_id
        self.request_begin_time: int = request_begin_time
        self.message_id: List[int] = [] # MinorId
    def insert_message(self, int_list: List[int]):
        merged_list=list(set(int_list) | set(self.message_id))
        self.message_id=merged_list
        
    def delete_message(self,int_list: List[int]):
        deleted_list=list(set(self.message_id)-set(int_list))
        self.message_id=deleted_list

class UserRequest(Request):
    def __init__(self, source_node_id=0, target_node_id=0, data_size=0, begin_time=0, request_id=0):
        super().__init__(source_node_id, target_node_id, data_size, begin_time, request_id)


"""I think every message should use a Major Id - Minor Id to index it"""
class UserMessage(Message):
    def __init__(self, from_id: int, to_id: int, target_node_id: int, request_id: int, message_id: int,
                 request_begin_time: int):
        super().__init__(from_id, to_id, target_node_id, request_id, message_id, request_begin_time)



"""define SwtichsStatsInfo here or just create another class in this file
what to do   1.  a controler view of SwitchStatsInfo, including
                    First node:
                    1.1.1 identifier for controller, index 2555     bitsize=8
                                                                    total bitsize=8
                    Rest of nodes at t=j-2:
                    1.2.1 all node remaining buffer                 bitsize=11
                    1.2.2 all nodes remaining inbound               bitsize=10
                    1.2.3 and all nodes remaining outbound          bitsize=8
                                                                    total bitsize=29
                                                                    
                2.  a normal node view of SwitchStatsInfo at t=j including 
                    part A what and who have I sent last time slice
                    First one out of 256 integers:
                    2.1.1 identify myself                                         bitsize=8
                    2.1.2 remaining outbound  t=j                                 bitsize=8
                    2.1.3 new request added into you    t=j                       bitsize=11
                    
                    Rest of 255 integers
                    For successful messages at t=j:
                    2.2.1 where the message will send to, to_node_id                            bitsize=8
                    2.2.2 final destination, target_node_id                                     bitsize=8
                    2.2.3 Request Id(Major Id) that I send                                      bitsize=13
                    2.2.4 from minor id (7 bits), to minor id (7 bits), continue read? (1 bit)  bitsize=15 X number of messages
                    
                    For failure messages at t=j:
                    2.3.1 where the message will send to, to_node_id                            bitsize=8
                    2.2.2 255 to denote you failed                                              bitsize=8
                    Just ignore:
                    2.4.1 255 to denote please don't read                                       bitsize=8

                        
                    2.x maybe node_info for the first time slice
"""

        
class UserSolution(Solution):
    
    def __init__(self, node_id: int, bw_in: int, bw_out: int, size: int, level: int, graph: List[List[int]],
                 nodes_info: List[Tuple[int, int, int, int, int]]):
        super().__init__(node_id, bw_in, bw_out, size, level, graph, nodes_info)
        nodes_info = sorted(nodes_info, key=lambda x: x[0])
        
        if nodes_info[0][0]==-1:
            nodes_info = nodes_info[1:]
        
        # Newspaper broadcasted by controller and each individual node will update their copy of the newspaper after hearing from controller's news reporting
        self.node_info_update_newspaper = []
        for i in range(len(graph[0])):
            new_node = NodePlaceholder(nodes_info[i][0], nodes_info[i][1], nodes_info[i][4], nodes_info[i][2], nodes_info[i][3], 
                 nodes_info[i][4], nodes_info[i][2], nodes_info[i][3])
            self.node_info_update_newspaper.append(new_node)
        
        # Your record of the request-messages: a giant library
        self.requests_messages_you_possess = {} # {request_id: UserRequest object}
        
        # Information that you know tonight before you sleep / tomorrow morning soon after you wake up
        self.remaining_outbound_of_myself = self.bw_out # Night
        self.remaining_buffer_of_myself = self.size # Morning
        
        # Find reachable (shing's work)
        self.find_reachable = []
        for i in range(len(graph[0])):
            find_reachable_object = FindReachable(nodes_info[i][0], nodes_info, graph, nodes_info)
            self.find_reachable.append(find_reachable_object)
        
    # Shing's work
    # the access node will receive request and divide into messages   
    def add_request_list(self, request_list: List[Request]) -> None:
        # Iterate through every request in List[Request]
        # # For each request, first check if self.remaining_buffer_of_myself >= new request's size 
        # If <, then ignore this entire request. Yes this will be detrimental to our success rate (hence our final score), but bopian
        # If >=, then you can add the new request
        #   How to add? You first create an object
        #   user_request_object = UserRequest(a bunch of parameters you input for yourself)
        #   then, you will do:
        #   self.requests_messages_you_possess[your new request id that you should know] = user_request_object
        #   last step, you will need to update your buffer by doing:
        #   self.remaining_buffer_of_myself -= new request's size 
        #   Everything in this indentation is within the >= logic of the if-else statement
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
            pass
            
        return SwitchStatsInfo()
    
        
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

