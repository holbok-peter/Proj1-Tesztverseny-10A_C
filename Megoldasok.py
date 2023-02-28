from Valaszok import Valaszok


class Megoldasok:
    _valaszok_list: list[Valaszok]
    helyes_megoldas: str
    válaszok: str = ''

    @property
    def versenyzok_szama(self) -> int:
        return len(self._valaszok_list)

    @property
    def m_lista(self):
        return self._valaszok_list

# 2.feladat:

    def __init__(self, fájl_neve: str):
        self._valaszok_list = []
        with open(fájl_neve, 'r', encoding='utf-8') as file:
            for index, sor in enumerate(file.read().splitlines()):
                if index == 0:
                    self.helyes_megoldas = sor
                else:
                    self._valaszok_list.append(Valaszok(sor))

# 3.feladat:

    def valaszok(self, azonosito: str) -> str:
        for versenyzo in self._valaszok_list:
            if versenyzo.azonosito == azonosito:
                self.válaszok: str = str(versenyzo.valaszok)
                return self.válaszok
        return "Nincs ilyen azonosító."

# 4.feladat:
    @property
    def megoldas(self):
        szöveg: str = ""
        for i, e in enumerate(self.válaszok):
            if e == self.helyes_megoldas[i]:
                szöveg += "+"
            else:
                szöveg += " "
        return szöveg

# 5.feladat:

    def feladat_index(self, keresett_id: int):
        helyes_megoldasok_szama: int = 0
        for i in self._valaszok_list:
            if i.valaszok[keresett_id - 1] == self.helyes_megoldas[keresett_id - 1]:
                helyes_megoldasok_szama += 1
        return [helyes_megoldasok_szama, round((helyes_megoldasok_szama / len(self._valaszok_list) * 100), 2)]

# 6.feladat:
