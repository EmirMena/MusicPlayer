from models.AVLNode_Author import AVLNode_Author
from models.array_stack import ArrayStack

class AVLTree_Author:
    def __init__(self,song=None) -> None:
        self.__root = AVLNode_Author(song=song)
    
    @property
    def root(self):
        return self.__root
    @root.setter
    def root(self,song):
        self.__root=song
    
    def end(self, children: list):
        end = False
        if len(children) == 0:
            end = True
            return end
        return False

    "LISTING METHODS"

    def generate_ascending_list(self):
        ascending_list = []
        if self.root is not None:
            self.root.generate_ascending_list(ascending_list)
        return ascending_list

    def generate_descending_list(self):
        stack = self.fill_stack()
        descending_list = []
        while not stack.is_empty():
            descending_list.append(stack.pop())
        return descending_list

    def fill_stack(self):
        stack = ArrayStack()
        if self.root is not None:
            self.root.fill_stack(stack)
        return stack

    "AUTHOR SEARCHING METHOD"

    def search_author(self, author):
        if self.root is None:
            return None
        node = self.root
        while node is not None:
            if node.song.author == author:
                return node.song
            elif author < node.song.author:
                node = node.left
            else:
                node = node.right
        return None
            
    "------------------------------------------------------------------------------------------------------------------------"
    def __ii_rotation(self, node:AVLNode_Author):
        father = node.father
        p = node 
        q = p.left 
        b = q.right 

        if father is not None:
            if father.right == p: father.right = q 
            else: father.left = q
        else: self.root = q
        #Rebuild the tree
        p.left = b
        q.right = p

        #Reasign fathers
        p.father = q
        if b is not None: b.father = p
        q.father = father
        
        p.f_eq = 0
        q.f_eq = 0

    def __dd_rotation(self, node:AVLNode_Author):
        father = node.father
        p = node 
        q = p.right
        b = q.left 

        if father is not None:
            if father.left == p: father.left = q
            else: father.right = q
        else: self.root = q
        #Rebuild the tree
        p.right = b
        q.left = p

        #Reasign fathers
        p.father=q
        if b is not None: b.father = p
        q.father = father
    
        p.f_eq = 0
        q.f_eq = 0

    def __id_rotation(self, node:AVLNode_Author):
        father = node.father
        p = node 
        q = p.left 
        r = q.right
        b = r.left
        c = r.right
     
        if father is not None:
            if father.right == p: father.right = r
            else: father.left = r
        else: self.root = r

        #Rebuilding the tree...
        q.right = b 
        p.left = c
        
        r.left = q
        r.right = p

        #Reasigning fathers...
        r.father = father
        p.father = r
        q.father = r
        if b is not None: b.father = q
        if c is not None: c.father = p
      
        if r.f_eq == -1: 
             p.f_eq = 0 
             q.f_eq = 1 
        elif r.f_eq == 0:
            p.f_eq = 0 
            q.f_eq = 0 
        elif r.f_eq == 1:
            p.f_eq = -1 
            q.f_eq =  0 
        r.f_eq = 0
    
    def __di_rotation(self, node):
        father = node.father
        p = node 
        q = p.right 
        r = q.left 
        b = r.right
        c = r.left
        
        if father is not None:
            if father.left == p: father.left = r
            else: father.right = r
        else: self.root = r
        
        #Rebuilding the tree...
        q.left = b 
        p.right = c 
      
        r.right = q
        r.left = p

        #Reasigning the fathers...
        r.father = father
        p.father = r
        q.father = r
        if b is not None: b.father = q
        if c is not None: c.father = p
        
        if r.f_eq == -1:
             p.f_eq = 0 
             q.f_eq = 1 
        elif r.f_eq == 0:
            p.f_eq = 0 
            q.f_eq = 0 
        elif r.f_eq == 1:
            p.f_eq = -1 
            q.f_eq =  0 
        r.f_eq = 0
    
    def __balance(self, node:AVLNode_Author):
        current_fe = node.f_eq
        if current_fe == 2:
            #Determine the rotation
            right_child_fe = node.right.f_eq
            if right_child_fe == 0:
                pass
            elif right_child_fe == 1:
                self.__dd_rotation(node)
            elif right_child_fe == -1:
                self.__di_rotation(node)
        else:
            left_child_fe = node.left.f_eq
            if left_child_fe == 0:
                pass
            elif left_child_fe == -1:
                self.__ii_rotation(node)
            elif left_child_fe == 1:
                self.__id_rotation(node)

    def __recalculate_fe(self, node:AVLNode_Author):
        if node is not None:
            node.f_eq = AVLNode_Author.height(node.right)-AVLNode_Author.height(node.left)
            if abs(node.f_eq) == 2:
                self.__balance(node)
            else:
                self.__recalculate_fe(node.father)
    "------------------------------------------------------------------------------------------------------------------------"

    "INSERT METHODS"

    def __insert_ordered(self, node:AVLNode_Author, song):
        n = node.song.author
        if song.author < n:
            if node.left is None:
                node.left = AVLNode_Author(song,None,None,node)
                self.__recalculate_fe(node)
            else:
                self.__insert_ordered(node.left,song)
        if song.author > n:
            if node.right is None:
                node.right = AVLNode_Author(song,None,None, node)
                self.__recalculate_fe(node)
            else:
                self.__insert_ordered(node.right,song)
    
    def insert(self, song):
        self.__insert_ordered(self.root, song)