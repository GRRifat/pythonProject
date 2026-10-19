class animal:

    def A(self):

        print("Cat and Dog")

class cat(animal):

    def call(self):
        print("Meo Meo")
class dog(cat):
    def call2(self):
        print("gheo gheo")
ri=dog()
ri.A()
ri.call()
ri.call2()



