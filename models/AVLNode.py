from models import AVLNode
from models.array_stack import ArrayStack

class AVLNode:
    def __init__(self, song=None, left:AVLNode=None, right:AVLNode=None, father:AVLNode=None,f_eq:int=0):
        self.__left = left
        self.__right = right
        self.__father = father
        self.__f_eq = f_eq

        self.__list = []
        self.insert_song(song)

    "------------------------------------------------------------------------------------------------------------------------"
    @property
    def list(self):
        return self.__list
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
    def height(node:AVLNode=None)->int:
        if node is None:
            return -1
        else:
            return 1 + max(AVLNode.height(node.left),AVLNode.height(node.right))

    "LISTING METHODS"

    def generate_ascending_list(self, ascending_list: []):
        if self.left != None:
            self.left.generate_ascending_list(ascending_list)
        ascending_list = self.add_list_to_returning_list(ascending_list)
        if self.right != None:
            self.right.generate_ascending_list(ascending_list)
    
    def fill_stack(self, stack: ArrayStack):
        if self.left != None:
            self.left.fill_stack(stack)
        stack.push(self.__list)
        if self.right != None:
            self.right.fill_stack(stack)
    
    def insert_song(self, song):
        self.__list.append(song)

    def add_list_to_returning_list(self, list:[]):
        for song in self.list:
            list.append(song)
        return list
    