
taxas_lista = [
    {
        "tipo": "NEGATIVADO",
        "taxas": {"6": 0.04, "12": 0.045, "18": 0.05, "24": 0.053, "36": 0.055}
    },
    {
        "tipo": "SCORE_ALTO",
        "taxas": {"6": 0.02, "12": 0.025, "18": 0.35, "24": 0.038, "36": 0.04}
    },
    {
        "tipo": "SCORE_BAIXO",
        "taxas": {"6": 0.03, "12": 0.035, "18": 0.45, "24": 0.048, "36": 0.05}
    }
]


def getTaxa(tipo, meses='6'):
    for lista in taxas_lista:
        if tipo in lista['tipo']:
            for mes, taxa in lista['taxas'].items():
                if mes == meses:
                    return taxa
