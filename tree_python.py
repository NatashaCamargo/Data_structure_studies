# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:20:02 2021

@author: Natasha Camargo
"""
#################################
##                             ##
##          Tree               ##
#################################
class TreeNode:
    def __init__(self, value):
        self.value = value # data
        self.children = [] # list of nodes children
        
    
    def add_children(self, child_node):
        # creating parent child relationship
        print("Adding {0}".format(child_node.value))
        self.children.append(child_node)
        
    def remove_child(self, child_node):
        print("Removing {child} from {parent}").format(child = child_node.value, parent = self.value)
        self.children = [child for child in self.children if child is not child_node]
        
    def traverse(self):
        # Moves trhough each node refferenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children