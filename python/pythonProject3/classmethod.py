"""class person:
    def __init__(self, name):
        person.name = name


p1=person("maeria")
print(p1.name)
print(person.name)"""
class person:
  #  def __init__(self, name):
      #  self.__class__.name="ji"
  @classmethod
  def cng(cls,name):
      cls.name =name



p1=person()
p1.cng("maria")
print(p1.name)
print(person.name)