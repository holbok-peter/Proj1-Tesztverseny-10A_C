class Valaszok:
    azonosító: str
    válaszok: str

    def __init__(self, sor: str):
        azon, válasz = sor.split(' ')
        self.azonosító = azon
        self.válaszok = válasz
