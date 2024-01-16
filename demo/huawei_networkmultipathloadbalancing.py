from typing import List, Tuple
from solution_common.message import Message, Request, SwitchStatsInfo
from solution_common.solution import Solution


class UserSolution(Solution):
    # Class variable to track if the class-wide method has been called
    _class_method_called_tracker_1 = False
    _class_method_called_tracker_2 = False
    # Create some class variables here
    
    def __init__(self, node_id: int, bw_in: int, bw_out: int, size: int, level: int, graph: List[List[int]],
                 nodes_info: List[Tuple[int, int, int, int, int]]):
        super().__init__(node_id, bw_in, bw_out, size, level, graph, nodes_info)
        
        # Call the class-wide methods
        self._compute_parameters_of_each_node()
        self._find_shortest_available_paths()
        
        # Only for node at level 1, 2, 3: Maybe need to define some local (instance) attributes that saves a copy of each parameter computed in the self._compute_parameters_of_each_node() class-wide method
        
        
        # Only for node at level 1, 2, 3: create an attribute to keep track of this node's buffer size, also create a dictionary that records the estimates on neighboring node's buffer size
        self.available_buffer = self.size
        self.neighbor_buffer_estimaes = {} # Item 5 computed by the _compute_parameters_of_each_node method
        
        # Only for node at level 1, 2, 3: Keep track of one's own requests
        # In the form of dictionary {request id : (message id, target node, request_begin_time)}
        self.messages_dictionary = {}
        
    
    
    """
    Compute the parameters include:
    1. Create a dictionary that classifies each node, for example, {152:3} means node index 152 is level 3 (core)
    2. For each level 1, 2, 3 node, find its neighbor that are potential senders (exclude level 0 and level 4 nodes as they don't send), put this info into another dictionary.
    Example dictionary: {152, [48, 52, 191]} means that node 152 may receive messages from node 48, 52, 191
    3. For each level 1, 2, 3 node, compute the number of neighbors that are potential senders (exclude level 0 and level 4 nodes as they don't send), put this info into another dictionary
    4. Create a dictionary that records the inbound bandwidth of each node, for example, {152:90} means node 152 has 90 bandwidths. Record only level 1, 2, 3 nodes.
    5. For each level 1, 2, 3 node, compute the average of inbound bandwidths per neighbor (at level 1, 2, 3), this average number becomes the limit cap that each of its neighboring sender is allowed to send
    So I want a dictionar of dictionary, e.g. {152, {48:100, 52:200, 191:300}} means node 152 has 3 senders (at level 1, 2, 3), for neighbor 48, you are assigned a cap of 100 bandwidths to send to this neighbor
    6. For each level 1, 2, 3 node, compute their original buffer, make this as a dictionary.
    ** Remember to make the dictionaries become class variables
    """
    @classmethod
    def _compute_parameters_of_each_node(cls):
        # Check if the method has already been called
        if not cls._class_method_called_tracker_1:
            # Perform the necessary actions and set class-wide attributes here
            
            
            
            # Mark that the method has been called
            cls._class_method_called_tracker_1 = True



    """ 
    Objective: create a giant dictionary {(152, 21): (4, [[152, 48, 99, 187, 21], [152, 52, 172, 63, 21]])} which contains the shortest paths that connects from node 152 to 21
    The '4' refers to the length of the shortest path
    Importance is that next time when we have a request message arriving at node 152 then we know that we need to send to either 48 or 52
    Priority: 
    1st priority: level 1 to level 0 directly
    2nd priority: any traversal that is bounded within level 2, 1, 0 (and shortest path from here)
    3rd priority: traversal that involves level 3 (and shortest path from here)
    Definitely need recursion, maybe can use some sort of dynamic programming techniques
    """
    # Find shortest available paths
    @classmethod
    def _find_shortest_available_paths(cls):
        # Check if the method has already been called
        if not cls._class_method_called_tracker_2:
            # Perform the necessary actions and set class-wide attributes here
            
            
            
            # Mark that the method has been called
            cls._class_method_called_tracker_2 = True
    
    
    
    

    """
    SwitchStatsInfo format for nodes at level 1, 2, 3:
    this node index (8) + this node current buffer size (11)
    recipient node index (8) + request id (13) + target node (8) // + request_begin_time (8) + message id (from) (7) + message id (to) (7)
    
    SwitchStatsInfo format for the controller node at level 4:
    this node index (8)
    for each other 207 nodes: (node index automatically labelled by position in this list, no need to do anything more) 
    buffer size (11) + inbound bandwidth (10) + outbound bandwidth (8)
    """

    def add_request_list(self, request_list: List[Request]) -> None:
        # Update self.messages_dictionary
        # Remember that you need to subtract your own self.available_buffer
        pass

    def ask_round_solution(self, neighbor_info_list: List[SwitchStatsInfo]) -> List[Message]:
        return []

    def next_round(self, result) -> SwitchStatsInfo:
        return SwitchStatsInfo()

