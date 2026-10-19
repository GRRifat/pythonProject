class stu:
    name=" "
    ID= " "
    sec = " "

                  #set value
    def value(self,Name,ID,sec):

        self.name=Name
        self.ID=ID
        self.sec=sec
    def display(self):


        print(f"Name:{self.name} ID:{self.ID} SECTION: {self.sec}")

    def dis(self,name):
        print(f"Name{self.name}")

Rifat=stu()
Rifat.value("Rifat",22135900,"D")
Rifat.display()
Rifat.value("Fahim",221,"D")
Rifat.display()








