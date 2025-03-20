# morning_lines est une liste de phrases qui seront affichées aléatoirement au début de chaque journée.
init python:
    import random
    
    morning_lines = [
        "Ugh... encore un matin difficile...",
        "Bon, une nouvelle journée commence !",
        "J'aurais dû me coucher plus tôt hier soir...",
        "C'est l'heure de se lever et d'affronter la journée !",
        "Hmm... juste cinq minutes de plus...",
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
    
    salutation_rdm = [
        "Bonjour.",
        "Bien le bonjour.",
        "Bonjour à vous.",
        "Bonjour, bonjour.", 
        "Salutation.",
    ]

    def get_random_salutation():
        return random.choice(salutation_rdm)

# predefined_notes est une liste de notes prédéfinies qui seront affichées aléatoirement lors de la correction des exercices.
init python: 
    import random
    
    predefined_notes = [14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20]
    
    def get_random_note():
     
        if random.choice([True, False]):
            return random.choice(predefined_notes) 
        else:
            return round(random.uniform(14, 20))  

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

    validation_rdm = [  
        "D'accord, allons-y.",  
        "Ok alors.",  
        "Ok.",  
        "D'accord.",  
        "Très bien.",  
        "Ça me va.",  
        "Entendu.",  
        "C'est parti.",  
        "Allons-y.",  
        "Parfait.",  
        "Ça marche.",  
        "On y va.",  
        "Pourquoi pas.",  
        "Ça convient.",  
        "On fait comme ça.",  
        "C'est bon.",  
        "Ça fonctionne.",  
        "Tout est bon.",  
        "Ça passe.",  
        "Go."  
    ]

    def get_random_validation():
        return random.choice(validation_rdm)
