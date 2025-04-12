class Config:
    tokens =(
        'NUMERO',
        'PUNTO',
        'MONEDA',
        'END'
        #'CANTIDAD',
        #'ORIGEN',
        #'DESTINO',
        )
    divisas=(
        "Dolares",
        "Euros",
        "Lempiras",
        "Pesos"
    )
    tasas = {
        "LempirasDolares": 0.039,
        "DolaresLempiras": 25.40,
        "LempirasEuros": 0.035,
        "EurosLempiras": 28.70, 
        "LempirasPesos": 0.79,
        "PesosLempiras": 1.27,
    }