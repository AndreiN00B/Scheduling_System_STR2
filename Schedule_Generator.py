class schedule:
    def __init__(self):
        # initializes the schedule class
        self.schedule = [[None, None, None, None, None],
                         [None, None, None, None, None],
                         [None, None, None, None, None],
                         [None, None, None, None, None],
                         [None, None, None, None, None],
                         [None, None, None, None, None],
                         [None, None, None, None, None],
                         [None, None, None, None, None],
                         [None, None, None, None, None]]
        self.free = []
        for x in range(5):
            for y in range(9):
                self.free.append(str(x) + str(y))

    def gen_schedule(self, list_sub):
        # generates a randomized non-conflicting schedule
        from random import randrange
        for sub in list_sub:
            _randomindex = str(self.free.pop(randrange(0, len(self.free))))
            self.schedule[int(_randomindex[1])][int(_randomindex[0])] = sub

    def output_schedule(self):
        s = ''
        for i in range(9):
            for j in range(5):
                s += str(self.schedule[i][j]) + ', '
            s += '\n'
        print(s)


list_sub = ["Math", "Phys", "Biol", "Chem", "Engl", "Fili"]
sched = schedule()
sched.gen_schedule(list_sub)
sched.output_schedule()
