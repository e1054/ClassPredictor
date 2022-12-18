class StudentClass:
    def __init__(self, id, block):
        self.id = id
        self.block = block
        self.classid = self.getClassID(id)
        self.classlevel = self.getClassLevel(id)


    def getClassID(self, id:int) ->int:
        i = 1
        if (id > 4): # Algebra CP
            i+=1
        if (id > 8): # Algebra E
            i+=1
        if (id > 12): # Algebra H
            i+=1
        if (id > 16): # Biology CP
            i+=1
        if (id > 20): # Biology E
            i+=1
        if (id > 24): # Biology H
            i+=1
        if (id > 30): # English CP
            i+=1
        if (id > 36): # US History
            i+=1
        if (id > 48): # Gym
            i+=1
        if (id > 60): # Spanish - CP
            i+=1
        if (id > 63): # Spanish - H
            i+=1
        if (id > 66): # French - CP
            i+=1
        if (id > 67): # French - H
            i+=1
        if (id > 68): # Chinese - CP
            i+=1
        if (id > 69): # Chinese - H
            i+=1
        if (id > 70): # Latin - CP
            i+=1
        if (id > 71):  # Latin - H
             i += 1
        return i

    def getClassLevel(self, id:int) ->str:
        if (id > 70): # Latin - CP
            return 'CP'
        if (id > 69): # Chinese - H
            return 'H'
        if (id > 67): # French - H
            return 'H'
        if (id > 66): # French - CP
            return 'CP'
        if (id > 63): # Spanish - H
            return 'H'
        if (id > 60): # Spanish - CP
            return 'CP'
        if (id > 48): # Gym
            return 'GYM'
        if (id > 36): # US History
            return 'HISTORY'
        if (id > 30): # English CP
            return 'CP'
        if (id > 24): # Biology H
            return 'H'
        if (id > 20): # Biology E
            return 'E'
        if (id > 16): # Biology CP
            return 'CP'
        if (id > 12): # Algebra H
            return 'H'
        if (id > 8): # Algebra E
            return 'E'
        if (id > 4): # Algebra CP
            return 'CP'

        return 'CP'




    