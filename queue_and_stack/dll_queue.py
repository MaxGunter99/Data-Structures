import sys
import os
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
os.system( 'clear' )


class Queue:

    def __init__( self ):

        self.size = 0
        self.queue = []

    # enqueue should add an item to the back of the queue.
    def enqueue( self , value ):

        print( f'Added { value } to queue' )
        self.queue.append( value )
        self.size += 1

    # dequeue should remove and return an item from the front of the queue.
    def dequeue( self ):

        if len( self.queue ) == 0:
            pass
        
        else:
            print( 'Queue:', self.queue )
            removed = self.queue[ 0 ] 
            print( 'Removed:' , removed )
            self.queue.pop( 0 )
            self.size -= 1
            return removed
            

        
    # len returns the number of items in the queue.
    def len(self):

        return self.size