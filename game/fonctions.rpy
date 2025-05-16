# morning_lines est une liste de phrases qui seront affichées aléatoirement au début de chaque journée.
init python:
    import random
    
    morning_lines = [
        "Ugh... encore un matin difficile...",
        "Bon, une nouvelle journée commence !",
        "J'aurais dû me coucher plus tôt hier soir...",
        "C'est l'heure de se lever et d'affronter la journée !",
        "Hmm... juste cinq minutes de plus...",
        "Hmm... je n'ai pas envie de me lever.",
        "Oh déjà...",
        "Oh super....",  
    ]
    
    def get_random_morning_line():
        return random.choice(morning_lines)

# entrepôt_rdm est une liste de phrases qui seront affichées aléatoirement au moment de la fouille de l'entrepôt.
init python:
    import random 
    
    entrepot_rdm = [
        "Tu jettes un coup d'œil à l'intérieur de l'entrepôt.",
        "Tu explores rapidement les alentours de l'entrepôt.",
        "Tu fouilles un peu dans l'entrepôt.",
        "Tu t'aventures prudemment dans l'entrepôt.",
        "Tu examines l'intérieur de l'entrepôt.",
        "Tu observes les environs de l'entrepôt.",
        "Tu commences à inspecter l'entrepôt.", 
    ]
    
    def get_random_entrepot(): 
        return random.choice(entrepot_rdm)

# salutation_rdm est une liste de phrases qui seront affichées aléatoirement au moment des salutations envers la professeure.
init python:
    import random
    
    salutation_rdm_list = [
        "Bonjour.",
        "Bien le bonjour.",
        "Bonjour, bonjour.",
        "Salutation.", 
    ]
    
    def get_random_salutation(): 
        return random.choice(salutation_rdm_list) 

# predefined_notes est une liste de notes prédéfinies qui seront affichées aléatoirement lors de la correction des exercices.
init python: 
    import random
    
    predefined_notes = [14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20]
    
    def get_random_note():
     
        if random.choice([True, False]):
            return random.choice(predefined_notes) 
        else:
            return round(random.uniform(14, 20), 1)  

# remerciement_rdm est une liste de phrases qui seront affichées aléatoirement au moment des remerciements envers la professeure.
init python:
    import random

    remerciement_rdm = [ 
        "Merci pour ces deux années ici.",
        "C'était un honneur d'être ici.",
        "On a appris plein de choses grâce à vous.",
        "Merci encore infiniment pour tout.",
        "Votre enseignement nous a beaucoup apporté, merci.",
        "Nous garderons un excellent souvenir de ces années, merci.",
        "Un grand merci pour votre patience et votre engagement.",
    ]

    def get_random_remerciement():
        return random.choice(remerciement_rdm)

# validation_rdm est une liste de phrases qui seront affichées aléatoirement au moment des validations de choix.
init python:
    import random

    validation_list = [  
        "D'accord.",  
        "Ok alors.",  
        "Ok.",  
        "Très bien.",    
        "Entendu.", 
        "Ça marche.",  
    ]

    def get_random_validation():
        return random.choice(validation_list)

# easter egg 
init python:
    import random

    def get_random_enchente_m():
        return "enchanté" if random.random() < 0.99 else "enchantier"

# easter egg
init python:
    import random

    def get_random_enchente_f():
        return "enchantée" if random.random() < 0.99 else "enchantier"

init python:
    import random

    start_list = [  
        "Démarrage en cours...",  
        "Initialisation en cours...",  
        "Activation en cours...",  
        "Lancement du système...",
        "Mise en route...",
        "Système en cours de préparation...",
        ]

    def get_random_start():
        return random.choice(start_list) 

init python:
    import random

    dortoir_list = [  
        "De retour au dortoir.",
        "On est enfin au dortoir.",
        "Nous voilà au dortoir.",
        "Enfin dans le dortoir.",
        "Le dortoir, enfin !",
        ]

    def get_random_dortoir():
        return random.choice(dortoir_list) 

init python:
    import random

    fais_du_bien_list = [  
        "Oui je confirme ça fait du bien.",
        "Ah oui, ça fait du bien !",
        "Je confirme, ça fait du bien.",
        "C'est clair, ça fait du bien.",
        "Oui, c'est agréable, ça fait du bien.",
        "Totalement d'accord, ça fait du bien.",
        "Je suis bien d'accord, ça fait du bien.",
    ]

    def get_random_fais_du_bien():
        return random.choice(fais_du_bien_list) 

init python:
    import random 

    comment_ca_va_list = [
        "Comment tu vas ?",
        "Tu vas bien ?",
        "Comment ça va ?",
        "Ça va comment ?",
        "Coucou, comment ça va ?",
        "Bonjour, comment ça va ?",
        "Salut, comment ça va ?",
        "Bonjour, ça va ?",
        "Salut, ça va ?", 
        "Oh salut, ça va ?", 
    ]

    def get_random_comment_ca_va():
        return random.choice(comment_ca_va_list)

init python:
    import random

    je_vais_bien_rdm_list = [
        "Je vais bien.",
        "Tout va bien.",
        "Ça roule.",
        "Je me sens bien.",
        "Nickel.",
        "Ça va super.",
        "Je vais bien, merci.",
    ]

    def get_random_je_vais_bien():
        return random.choice(je_vais_bien_rdm_list)

init python:
    import random 

    thanks_list = [
        "Merci.",
        "Merci beaucoup.",
        "Merci infiniment.",
    ]

    def get_random_thanks():
        return random.choice(thanks_list)  

init python:
    import random 

    Nothing_list = [
        "De rien.",
        "Mais de rien.",
        "Pas de souci.",
    ]

    def get_random_nothing():
        return random.choice(Nothing_list)  

init python:
    import random 

    endlesson_list = [
        "Le cours est fini, vous êtes libres de partir.",
        "C'est tout, vous pouvez sortir.",
        "On s'arrête ici, vous pouvez y aller.",
        "Le cours touche à sa fin, vous pouvez partir.",
        "Voilà, c'est la fin du cours, vous pouvez sortir.",
        "Nous avons terminé, vous êtes libres.",
        "Fin de la leçon, vous pouvez quitter la salle.",
        "C'est bon, vous pouvez partir.",
        "La séance est terminée, vous pouvez quitter la classe.", 
    ]

    def get_random_endlesson():
        return random.choice(endlesson_list)

init python:
    import random 

    toilet_list = [
        "Bon je reviens, je vais juste aux toilettes.",
        "Bon je reviens je vais juste aux toilettes, j'ai le cigare au bout des lévres.",
        "Je vais juste aux toilettes, je reviens.", 
        "Je vais juste aux toilettes, je reviens dans deux minutes.",
        "Je vais juste aux toilettes, je reviens dans un instant.",
        "Je vais juste aux toilettes, je reviens dans un petit moment.",
        "Bon je reviens, je vais me couler une dalle.", 
        "Bon je reviens, je vais couler un bronze.", 
        "Bon je reviens, je vais sur le trône.", 
        "Bon je reviens, je vais poser un classique.", 
    ]

    def get_random_toilet():
        return random.choice(toilet_list)  

init python:
    import random 

    go_eat_list = [
        "Bon on va manger ?",
        "On se fait un repas ?",
        "Ça te dit de manger ?",
        "Prêt à manger ?",
        "On va grignoter quelque chose ?",
        "Tu veux manger avec moi ?",
        "On se pose pour manger ?",
        "T'es chaud pour un repas ?",
        "Ça te tente de manger ?",
        "Tu es partant pour manger ?",
        "Et si on mangeait ?",
        "Viens, on va casser la croûte !",
        "On se fait une pause bouffe ?",
        "Si on allait remplir nos estomacs ?",
        "Allez, c’est l’heure de manger !",
        "Tu veux qu’on aille se nourrir un peu ?",
        "On se fait un petit festin ?", 
        "Viens, j’t’embarque manger !",
        "Et si on calmait notre faim ensemble ?",
    ]

    def get_random_go_eat():
        return random.choice(go_eat_list)

init python:
    import random

    Service_list = [
        "C’est bon, tu t’es servie ?",
        "Tu t’es bien servie à manger ?", 
        "Tu t’es fait une assiette ?", 
        "C’est bon, tu t’es fait une assiette ?",
    ]

    def get_random_service():
        return random.choice(Service_list)

init python:
    import random

    Sit_list = [ 
        "Oui, c’est bon, on peut y aller.",
        "J’ai fini, on s’installe ?",
        "On peut aller s’asseoir maintenant.",
        "Je suis prête, allons nous poser.",
        "J’ai tout pris, on va s’asseoir ?",
        "Tout est bon pour moi, on y va.",
        "Oui, j’ai ce qu’il faut. On se pose ?",
        "C’est bon, viens, on s’assoit.",
        "J’ai tout, allons nous installer.",
        "C’est prêt de mon côté, direction la table !",
    ]

    def get_random_sit():
        return random.choice(Sit_list)

init python:
    import random 

    find_food_list = [

        "Bon on va prendre à manger ?",
        "Bon on va chercher à manger ?",
        "Bon on va se prendre à manger ?",
        "Bon on va se chercher à manger ?",
        "On va chercher à manger ?", 
        "On va prendre à manger ?",
        "On va se chercher à manger ?",
        "On va se prendre à manger ?",

    ]

    def get_random_find_food():
        return random.choice(find_food_list) 

init python:
    import random 

    go_in_class_list = [

        "Bon on va en cours ?",
        "On file en cours ?",
        "On part en cours maintenant ?",
        "C'est l'heure des cours, on y va ?",
        "C'est parti pour les cours ?", 
        "C’est l’heure, on y va pour les cours ?", 
        "On y va ? Les cours nous attendent ! ",
    ]

    def get_random_go_in_class():
        return random.choice(go_in_class_list) 

init python:
    import random 

    suivi_list = [  
        "D'accord, je te suis.",  
        "Je te suis.",  
        "Je te suis, allons-y.",  
        "Oui, je te suis.", 
        "Je te suis, pas de problème.",
        "Je te suis, allons-y ensemble.",
        "Oui je te suis, pas de problème.",
        "Oui je te suis, allons-y ensemble.",
        "Je te suis, pas de souci.",
        ] 

    def get_random_suivi():
        return random.choice(suivi_list)

init python:
    import random

    return_dorm_list = [  
        "On rentre au dortoir ?",
        "Bon on rentre au dortoir ?",
        "On y va, direction le dortoir ?",
        "Tu veux qu’on retourne au dortoir ?",
        "On reprend le chemin du dortoir ?",
        "Bon on file au dortoir ?",        
        "On file au dortoir ?", 
        "Bon on rentre se poser au dortoir ?",
        "On rentre se poser au dortoir ?",
        "Ça te dit de retourner au dortoir ?", 
    ] 

    def get_random_return_dorm():
        return random.choice(return_dorm_list)
