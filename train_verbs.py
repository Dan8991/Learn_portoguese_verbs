import json
import random
from conjugations import present, preterito_perfeito_simples, preterito_imperfeito, futuro_presente_do_indicativo
from time import sleep

with open("verbs.json", "r") as f:
    verbs = json.load(f)

weight_regular = 1
weight_irregular = 3

regular_verbs = [v for v in verbs.keys() if verbs[v]["regular"]]
irregular_verbs = [v for v in verbs.keys() if not verbs[v]["regular"]]

n_trials = 100

tenses = ["presente", "preterito perfeito simples", "preterito imperfeito", "futuro presente do indicativo"]
conjugate = {
    "presente": present,
    "preterito perfeito simples": preterito_perfeito_simples,
    "preterito imperfeito": preterito_imperfeito,
    "futuro presente do indicativo": futuro_presente_do_indicativo
}


for i in range(n_trials):

    is_regular = random.choice(weight_regular * [True] + weight_irregular * [False])
    verbs_set = regular_verbs if is_regular else irregular_verbs

    verb = random.choice(verbs_set)
    tense = tenses[random.randint(0, len(tenses) - 1)]
    ind = random.randint(0, 4)

    print("---------------------------")
    if is_regular:
        conjugated = conjugate[tense](verb, ind + 1)
        print(f"Verbo: {verb} \nTempo: {tense} \npersona: {ind+1}")
    else:
        if verbs[verb][tense]["regular"]:
            conjugated = conjugate[tense](verb, ind + 1) 
            print(f"Verbo: {verb} \nTempo: {tense} \npersona: {ind+1}")
        else:
            conjugated = list(verbs[verb][tense]["conjugation"].keys())[ind]
            person = verbs[verb][tense]["conjugation"][conjugated][0]
            print(f"Verbo: {verb} \nTempo: {tense} \npersona: {person}")
    print("---------------------------")

    print()
    input()
    print(conjugated)
    print()
    sleep(2)
    


