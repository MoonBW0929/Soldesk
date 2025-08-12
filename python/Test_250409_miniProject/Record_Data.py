class RecordData:
    def __init__(self, no, name, vd, date, champ, kill, death, assist):
        self.no = no
        self.name = name
        self.vd = vd
        self.date = date
        self.champ = champ
        self.kill = int(kill)
        self.death = int(death)
        self.assist = int(assist)