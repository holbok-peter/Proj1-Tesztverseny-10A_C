from Megoldások import Megoldások


def main() -> None:
    valaszok: list[Megoldások] = []
    with open('valaszok.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            valaszok.append(Megoldások(sor))


if __name__ == "__main__":
    main()
