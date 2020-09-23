
# Given an array of elements, our task is to construct a complete binary tree from this array in level order fashion. i=root, 2i+1=left, 2i+2 =right
# binary tree creation, traversals
class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

# Helper function helps us in adding data  
# to the tree in Level Order 
def insertValue(data): 
    global q1
    global head
    newnode = Node(data) 
    if q1: 
        temp = q1[0]
        
        
    if head == None: 
        head = newnode 
    elif temp.left == None: 
        temp.left = newnode 
    elif temp.right == None: 
        temp.right = newnode  
        q1.pop(0)
    q1.append(newnode) 
            
def create_tree(array):
    global head
    for i in array:
        insertValue(i)

def preorder_trav(head):
    if(head!=None):
        print(head.value)
        preorder_trav(head.left) 
        preorder_trav(head.right)

def postorder_trav(head):
    if(head!=None):
        postorder_trav(head.left)
        postorder_trav(head.right)
        print(head.value)
    
def inorder_trav(head):
    if(head!=None):
        inorder_trav(head.left)
        print(head.value) 
        inorder_trav(head.right)
        
def level_order(head, queue, visited):
    queue.append(head)
    print(head.value)
    while queue:
        s=queue.pop(0)
        if s.left!=None:
            print(s.left.value)
            queue.append(s.left)
        if s.right!=None:
            print(s.right.value)
            queue.append(s.right)
                
if __name__ == '__main__':
    a = [1,2,3,3,4,5,6,7,8]
    head=None
    queue=[]
    q1=[]
    visited=[]
    create_tree(a)
    #print('b210')
    #preorder_trav(head)
    #postorder_trav(head)
    #inorder_trav(head)
    #print(head.left.left)
    
    level_order(head,queue,visited)