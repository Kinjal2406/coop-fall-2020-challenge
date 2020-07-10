class EventSourcer():
    # Do not change the signature of any functions
    

    def __init__(self):
        self.value = 0
        self.temp = []

        

    def add(self, num: int):
        #print(self.value)
        self.value = self.value + num
        self.temp.append(self.value)
        pass
        

    def subtract(self, num: int):
        self.value = self.value - num
        self.temp.append(self.value)
        pass

    def undo(self):
        if(len(self.temp)>1):
            self.value = self.temp[-2]
        #self.temp.append(self.value)
        pass

    def redo(self):
        if(len(self.temp)>0):
            self.value = self.temp[-1]
        #self.temp.append(self.value)
        pass

    def bulk_undo(self, steps: int):
        if(steps<len(self.temp)):
            self.value =  self.temp[-2-(steps)+1]
        if(steps==len(self.temp)):
            self.value = 0
        pass

    def bulk_redo(self, steps: int):
        if(len(self.temp)>-1):
            self.value = self.temp[-1]
        pass
