# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:07:52 2021

@author: Natasha Camargo
"""
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node
        
        
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
        
    def get_head_node():
        