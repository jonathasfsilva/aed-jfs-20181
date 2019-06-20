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

    def transplant(self, u, v):
        if u.getParent() is self.nil:
            self.setRoot(v)
        elif u is u.getParent().getLeft():
            u.getParent().setLeft(v)
        else:
            u.getParent().setRight(v)
        v.setParent(u.getParent())

    def delete(self, z):
        y = z
        y_original_color = y.getColor()
        if z.getLeft() is self.nil:
            x = z.getRight()
            self.transplant(z, z.getRight())
        elif z.getRight() is self.nil:
            x = z.getLeft()
            self.transplant(z, z.getLeft())
        else:
            y = self.minimum(z.getRight())
            y_original_color = y.getColor()
            x = y.getRight()
            if y.getParent() is z:
                x.setParent(y)
            else:
                self.transplant(y, y.getRight())
                y.setRight(z.getRight())
                y.getRight().setParent(y)
            self.transplant(z, y)
            y.setLeft(z.getLeft())
            y.getLeft().setParent(y)
            y.setColor(z.getColor())
        if y_original_color == 'black':
            self.deleteFixUp(x)

    def deleteFixUp(self, x):
        while x is not self.getRoot() and x.getColor() == 'black':
            if x is x.getParent().getLeft():
                w = x.getParent().getRight()
                if w.getColor() == 'red':
                    w.setColor('black')
                    x.getParent().setColor('red')
                    self.leftRotate(x.getParent())
                    w = x.getParent().getRight()
                if w.getLeft().getColor() == 'black' and w.getRight().getColor() == 'black':
                    w.setColor('red')
                    x = x.getParent()
                else:
                    if w.getRight().getColor() == 'black':
                        w.getLeft().setColor('black')
                        w.setColor('red')
                        self.rightRotate(w)
                        w = x.getParent().getRight()
                    w.setColor(x.getParent().getColor())
                    x.getParent().setColor('black')
                    w.getRight().setColor('black')
                    self.leftRotate(x.getParent())
                    x = self.getRoot()
            else:
                w = x.getParent().getLeft()
                if w.getColor() == 'red':
                    w.setColor('black')
                    x.getParent().setColor('red')
                    self.rightRotate(x.getParent())
                    w = x.getParent().getRight()
                if w.getRight().getColor() == 'black' and w.getLeft().getColor() == 'black':
                    w.setColor('red')
                    x = x.getParent()
                else:
                    if w.getLeft().getColor() == 'black':
                        w.getRight().setColor('black')
                        w.setColor('red')
                        self.leftRotate(w)
                        w = x.getParent().getLeft()
                    w.setColor(x.getParent().getColor())
                    x.getParent().setColor('black')
                    w.getLeft().setColor('black')
                    self.rightRotate(x.getParent())
                    x = self.getRoot()
        x.setColor('black')
