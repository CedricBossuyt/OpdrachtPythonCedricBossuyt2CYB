class Poetser:
    def __init__(self, naam):
        self._naam = naam

    @property
    def naam(self):
        return self._naam

    @naam.setter
    def naam(self, nieuwe_naam):
        self._naam = nieuwe_naam