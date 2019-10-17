import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value < self.value:

            if not self.left:

                self.left = BinarySearchTree( value )

            else:

                self.left.insert( value )

        else:

            if not self.right:

                self.right = BinarySearchTree( value )

            else:

                self.right.insert( value )

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if self.value == target:

            return True

        if target < self.value:

            if not self.left:

                return False

            else:

                return self.left.contains( target )

        else:

            if not self.right:

                return False

            else:

                return self.right.contains( target )


    # Return the maximum value found in the tree
    def get_max(self):

        if not self.right:

            return self.value

        return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        
        cb( self.value )

        if self.left:
            
            self.left.for_each( cb )

        if self.right:

            self.right.for_each( cb )

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        # Inorder(tree)
        #     1. Traverse the left subtree, i.e., call Inorder(left-subtree)
        #     2. Visit the root.
        #     3. Traverse the right subtree, i.e., call Inorder(right-subtree)


        if self.left:
            self.left.in_order_print( node.left )
        print( self.value )
        if self.right:
            self.right.in_order_print( node.right )



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        # print root
        # go to smallest parents smallest node and print it ( left )
        # print parent
        # print parents right node
        # go to next biggest parent

        data = []

        data.append( self )
        print( self.value )
        count = 0

        answer = []


        while count < 3:
            for i in range( len( data ) ):

                if data[ i ].right is not None:
                    if data[ i ].right not in data:

                        data.append( data[ i ].right )
                        print( data[ i ].right.value )

                        if data[ i ].right.right is not None:
                            if data[ i ].right.right not in data:

                                data.append( data[ i ].right.right )
                                print( data[ i ].right.right.value )

                        elif data[ i ].right.left is not None:
                            if data[ i ].right.left not in data:

                                data.append( data[ i ].right.left )
                                print( data[ i ].right.left.value )

                if data[ i ].left is not None:
                    if data[ i ].left not in data:
                        
                        data.append( data[ i ].left )
                        print( data[ i ].left.value )

            count += 1


















        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass