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

    def insert(self, z):
        """Recebe uma entrada e a insere na árvore."""
        x = self.getRoot()
        y = self.nil
        z = Node(z)
        while x is not self.nil:
            y = x
            if (z.getData() < x.getData()):
                x = x.getLeft()
            else:
                x = x.getRight()
        z.setParent(y)
        if y is self.nil:
            self.setRoot(z)
        elif z.getData() < y.getData():
            y.setLeft(z)
        else:
            y.setRight(z)
        z.setLeft(self.nil)
        z.setRight(self.nil)
        z.setColor('red')
        self.insertFixUp(z)

    def insertFixUp(self, z):
        while z.getParent().getColor() == 'red':
            if z.getParent() is z.getParent().getParent().getLeft():
                y = z.getParent().getParent().getRight()
                if y.getColor() == 'red':
                    z.getParent().setColor('black')
                    y.setColor('black')
                    z.getParent().getParent().setColor('red')
                    z = z.getParent().getParent()
                else:
                    if z == z.getParent().getRight():
                        z = z.getParent()
                        self.leftRotate(z)
                    z.getParent().setColor('black')
                    z.getParent().getParent().setColor('red')
                    self.rightRotate(z.getParent().getParent())
            else:
                y = z.getParent().getParent().getLeft()
                if y.getColor() == 'red':
                    z.getParent().setColor('black')
                    y.setColor('black')
                    z.getParent().getParent().setColor('red')
                    z = z.getParent().getParent()
                else:
                    if z == z.getParent().getLeft():
                        z = z.getParent()
                        self.rightRotate(z)
                    z.getParent().setColor('black')
                    z.getParent().getParent().setColor('red')
                    self.leftRotate(z.getParent().getParent())
        self.getRoot().setColor('black')
