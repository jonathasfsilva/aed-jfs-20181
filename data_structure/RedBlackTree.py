from Tree import Tree

class RBTree(Tree):
    u"""Árvore Vermelho e Preto."""


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

    def leftRotate(self, x):
        """Rotaçao simples à esquerda."""
        y = x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft() is not self.nil:
            y.getLeft().setParent(x)
        y.setParent(x.getParent())
        if x.getParent() is self.nil:
            self.setRoot(y)
        elif x is x.getParent().getLeft():
            x.getParent().setLeft(y)
        else:
            x.getParent().setRight(y)
        y.setLeft(x)
        x.setParent(y)

    def rightRotate(self, x):
        """Rotaçao simples à direita."""
        y = x.getLeft()
        x.setLeft(y.getRight())
        if x.getRight() is not self.nil:
            y.getRight().setParent(x)
        y.setParent(x.getParent())
        if x.getParent() is self.nil:
            self.setRoot(y)
        elif x is x.getParent().getRight():
            x.getParent().setRight(y)
        else:
            x.getParent().setLeft(y)
        y.setRight(x)
        x.setParent(y)
