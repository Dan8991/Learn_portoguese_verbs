def present(verb, person):
    if person == 1:
        return verb[:-2] + "o"
    if person == 4:
        return verb[:-1] + "mos"

    last_letter = verb[-2]
    if last_letter == "a":
        letter = "a"
    else:
        letter = "e"
    if person == 2:
        return verb[:-2] + letter + "s"
    elif person == 3:
        return verb[:-2] + letter
    elif person == 5:
        return verb[:-2] + letter + "m"

def preterito_perfeito_simples(verb, person):
    desinenza = verb[-2:]
    if person == 1:
        if desinenza == "ar":
            return verb[:-2] + "ei"
        else:
            return verb[:-2] + "i"

    if desinenza == "ar" and person == 3:
        return verb[:-2] + "ou"

    if person == 2:
        return verb[:-1] + "ste"

    if person == 3:
        return verb[:-1] + "u"

    if person == 4:
        return verb[:-1] + "mos"

    if person == 5:
        return verb[:-1] + "ram"

def preterito_imperfeito(verb, person):
    radice = verb[:-2]
    desinenza = verb[-2:]

    if desinenza == "ar":
        if person == 1 or person == 3:
            return radice + "ava"
        if person == 2:
            return radice + "avas"
        if person == 4:
            return radice + "ávamos"
        if person == 5:
            return radice +  "avam"

    if person == 1 or person == 3:
        return radice + "ia"
    if person == 2:
        return radice + "ias"
    if person == 4:
        return radice + "íamos"
    if person == 5:
        return radice +  "iam"

def futuro_presente_do_indicativo(verb, person):
    if person == 1:
        return verb[:-1] + "rei"
    if person == 2:
        return verb[:-1] + "rás"
    if person == 3:
        return verb[:-1] + "rá"
    if person == 4:
        return verb[:-1] + "remos"
    if person == 5:
        return verb[:-1] + "rão"
    
