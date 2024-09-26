class person:
    def __init__(self, phy,chem,bio,math):
        self.phy = phy
        self.chem = chem
        self.bio = bio
        self.math = math

    @property
    def change(self):

        return str((self.bio+self.math+self.chem+self.phy)/4)+"%"


p=person(80,90,80,90)
print(p.change)
p.phy=70
print(p.phy)
print(p.change)