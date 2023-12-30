class Poetssessie:
    def __init__(self, persoon_id, duur):
        self._persoon_id = persoon_id
        self._duur = duur

    @property
    def persoon_id(self):
        return self._persoon_id

    @property
    def duur(self):
        return self._duur

    @duur.setter
    def duur(self, nieuwe_duur):
        self._duur = nieuwe_duur
