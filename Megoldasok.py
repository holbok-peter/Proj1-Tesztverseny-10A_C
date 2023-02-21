from Valaszok import Valaszok


class Megoldasok:
    _valaszok: list[Valaszok] = []

    @property
    def versenyzok_szama(self) -> int:
        return len(self._valaszok)

    def __init__(self, fájl_neve: str):
        self._valaszok = []
        with open(fájl_neve, 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines()[1:]:
                self._valaszok.append(Valaszok(sor))
