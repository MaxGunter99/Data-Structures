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
        print( 'Dictionary:' , self.dictionary )

        if key in self.dictionary:
            return self.dictionary[ key ]
        else:
            return None




        

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
        
        if self.size == self.limit:

            print( f'Storage is at its max of {self.limit}\n { self.dictionary }\n' )

            if key in self.dictionary:
                        
                print( 'Key is in dictionary already' , key , value )
                self.dictionary.update( { key : value } )

                for i in range( self.size ):

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

                    self.storage.move_to_front( self.storage.tail )

            else:
                print( "Limit reached . . . removing oldest value" )
                the_key_from_dict = self.storage.tail.value.keys()
                the_value_from_dict = self.storage.tail.value.values()
                the_key = list( the_key_from_dict )
                del self.dictionary[ the_key[0] ]
                self.storage.delete( self.storage.tail )
                self.dictionary.update( { key : value } )
                self.dictionary.update( item )
                self.storage.add_to_tail( item )
                print( 'Updated Dictionary:' , self.dictionary )
        
        elif self.size < self.limit:

            print( '\nItem:' , item )

            if key in self.dictionary:
                        
                print( 'Key is in dictionary already' , key , value )
                self.dictionary.update( { key : value } )

                if self.size == 1:

                    the_key_from_dict = self.storage.tail.value.keys()
                    the_value_from_dict = self.storage.tail.value.values()
                    the_key = list( the_key_from_dict )
                    the_value = list( the_value_from_dict )
                    object_to_delete = self.storage.tail
                    print( 'Duplicate Item, Different Value' )
                    self.storage.delete( object_to_delete )
                    self.storage.add_to_tail( item )

                else:

                    for i in range( self.size ):

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

                        self.storage.move_to_front( self.storage.tail )
        

            else:

                self.dictionary.update( item )
                self.storage.add_to_head( item )
                self.size += 1

        return self.size



