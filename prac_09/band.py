class Band():
    def __init__(self, name):
        self.roster = []
        self.name = name

    def add(self, musician):
        self.roster.append(musician)

    def play(self):
        result = ''
        for musician in self.roster:
            result += musician.play()
            result += '\n'
        return result

    def __str__(self):
        return f"{self.name} ({''.join(f'{musician} ' for musician in self.roster)})"