from Megoldasok import Megoldasok


def main() -> None:

    print('1. feladat: Az adatok beolvasása')

    m = Megoldasok('valaszok.txt')
    print(f'2. feladat: A vetélkedőn {m.versenyzok_szama} versenyző indult.')


if __name__ == "__main__":
    main()
