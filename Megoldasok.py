from Szavazatok import Szavazatok


class Megoldasok:
    _szavazatok: list[Szavazatok] = []

    @property
    def versenyzok_szama(self) -> int:
        return len(self._szavazatok)

    def __init__(self, fájl_neve: str):
        self._szavazatok = []
        with open(fájl_neve, 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines()[1:]:
                self._szavazatok.append(Szavazatok(sor))
