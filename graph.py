def ajouter_noeud(G, lettre):
    G.update({lettre : []})
    return G

def ajouter_arete(G, lettre1, lettre2):
    if lettre1 in G and lettre2 in G:
        G[lettre1].append(lettre2)
        return G
    else:
        return "Erreur noeud non existant"


def parcours_en_profondeur(G, deb):
    a_explore = [deb]
    deja_visit = []
    while a_explore:
        dernier_noeud = a_explore.pop()
        if dernier_noeud not in deja_visit:
            print(dernier_noeud)
            deja_visit.append(dernier_noeud)
        if G[dernier_noeud]:
            for i in G[dernier_noeud]:
                if i not in deja_visit:
                    a_explore.append(i)


def parcours_en_largeur(G, deb):
    a_explore = [deb]
    deja_visit = []
    while a_explore:
        premier_noeud = a_explore.pop(0)
        if premier_noeud not in deja_visit:
            print(premier_noeud)
            deja_visit.append(premier_noeud)
            for i in G[premier_noeud]:
                if i not in deja_visit:
                    a_explore.append(i)



dico = {"A" : ["B"],
        "B" : [],
        "C" : ["A", "B"],
        "D" : ["C"],
        "E" : ["D", "C"]}

parcours_en_profondeur(dico, 'E')
print("---------------------------")
parcours_en_largeur(dico, 'E')

