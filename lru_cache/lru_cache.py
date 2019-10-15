import sys
import os
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
os.system( 'clear' )

class LRUCache:

    # LEAST RECENTLY USED CACHE

    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):

        self.size = 0
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    
    def get(self, key):

        print( 'KEYYYY' , key )

        # if key == 'nonexistant':
        #     return None
        
        if not self.storage.head:
            pass

        else:
        
            head_value = self.storage.head.value

            print( f'Head Value: { head_value[0] }' )
            print( f'Head.next Value: { self.storage.head.next.value[0] }' )

            if head_value[0] == key:

                return head_value[1]

            elif self.storage.head.next.value[0] == key:

                return self.storage.head.next.value[1]

            else:

                print( 'NOOOOO' )


        if not self.storage.tail:

            pass

        else:
        
            tail_value = self.storage.tail.value

            print( f'Tail Value: { tail_value[0] }' )
            print( f'Head.next Value: { self.storage.tail.prev.value[0] }' )

            if tail_value[0] == key:

                return tail_value[1]

            elif self.storage.tail.prev.value[0] == key:

                print( 'YES' , self.storage.tail.prev.value[1] )

            else:

                print( 'NOOOOO' )

        

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
        
        item = [ key , value ]
        
        if self.size == 10:

            print( 'Storage is at its max of 10' )
            pass
        
        else:

            self.storage.add_to_head( item )
            self.size += 1

        return self.size


