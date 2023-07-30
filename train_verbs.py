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
pessoas = ["eu", "tu", "ele", "nós", "eles"]

weights, comb = [], []
for verb in verbs:
    for tense in verbs[verb]:
        if tense != "regular" and not verbs[verb][tense]["regular"]:
            weights.extend([w for _, (_, w) in verbs[verb][tense]["conjugation"].items()])
            comb.extend([[verb, tense, conj_verb, p] for conj_verb, (p, _) in verbs[verb][tense]["conjugation"].items()])

for i in range(n_trials):

    regularity = random.choice(["regular", "irregular", "only_irregular", "only_irregular"])
    regularity = "only_irregular"
    verbs_set = regular_verbs if regularity == "regular" else irregular_verbs

    verb = random.choice(verbs_set)
    tense = tenses[random.randint(0, len(tenses) - 1)]
    ind = random.randint(0, 4)

    print("---------------------------")
    person = None
    if regularity == "regular":
        conjugated = conjugate[tense](verb, ind + 1)
        print(f"Verbo: {verb} \nTempo: {tense} \npersona: {ind+1}")
    elif regularity == "irregular":
        if verbs[verb][tense]["regular"]:
            conjugated = conjugate[tense](verb, ind + 1) 
            print(f"Verbo: {verb} \nTempo: {tense} \npersona: {ind+1}")
        else:
            conjugated = list(verbs[verb][tense]["conjugation"].keys())[ind]
            person = verbs[verb][tense]["conjugation"][conjugated][0]
            print(f"Verbo: {verb} \nTempo: {tense} \npersona: {person}")
    else:
        sample_from = ([[c] * (w + 1) for c, w in zip(comb, weights)])
        verb, tense, conjugated, person = random.choice(sample_from)[0]
        print(f"Verbo: {verb} \nTempo: {tense} \npersona: {person}")
    print("---------------------------")

    print()
    input(pessoas[person - 1 if person is not None else ind] + " ")
    print(pessoas[person - 1 if person is not None else ind] + " " + conjugated)
    print()
    print("Did you get it right? (y/n)")
    ans = input()
    if ans == "n" and not verbs[verb]["regular"] and not verbs[verb][tense]["regular"]:
        verbs[verb][tense]["conjugation"][conjugated][1] += 1
        with open("verbs.json", "w") as f:
            json.dump(verbs, f, indent=4)
    elif ans == "y" and not verbs[verb]["regular"] and not verbs[verb][tense]["regular"]:
        if verbs[verb][tense]["conjugation"][conjugated][1] > 0:
            verbs[verb][tense]["conjugation"][conjugated][1] -= 1
            with open("verbs.json", "w") as f:
                json.dump(verbs, f, indent=4)


    


