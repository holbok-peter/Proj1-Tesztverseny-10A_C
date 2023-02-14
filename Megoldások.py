from Szavazatok import Szavazatok


class Megoldások:
    _szavazatok: list[Szavazatok] = []


    def __init__(self, fájl_neve: str):
        self._szavazatok = []
        with open(fájl_neve, 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines():
                self._szavazatok.append(Szavazatok(sor))