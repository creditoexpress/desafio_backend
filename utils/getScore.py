def getScore(qs):
    score = 0
    for cliente in qs:
        score = cliente.score

    return score
