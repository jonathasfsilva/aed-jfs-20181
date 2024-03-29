from Node import Node

class Tree(Node):
    u"""Árvore Binária."""


    def __init__(self):
        """
        A árvore é iniciada com o nó 'nil',
        para onde todas as folhas irão apontar
        """
        self.nil = Node(None)
        self.nil.setColor('black')
        self.nil.setParent(self.nil)
        self.nil.setLeft(self.nil)
        self.nil.setRight(self.nil)
        self.__root = self.nil

    def setRoot(self, root):
        u"""Define raiz da árvore."""
        self.__root = root

    def getRoot(self):
        """Retorna a raiz da arvore."""
        return self.__root

    def isEmpty(self):
        """Retorna se a arvore esta vazia ou nao."""
        if self.getRoot() is self.nil:
            return True
        else:
            return False

    def minimum(self, node):
        """Retorna o minino daquele no."""
        if node is not self.nil:
            while node.getLeft() is not self.nil:
                node = node.getLeft()
            return node

    def maximum(self, node):
        """Retorna o maximo daquel no."""
        if node is not self.nil:
            while node.getRight() is not self.nil:
                node = node.getRight()
            return node

    def successor(self, x):
        """Retorna o sucessor."""
        if x is not self.nil:
            if x.getRight() is not self.nil:
                return self.minimum(x.getRight())
            else:
                father = x.getParent()
                while (father is not self.nil) and (x is father.getRight()):
                    x = father
                    father = x.getParent()
                    return father

    def preOrderTreeWalk(self, x):
        """Plota arvore em preOrdem."""
        if x is not self.nil:
            print(x.getData(), end = " ")
            self.preOrderTreeWalk(x.getLeft())
            self.preOrderTreeWalk(x.getRight())

    def inOrderTreeWalk(self, x):
        """Plota arvore em ordem."""
        if x is not self.nil:
            self.inOrderTreeWalk(x.getLeft())
            print(x.getData(), end = "\n")
            self.inOrderTreeWalk(x.getRight())

    def postOrderTreeWalk(self, x):
        """Plota arvore em posOrdem."""
        if x is not self.nil:
            self.postOrderTreeWalk(x.getLeft())
            self.postOrderTreeWalk(x.getRight())
            print(x.getData(), end = " ")

    def search(self, k):
        """Busca e retorna o no."""
        x = self.getRoot()
        while (x is not self.nil) and (k != x.getData()):
            if k < x.getData():
                x = x.getLeft()
            else:
                x = x.getRight()
        return x
