# MRO : Method Resolution Order
# MRO use DFS (Depth First Search)
class Parents:
    def parents():
        pass
class Son(Parents):
    def son(self):
        print("Son of Mask")
class Daughter(Parents):
    def daughter(self):
        print("Daughter of Mask")
class Nephews(Son, Daughter):
    def nephews(self):
        print("The Nephews are here!")
class MaskFamily(Nephews, Son, Daughter):
    pass

# Out: MaskFamily -> Nephews -> Son -> Daughter -> Parents -> Object


family = MaskFamily()
family.son()
print(family.__class__.__mro__)