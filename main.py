from Megoldasok import Megoldasok


def main() -> None:

    print('1. feladat: Az adatok beolvasása')

    m = Megoldasok('valaszok.txt')

    print(f'2. feladat: A vetélkedőn {m.versenyzok_szama} versenyző indult.')

    bekert_azonosito: str = str(input('3. Feladat: A versenyző azonosítója = '))
    for e in m.m_lista:
        if bekert_azonosito not in e.azonosito:
            print('Nincs ilyen azonosító.')
            break
        else:
            print(f'{e.valaszok}   (a versenyző válasza)')
            break

#  print(f'4. feladat: {} (a helyes megoldás)')


if __name__ == "__main__":
    main()
