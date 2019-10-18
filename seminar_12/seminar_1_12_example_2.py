class Tree():
    def __init__(self, kind, height):
        self.__kind = kind
        self.__age = 0
        self.__height = height

    def info(self):
        print("Tree" + str((self.__age, self.__kind, self.__height)))

    def grow(self):
        self.__age += 1
        self.__height += 0.5

    def getKind(self):
        return self.__kind

    def getHeight(self):
        return self.__height

    def __lt__(self, other):
        return self.__height < other.getHeight()

class FruitTree(Tree):  # FruitTree - наследник класса Tree
    def __init__(self, kind, height, group="unknown"):
        super().__init__(kind, height)
        self.__group = group

    def giveFruits(self):
        print("Collected 10kg of %ss" % self.getKind()) # нельзя __kind, т.к. он private!

tree1 = Tree("oak", 2)
# tree1.giveFruits()
tree2 = FruitTree("apple", 0.7)
tree2.info()  # Есть доступ к методам родителя
tree2.grow()
tree2.info()
tree2.giveFruits()
# А для родительского экземпляра метод give_fruits() недоступен
# tree1.give_fruits() # Вызовет ошибку

trees = (tree1, tree2)
sorted(trees)