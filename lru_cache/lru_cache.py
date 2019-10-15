import sys
import os
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
os.system( 'clear' )

class LRUCache:

    # LEAST RECENTLY USED CACHE

    # TAIL IS THE MOST RECENTLY ADDED
    # HEAD IS THE FIRST ONE YOU ADDED

    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):

        os.system( 'clear' )

        self.limit = limit
        self.size = 0
        # Store key/values in here
        self.dictionary = {}
        # retain order of adding the key/values
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    
    def get(self, key):

        print( '\n\n----------- Key:' , key , '\n\n' )

        for i in range( self.size ):

            the_key_from_dict = self.storage.tail.value.keys()
            the_value_from_dict = self.storage.tail.value.values()
            the_key = list( the_key_from_dict )
            the_value = list( the_value_from_dict )

            if the_key[0] == key:

                print( f'\nFound it' )

                return the_value[0]

            self.storage.move_to_front( self.storage.tail )




        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        
        item = { key: value }
        
        if self.size == 10:

            print( f'Storage is at its max of 10\n { self.storage.tail.value }\n' )
        
        else:
            print( '\n-----------------------------' )
            print( '\nItem:' , item )

            if self.size == 0:

                self.storage.add_to_head( item )
                self.size += 1
                print( 'Start:' , self.storage.tail.value , ', Storage:' , self.size )

            else:

                if self.size == 1:

                    if self.storage.tail.value == item:
                        
                        print( 'same item' )

                    else:

                        self.storage.add_to_head( item )
                        self.size += 1

                elif self.size > 1:

                    print( '\n EXISTING ITEMS:\n' )
                    for i in range( self.size ):

                        # print( 'Tail:' , self.storage.tail.value , ', Storage:' , self.size )

                        # Dictionary Translations
                        the_key_from_dict = self.storage.tail.value.keys()
                        the_value_from_dict = self.storage.tail.value.values()
                        the_key = list( the_key_from_dict )
                        the_value = list( the_value_from_dict )
                        object_to_delete = self.storage.tail

                        if key == the_key[0]:
                            
                            print( 'Duplicate Item, Different Value' )
                            self.storage.delete( object_to_delete )
                            self.storage.add_to_tail( item )
                            self.storage.move_to_front( self.storage.tail )

                        elif i == self.size - 1:
                            self.storage.add_to_head( item )
                            self.size += 1

                        self.storage.move_to_front( self.storage.tail )

                    print( '\n\n\n\n CHECK \n\n\n\n' )

                    for i in range( self.size ):

                        print( 'Tail:' , self.storage.tail.value , ', Storage:' , self.size )
                        self.storage.move_to_front( self.storage.tail )



        return self.size



