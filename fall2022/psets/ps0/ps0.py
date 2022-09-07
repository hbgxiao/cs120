#################
#               #
# Problem Set 0 #
#               #
#################
 
 
#
# Setup
#
class BinaryTree:
   def __init__(self, root):
       self.root: BTvertex = root
class BTvertex:
   def __init__(self, key):
       self.parent: BTvertex = None
       self.left: BTvertex = None
       self.right: BTvertex = None
       self.key: int = key
       self.size: int = None
 
#
# Problem 1a
#
 
# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
   if v == None:
       return 0
   elif v.right == v.left == None:
       v.size = 1
   else:
       v.size = calculate_sizes(v.left) + calculate_sizes(v.right) + 1
   return v.size
  
#
# Problem 1c
#
 
# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
# do we need to check??
def find_vertex(r):
   if r == None:
       return None
   elif r.left == None and r.right != None:
       if r.right.size <= r.size/2:
           return r
       else:
           return find_vertex(r.right)
   elif r.right == None and r.left != None:
       if r.left.size <= r.size/2:
           return r
       else:
           return find_vertex(r.left)
   elif r.left.size <= r.size/2 and r.right.size <= r.size/2:
       return r
   elif r.left.size > r.right.size:
       find_vertex(r.left)
   else:
       find_vertex(r.right)

