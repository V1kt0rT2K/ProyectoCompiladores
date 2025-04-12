class Config:
    tokens =(
        'NUMERO',
        'PUNTO',
        'MONEDA',
        'END'
    )
    divisas = (
        "Dolares",
        "Euros",
        "Lempiras",
        "Pesos",
        "Yenes",
        "Libras",
        "Bitcoin"
    )
    tasas = {
        "LempirasDolares": 0.039,
        "DolaresLempiras": 25.40,
        "LempirasEuros": 0.035,
        "EurosLempiras": 28.70, 
        "LempirasPesos": 0.79,
        "PesosLempiras": 1.27,
        "LempirasYenes": 5.92,
        "YenesLempiras": 0.17,
        "LempirasLibras": 0.030,
        "LibrasLempiras": 33.33,
        "LempirasBitcoin": 0.0000021,
        "BitcoinLempiras": 476190.48,
    }