class abs:
    def stop(self, false=None):
        self.enf=false
        self.run=false
        self.brk=false
    def start(self):
        self.enf=True
        self.run=True
        self.brk=True
        print("start car")

a=abs()
a.start()