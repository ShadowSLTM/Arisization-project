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

<<<<<<< HEAD
=======

>>>>>>> 9902371b6fd1a713875ee474627a89602293e339
# predefined_notes est une liste de notes prédéfinies qui seront affichées aléatoirement lors de la correction des exercices.
init python:
    import random
    
    predefined_notes = [14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20]
    
    def get_random_note():
     
        if random.choice([True, False]):
            return random.choice(predefined_notes) 
        else:
            return round(random.uniform(14, 20), 1)  