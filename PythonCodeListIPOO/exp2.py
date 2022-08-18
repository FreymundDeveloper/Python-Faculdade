class Tv:
    ligada = None
    canal = None

    def __init__(self):
        self.ligada = False
        self.canal = 2

    def __del__(self):
        self.ligada = None
        self.canal = None

    def setCanal(self, c):
        self.canal = c


tv = Tv()
print('ligada:' + str(tv.ligada))
print('Canal: %d' % tv.canal)
tv_sala = Tv()
tv_sala.canal = 5
tv_sala.ligada = True
print(tv_sala.ligada)
print(tv_sala.canal)
del tv
