"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:

    def __init__( self , value , prev = None , next = None ):

        self.value = value
        self.prev = prev
        self.next = next

        print( f'ListNode: Value: { self.value } , Prev: { self.prev } , Next: { self.next } ' )

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after( self , value ):

        current_next = self.next
        self.next = ListNode( value , self , current_next )

        if current_next:

            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before( self , value ):

        current_prev = self.prev
        self.prev = ListNode( value , current_prev , self )

        if current_prev:

            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete( self ):

        if self.prev:

            self.prev.next = self.next

        if self.next:

            self.next.prev = self.prev



"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:

    def __init__( self , node = None ):

        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):

        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head( self , value ):

        print( 'Add to head:' , value )

        if self.head:

            self.head.insert_before( value )
            self.head = self.head.prev

        else:

            self.head = ListNode( value )
            self.tail = self.head

        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head( self ):

        head_value = self.head.value

        print( f'Removing: { head_value }' )

        # if not self.head:

        #     return None

        head = self.head
        self.delete( head )

        return head_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):

        print( 'Add to tail:' , value )
        
        if self.tail:

            self.tail.insert_after( value )
            self.tail = self.tail.next

        else:

            self.head = ListNode( value )
            self.tail = self.head

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail( self ):
        
        if self.length > 1:

            tail = self.tail
            temp = self.tail.prev
            self.tail.delete()
            self.tail = temp
            self.length -= 1

        elif self.length == 1:
            
            tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1

        return tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        
        if self.length == 1:

            pass

        if node is self.tail:

            self.tail = node.prev

        node.delete()
        self.length -= 1
        self.add_to_head( node.value )

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        
        if self.length == 1:

            pass
        
        if node is self.head:

            self.head = node.next

        node.delete()
        self.length -= 1
        self.add_to_tail( node.value )

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete( self , node ):

        if node is self.head:

            self.head = node.next


        if node is self.tail:

            self.tail = node.prev

        # if theres a node that isnt head or tail

        node.delete()
        self.length -= 1

        
    """Returns the highest value currently in the list"""
    def get_max( self ):
        
        max = 0

        if self.length:

            current = self.head
            max = current.value

        while current.next:

            if current.next.value > max:

                max = current.next.value

            current = current.next

        print( 'Max:' , max )
        return max
