from typing import List, Tuple
from solution_common.message import Message, Request, SwitchStatsInfo
from solution_common.solution import Solution


#this class serves for the node information 101 for each node
class NodePlaceholder:

    def __init__(self, node_id, level, buffer_size, incoming_bandwidth, outgoing_bandwidth, 
                 remaining_buffer, remaining_inbound, remaining_outbound):
        # Instance attributes
        self.node_id = node_id
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
        self.graph = graph
        self.node_info = node_info

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
        
        self.level_0_reachable = set(self.level_0_reachable)
        self.level_0_reachable = sorted(self.level_0_reachable)
        self.level_2_reachable = set(self.level_2_reachable)
        self.level_2_reachable = sorted(self.level_2_reachable)
              
        # Iterate through connected nodes at level 2
        for j in self.level_2_reachable:
            for i in range(len(self.graph[0])):
                c = self.graph[j][i]
                if c == 1 and i != j:
                    k = self.node_info[i][1]
                    if k == 3:
                        self.level_3_reachable.append(i)
        
        self.level_3_reachable = set(self.level_3_reachable)
        self.level_3_reachable = sorted(self.level_3_reachable)
        
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
        
        self.level_1_reachable = set(self.level_1_reachable)
        self.level_1_reachable = sorted(self.level_1_reachable)
        self.level_3_reachable = set(self.level_3_reachable)
        self.level_3_reachable = sorted(self.level_3_reachable)
        
        # Iterate through connected nodes at level 1
        for j in self.level_1_reachable:
            for i in range(len(self.graph[0])):
                c = self.graph[j][i]
                if c == 1 and i != j:
                    k = self.node_info[i][1]
                    if k == 0:
                        self.level_0_reachable.append(i)
        
        self.level_0_reachable = set(self.level_0_reachable)
        self.level_0_reachable = sorted(self.level_0_reachable)
    
    def if_I_am_level_3(self):
        # Iterate through immediate neighbors
        for i in range(len(self.graph[0])):
            c = self.graph[self.node_id][i]
            if c == 1 and i != self.node_id:
                k = self.node_info[i][1]
                if k == 2:
                    self.level_2_reachable.append(i)
        
        self.level_2_reachable = set(self.level_2_reachable)
        self.level_2_reachable = sorted(self.level_2_reachable)
        
        # Iterate through connected nodes at level 2
        for j in self.level_2_reachable:
            for i in range(len(self.graph[0])):
                c = self.graph[j][i]
                if c == 1 and i != j:
                    k = self.node_info[i][1]
                    if k == 1:
                        self.level_1_reachable.append(i)
        
        self.level_1_reachable = set(self.level_1_reachable)
        self.level_1_reachable = sorted(self.level_1_reachable)
                        
        # Iterate through connected nodes at level 1
        for j in self.level_1_reachable:
            for i in range(len(self.graph[0])):
                c = self.graph[j][i]
                if c == 1 and i != j:
                    k = self.node_info[i][1]
                    if k == 0:
                        self.level_0_reachable.append(i)
        
        self.level_0_reachable = set(self.level_0_reachable)
        self.level_0_reachable = sorted(self.level_0_reachable)
    

#Below three classes if for rewriting and defining all the classes in message.py

class UserRequest:
    def __init__(self, request_id: int, target_node_id: int, request_begin_time: int):
        self.request_id: int = request_id # MajorId
        self.target_node_id: int = target_node_id
        self.request_begin_time: int = request_begin_time
        self.message_id: List[int] = [] # MinorId
    def insert_message(self, int_list: List[int]):
        merged_list=list(set(int_list) | set(self.message_id))
        self.message_id=sorted(merged_list)
        
    def delete_message(self,int_list: List[int]):
        deleted_list=list(set(self.message_id)-set(int_list))
        self.message_id=sorted(deleted_list)


"""define SwtichsStatsInfo here or just create another class in this file
what to do   1.  a controler view of SwitchStatsInfo, including
                    First node:
                    1.1.1 identifier for controller, index 255      bitsize=8
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
                    2.1.3 new request added into you    t=j                       bitsize=11 line 207
                    
                    Rest of 255 integers
                    For successful messages at t=j:
                    2.2.1 where the message will send to, to_node_id                            bitsize=8
                    2.2.2 final destination, target_node_id                                     bitsize=8
                    2.2.3 Request Id(Major Id) that I send                                      bitsize=13
                                                                                                total bitsize=29
                    2.2.4 Request begin time from 0 to 200                                      bitsize=8 + 7 blank space
                    2.2.5 from minor id (7 bits), to minor id (7 bits), continue read? (1 bit)  bitsize=15 X number of messages
                    
                    For failure messages at t=j:
                    2.3.1 where the message will send to, to_node_id                            bitsize=8
                    2.3.2 255 to denote you failed                                              bitsize=8
                    2.3.3 how many you failed                                                   bitsize=8
                    Just ignore:
                    2.4.1 255 to denote please don't read                                       bitsize=8

                3.  SwitchStatsInfo if I am level 0
                    First one out of 256 integers:
                    3.1.1 identify myself as 254                                                bitsize=8
                    
                    
                    2.x maybe node_info for the first time slice
"""

        
class UserSolution(Solution):
    
    def __init__(self, node_id: int, bw_in: int, bw_out: int, size: int, level: int, graph: List[List[int]],
                 nodes_info: List[Tuple[int, int, int, int, int]]):
        super().__init__(node_id, bw_in, bw_out, size, level, graph, nodes_info)
        
        # nodes_info: List[Tuple[int, int, int, level, node_id]]
        # 
        # Our original thinking (also this is the ordering of our self-defined self.nodes_info):
        # Position 0: node_id
        # Position 1: level
        # Position 2: inbound_bandwidth
        # Position 3: outbound_bandwidth
        # Position 4: buffer_size
        # 
        # Reality:
        # Position 0: inbound_bandwidth
        # Position 1: outbound_bandwidth
        # Position 2: buffer_size
        # Position 3: level
        # Position 4: node_id
        # 
        # Level in nodes_info only range from 0 to 3 inclusive, does not contain a node whose level is 4
        # node_id in nodes_info starts from 0 and to N-1 (N is number of nodes excluding controller)
        # so nodes_info shouldn't contain the controller
        #
        # Also nodes_info is sorted in terms of the position 4 element node_id, in ascending order
        # 
        # We have also verified that len(graph) == len(nodes_info) and len(graph[0]) == len(nodes_info)
        # Therefore we can conclude that graph doesn't contain the controller
        
        nodes_info_2 = []
        for tup in nodes_info:
            tup2 = (tup[4], tup[3], tup[0], tup[1], tup[2])
            nodes_info_2.append(tup2)
        nodes_info_2 = sorted(nodes_info_2, key=lambda x: x[0])
        self.nodes_info = nodes_info_2
        
        # Newspaper broadcasted by controller and each individual node will update their copy of the newspaper after hearing from controller's news reporting
        self.node_info_update_newspaper = []
        for tup in self.nodes_info:
            new_node = NodePlaceholder(node_id=tup[0],
                                       level=tup[1],
                                       incoming_bandwidth=tup[2],
                                       outgoing_bandwidth=tup[3],
                                       buffer_size=tup[4],
                                       remaining_inbound=tup[2],
                                       remaining_outbound=tup[3],
                                       remaining_buffer=tup[4]
                                       )
            self.node_info_update_newspaper.append(new_node)
        
        # Your record of the request-messages: a giant library
        self.requests_messages_you_possess = {} # {request_id: UserRequest object}
        
        # Information that you know tonight before you sleep / tomorrow morning soon after you wake up
        self.remaining_outbound_of_myself = self.bw_out # Night
        self.remaining_buffer_of_myself = self.size # Morning
        self.new_messages_success_added_count = 0
        self.new_messages_temporary_storage = []
        # Find reachable (shing's work)
        self.find_reachable = []
        for tup in self.nodes_info:
            find_reachable_object = FindReachable(tup[0], tup[1], self.graph, self.nodes_info)
            self.find_reachable.append(find_reachable_object)
        
    # Shing's work
    # the access node will receive request and divide into messages   
    def add_request_list(self, request_list: List[Request]) -> None:
        for new_request in request_list:
            user_request_object = UserRequest(new_request.request_id, new_request.target_node_id, new_request.begin_time)
            user_request_object.message_id = [i for i in range(new_request.data_size)]
            self.new_messages_temporary_storage.append(user_request_object)
            
        # Iterate through every request in List[Request]
        # # For each request, first check if self.remaining_buffer_of_myself >= new request's size 
        # If <, then ignore this entire request. Yes this will be detrimental to our success rate (hence our final score), but bopian
        # If >=, then you can add the new request
        #   How to add? You first create an object
        #   user_request_object = UserRequest(a bunch of parameters you input for yourself)
        #   then, you will do:
        #   self.requests_messages_you_possess[your new request id that you should know] = user_request_object
        #   (FYI, self.requests_messages_you_possess is a dictionary, look at line 199)
        #   last step, you will need to update your buffer by doing:
        #   self.remaining_buffer_of_myself -= new request's size 
        #   Everything in this indentation is within the >= logic of the if-else statement
        pass

    #pre-define : neighbor_info_list for normal node
    #1. Normal node takes controller's newspaper and updates its own newspaper to current
    #2  Normal node will take neibours' SwitchStatsInfos
    #2. The normal node needs to make a decision: List[Message] of which path to send
    #3. And the simulator will return a message than contains all the successful and fails one
    #4. Controller updates its own newspaper, such as buffer size 
    #5. Normal nodes will updates its own SwitchStatInfo
    def ask_round_solution(self, neighbor_info_list: List[SwitchStatsInfo]) -> List[Message]:
        def bin_tran(num):
            return format(num, '032b')
        # If you are level 1, 2, 3
        if self.level == 1 or self.level == 2 or self.level == 3:
            for switchStatsInfo in neighbor_info_list:
                if len(switchStatsInfo.info) == 0:
                    continue
                
                sender_node_id = int(bin_tran(switchStatsInfo.info[0])[1:9],2)  # 0xFF000000>>1 ; >>23
                
                # A normal node receiving news reporting from the controller
                if sender_node_id == 255:
                    for node_id, node_news_update_int in enumerate(switchStatsInfo.info[1:len(self.graph[0])+1]):
                        remaining_buffer = int( bin_tran(node_news_update_int)[1:12] , 2)   #(0xFFE00000>>1)) >> 20 
                        remaining_inbound = int( bin_tran(node_news_update_int)[1:22],2)  #(0x1FF800>>1)) >> 10
                        remaining_outbound = int( bin_tran(node_news_update_int)[1:30] ,2)   # (0x7F8>>1)) >> 2
                        self.node_info_update_newspaper[node_id].remaining_buffer = remaining_buffer
                        self.node_info_update_newspaper[node_id].remaining_inbound = remaining_inbound
                        self.node_info_update_newspaper[node_id].remaining_outbound = remaining_outbound
                
                # Server at level 0 speaking
                elif sender_node_id == 254:
                    continue
                
                # A normal node receiving messages from ohter normal nodes
                else:
                    continue_read = True
                    counting_receive_success = 0
                    integer_to_read_index = 1
                    while continue_read:
                        integer_to_read = switchStatsInfo.info[integer_to_read_index]
                        request_message_recipient = int( bin_tran(integer_to_read)[1:9],2)  #(0xFF000000>>1)) >> 23
                        if request_message_recipient == 255:
                            continue_read = False
                            break
                        target_node_id = int( bin_tran(integer_to_read)[1:17],2)   #(0x00FF0000>>1)) >> 15
                        if target_node_id == 255:
                            integer_to_read_index += 1
                            continue
                        else:
                            request_id = int( bin_tran(integer_to_read)[1:30],2) #0x0000FFF8>>1)) >> 2
                            request_begin_time = int( bin_tran(switchStatsInfo.info[integer_to_read_index+1])[1:9] ,2) #(0xFF000000>>1)) >> 23
                            new_user_request = UserRequest(request_id, target_node_id, request_begin_time)
                            integer_to_read_index += 1
                            message_from = int( bin_tran(switchStatsInfo.info[integer_to_read_index])[1:23],2)  #(0x1FC00>>1)) >> 9
                            message_to = int( bin_tran(switchStatsInfo.info[integer_to_read_index])[1:30],2)   #(0x3F8>>1)) >> 2
                            new_user_request.insert_message(list(range(message_from, message_to)))
                            continue_read_2 = int( bin_tran(switchStatsInfo.info[integer_to_read_index])[1:31],2)   #(0x4>>1)) >> 1
                            integer_to_read_index += 1
                            while continue_read_2:
                                message_from = int( bin_tran(switchStatsInfo.info[integer_to_read_index])[1:8],2) #(0xFE000000>>1)) >> 24
                                message_to = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:15],2)  #(0x1FC0000>>1)) >> 17
                                new_user_request.insert_message(list(range(message_from, message_to)))
                                continue_read_2 = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:16],2)  #(0x20000>>1)) >> 16
                                if continue_read_2==0:
                                    integer_to_read_index += 1
                                    continue
                                else:
                                    message_from = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:23] ,2) #(0x1FC00>>1)) >> 9
                                    message_to = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:30] , 2) # (0x3F8>>1)) >> 2
                                    new_user_request.insert_message(list(range(message_from, message_to)))
                                    continue_read_2 = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:31],2)  # & (0x4>>1)) >> 1
                                    integer_to_read_index += 1
                            if request_message_recipient == self.node_id:
                                if new_user_request.request_id not in self.requests_messages_you_possess:
                                    self.requests_messages_you_possess[new_user_request.request_id] = new_user_request
                                else:
                                    self.requests_messages_you_possess[new_user_request.request_id].insert_message(new_user_request.message_id)
                                counting_receive_success += len(new_user_request.message_id)
                    self.remaining_buffer_of_myself -= counting_receive_success
            # Add new requests here
            self.new_messages_success_added_count = 0
            for user_request_object in self.new_messages_temporary_storage:
                if self.remaining_buffer_of_myself < len(user_request_object.message_id): # Not enough storage
                    pass
                else: # enough storage
                    self.requests_messages_you_possess[user_request_object.request_id] = user_request_object
                    self.remaining_buffer_of_myself -= len(user_request_object.message_id)
                    self.new_messages_success_added_count + len(user_request_object.message_id)
            self.new_messages_temporary_storage = []
        
            return self.run_algorithm()
        
        # If you are controller
        elif self.level == 4:
            node_info_successfully_received = [0 for i in range(len(self.graph[0]))]
            node_info_failed_to_receive = [0 for i in range(len(self.graph[0]))]
            for switchStatsInfo in neighbor_info_list:
                if len(switchStatsInfo.info) == 0:
                    continue
                sender_node_id = int(bin_tran(switchStatsInfo.info[0])[1:9],2)  #(0xFF000000>>1)) >> 23
                if sender_node_id == 254:
                    continue
                sender_remaining_outbound = int(bin_tran(switchStatsInfo.info[0])[1:17],2) #(0x00FF0000>>1)) >> 15
                self.node_info_update_newspaper[sender_node_id].remaining_outbound = sender_remaining_outbound
                sender_received_new_requests = int(bin_tran(switchStatsInfo.info[0])[1:28],2)  #(0xFFE0>>1)) >> 4
                self.node_info_update_newspaper[sender_node_id].remaining_buffer -= sender_received_new_requests
                
                # Let me think
                continue_read = True
                integer_to_read_index = 1
                while continue_read:
                    integer_to_read = switchStatsInfo.info[integer_to_read_index]
                    request_message_recipient = int(bin_tran(integer_to_read)[1:9],2)  #(0xFF000000>>1)) >> 23
                    if request_message_recipient == 255:
                        continue_read = False
                        break
                    target_node_id = int(bin_tran(integer_to_read)[1:17],2)  #0x00FF0000>>1)) >> 15
                    if target_node_id == 255:
                        how_many_failed = int(bin_tran(integer_to_read)[1:25],2)  #(0x0000FF00>>1)) >> 7
                        node_info_failed_to_receive[request_message_recipient] += how_many_failed
                        integer_to_read_index += 1
                        continue
                    else:
                        request_id = int(bin_tran(integer_to_read)[1:30],2)  #(0x0000FFF8)>>1) >> 2 
                        request_begin_time = int(bin_tran(switchStatsInfo.info[integer_to_read_index+1])[1:9],2)  #(0xFF000000>>1)) >> 23
                        new_user_request = UserRequest(request_id, target_node_id, request_begin_time)
                        integer_to_read_index += 1
                        message_from = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:23],2)  #(0x1FC00>>1)) >> 9
                        message_to = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:30],2)  #(0x3F8>>1)) >> 2
                        new_user_request.insert_message(list(range(message_from, message_to)))
                        continue_read_2 = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:31],2) #(0x4>>1)) >> 1
                        integer_to_read_index += 1
                        while continue_read_2:
                            message_from = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:8],2) #(0xFE000000>>1)) >> 24
                            message_to = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:15],2) #(0x1FC0000>>1)) >> 17
                            new_user_request.insert_message(list(range(message_from, message_to)))
                            continue_read_2 = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:16],2)   #(0x20000>>1)) >> 16
                            if continue_read_2==0:
                                integer_to_read_index += 1
                                continue
                            else:
                                message_from = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:23],2) #(0x1FC00>>1)) >> 9
                                message_to = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:30],2) #(0x3F8>>1)) >> 2
                                new_user_request.insert_message(list(range(message_from, message_to)))
                                continue_read_2 = int(bin_tran(switchStatsInfo.info[integer_to_read_index])[1:31],2)  #(0x4>>1)) >> 1
                                integer_to_read_index += 1
                        self.node_info_update_newspaper[sender_node_id].remaining_buffer += len(new_user_request.message_id)
                        self.node_info_update_newspaper[request_message_recipient].remaining_buffer -= len(new_user_request.message_id)
                        node_info_successfully_received[request_message_recipient] += len(new_user_request.message_id)
                        
            for i in range(len(self.graph[0])):
                if node_info_successfully_received[i] >= self.node_info_update_newspaper[i].remaining_inbound: # Problem of not enough inbound bandwidth
                    pass
                else: # Problem of not enough buffer
                    self.node_info_update_newspaper[i].remaining_inbound = max(0, self.node_info_update_newspaper[i].remaining_inbound - node_info_failed_to_receive[i])
            
            return []

        else: # self.level == 0:
            return []
            
    
    # Guys, our algorithm is here
    def run_algorithm(self) -> List[Message]:
        # Run our algorithm here
        # Let me think think
        message_to_send = []
        remaining_messages_I_can_send = self.remaining_outbound_of_myself
        if self.level == 1:
            send_to_level_2_buffer_cap = 0.6                                    # Feel free to adjusta
            send_to_level_2_inbound_bandwidth_cap = 0.8                         # Feel free to adjust
            priority_1_list = [] # From level 1 directly to level 0
            priority_2_list = [] # From level 1 to level 2 then can reach back level 1 and level 0
            priority_3_list = [] # From level 1 to level 2 then level 3, then back to level 2 and back to level 1, and finally reach level 0
            for request_id, user_request_object in self.requests_messages_you_possess.items():
                if user_request_object.target_node_id in self.find_reachable[self.node_id].level_0_reachable:
                    priority_1_list.append((request_id, user_request_object.request_begin_time))
                else:
                    priority_2 = False
                    for level_2_node in self.find_reachable[self.node_id].level_2_reachable:
                        if user_request_object.target_node_id in self.find_reachable[level_2_node].level_0_reachable:
                            priority_2 = True
                            break
                    if priority_2:
                        priority_2_list.append((request_id, user_request_object.request_begin_time))
                    else:
                        priority_3_list.append((request_id, user_request_object.request_begin_time))
            priority_1_list = sorted(priority_1_list, key=lambda x: x[1]) # Sort by request_begin_time because we need to take care of the latency which is part of the scoring
            priority_2_list = sorted(priority_2_list, key=lambda x: x[1]) # Sort by request_begin_time because we need to take care of the latency which is part of the scoring
            priority_3_list = sorted(priority_3_list, key=lambda x: x[1]) # Sort by request_begin_time because we need to take care of the latency which is part of the scoring
            
            for tup in priority_1_list: # tup means tuple
                if remaining_messages_I_can_send > 0:
                    user_request_object = self.requests_messages_you_possess[tup[0]] # tup[0] is request_id
                    number_to_send = min(len(user_request_object.message_id), remaining_messages_I_can_send)
                    for i in range(number_to_send):
                        message = Message(self.node_id, user_request_object.target_node_id, user_request_object.target_node_id, 
                                          user_request_object.request_id, user_request_object.message_id[i], user_request_object.request_begin_time)
                        message_to_send.append(message)
                        remaining_messages_I_can_send -= 1
            
            for tup in priority_2_list: # tup means tuple
                if remaining_messages_I_can_send > 0:
                    user_request_object = self.requests_messages_you_possess[tup[0]] # tup[0] is request_id
                    how_much_I_can_send = min(len(user_request_object.message_id), remaining_messages_I_can_send)
                    my_level_2_recipients = []
                    for level_2_node in self.find_reachable[self.node_id].level_2_reachable:
                        if user_request_object.target_node_id in self.find_reachable[level_2_node].level_0_reachable:
                            my_level_2_recipients.append(level_2_node)
                    my_level_2_recipients_how_much_they_can_eat = {} # {level_2_node: how_much_one_can_eat}
                    for level_2_node in my_level_2_recipients:
                        # Reading newspaper
                        how_much_one_can_eat = min(int(self.node_info_update_newspaper[level_2_node].remaining_buffer - self.node_info_update_newspaper[level_2_node].buffer_size * (1-send_to_level_2_buffer_cap)), 
                                                   int(self.node_info_update_newspaper[level_2_node].remaining_inbound * send_to_level_2_inbound_bandwidth_cap))
                        how_much_one_can_eat = max(how_much_one_can_eat, 0) # prevent it from going negative
                        my_level_2_recipients_how_much_they_can_eat[level_2_node] = how_much_one_can_eat
                    my_level_2_recipients_how_much_they_can_eat_in_total = 0
                    for level_2_node, how_much_one_can_eat in my_level_2_recipients_how_much_they_can_eat.items():
                        my_level_2_recipients_how_much_they_can_eat_in_total += how_much_one_can_eat
                    if my_level_2_recipients_how_much_they_can_eat_in_total <= how_much_I_can_send:
                        # I can send more than they can eat, so the number I will send is exactly how much each of them can eat
                        # No need to allocate
                        my_level_2_recipients_how_much_I_allocate = my_level_2_recipients_how_much_they_can_eat
                    else: #my_level_2_recipients_how_much_they_can_eat_in_total > how_much_I_can_send
                        # Need to allocate, very mafan one , yes I agree 
                        # Allocate according to the ratio of how much they can eat
                        # Beause you want to spread out to more level 2 nodes
                        my_level_2_recipients_how_much_I_allocate = {}
                        my_level_2_recipients_how_much_I_allocate_in_total = 0
                        for level_2_node, how_much_one_can_eat in my_level_2_recipients_how_much_they_can_eat.items():
                            how_much_I_allocate = int( (my_level_2_recipients_how_much_they_can_eat[level_2_node] / my_level_2_recipients_how_much_they_can_eat_in_total) * how_much_I_can_send )
                            my_level_2_recipients_how_much_I_allocate[level_2_node] = how_much_I_allocate
                            my_level_2_recipients_how_much_I_allocate_in_total += how_much_I_allocate
                        # Handle situation where my_level_2_recipients_how_much_I_allocate_in_total != how_much_I_can_send 
                        # Due to existence of some remainders due to rounding down / rounding up
                        while my_level_2_recipients_how_much_I_allocate_in_total < how_much_I_can_send: # Some remainders due to rounding down / rounding up
                            # Just randomly allocate to the level_2_nodes
                            for level_2_node, how_much_I_allocate in my_level_2_recipients_how_much_I_allocate.items():
                                if my_level_2_recipients_how_much_I_allocate_in_total < how_much_I_can_send: # Some remainder due to rounding down / rounding up
                                    my_level_2_recipients_how_much_I_allocate[level_2_node] += 1
                                    my_level_2_recipients_how_much_I_allocate_in_total += 1
                                else:
                                    break
                        while my_level_2_recipients_how_much_I_allocate_in_total > how_much_I_can_send: # Some remainders due to rounding down / rounding up
                            # Just randomly allocate to the level_2_nodes
                            for level_2_node, how_much_I_allocate in my_level_2_recipients_how_much_I_allocate.items():
                                if my_level_2_recipients_how_much_I_allocate_in_total > how_much_I_can_send: # Some remainders due to rounding down / rounding up
                                    my_level_2_recipients_how_much_I_allocate[level_2_node] -= 1
                                    my_level_2_recipients_how_much_I_allocate_in_total -= 1
                                else:
                                    break
                    # So now we have finished allocation and the dictionary my_level_2_recipients_how_much_I_allocate is now ready
                    # Also how much I allocate in total is guaranteed to be <= how_much_I_can_send
                    # So now I will send messages (means now I will put messages into message_to_send list)
                    index = 0
                    for level_2_node, how_much_I_allocate in my_level_2_recipients_how_much_I_allocate.items():
                        while how_much_I_allocate > 0:
                            message = Message(self.node_id, level_2_node, user_request_object.target_node_id, 
                                                user_request_object.request_id, user_request_object.message_id[index], user_request_object.request_begin_time)
                            message_to_send.append(message)
                            remaining_messages_I_can_send -= 1
                            how_much_I_allocate -= 1
                            index += 1
                    
            for tup in priority_3_list: # tup means tuple
                if remaining_messages_I_can_send > 0:
                    user_request_object = self.requests_messages_you_possess[tup[0]] # tup[0] is request_id
                    how_much_I_can_send = min(len(user_request_object.message_id), remaining_messages_I_can_send)
                    my_level_2_recipients = []
                    for level_2_node in self.find_reachable[self.node_id].level_2_reachable:
                        reachable = False
                        for level_3_node in self.find_reachable[level_2_node].level_3_reachable:
                            if user_request_object.target_node_id in self.find_reachable[level_3_node].level_0_reachable:
                                reachable = True
                                break
                        if reachable:
                            my_level_2_recipients.append(level_2_node)
                    my_level_2_recipients_how_much_they_can_eat = {} # {level_2_node: how_much_one_can_eat}
                    for level_2_node in my_level_2_recipients:
                        # Reading newspaper
                        how_much_one_can_eat = min(int(self.node_info_update_newspaper[level_2_node].remaining_buffer - self.node_info_update_newspaper[level_2_node].buffer_size * (1-send_to_level_2_buffer_cap)), 
                                                   int(self.node_info_update_newspaper[level_2_node].remaining_inbound * send_to_level_2_inbound_bandwidth_cap))
                        how_much_one_can_eat = max(how_much_one_can_eat, 0) # prevent it from going negative
                        my_level_2_recipients_how_much_they_can_eat[level_2_node] = how_much_one_can_eat
                    my_level_2_recipients_how_much_they_can_eat_in_total = 0
                    for level_2_node, how_much_one_can_eat in my_level_2_recipients_how_much_they_can_eat.items():
                        my_level_2_recipients_how_much_they_can_eat_in_total += how_much_one_can_eat
                    if my_level_2_recipients_how_much_they_can_eat_in_total <= how_much_I_can_send:
                        # I can send more than they can eat, so the number I will send is exactly how much each of them can eat
                        # No need to allocate
                        my_level_2_recipients_how_much_I_allocate = my_level_2_recipients_how_much_they_can_eat
                    else: #my_level_2_recipients_how_much_they_can_eat_in_total > how_much_I_can_send
                        # Need to allocate, very mafan one
                        # Allocate according to the ratio of how much they can eat
                        # Beause you want to spread out to more level 2 nodes
                        my_level_2_recipients_how_much_I_allocate = {}
                        my_level_2_recipients_how_much_I_allocate_in_total = 0
                        for level_2_node, how_much_one_can_eat in my_level_2_recipients_how_much_they_can_eat.items():
                            how_much_I_allocate = int( (my_level_2_recipients_how_much_they_can_eat[level_2_node] / my_level_2_recipients_how_much_they_can_eat_in_total) * how_much_I_can_send )
                            my_level_2_recipients_how_much_I_allocate[level_2_node] = how_much_I_allocate
                            my_level_2_recipients_how_much_I_allocate_in_total += how_much_I_allocate
                        # Handle situation where my_level_2_recipients_how_much_I_allocate_in_total != how_much_I_can_send 
                        # Due to existence of some remainders due to rounding down / rounding up
                        while my_level_2_recipients_how_much_I_allocate_in_total < how_much_I_can_send: # Some remainders due to rounding down / rounding up
                            # Just randomly allocate to the level_2_nodes
                            for level_2_node, how_much_I_allocate in my_level_2_recipients_how_much_I_allocate.items():
                                if my_level_2_recipients_how_much_I_allocate_in_total < how_much_I_can_send: # Some remainder due to rounding down / rounding up
                                    my_level_2_recipients_how_much_I_allocate[level_2_node] += 1
                                    my_level_2_recipients_how_much_I_allocate_in_total += 1
                                else:
                                    break
                        while my_level_2_recipients_how_much_I_allocate_in_total > how_much_I_can_send: # Some remainders due to rounding down / rounding up
                            # Just randomly allocate to the level_2_nodes
                            for level_2_node, how_much_I_allocate in my_level_2_recipients_how_much_I_allocate.items():
                                if my_level_2_recipients_how_much_I_allocate_in_total > how_much_I_can_send: # Some remainders due to rounding down / rounding up
                                    my_level_2_recipients_how_much_I_allocate[level_2_node] -= 1
                                    my_level_2_recipients_how_much_I_allocate_in_total -= 1
                                else:
                                    break
                    # So now we have finished allocation and the dictionary my_level_2_recipients_how_much_I_allocate is now ready
                    # Also how much I allocate in total is guaranteed to be <= how_much_I_can_send
                    # So now I will send messages (means now I will put messages into message_to_send list)
                    index = 0
                    for level_2_node, how_much_I_allocate in my_level_2_recipients_how_much_I_allocate.items():
                        while how_much_I_allocate > 0:
                            message = Message(self.node_id, level_2_node, user_request_object.target_node_id, 
                                                user_request_object.request_id, user_request_object.message_id[index], user_request_object.request_begin_time)
                            message_to_send.append(message)
                            remaining_messages_I_can_send -= 1
                            how_much_I_allocate -= 1
                            index += 1
        
        elif self.level == 2:
            
            pass
        
        elif self.level == 3:
            
            pass
        
        return message_to_send
        
    # 1. take result: List[Tuple[Message, bool]] and extract out the Message
    # 2. create success dict and fail dict 
    # 2. decode the message and update the SwitchStatsInfo for different levels
    # 3. return SwitchStatsInfo
    def next_round(self, result: List[Tuple[Message, bool]]) -> SwitchStatsInfo:             
        def bin_tran(num):
            return format(num, '032b')
        def get_minor_id_range_list(userRequest):
            minor_id_range_list = [] # It is a list of list, every list inside will be minor id to minor id for one request
            message_id_list = userRequest.message_id
            slow , fast = 0 ,0
            while fast < len(message_id_list):
                message_id_fast = message_id_list[fast]
                while fast < len(message_id_list) and message_id_fast in message_id_list:
                    message_id_fast += 1
                    fast += 1
                minor_id_range_list.append([message_id_list[slow],message_id_list[fast-1]+1])
                slow = fast
            return minor_id_range_list
        def convert_to_signed_int(bin_str):
            # Convert the binary string to an integer
            num = int("0" + bin_str[:-1], 2)
            return num

        if self.level == 1 or self.level == 2 or self.level == 3:        
            #count for success and fail messages
            success = 0
            fail = 0
            for message_result in result:
                if message_result[1]==True:
                    success+=1
                else:
                    fail+=1
                    
            """Define and append the success_dict and fail_dict"""
            success_dict={} #success_dict = {to_node_id : {request_id : UserRequest Object} , , , ,}
            fail_dict={} #fail_dict = {to_node_id : counts}
            #append success dict
            for pair in result:
                Message=pair[0]
                bool=pair[1]
                if bool:
                    if Message.to_node_id not in success_dict:
                        success_dict[Message.to_node_id] = {}
                    else:
                        request_id_dict = success_dict[Message.to_node_id]
                        if Message.request_id not in request_id_dict:
                            request_id_dict[Message.request_id] = UserRequest(Message.request_id, Message.target_node_id, Message.request_begin_time)
                            request_id_dict[Message.request_id].message_id.append(Message.message_id)
                        else:
                            request_id_dict[Message.request_id].message_id.append(Message.message_id)
                    self.requests_messages_you_possess[Message.request_id].delete_message([Message.message_id])
                    self.remaining_buffer_of_myself += 1
                else:#append fail dict
                    if Message.to_node_id not in fail_dict:
                        fail_dict[Message.to_node_id] = 1
                    else:
                        fail_dict[Message.to_node_id] += 1
            
            """Define and update normal node SwtichStatsInfo"""
            switchStatsInfo = [0 for i in range(256)]
            integer_index = 0
            """2.1.1 to 2.1.3 the first integer"""
            bin_first_int = bin_tran(switchStatsInfo[integer_index])
            self.remaining_outbound_of_myself -= fail
            bin_first_int = bin_tran(self.node_id)[24:] + bin_first_int[8:] #[0:8]
            bin_first_int = bin_first_int[0:8] + bin_tran(self.remaining_outbound_of_myself)[24:] + bin_first_int[16:] #[8:16]
            if self.level == 1: #take care of the access level
                bin_first_int = bin_first_int[0:16] + bin_tran(self.new_messages_success_added_count)[21:] + "00000" #[16:]
            else: #level =2 , 3
                bin_first_int = bin_first_int[0:16] + "0" * 16  #[16:]
            switchStatsInfo[integer_index] = convert_to_signed_int(bin_first_int)
            integer_index += 1
            """2.2.1 to 2.2.5"""     
            #two for loop, the outer loop is different to_node_id
            #              the inner loop is different request_id   
            for to_node_id, request_id_dict in success_dict.items():
                for request_id, userRequest in request_id_dict.items():
                    # 2.2.1 to 2.2.3
                    integer_value = switchStatsInfo[integer_index]
                    integer_value_bin = bin_tran(integer_value)
                    integer_value_bin = bin_tran(to_node_id)[24:] + bin_first_int[8:] #[0:8]
                    integer_value_bin = bin_first_int[0:8] + bin_tran(userRequest.target_node_id)[24:] + bin_first_int[16:]  #[8:16]
                    integer_value_bin = integer_value_bin[0:16] + bin_tran(request_id)[19:] + integer_value_bin[29:] #[16:29]
                    integer_value_bin = integer_value_bin[0:29] + "000"   #[29:]
                    switchStatsInfo[integer_index] = convert_to_signed_int(integer_value_bin)
                    integer_index += 1
                    # 2.2.4 - 2.2.5
                    # the first 2.2.4 + 2.2.5 * 1
                    # the first 2.2.4
                    integer_value = switchStatsInfo[integer_index]
                    integer_value_bin = bin_tran(integer_value)
                    integer_value_bin = bin_tran(userRequest.request_begin_time)[24:] + integer_value_bin[8:] #[0:8]
                    integer_value_bin = integer_value_bin[0:8] + "0000000" + integer_value_bin[15:] #[8:15]
                    # the first 2.2.5 * 1
                    minor_id_range_list = get_minor_id_range_list(userRequest) # It is a list of list, every list inside will be minor id to minor id for one request
                    first_range = minor_id_range_list[0]
                    first_range_start = first_range[0]
                    first_range_end = first_range[1]
                    first_range_start_bit = bin_tran(first_range_start)
                    first_range_end_bit = bin_tran(first_range_end)
                    integer_value_bin = integer_value_bin[0:15] + first_range_start_bit[25:] + first_range_end_bit[25:] + integer_value_bin[29:] #[15:29]
                    if len(minor_id_range_list) > 1:
                        integer_value_bin = integer_value_bin[0:29] + "100"  #[29:]
                    else:
                        integer_value_bin = integer_value_bin[0:29] + "000" #[29:]
                    minor_id_range_list.pop(0)
                    switchStatsInfo[integer_index] = convert_to_signed_int(integer_value_bin)
                    integer_index += 1
                    #the rest of 2.2.5 * 2 * n
                    count_range = 0
                    integer_value = switchStatsInfo[integer_index]
                    integer_value_bin = bin_tran(integer_value)
                    for Range in minor_id_range_list: #Range is a list that have 2 element as i mentioned above
                        if count_range == 2:
                            switchStatsInfo[integer_index] = convert_to_signed_int(integer_value_bin[0:30] + "00")
                            integer_index += 1
                            integer_value = switchStatsInfo[integer_index]
                            integer_value_bin = bin_tran(integer_value)
                        start_range = Range[0]
                        end_range = Range[1]
                        start_range_bit = bin_tran(start_range)
                        end_range_bit = bin_tran(end_range)
                        #combine range is a 14 binary bit
                        combine_range = start_range_bit[25:] + end_range_bit[25:]
                        if minor_id_range_list[-1] == Range: # if there is no more Range
                            if count_range == 0:
                                integer_value_bin = combine_range + "0" + integer_value_bin[15:] #[0:15]
                                integer_value_bin = integer_value_bin[0:15] + "0" * 17 # [15:]
                                switchStatsInfo[integer_index] = convert_to_signed_int(integer_value_bin)
                                integer_index += 1
                            elif count_range == 1:
                                integer_value_bin = integer_value_bin[0:15] + combine_range + "0" + "00"   #[15:]
                                switchStatsInfo[integer_index] = convert_to_signed_int(integer_value_bin)
                                integer_index += 1
                            # if count_range == 0:
                                # integer_value_bin[15:] = "0" * 17
                                # switchStatsInfo[integer_index] = int(integer_value_bin , 2)
                                # integer_index += 1
                            # else:
                                # switchStatsInfo[integer_index] = int(integer_value_bin + "00" , 2)
                                # integer_index += 1
                        else:
                            if count_range ==0 :
                                integer_value_bin = combine_range + "1" + integer_value_bin[15:] #[0:15]
                            elif count_range == 1:
                                integer_value_bin = integer_value_bin[0:15] + combine_range + "1" + integer_value_bin[30:] #[15:30]
                        count_range += 1
                    
            for to_node_id, number_of_failure in fail_dict.items(): # add into your swtichStatsInfo to mention your failure
                integer_value = switchStatsInfo[integer_index]
                integer_value_bin = bin_tran(integer_value)
                integer_value_bin = bin_tran(to_node_id)[24:] + integer_value_bin[8:] #[0:8]
                integer_value_bin = integer_value_bin[0:8] + bin_tran(255)[24:] + integer_value_bin[16:] #[8:16]
                integer_value_bin = integer_value_bin[0:16] + bin_tran(number_of_failure)[24:] + integer_value_bin[24:] #[16:24]
                integer_value_bin = integer_value_bin[0:24] + "0" * 8 #[24:]
                switchStatsInfo[integer_index] = convert_to_signed_int(integer_value_bin)
                integer_index += 1
            
            
            for rest_integer_index in range(integer_index,256): # The rest of the integers to_node_id should make it to 255
                integer_index = rest_integer_index
                integer_value = switchStatsInfo[integer_index]
                integer_value_bin = bin_tran(integer_value)
                integer_value_bin = bin_tran(255)[24:] * 4 #[:]
                switchStatsInfo[integer_index] = convert_to_signed_int(integer_value_bin)
                
        elif self.level == 4:
            """Define and update controller SwtichStatsInfo"""
            switchStatsInfo = [0 for i in range(256)]
            integer_index = 0
            integer_value = switchStatsInfo[integer_index]
            integer_value_bin = bin_tran(integer_value)
            integer_value_bin = bin_tran(255)[24:] + integer_value_bin[8:] #[0:8]
            integer_value_bin = integer_value_bin[0:8] + "0" * 24 #[8:]
            switchStatsInfo[integer_index] = convert_to_signed_int(integer_value_bin)
            integer_index += 1
            for node in self.node_info_update_newspaper:
                integer_value = switchStatsInfo[integer_index]
                integer_value_bin = bin_tran(integer_value)
                integer_value_bin = bin_tran(node.remaining_buffer)[21:] + integer_value_bin[11:] # [0:11]
                integer_value_bin = bin_first_int[0:11] + bin_tran(node.remaining_inbound)[22:] + integer_value_bin[21:] #[11:21]
                integer_value_bin = integer_value_bin[0:21] + bin_tran(node.remaining_outbound)[24:] + integer_value_bin[29:] #[21:29]
                integer_value_bin = integer_value_bin[0:29] + "0" * 3 #[29:]
                switchStatsInfo[integer_index] = convert_to_signed_int(integer_value_bin)
                integer_index += 1
                 
        else: #level ==0
            switchStatsInfo = [0 for i in range(256)]
            integer_index = 0
            integer_value = switchStatsInfo[integer_index]
            integer_value_bin = bin_tran(integer_value)
            integer_value_bin = bin_tran(254)[24:] + integer_value_bin[8:] #[0:8]
            integer_value_bin = integer_value_bin[0:8] + "0" * 24 #[8:]
            switchStatsInfo[integer_index] = convert_to_signed_int(integer_value_bin)
            integer_index += 1
            
        switchStatsInfo_2 = SwitchStatsInfo()
        switchStatsInfo_2.info = switchStatsInfo
        return switchStatsInfo_2