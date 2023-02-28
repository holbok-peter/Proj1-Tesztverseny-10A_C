from Megoldasok import Megoldasok


def main() -> None:

    # 1.feladat:

    print('1. feladat: Az adatok beolvasása')

    m = Megoldasok('valaszok.txt')

    # 2.feladat:

    print(f'2. feladat: A vetélkedőn {m.versenyzok_szama} versenyző indult.')

    # 3.feladat:

    bekert_azonosito: str = str(input('3. Feladat: A versenyző azonosítója = '))
    print(f'{m.valaszok(bekert_azonosito)}  ')
    m.valaszok(bekert_azonosito)

    # 4.feladat:

    print('4. feladat:')

    print(m.helyes_megoldas, '(a helyes megoldás)')

    print(f' {m.megoldas} (a versenyző helyes válaszai)')

    # 5.feladat:

    keresett_id = int(input('5.feladat: A fekadat sorszáma = '))
    megoldas = m.feladat_index(keresett_id)
    print(f'A feladatra {megoldas[0]} fő, a versenyzők {megoldas[1]}-a adott helyes választ. ')

    # 6.feladat:

    print("6. feladat: A versenyzők pontszámának meghatározása")


if __name__ == "__main__":
    main()
