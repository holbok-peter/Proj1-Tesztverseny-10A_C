from Valaszok import Valaszok


class Megoldasok:
    _valaszok_list: list[Valaszok]

    @property
    def versenyzok_szama(self) -> int:
        return len(self._valaszok_list)

    @property
    def m_lista(self):
        return self._valaszok_list

    def __init__(self, fájl_neve: str):
        self._valaszok_list = []
        with open(fájl_neve, 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines()[1:]:
                self._valaszok_list.append(Valaszok(sor))
