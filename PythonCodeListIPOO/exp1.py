class TV:
    ligado = None
    canal = None

    def __init__(self, c):
        self.canal = c
        self.ligado = False


tv = TV(5)
print(tv.canal)
