#!/usr/bin/python3
"""
Defines a function canUnlockAll that determines if a box can be unlock
"""

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])
    
    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])
            
            return len(unlocked) == n

