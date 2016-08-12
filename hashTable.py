""" Hashtable class: creates a nasn table and collisions are resolved using
open addressing and linear probing"""
"""Author: Vishnu Muralidharan"""
class HashTable:
    def __init__(self):
        self.size = 11 # size of hashtable
        self.slots = [None] * self.size # initiialize slots and data to null elements
        self.data = [None] * self.size

# function to insert a key-value pair in the hash table
    def put(self,key,data):
        # get the hash value for the key-value pair
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == None:   # if the computed hash value is an empty slot
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:
            # if the slot already has a key associated with it, overwrite the data
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                # if the slot has an associated key-value pair,
                # compute the next available slot using rehashing
                nextslots = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslots] != None and self.slots[nextslots] != key:
                    nextslots = rehash(nextslots,len(self.slots))
                #if rehashe value is an empty slot
                if self.slots[nextslots] == None:
                    self.slots[nextslots] = key
                    self.data[nextslots] = data
                else:
                    # if the rehashed slot already has a key, replace the data
                    if self.slots[nextslots] == key:
                        self.data[nextslots] = data

# function to compute the hash value gicen the key and hash map size
    def hashfunction(self,key,size):
         return key%size

# function rehash is used to oompute the next available slot
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
# function to rettieve the associated data given a key
    def get(self,key):
        stop = None
        found = False
        data = None
        startslot = self.hashfunction(key,len(self.slots))  # startslot computes the first slot to be seatchedd
        position = startslot
        while self.slots[position] != None and not found and not stop:
            # if the key matches at the startslot, return data
            if self.slots[position] == key:
                data = self.slots[position]
                found = True
            else:
            # rehash until the key matches
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
            return data

# function overrides for the in-built getitem and setitem function
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        return self.put(key,data)
    

            
