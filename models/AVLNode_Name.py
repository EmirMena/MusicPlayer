from models import AVLNode_Name
from models.array_stack import ArrayStack

class AVLNode_Name:
    def __init__(self, song=None, left:AVLNode_Name=None, right:AVLNode_Name=None, father:AVLNode_Name=None,f_eq:int=0):
        self.__song = song
        self.__left = left
        self.__right = right
        self.__father = father
        self.__f_eq = f_eq

    "------------------------------------------------------------------------------------------------------------------------"
    @property
    def song(self):
        return self.__song
    @song.setter
    def song(self, song):
        self.__song = song
    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, left):
        self.__left=left
    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, right):
        self.__right=right
    @property
    def f_eq(self):
        return self.__f_eq
    @f_eq.setter
    def f_eq(self, f_eq):
        self.__f_eq = f_eq
    @property
    def father(self):
        return self.__father
    @father.setter
    def father(self, father):
        self.__father = father
    "------------------------------------------------------------------------------------------------------------------------"

    @staticmethod
    def height(node:AVLNode_Name=None)->int:
        if node is None:
            return -1
        else:
            return 1 + max(AVLNode_Name.height(node.left),AVLNode_Name.height(node.right))

    "LISTING METHODS"

    def ascending_list(self):
        if self.left != None:
            self.left.ascending_list()
        self.print_node_info()
        if self.right != None:
            self.right.ascending_list()
    
    def descending_list(self, stack: ArrayStack):
        if self.left != None:
            self.left.descending_list(stack)
        stack.push(self.song)
        if self.right != None:
            self.right.descending_list(stack)
    
    "NODE INFO PRINTING METHOD"

    def print_node_info(self):
        print("Nombre: " + str(self.song.name) + " Autor: " + str(self.song.author) + " Género: " + str(self.song.genre))