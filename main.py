from Megoldasok import Megoldasok


def main() -> None:

    print('1. feladat: Az adatok beolvasása')

    m = Megoldasok('valaszok.txt')
    v: str = ""

    print(f'2. feladat: A vetélkedőn {m.versenyzok_szama} versenyző indult.')

    bekert_azonosito: str = str(input('3. Feladat: A versenyző azonosítója = '))
    for e in m.m_lista:
        if bekert_azonosito == e.azonosito:
            v = e.valaszok
            print(f'{e.valaszok}   (a versenyző válasza)')
            break
    else:
        print('Nincs ilyen azonosító.')

    print('4. feladat:')

    print(m.helyes_megoldas, '(a helyes megoldás)')
    for i, e in enumerate(v):
        if e == m.helyes_megoldas[i]:
            print('+', end='')
        else:
            print(' ', end='')
    print(' (a versenyző helyes válaszai)')

    keresett_id = int(input('5.feladat: A fekadat sorszáma = '))
    megoldas = m.feladat_index(keresett_id)
    print(f'A feladatra {megoldas[0]} fő, a versenyzők {megoldas[1]}-a adott helyes választ. ')


if __name__ == "__main__":
    main()
