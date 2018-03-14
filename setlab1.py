class set:

    def __init__(self, data):
        self.data = ("hello", "red", "ball", "red")
        element = input("type element:")
        self.set = set(data)
    def addData(self, element):
        self.set.add(element)
    def removeData(self, element):
        self.set.discard(element)
    def member(self, element):
        return element in self.set
    def intersect(self, set2):
        return self.set.intersection(set2)
    def uninon(self, set2):
        return self.set.union(set2)
    def subtract(self, set2):
        return self.set.subtract(set2)
