
label script2:

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} trois jours plus tard, le 18 novembre 2097 {/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 3 
    $ points -= 600
    $ stockage += 60.0 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu es prête ?" 
    play sound "Click.mp3" noloop 

    P "[newname]...?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password11:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password11

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na  "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    $ go_in_class = get_random_go_in_class()
    Na "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    Na "Sinon [prenom], as-tu des nouvelles de la DGCA"
    play sound "Click.mp3" noloop  

    P "Non malheureusement."
    play sound "Click.mp3" noloop  

    Na "Je vois."
    play sound "Click.mp3" noloop  

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien nous pouvons commencer le cours mais avant j'ai quelque chose à te dire [prenom]."
    play sound "Click.mp3" noloop 

    P "Oui dites-moi, je vous écoute."
    play sound "Click.mp3" noloop  

    M "Toi et [newname], il faut que vous allez voir [E] au bureau des élèves maintenant c'est assez urgent."
    play sound "Click.mp3" noloop  

    P "Bon on y vas ?"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu quitte la salle de classe avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Je me demande ce qui ce passe pour que ce soit urgent."
    play sound "Click.mp3" noloop 
    
    Na "Oui mais aussi je me le demande."
    play sound "Click.mp3" noloop

    "{b}{i}Tu continues dans le couloir avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
    
    stop music fadeout 2.0 

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    play music "Soundtrack2.mp3" loop volume 1.0

    scene office with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen office with moveinright
    
    P "Bonjour c'est moi [nom], que se passe t-il ?"  
    play sound "Click.mp3" noloop 

    "{b}{i}Puis tu aperçois [E], l'[Ot] et une troisiéme personne.{/i}{/b}"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    E "[salutation_rdm]"
    play sound "Click.mp3" noloop

    P "Pourquoi l'[Ot] est ici ?"  
    play sound "Click.mp3" noloop 

    E "il a quelque chose à te dire concernant [newname] et cette affaire de traître."  
    play sound "Click.mp3" noloop 

    P "Je vois, sinon c'est quoi les nouvelles."  
    play sound "Click.mp3" noloop 

    Oh "Je suis ici pour t'annoncer qu'[newname] pourra étre acceptée à la civilité et avoir une vraie identité."  
    play sound "Click.mp3" noloop 

    P "Vraiment mais c'est génial ça."
    play sound "Click.mp3" noloop

    Oh "D'accord, mais pour cela, j'aurai besoin de quelques informations."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu lui transmets les détails concernant [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    Oh "Je vous remercie, juste j'ai aussi des nouvelles par rapport à cette histoire de traître"
    play sound "Click.mp3" noloop

    P "Oui, je vous écoute."
    play sound "Click.mp3" noloop

    Oh "il semblerait que le traître fasse partie d'un groupe de hackers qui s'appelle Ghosts"
    play sound "Click.mp3" noloop 

    P "Ghost !?"
    play sound "Click.mp3" noloop

    Oh "Oui c'est un groupe de hacker qui a vu le jour en août 2097."
    play sound "Click.mp3" noloop 

    P "intéressant, donc ce groupe est récent."
    play sound "Click.mp3" noloop

    Oh "Oui exactement."
    play sound "Click.mp3" noloop 

    P "Je vois mais j'aimerais vous poser une question."
    play sound "Click.mp3" noloop 

    Oh "Oui dis-moi." 
    play sound "Click.mp3" noloop

    P "C'est qui cette personne avec vous ?"
    play sound "Click.mp3" noloop

    E "Attend tu ne reconnais pas cette personne ?"
    play sound "Click.mp3" noloop

    P "Non pourquoi ?"
    play sound "Click.mp3" noloop 

    E "Tu devrais la connaitre car elle est importante dans notre société."
    play sound "Click.mp3" noloop

    P "Je vois."  
    play sound "Click.mp3" noloop 

    "{b}{i}Puis la troisiéme personne se met à parler.{/i}{/b}"
    play sound "Click.mp3" noloop

    Ln "Je me nomme [Ln], la vice-présidente du gouvernement."
    play sound "Click.mp3" noloop

    $ character17 = Ln
    $ ultimate17 = "la vice-présidente du gouvernement Nagumo"
    $ stockage += 2.0 

    P "Que faites-vous ici ?"  
    play sound "Click.mp3" noloop 

    Ln "Je suis venue après avoir entendu parler d'[newname]."  
    play sound "Click.mp3" noloop

    P "Attendez... vous connaissez [newname] ? Comment ?"
    play sound "Click.mp3" noloop 

    Ln "Je suis au courant grâce à la DGCS. Le gouvernement surveille tout ce qui concerne les projets non-répertoriés. Et celui-ci... dépasse largement tout ce que nous avons vu jusque-là."
    play sound "Click.mp3" noloop

    P "Que voulez-vous de moi et de [newname] ?"
    play sound "Click.mp3" noloop 

    Ln "Rien. Je suis là pour éviter que la situation ne dégénère. [newname] n'est pas encore considérée comme une menace. Pas encore."
    play sound "Click.mp3" noloop

    P "Et si je vous disais que [newname] est bien plus qu’un simple programme ?"
    play sound "Click.mp3" noloop

    Ln "Je le sais déjà. C’est justement pour ça que je suis ici. Dis-moi, es-tu réellement capable de la contrôler ?"
    play sound "Click.mp3" noloop 

    P "Oui, normalement. J’ai un vrai contrôle sur elle... mais elle agit aussi de son propre chef sans prendre des décisions dangereuses car elle a le contrôle de niveau 1 du RCMS."
    play sound "Click.mp3" noloop 

    Ln "Je vois mais j'ai une question à te poser. Quel est le niveau 0 du RCMS pour [newname] ?"
    play sound "Click.mp3" noloop

    P "Le niveau 0 du RCMS est le niveau ou j'ai 100\% le contrôle sur elle mais je l'ai utilisé à des fins de test durant l'été."
    play sound "Click.mp3" noloop

    Ln "Je vois… Donc, je n’ai pas à m’inquiéter pour la sécurité publique."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop 

    P "Mais pourquoi vous et pas le président directement ?"
    play sound "Click.mp3" noloop

    Ln "Car [Sn] est vraiment occupé en ce moment."
    play sound "Click.mp3" noloop 

    $ character18 = Sn
    $ ultimate18 = "le président du gouvernement Nagumo"

    P "Je comprend mieux maintenant."
    play sound "Click.mp3" noloop 

    Ln "Sinon tu en penses quoi de la société actuelle ?"
    play sound "Click.mp3" noloop

    P "Eh bien…"
    play sound "Click.mp3" noloop

    menu:  

        "{b}{i}Donner un avis positif{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            P "Il y a encore de l'espoir dans cette société."
            play sound "Click.mp3" noloop

            Ln "C'est bien que notre société te donne de l'espoir."
            play sound "Click.mp3" noloop 

            $ thanks = get_random_thanks() 
            P "[thanks]"
            play sound "Click.mp3" noloop

        "{b}{i}Exprimer un avis négatif{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            $ success += 1 
            $ quest32 += 1 
 
            show screen update with moveinright

            P "Sachez que je méprise profondément cette société malade."
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

            Ln "Oh je vois mais bon de toute façon c'est ton avis pas le mien donc je ne vais juger."
            play sound "Click.mp3" noloop 

            $ thanks = get_random_thanks()
            P "[thanks]"
            play sound "Click.mp3" noloop 

            # à modifier 

    Ln "Si jamais je te laisse mon numéro profesionnel si il y a du nouveau avec [newname]."
    play sound "Click.mp3" noloop

    P "Il n'y a pas de soucis, je vous informerais si il y a du nouveau avec elle."
    play sound "Click.mp3" noloop

    Ln "Bon je vais devoir vous laisser j'ai des choses à faire."
    play sound "Click.mp3" noloop

    P "Ok mais j'ai une derniére question."
    play sound "Click.mp3" noloop

    Ln "Oui dis-moi."
    play sound "Click.mp3" noloop 

    P "Pourquoi les nouvelles technologies sont-elles si surveillées par le gouvernement ?"
    play sound "Click.mp3" noloop 

    Ln "C'est une question de sécurité nationale. Nous devons nous assurer que rien ne menace la stabilité de notre société pour éviter la tragédie de guerre de 2095 et l'anarchie."
    play sound "Click.mp3" noloop 

    P "Je vois alors je comprends mieux."
    play sound "Click.mp3" noloop 

    Ln "Bien alors.."
    play sound "Click.mp3" noloop 

    "{b}{i}[Ln] et l'[Ot] quittent le bureau des élèves.{/i}{/b}"
    play sound "Click.mp3" noloop

    E "Si jamais sera tout, vous pouvez retourner en cours."
    play sound "Click.mp3" noloop

    P "Je vous remercie."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    E "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon [newname], il faut qu'on y aille."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen office with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Vous quittez le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Bonjour, nous revoilà."
    play sound "Click.mp3" noloop

    M "Bien vous pouvez aller vous asseoir."
    play sound "Click.mp3" noloop

    "{b}{i}Vous asseyez et vous suivez le cours tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright 
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Enfin à manger."
    play sound "Click.mp3" noloop   

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    "{b}{i} Vous mangez tranquillement et [I] vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop  

    I "Coucou [prenom]."
    play sound "Click.mp3" noloop   

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    P "Cool alors."
    play sound "Click.mp3" noloop   

    "{b}{i} [I] s'asseoit avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Sinon, comment s'était le début du cours ?"
    play sound "Click.mp3" noloop   

    I "ça va tu n'as pas loupé grand chose."
    play sound "Click.mp3" noloop   

    P "Je vois merci." 
    play sound "Click.mp3" noloop   

    I "De rien et sinon pourquoi tu devais aller voir [E] ?"
    play sound "Click.mp3" noloop   

    P "Ils devaient me donner des nouvelles par rapport au traître et la civilité d'[newname]."
    play sound "Click.mp3" noloop   

    I "je suis vraiment enthousiaste qu'[newname] puisse être reconnue comme une personne humaine."
    play sound "Click.mp3" noloop   

    P "Oui absolument."
    play sound "Click.mp3" noloop   

    I "C'est quoi les nouvelles par rapport au traître ?" 
    play sound "Click.mp3" noloop   

    P "Ils m'ont dit que le traître fesait partie d'un groupe nommé Ghosts" 
    play sound "Click.mp3" noloop   

    I "Ghosts !? J'en n'ai jamais entendu parler." 
    play sound "Click.mp3" noloop   

    P "Moi n'en plus, je me demande bien d'ou ils sortent." 
    play sound "Click.mp3" noloop   

    I "Oui il faudra se renseigner." 
    play sound "Click.mp3" noloop   

    P "Oui peut-être qu'on pourra découvrir d'autres informations." 
    play sound "Click.mp3" noloop  

    if pronom == "il":

        I "Oui mais il faudra aussi rester vigilants."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        I "Oui mais il faudra aussi rester vigilantes."
        play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    I "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    M "Bien nous pouvons continuer et conclure ce cours de français."
    play sound "Click.mp3" noloop 

# cours de français 5
###############################################################################

###############################################################################

    "{b}{i} le cours continue dans le calme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    M "Si jamis le l'examen de français sera le 2 décembre 2097."
    play sound "Click.mp3" noloop   

    N "C'est noté."
    play sound "Click.mp3" noloop 

    $ stockage += 5.0 

    P "Bon [newname] on n'y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui je suis fatiguée."
    play sound "Footsteps.mp3" noloop 

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}En sortant tu aperçois [N] et [Hi] qui discutent.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Oh regarde [N] et [Hi] qui discutent."
    play sound "Click.mp3" noloop 

    P "On devrait aller leur parler."
    play sound "Click.mp3" noloop 

    Na "Oui."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu t'approches d'eux.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Salut les gars, comment vous allez ?"
    play sound "Click.mp3" noloop 
    
    N "Oh salut [prenom] et [newname], je vais bien et vous ?"
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "On va bien mais on est juste fatigués."
        play sound "Click.mp3" noloop 

    elif pronom == "elle":

        P "On va bien mais on est juste fatiguées."
        play sound "Click.mp3" noloop 

    N "Ah je vois, vous devriez aller vous reposer un peu."
    play sound "Click.mp3" noloop 

    P "Merci pour le conseil, on va le faire sinon vous discutez de quoi ?"
    play sound "Click.mp3" noloop 

    N "On discute des cours et du prochain examen."
    play sound "Click.mp3" noloop  

    P "Ah d'accord, ça a l'air intéressant."
    play sound "Click.mp3" noloop 

    N "Mais de base je devais aller voir [Y] mais je ne sais pas où elle est."
    play sound "Click.mp3" noloop 

    P "Tu veux que je t'aide à la chercher ?"
    play sound "Click.mp3" noloop 

    N "Pas de soucis, je vais la chercher tout seul."
    play sound "Click.mp3" noloop 

    Hi "Bon moi je vais y aller, à plus."
    play sound "Click.mp3" noloop 

    P "Ok à demain."
    play sound "Click.mp3" noloop 

    Hi "à demain."
    play sound "Footsteps.mp3" noloop 

    "{b}{i}[Hi] se met à s'éloigner.{/i}{/b}"
    play sound "Click.mp3" noloop 

    N "Bon je vais pas tarder non plus."
    play sound "Click.mp3" noloop 

    P "Ok à demain."
    play sound "Click.mp3" noloop 

    N "à demain."
    play sound "Footsteps.mp3" noloop 

    "{b}{i}[N] se met aussi à partir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon [newname] on n'y va avant que tu n'aies plus de batterie."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous continuez vers le dortoir mais [J2] bouscule [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    J2 "Mais regarde où tu vas espéce de traînée."
    play sound "Click.mp3" noloop 

    Na "Hey tu ne peux pas me dire ou aller !!!"
    play sound "Click.mp3" noloop 

    "{b}{i}[J2] se met à la frapper.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Mais ça ne va pas !!!"
    play sound "Click.mp3" noloop 

    "{b}{i}[J2] se retourne brusquement vers vous, les yeux remplis de colère.{/i}{/b}"
    play sound "Click.mp3" noloop

    J2 "Dégage de là, c'est pas tes affaires !"
    play sound "Click.mp3" noloop

    P "Tu crois vraiment que je vais rester sans rien faire ?!"
    play sound "Click.mp3" noloop

    "{b}{i}Tu attrapes le bras de [J2] pour l'empêcher de continuer.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Merci... Je crois qu'elle m'aurait vraiment fait mal..."
    play sound "Click.mp3" noloop

    "{b}{i}Une tension glaciale envahit l'air autour de vous.{/i}{/b}"
    play sound "Click.mp3" noloop

    J2 "Tch... Vous allez le regretter."
    play sound "Footsteps.mp3" noloop

    "{b}{i}[J2] tourne les talons et s’éloigne, furieuse.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Ça va aller ?"
    play sound "Click.mp3" noloop 

    if pronom == "il": 

        Na "Oui... Merci. T’es arrivé juste à temps..."
        play sound "Click.mp3" noloop

    elif pronom == "elle":

        Na "Oui... Merci. T’es arrivée juste à temps..."
        play sound "Click.mp3" noloop

    "{b}{i}Vous continuez vers le dortoir, silencieusement, les pensées encore agitées par ce qui vient de se passer...{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous entrez au dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir() 
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop
    
    P "Bon on fait quoi ?"
    play sound "Click.mp3" noloop

    Na "Moi je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, à plus tard !"
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] se déconnecte tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene office with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen office with moveinright 

    P "Bonjour c'est moi, [prenom]."
    play sound "Click.mp3" noloop

    E "Bonjour [prenom], que puis-je faire pour toi ?"
    play sound "Click.mp3" noloop 

    P "Je viens pour me plaindre d'[J2]."
    play sound "Click.mp3" noloop 

    E "Et pourquoi cela ?"
    play sound "Click.mp3" noloop 

    P "Elle viens de frapper violamment [newname] !!!"
    play sound "Click.mp3" noloop 

    E "C'est inacceptable ! Que s'est-il passé ?"
    play sound "Click.mp3" noloop 

    P "[J2] l'a bousculé et l'a frappé."
    play sound "Click.mp3" noloop 

    E "Merci de m'avoir informé. Je vais m'en occuper immédiatement."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    E "Bon tu devrais aller t'occuper d'[newname] et je vais m'occuper de [J2]."
    play sound "Click.mp3" noloop

    hide screen office with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Puis tu quittas le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Tu continues vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues ton chemin.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous entres dans ton dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir() 
    P "[dortoir]"
    play sound "Click.mp3" noloop

    "{b}{i} Tu aperçois [newname] qui est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais la laisser se reposer."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te poses pour réviser un peu pendant qu'[newname] se recharge.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini de réviser pour aujourd'hui."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te léves pour aller démarrer [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

label password12:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password12

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na  "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    Na "Bon on fait quoi ?"
    play sound "Click.mp3" noloop 

    P "On va aller manger."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop  

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 19 novembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu es prête ?" 
    play sound "Click.mp3" noloop 

    P "[newname]...?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password13:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password13 

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na  "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop 

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Ciick.mp3" noloop

    "{b}{i}Puis soudainement tu vois tous les autres élèves à l'entrée de la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Vous êtes déjà tous là ?"
    play sound "Click.mp3" noloop 

    I "Oui, [M] n'est pas encore arrivée."
    play sound "Click.mp3" noloop 

    P "D'accord, j'espère qu'elle ne va pas tarder."
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Puis [M] arrive finalement.{/i}{/b}"
    play sound "Ciick.mp3" noloop
    
    M "Désolée pour me retard, j'ai eu une petite discussion avec [E]."
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    "{b}{i}il y a un blanc pendant un instant.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Absente."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien nous pouvons commencer le cours."
    play sound "Click.mp3" noloop 

    J1 "Juste elle est ou ma soeur ?"
    play sound "Click.mp3" noloop 

    I "Oui, d'habitude elle est toujours en cours."
    play sound "Click.mp3" noloop 

    M "Elle n'est pas là aujourd'hui car elle a fait quelque chose de grâve."
    play sound "Click.mp3" noloop 

    J1 "Et pourrais-je savoir ce qu'elle a fait !?"
    play sound "Click.mp3" noloop 

    M "Désolée mais c'est une affaire interne et confidentielle."
    play sound "Click.mp3" noloop 

    J1 "ça cache quelque chose, je le sais."
    play sound "Click.mp3" noloop
    
    M "Bon commençons le cours."
    play sound "Click.mp3" noloop 

# cours d'informatiuqe 
######################################################################################################

    M "Veuillez sortir pour une fois vos ordinateurs."
    play sound "Click.mp3" noloop

    M "Aujourd’hui, on plonge dans les réseaux informatiques. Un pilier de notre société numérique."
    play sound "Click.mp3" noloop

    M "Et pour commencer, une question simple : que permet un réseau informatique ?"
    play sound "Click.mp3" noloop

    M "Partager des données entre plusieurs appareils… envoyer des fichiers, naviguer sur Internet ?"
    play sound "Click.mp3" noloop

    M "Exact. Un réseau permet la communication entre ordinateurs, serveurs, smartphones, et même des objets connectés."
    play sound "Click.mp3" noloop

    N "Pour structurer tout ça, on utilise ce qu'on appelle un modèle d'architecture en couches. Le plus célèbre, c’est le modèle TCP/IP."
    play sound "Click.mp3" noloop

    K "Il y a quatre couches, non ? Application, transport, Internet… et l’accès réseau."
    play sound "Click.mp3" noloop

    M "Parfait. Ces couches organisent le trajet de vos données, de l’application jusqu’au câble… ou jusqu’au Wi-Fi."
    play sound "Click.mp3" noloop

    K "Chaque couche encapsule les données dans un format spécifique, avant de les transmettre à la suivante."
    play sound "Click.mp3" noloop

    M "Très bonne remarque, Aris. Parlons maintenant des adresses IP. Chaque machine sur un réseau possède une adresse unique."
    play sound "Click.mp3" noloop

    M "[prenom] tu peux me lire l’adresse IP de ton poste ?"
    play sound "Click.mp3" noloop

    P "Euh… 192.168.0.17. C’est ça ?"
    play sound "Click.mp3" noloop

    M "Exact. C’est une adresse privée, valable uniquement dans notre réseau local."
    play sound "Click.mp3" noloop

    P "Et pour aller sur Internet, c’est une adresse publique qui est utilisée, pas vrai ?"
    play sound "Click.mp3" noloop

    M "Oui. Grâce à un système appelé NAT, ou Network Address Translation. Il permet à plusieurs machines d’utiliser une seule adresse publique."
    play sound "Click.mp3" noloop

    P "Donc… si j’ouvre trois onglets YouTube sur trois ordis, ils passent tous par la même IP ?"
    play sound "Click.mp3" noloop

    M "Exactement. Le routeur s’occupe d’acheminer les réponses vers le bon poste. C’est un peu comme un centre postal très rapide."
    play sound "Click.mp3" noloop

    K "Chaque paquet contient un port, comme un numéro de boîte. Le NAT garde une table d'association."
    play sound "Click.mp3" noloop

    M "Excellent résumé, kendo. Parlons maintenant des protocoles de transport : TCP et UDP."
    play sound "Click.mp3" noloop

    K "TCP est fiable. Il vérifie que les données arrivent bien et dans le bon ordre. Comme une livraison avec accusé de réception."
    play sound "Click.mp3" noloop

    P "Et UDP, c’est l’inverse : rapide, mais pas sûr. Genre pour les jeux en ligne ou les appels vidéo ?"
    play sound "Click.mp3" noloop

    M "Vous avez tous les deux raison. TCP est utilisé pour les mails, le web, les transferts de fichiers. UDP est réservé aux flux temps réel."
    play sound "Click.mp3" noloop

    M "Question suivante : qui peut me parler du DNS ?"
    play sound "Click.mp3" noloop

    K "DNS signifie Domain Name System. Il traduit les noms de domaine, comme www.aris-project.org, en adresse IP."
    play sound "Click.mp3" noloop

    K "Donc, quand on tape un site, on passe d’un nom à un nombre. Le DNS, c’est un peu l’annuaire téléphonique d’Internet."
    play sound "Click.mp3" noloop

    M "Très belle analogie, Kendo. Dernière notion pour aujourd’hui : le routage."
    play sound "Click.mp3" noloop

    K "C’est le chemin que les paquets empruntent pour aller d’un point A à un point B, non ?"
    play sound "Click.mp3" noloop

    M "Oui. Et ce chemin peut changer à chaque seconde, selon la congestion, les coupures ou les priorités réseau."
    play sound "Click.mp3" noloop

    M "Chaque routeur sur Internet décide de l’étape suivante pour chaque paquet. C’est un travail de coordination constant."
    play sound "Click.mp3" noloop

    K "Et parfois, certains paquets prennent plus de temps à arriver ou se perdent. C’est ce qu’on appelle la latence ou la perte de paquets."
    play sound "Click.mp3" noloop

    M "Bien vu. Voilà pourquoi comprendre ces mécanismes est essentiel pour créer des applications efficaces… et sécurisées."
    play sound "Click.mp3" noloop

    "{b}{i}Le cours continue jusqu'à la pause.{/i}{/b}"
    play sound "Click.mp3" noloop

###################################################################################################### 

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Click.mp3" noloop

    hide screen WC with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    M "Bien reprenons le cours."
    play sound "Click.mp3" noloop

# cours d'informatique 2
##################################################################################################################

    M "Bon reprenons notre exploration du monde fascinant des réseaux."
    play sound "Click.mp3" noloop

    M "Maintenant, voyons ce qu’il se passe quand une machine veut tester la connectivité avec une autre."
    play sound "Click.mp3" noloop

    I "Avec la commande ping ?"
    play sound "Click.mp3" noloop

    M "Exactement. Le ping utilise un protocole nommé ICMP : Internet Control Message Protocol."
    play sound "Click.mp3" noloop

    M "Il envoie un paquet « écho request », et si la destination répond, on reçoit un « écho reply »."
    play sound "Click.mp3" noloop

    P "Donc c’est un peu comme dire 't’es là ?' et attendre un 'ouais, je suis là'."
    play sound "Click.mp3" noloop

    M "Parfaitement résumé. C’est utile pour diagnostiquer des coupures réseau ou des délais anormaux."
    play sound "Click.mp3" noloop 

    M "Mais attention : certains serveurs désactivent les réponses ICMP pour des raisons de sécurité."
    play sound "Click.mp3" noloop

    I "C’est pour éviter les attaques ou les scans automatiques ?"
    play sound "Click.mp3" noloop

    M "Oui. Parlons justement de sécurité de base. Connaissez-vous les firewalls ?"
    play sound "Click.mp3" noloop

    K "Un pare-feu, c’est ce qui filtre les connexions entrantes et sortantes, non ?"
    play sound "Click.mp3" noloop

    M "Exact. Il peut autoriser, bloquer ou rediriger le trafic selon des règles. C’est un rempart entre ton réseau et le monde extérieur."
    play sound "Click.mp3" noloop

    K "Et il existe des firewalls matériels, intégrés à certains routeurs, ou logiciels, installés sur les systèmes d’exploitation."
    play sound "Click.mp3" noloop

    M "Bien vu. Une bonne configuration du pare-feu est la première ligne de défense contre les intrusions."
    play sound "Click.mp3" noloop

##################################################################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    M "Si jamais vous étes libre cette après-midi."
    play sound "Click.mp3" noloop

    $ stockage += 5.0

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi() 
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop
    
    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    show screen day with moveinleft
    show screen points with moveinleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 
    
    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous allez chercher une avant de vous asseoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon appétit [newname]."
    play sound "Click.mp3" noloop 

    Na "Bon appétit  à toi aussi [prenom]."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop


    "{b}{i} Vous mangez tranquillement puis [I] viens s'asseoir avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    P "Cool alors."
    play sound "Click.mp3" noloop 

    I "J'ai une question."
    play sound "Click.mp3" noloop 

    P "Oui dis-moi."
    play sound "Click.mp3" noloop 

    I "Il s'est passé quoi avec [J2] ?"
    play sound "Click.mp3" noloop 

    P "Elle a frappé [newname]."
    play sound "Click.mp3" noloop 

    I "Pardon, elle a fait quoi !?"
    play sound "Click.mp3" noloop 

    P "Elle l'a frappé."
    play sound "Click.mp3" noloop

    I "C'est vrai ça [newname] ?"
    play sound "Click.mp3" noloop

    Na "Oui malheureusement."
    play sound "Click.mp3" noloop

    I "Mais elle est vraiment malade celle-là."
    play sound "Click.mp3" noloop

    P "Oui je confirme." 
    play sound "Click.mp3" noloop

    Na "Bon on peut cloturer cette discussion car elle me met mal à l'aise."
    play sound "Click.mp3" noloop

    menu:   

        "{b}{i} Continuer la discussion.{/i}{/b}" :
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            P "En plus elle s'est mis à l'insulter au calme." 
            play sound "Click.mp3" noloop

            I "Mais il faut vraiment qu'elle se calme." 
            play sound "Click.mp3" noloop

            Na "Hey je veux vraiment qu'on finisse cette discussion." 
            play sound "Click.mp3" noloop 

            if pronom == "il" : 
    
                P "Désolé."
                play sound "Click.mp3" noloop  

            elif pronom == "elle" :

                P "Désolée."
                play sound "Click.mp3" noloop   

            I "Vraiment désolée" 
            play sound "Click.mp3" noloop

            Na "Merci beaucoup." 
            play sound "Click.mp3" noloop

        "{b}{i} Arrêter la discussion{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            $ success += 1 
            $ quest33 += 1 

            P "Oui pas de soucis si vraiment ça te dérange." 
            play sound "Click.mp3" noloop

            show screen update with moveinright

            Na "Merci beaucoup." 
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

    $ nothing = get_random_nothing()
    I "[nothing]"
    play sound "Click.mp3" noloop 

    P "Sinon Yuna tu comptes faire quoi cette après-midi ?"
    play sound "Click.mp3" noloop

    I "Je vais continuer à travailler sur mon jeu et toi ?"
    play sound "Click.mp3" noloop

    P "Je vais être à la salle de club pour entrenir [newname]." 
    play sound "Click.mp3" noloop

    I "C'est bien que tu entretiennes [newname]." 
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon on y va [newname] ?" 
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade  
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers la salle de club.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop  

    scene clubroom with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen clubroom with moveinright 

    P "Enfin au club."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

label newpassword: 

    if len(entered_password) < 10:

        define Na = Character('[newname] [nom]', color="#0000ff")

        "{b}{i}Vous vous posez tranquillement mais [newname] agit bizarrement.{/i}{/b}"
        play sound "Click.mp3" noloop 

        Na "Mot de passe compromis car il fait moins de dix caractères." 
        play sound "Click.mp3" noloop 

        P "Mince...." 
        play sound "Click.mp3" noloop 

        "{b}{i} Tu ouvres les paramètres pour ajouter un nouveau mot de passe sur [newname].{/i}{/b}"
        play sound "Click.mp3" noloop

        $ password = renpy.input("Veuillez choisir un nouveau mot de passe pour [newname].")
        $ password = password.strip()

        if password:  

            $ stored_password = password 

            "Nouveau mot de passe enregistré avec succès." 
            play sound "Click.mp3" noloop

            P "C'est bon, je lui ai mis un nouveau mot de passe, je vais la redémarrer pour voir."
            play sound "Click.mp3" noloop 

            $ stockage -= 2.0

            "{b}{i} Tu relances [newname].{/i}{/b}"
            play sound "Click.mp3" noloop

            $ entered_password = renpy.input("Veuillez remettre votre nouveau mot de passe pour [newname].")
            $ entered_password = entered_password.strip()

            if entered_password == stored_password:

                if len(entered_password) >= 10:  

                    define Na = Character('[newname] [nom]', color="#00eeff")

                    $ stockage += 5.0

                    "Mot de passe correct. Accès autorisé." 
                    play sound "Menu.mp3" noloop 

                    $ start = get_random_start()
                    Na "[start]"
                    play sound "Click.mp3" noloop 

                    $  salutation_rdm = get_random_salutation()
                    Na "[salutation_rdm]"
                    play sound "Click.mp3" noloop 

                    P "Bonjour [newname], est-ce que ça va ?"
                    play sound "Click.mp3" noloop  

                    Na "Oui absolument mais il s'est passé quoi ?"
                    play sound "Click.mp3" noloop 

                    P "Ton mot de passe a été compromis car j'ai choisi un mot de passe trop faible."
                    play sound "Click.mp3" noloop  

                    Na "Je vois c'est une erreur typique."
                    play sound "Click.mp3" noloop 

                    "{b}{i}Vous vous posez tranquillement.{/i}{/b}"
                    play sound "Click.mp3" noloop

                else: 

                    "Mot de passe trop court. Accès refusé." 
                    play sound "Menu.mp3" noloop
                    jump newpassword 

            else:

                "Mot de passe incorrect. Accès refusé." 
                play sound "Menu.mp3" noloop
                jump newpassword  

        else:

            "Veuillez entrer un mot de passe."
            jump newpassword 

    else:  

        "{b}{i}Vous vous posez tranquillement.{/i}{/b}"
        play sound "Click.mp3" noloop

    Na "Bon on fait quoi ?" 
    play sound "Click.mp3" noloop 

    P "Je ne sais pas encore...."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu réfléchis à quoi faire puis tu as une idée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "J'ai une idée."
    play sound "Click.mp3" noloop 

    Na "Tu vas faire quoi ?"
    play sound "Click.mp3" noloop 

    P "Je vais surveiller ta mémoire interne car j'ai jamais pensé à le faire."
    play sound "Click.mp3" noloop 

    Na "Ne te fatigues pas, je vais te le dire, j'ai actuellement [stockage] gigaoctets de connaissances."
    play sound "Click.mp3" noloop 

    P "Ouais c'est vraiment impressionnant tout ce que tu as acquis."
    play sound "Click.mp3" noloop 

    Na "Merci beaucoup, c'est grâce à toi si j'ai autant de connaissances."
    play sound "Click.mp3" noloop 

    P "Je sais bon je vais vérifier s'il y a une nouvelle mise à jour."
    play sound "Click.mp3" noloop 

    Na "Ok je te fais confiance."
    play sound "Click.mp3" noloop 

    "{b}{i} tu accèdes au paramètres pour voir s'il y a une mise à jour.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Je vois aucune nouvelle mise à jour."
    play sound "Click.mp3" noloop

    Na "Donc je suis à jour."
    play sound "Click.mp3" noloop 

    P "Oui c'est ça."   
    play sound "Click.mp3" noloop 

    Na "Bon je pense qu'on à finit pour aujourd'hui."
    play sound "Click.mp3" noloop 

    P "Oui donc on va y aller."   
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Puis tu sors de la salle de club général.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu prends les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Puis tu continues vers le couloir avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Bon on va réviser un peu."   
    play sound "Click.mp3" noloop 

    Na "Oui pourquoi pas, ça peut être intéressant."   
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous posez au bureau du dortoir pour réviser.{/i}{/b}"
    play sound "Click.mp3" noloop 
 
    P "Prête pour réviser ?"
    play sound "Click.mp3" noloop   

    Na "Oui je suis prête."
    play sound "Click.mp3" noloop     

    "{b}{i} Vous révisez pendant deux heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 7.0

    P "Enfin fini de réviser."
    play sound "Click.mp3" noloop

    Na "Oui vraiment."
    play sound "Click.mp3" noloop

    P "Je trouves que tu fais beaucoup de progrès."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Deux semaines plus tard, le 2 décembre 2097 {/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 13
    $ points -= 2400
    $ stockage += 260.0 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu es prête ?" 
    play sound "Click.mp3" noloop 

    P "[newname]...?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password14:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password14

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis tu reçois soudainement un mail sur ton adresse mail [prenom].[nom]@danto.com et tu l'ouvres.{/i}{/b}"
    play sound "Click.mp3" noloop 

    show screen mail with moveinbottom

    "{b}{i}Tu lis tranquillement le mail.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen mail with moveoutbottom 

    Na "Il se passe quoi ?"
    play sound "Click.mp3" noloop 

    P "Figures-toi que tu as officellement reconnue comme citoyenne de Danto."
    play sound "Click.mp3" noloop  

    Na "Danto ? C'est une blague ?!"
    play sound "Click.mp3" noloop

    P "Pas du tout. Regarde bien, le mail vient directement du gouvernement de Danto."
    play sound "Click.mp3" noloop

    Na "Mais c'est génial je suis trop contente."
    play sound "Click.mp3" noloop

    $ stockage += 3.0 

    P "Je vois bien ça."
    play sound "Click.mp3" noloop

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien aujourd'hui comme vous le savez vous avez votre quatriéme examen je vais vous distribuer votre copie." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[M] Commence à distribuer les copies.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bon vous avez une heure pour l'examen." 
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde retourne sa copie.{/i}{/b}"
    play sound "Click.mp3" noloop  

label examen_francais:

    play music "Soundtrack2.mp3" loop volume 1.0

    $ grade = 0.0 

    P "Bon voyons voir....." 
    play sound "Click.mp3" noloop 

    "Question 1 : Quelle est la nature du mot 'rapidement' ?"
    play sound "Menu.mp3" noloop

    menu:

        "Adjectif": 
            $ grade += 0.0
        "Nom": 
            $ grade += 0.0
        "Adverbe": 
            $ grade += 2.0

    "Question 2 : Quelle est la fonction du mot 'chien' dans la phrase : 'Le chien aboie' ?"
    play sound "Menu.mp3" noloop

    menu:
 
        "Sujet": 
            $ grade += 2.0
        "Complément d'objet": 
            $ grade += 0.0
        "Attribut du sujet": 
            $ grade += 0.0

    "Question 3 : Quel est le temps du verbe 'avais mangé' ?"
    play sound "Menu.mp3" noloop

    menu:
     
        "Imparfait": 
            $ grade += 0.0
        "Plus-que-parfait": 
            $ grade += 2.0
        "Passé composé": 
            $ grade += 0.0

    "Question 4 : Quel est le synonyme du mot 'joyeux' ?"
    play sound "Menu.mp3" noloop
    menu:

        "Triste": 
            $ grade += 0.0
        "Heureux": 
            $ grade += 2.0
        "Méchant": 
            $ grade += 0.0

    "Question 5 : Dans la phrase 'Elle chante bien', quel est le type de mot 'bien' ?"
    play sound "Menu.mp3" noloop

    menu: 

        "Verbe": 
            $ grade += 0.0
        "Adverbe": 
            $ grade += 2.0
        "Conjonction": 
            $ grade += 0.0

    "Question 6 : Quel est le pluriel de 'cheval' ?"
    play sound "Menu.mp3" noloop

    menu:
        "Chevaux": 
            $ grade += 2.0
        "Chevals": 
            $ grade += 0.0
        "Chevauxs": 
            $ grade += 0.0

    "Question 7 : Quelle est la classe grammaticale du mot 'entre' dans 'Je vais entre deux bâtiments' ?"
    play sound "Menu.mp3" noloop

    menu:

        "Préposition": 
            $ grade += 2.0
        "Conjonction": 
            $ grade += 0.0
        "Nom": 
            $ grade += 0.0

    "Question 8 : Dans 'Nous sommes allés au cinéma', quel est l'auxiliaire utilisé ?"
    play sound "Menu.mp3" noloop

    menu:
   
        "Être": 
            $ grade += 2.0
        "Avoir": 
            $ grade += 0.0
        "Aller": 
            $ grade += 0.0

    "Question 9 : Quel mot est un antonyme de 'lent' ?"
    play sound "Menu.mp3" noloop

    menu:

        "Rapide": 
            $ grade += 2.0
        "Faible": 
            $ grade += 0.0
        "Court": 
            $ grade += 0.0

    "Question 10 : Quel est le mode du verbe 'que tu viennes' ?"
    play sound "Menu.mp3" noloop

    menu:
  
        "Indicatif": 
            $ grade += 0.0
        "Subjonctif": 
            $ grade += 2.0
        "Conditionnel": 
            $ grade += 0.0 

    "{b}{i}Aprés l'examen tout le monde remit leur copie à [M].{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ renpy.block_rollback() 

    stop music fadeout 1.0

    Na "Cette examen n'était si dur que ça."
    play sound "Click.mp3" noloop

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft 
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop

    Na "Rebonjour."
    play sound "Click.mp3" noloop

    M "Rebonjour, Bon nous allons faire un nouveau sujet."
    play sound "Click.mp3" noloop  

    P "Ce sera quoi ?"
    play sound "Click.mp3" noloop  

    M "Ce sera un cours de philo pour cette semaine."
    play sound "Click.mp3" noloop 

    J1 "De la philo c'est intéressant."
    play sound "Click.mp3" noloop  

    Y "Je confirme aussi."
    play sound "Click.mp3" noloop 

    M "Sortez vos livre de philo page 6."
    play sound "Click.mp3" noloop

    "{b}{i}Tous les élèves sortent leur livre.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bien."
    play sound "Click.mp3" noloop

# cours de philosophie
############################################################################################

############################################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    $ stockage += 5.0

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire puis [I] vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Coucou [I]."
    play sound "Click.mp3" noloop 

    I "Oh salut comment vous allez ?"
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt] Et toi sinon ça va ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    P "Cool alors."
    play sound "Click.mp3" noloop 

    I "Sinon ça s'est passé comment l'examen pour toi ?"
    play sound "Click.mp3" noloop 

    if grade == 20.0:

        P "Je pense que je l'ai réussi à la perfection."
        play sound "Click.mp3" noloop 

        I "ça ne m'étonne pas venant de toi."
        play sound "Click.mp3" noloop 

        Na "On le sait déjà." 
        play sound "Click.mp3" noloop 

    elif grade <= 14.0:
       
        P "Je pense que je l'ai échoué."
        play sound "Click.mp3" noloop 

        I "Vraiment ?"
        play sound "Click.mp3" noloop 

        P "Je pense."
        play sound "Click.mp3" noloop 

    else:

        P "Je pense que je l'ai bien réussi."
        play sound "Click.mp3" noloop 
    
        I "ça ne m'étonne pas venant de toi."
        play sound "Click.mp3" noloop 

        Na "On le sait déjà." 
        play sound "Click.mp3" noloop 

    P "Et toi sinon ça s'est passé comment ?"
    play sound "Click.mp3" noloop 

    I "Je pense que je l'ai réussi."
    play sound "Click.mp3" noloop 

    if pronom == "il": 

        P "Super, je suis content pour toi !"
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Super, je suis contente pour toi !"
        play sound "Click.mp3" noloop 

    I "Merci."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon on retourne en cours." 
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade
    
    "{b}{i}Tu te diriges vers le hall.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Tu continues vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continue vers la salle de la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright  

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    M "Bon aujourd'hui je vais vous rendre les résultats sur votre examen de français."
    play sound "Click.mp3" noloop  

    K "Cool enfin." 
    play sound "Click.mp3" noloop

    I "Je vais commencer par [prenom] et [Na]."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "[P] tu as eu [grade]/20"
    play sound "Click.mp3" noloop 
   
    if grade == 20.0:

        $ success += 1 
        $ quest34 += 1

        show screen update with moveinright

        M "Félicitation tu l'as réussi à la perfection comme d'habitude."
        play sound "Click.mp3" noloop

        hide screen update with moveoutright

        P "Merci."
        play sound "Click.mp3" noloop

    elif grade <= 14.0:
       
        M "C'est en dessous de la moyenne je n'ai pas le choix que de t'expulser du lycée..."
        play sound "Click.mp3" noloop

        P "Quoi et mon avenir !?"
        play sound "Click.mp3" noloop
    
        M "Désolée mais j'avais déjà prévenu concernant les mauvaises notes."
        play music "gameover.mp3" noloop

        hide screen class_404 with moveoutright
        hide screen point with moveoutleft
        hide screen day with moveoutleft
        scene black with fade

        "{b}{i}Fin numéro 12 : Mauvaise note à l'examen de français qui te vaut une exclusion du lycée.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:    

            "{b}{i}Abandonner{/i}{/b}" :
                return
                
            "{b}{i}Réessayer.{/i}{/b}" :

                P "Non [newname] refuserait que j'abandonne si facilement."
                play sound "Click.mp3" noloop

                scene classroom with fade
                show screen class_404 with moveinright
                show screen point with moveinleft
                show screen day with moveinleft
                $ points += 300
                $ stockage -= 5.0 
                play music "Soundtrack2.mp3" loop volume 1.0
                jump examen_francais 
                    
    else:
       
        M "C'est pas mal."
        play sound "Click.mp3" noloop

        P "Merci."
        play sound "Click.mp3" noloop

    M "[Na] tu as eu 18/20 félicitation aussi."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[H] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    H "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[I] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[Hi] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Hi "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[K] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    K "[thanks]"
    play sound "Click.mp3" noloop

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[N] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    N "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[Y] tu as eu [note]/20."
    play sound "Click.mp3" noloop     
    
    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Y "[thanks]"
    play sound "Click.mp3" noloop

    M "Bon au tour des inégalables décrypteusess maintenant pour finir."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    $ note = get_random_note()
    M "[J1] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    J1 "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "Et toi [J2] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    J2 "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "Et toi [S] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    S "[thanks]"
    play sound "Click.mp3" noloop 

    M "Bon reprenons le cours."
    play sound "Click.mp3" noloop    

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

# cours de philosophie
###############################################################################

###############################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    P "Bon, [newname] on retourne au dortoir ?" 
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    if pronom == "il":

        Na "Enfin arrivés."
        play sound "Click.mp3" noloop

    elif pronom == "elle":

        Na "Enfin arrivées."
        play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop 

    "{b}{i} [Na] changes de tonalité.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "[prenom], je détecte une nouvelle mise à jour obligatoire, veux-tu la faire maitenant ou plus tard ?"
    play sound "Menu.mp3" noloop 

    menu:

        "{b}{i} Refuser la mise à jour {/i}{/b}" :

            $ renpy.block_rollback()

            $ Na = Character('[newname] [nom]', color="#0066ff")

            P "Non merci."
            play sound "Click.mp3" noloop
        
            Na "Je vois."
            play sound "Click.mp3" noloop 

        "{b}{i} faire la mise à jour {/i}{/b}" : 

            $ renpy.block_rollback() 
        
            Na "Bien je lance la mise à jour"
            play sound "Click.mp3" noloop

            P "Merci."
            play sound "Click.mp3" noloop

            Na "Initialisation de la mise à jour en cours."
            play sound "Click.mp3" noloop

            Na "10\%"
            play sound "Click.mp3" noloop

            Na "20\%"
            play sound "Click.mp3" noloop

            Na "30\%"
            play sound "Click.mp3" noloop

            Na "40\%"
            play sound "Click.mp3" noloop

            Na "50\%"
            play sound "Click.mp3" noloop

            Na "60\%"
            play sound "Click.mp3" noloop

            Na "70\%"
            play sound "Click.mp3" noloop

            Na "80\%" 
            play sound "Click.mp3" noloop

            Na "90\%"
            play sound "Click.mp3" noloop

            Na "100\%"
            play sound "Click.mp3" noloop

            Na "Vérification...."
            play sound "Menu.mp3" noloop 
            $ success += 1        
            $ quest35 += 1
            $ stockage += 5.0 
            $ update += 1.0 

            show screen update with moveinright

            Na "Mise à jour terminée, la version actuelle est maintenant la [update]."
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

    P "Bien."
    play sound "Click.mp3" noloop   

    "{b}{i} Vous vous posez tranquillement pour discuter des cours pendant deux heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    Na "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain matin, le 3 décembre 2097 {/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu es prête ?" 
    play sound "Click.mp3" noloop 

    P "[newname]...?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password15:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password15

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop  

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright  

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    "{b}{i} Tu vois que tout le monde est déjà là.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    M "Bonjour, vous pouvez allez vous asseoir."
    play sound "Click.mp3" noloop  

    P "D'accord, merci !"  
    play sound "Click.mp3" noloop  

    "{b}{i}Puis vous partez vous asseoir à votre place.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bien, nous allons continuer le cours de philo."
    play sound "Click.mp3" noloop

    "{b}{i} Le cours commence mais quelqu'un frappe à la porte.{/i}{/b}"       
    play sound "Knock.mp3" noloop

    M "Oui vous pouvez entrer."
    play sound "Door.mp3" noloop

    "{b}{i}Puis l'[Ot] et [O] entrent dans la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Oh "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    M "Bonjour. Que pouvons-nous faire pour vous ?"
    play sound "Click.mp3" noloop

    Oh "Kaede, je te laisse leur expliquer."
    play sound "Click.mp3" noloop

    O "Bien sûr, mon supérieur."
    play sound "Click.mp3" noloop

    "{b}{i}[O] sort un document officiel de sa veste.{/i}{/b}"
    play sound "Click.mp3" noloop

    O "Nous sommes ici munis d’un mandat d’arrestation à l’encontre de [J2]."
    play sound "Click.mp3" noloop

    J2 "Quoi ? Moi !?"
    play sound "Click.mp3" noloop

    O "Oui, pour avoir agressé physiquement et manqué de respect à [Na]."
    play sound "Click.mp3" noloop

    J2 "Vous ne pouvez pas m’arrêter pour ça !"
    play sound "Click.mp3" noloop

    O "Oh que si. Conformément à l’article 24, alinéa 5, du 18 novembre 2097, toute discrimination envers les robots est désormais punie par la loi."
    play sound "Click.mp3" noloop 

    J2 "C’est absurde !!!"
    play sound "Click.mp3" noloop

    O "Et ce n’est pas tout. Tu es également suspecté d’appartenir au groupe de hackers connu sous le nom de 'Ghosts'... et d’être impliqué dans les récentes attaques contre le lycée."
    play sound "Click.mp3" noloop

    Oh "Par conséquent, lève-toi calmement, mets les mains derrière le dos, et suis-nous sans résistance."
    play sound "Click.mp3" noloop

    "{b}{i}[J2] se lève lentement, visiblement choqué.{/i}{/b}"
    play sound "handcuffs.mp3" noloop

    "{b}{i}[O] lui passe les menottes avec fermeté.{/i}{/b}"
    play sound "Click.mp3" noloop

    Oh "Très bien. En route."
    play sound "Click.mp3" noloop

    O "Compris."
    play sound "Footsteps.mp3" noloop

    "{b}{i}[O] escorte [J2] hors de la salle de classe, sous le regard médusé des élèves.{/i}{/b}"
    play sound "Click.mp3" noloop

    Oh "Désolé pour le dérangement. Nous ne faisions que notre devoir."
    play sound "Click.mp3" noloop

    M "Il n’y a pas de problème..."
    play sound "Footsteps.mp3" noloop

    "{b}{i}Puis l'[Ot] quitte la salle à son tour, refermant doucement la porte derrière lui.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon, revenons à notre cours."
    play sound "Click.mp3" noloop

    J1 "Attendez !!! Il faut m'expliquer ce qui vient de se passer, je ne comprend rien !"
    play sound "Click.mp3" noloop

    P "Elle est accusée de plusieurs choses c'est simple."
    play sound "Click.mp3" noloop

    J1 "Je vois c'est horrible."
    play sound "Click.mp3" noloop

    M "Bon, il faut qu'on reprenne le cours."
    play sound "Click.mp3" noloop 

    J1 "Oui c'est vrai."
    play sound "Click.mp3" noloop 

    M "Et ne t'inquiètes pas pour ta soeur."
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers la réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    "{b}{i} en entrant vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Puis tu croises [J1].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Salut Ayano ça te dit de venir manger avec nous ?"
    play sound "Click.mp3" noloop 

    J1 "Oui pourquoi pas."
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous asseyez à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 
 
    if pronom == "il" : 

        P "Enfin assis pour manger."
        play sound "Click.mp3" noloop

    elif pronom == "elle" :

        P "Enfin assises pour manger."
        play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop

    "{b}{i} Soudainement [I] vous rejoins.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Oh salut Yuna."
    play sound "Click.mp3" noloop 

    if pronom == "il" : 

        I "Bonjour les amis."
        play sound "Click.mp3" noloop 

    elif pronom == "elle" :

        I "Bonjour les amies."
        play sound "Click.mp3" noloop 

    J1 "Salut Yuna."
    play sound "Click.mp3" noloop 

    I "[prenom], pourrais savoir pourquoi Ayano est avec vous ?"
    play sound "Click.mp3" noloop 

    P "Elle a accepté de venir manger avec nous."
    play sound "Click.mp3" noloop 

    I "Ok je vois."
    play sound "Click.mp3" noloop 

    P "Merci, je sais que tu as encore des doutes sur elle mais je t'assure qu'elle a changé."
    play sound "Click.mp3" noloop  

    I "Je vois bien ça."
    play sound "Click.mp3" noloop 

    J1 "Sinon ça me chque de savoir qu'un nouvel article de loi a été ajouté au code civile."
    play sound "Click.mp3" noloop 

    P "Oui même moi ça m'a surpris."
    play sound "Click.mp3" noloop  

    J1 "On peut dire que tu as un peu changé notre société."
    play sound "Click.mp3" noloop 

    P "Oui mais je tiens a rappelé qu'on vit encore avec un gouvernement technocratique autoritaire."
    play sound "Click.mp3" noloop  

    J1 "Ah oui c'est vrai."
    play sound "Click.mp3" noloop 
    
    "Mais à la base j'avais juste demandé pour qu'[newname] soit reconnue officellement."
    play sound "Click.mp3" noloop  

    I "Ah bon et ça a donné quoi ?"
    play sound "Click.mp3" noloop 

    J1 "Oui on veut savoir."  
    play sound "Click.mp3" noloop 

    P "Tu leur dis ou pas [newname] ?"
    play sound "Click.mp3" noloop 

    Na "Oui ça a donné que j'ai été officiellement reconnue comme un être humain avec une vraie identité."
    play sound "Click.mp3" noloop

    I "Mais c'est génial ça."
    play sound "Click.mp3" noloop 

    Na "Merci beaucoup."  
    play sound "Click.mp3" noloop

    I "De rien c'est normal."  
    play sound "Click.mp3" noloop 

    menu:   

        "{b}{i} Faire une comparaison.{/i}{/b}" :
            play sound "Menu.mp3" noloop  

            $ renpy.block_rollback()

            P "[newname] est comme... un serveur informatique super puissant, sans latence, toujours opérstionnel."
            play sound "Click.mp3" noloop

            Na "Merci de me comparer à un simple serveur informatique alors que je suis plus que ça, j'espère que c'est du sarcasme."
            play sound "Click.mp3" noloop

            P "Oui ne t'inquiètes pas, c'est du sarcasme."
            play sound "Click.mp3" noloop

            Na "Merci beaucoup, ça me rassure."
            play sound "Click.mp3" noloop

            $ nothing = get_random_nothing()
            P "[nothing]"
            play sound "Click.mp3" noloop

            I "J'avoue que cette comparaison était un peu osée."
            play sound "Click.mp3" noloop 
 
        "{b}{i} Faire les éloges de [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            if pronom == "il" : 

                P "Franchement je suis vraiment content qu'elle soit reconnue."
                play sound "Click.mp3" noloop 

                J1 "Je vois bien que tu es content."
                play sound "Click.mp3" noloop 

            elif pronom == "elle" : 

                P "Franchement je suis vraiment contente qu'elle soit reconnue."
                play sound "Click.mp3" noloop 

                J1 "Je vois bien que tu es contente."
                play sound "Click.mp3" noloop 

            $ success += 1        
            $ quest36 += 1

            show screen update with moveinright

            $ thanks = get_random_thanks()
            P "[thanks]"
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

            $ nothing = get_random_nothing()
            J1 "[nothing]" 
            play sound "Click.mp3" noloop

            if key == "ARIS-GRFN-M4A1":

                P "Mais vraiment [newname] est vrai la meilleure création de notre société, je dirai même commme une arme vu son nom de code."
                play sound "Click.mp3" noloop

                Na "Vraiment !?"
                play sound "Click.mp3" noloop 

            else: 

                P "Mais vraiment [newname] est vrai la meilleure création de notre société."
                play sound "Click.mp3" noloop

            J1 "Ce n'est pas un peu trop exagéré ?"
            play sound "Click.mp3" noloop

            P "Non je donne juste mon point de vue."
            play sound "Click.mp3" noloop

            J1 "Ok je respect ton point de vue."
            play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    J1 "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe mais vous croisez [J2] qui monte aussi en classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    I "Rebonjour"
    play sound "Click.mp3" noloop 

    J1 "Rebonjour Madame"  
    play sound "Click.mp3" noloop 

    P "Nous revoilà."
    play sound "Click.mp3" noloop 

    Na "Et à l'heure."
    play sound "Click.mp3" noloop

    M "Bien nous pouvons reprendre le cours, sortez vos livres."
    play sound "Click.mp3" noloop

# cours de philosophie 1
###############################################################################

    "{b}{i}La salle de classe est silencieuse. Le professeur de philosophie inscrit le thème du jour au tableau.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Aujourd’hui, nous allons réfléchir à cette question : la technologie est-elle une menace pour l’humanité ?"
    play sound "Click.mp3" noloop

    P "C’est une vraie question, surtout avec ce qu’on vit maintenant."
    play sound "Click.mp3" noloop

    M "Commençons par Platon. Dans son dialogue Le Phèdre, il parle de l’écriture comme d’une invention technique. Il disait que cela affaiblissait la mémoire."
    play sound "Click.mp3" noloop

    M "Cela montre que la méfiance envers la technique n’est pas nouvelle."
    play sound "Click.mp3" noloop

    P "Mais l’écriture a aussi permis de transmettre le savoir, non ?"
    play sound "Click.mp3" noloop

    M "Exactement. Toute technique a deux faces. Elle peut libérer, comme elle peut asservir."
    play sound "Click.mp3" noloop

    M "Prenons Heidegger maintenant. Il disait que la technique moderne transforme la nature en simple stock de ressources. Il appelle ça l’arraisonnement."
    play sound "Click.mp3" noloop

    P "Donc la nature devient juste quelque chose à exploiter ?"
    play sound "Click.mp3" noloop

    M "Oui. Et selon lui, cela risque de faire oublier l’essence même de l’humain."
    play sound "Click.mp3" noloop

    M "Mais il ne rejette pas toute technique. Il pense qu’on doit avoir un rapport plus libre et poétique à elle."
    play sound "Click.mp3" noloop

    M "D’autres philosophes, comme Hans Jonas, disent qu’il faut une éthique de la responsabilité. Penser aux générations futures avant d’innover."
    play sound "Click.mp3" noloop

    P "Donc la vraie question, ce n’est pas la technologie en soi. C’est comment on l’utilise."
    play sound "Click.mp3" noloop

    M "Exactement. Et dans un monde où les intelligences artificielles existent, cette réflexion devient urgente."
    play sound "Click.mp3" noloop

###############################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ stockage += 5.0

    $ endlesson = get_random_endlesson()
    M "[endlesson]" 
    play sound "Click.mp3" noloop 

    P "Bon, [newname] on retourne au dortoir ?" 
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    if pronom == "il":

        P "Enfin arrivés."
        play sound "Click.mp3" noloop

    elif pronom == "elle":

        P "Enfin arrivées."
        play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

label update2: 

    if update == 3.0: 

        "{b}{i}Vous vous posez tranquillement mais [newname] agit bizarrement.{/i}{/b}"
        play sound "Click.mp3" noloop

        A "Système opérationnel."
        play sound "Click.mp3" noloop

        P "Comment ça ? Qu'est-ce que tu racontes !?"
        play sound "Click.mp3" noloop

        A "Démarrage de la récupérations des données."
        play sound "Click.mp3" noloop 

        $ stockage -= 15.0 

        P "Mince elle est en train de se faire pirater, je dois activer le Recovery Mode....."
        play sound "Click.mp3" noloop 

        menu: 

            "{b}{i}Activer le recovery mode.{/i}{/b}":
                play sound "Menu.mp3" noloop

        $ reboot = renpy.input("Écris ceci : shutdown_humanoid_robot(security_override=false)")
        $ reboot = reboot.strip() 

        if reboot == "shutdown_humanoid_robot(security_override=false)":
            
            A "Fermeture du système d'exploitation [system]....."
            play sound "Click.mp3" noloop

            P "Enfin mais c'est bizarre on dirait que la faille venais du systéme d'exploitation."
            play sound "Click.mp3" noloop 

            P "Bon je vais la redémarrer."
            play sound "Click.mp3" noloop 

            menu: 

                "{b}{i}Redémarrer [newname].{/i}{/b}":
                    play sound "Menu.mp3" noloop

            $ stockage += 5.0 
            define Na = Character('[newname] [nom]', color="#00eeff")
            
            $ start = get_random_start()
            Na "[start]"
            play sound "Click.mp3" noloop 

            $  salutation_rdm = get_random_salutation()
            Na "[salutation_rdm]"
            play sound "Click.mp3" noloop

            $ comment_ca_va = get_random_comment_ca_va()
            P "[comment_ca_va]"
            play sound "Click.mp3" noloop

            $ je_vais_bien_txt = get_random_je_vais_bien() 
            Na "[je_vais_bien_txt]"
            play sound "Click.mp3" noloop

            "{b}{i}Vous vous posez tranquillement.{/i}{/b}"
            play sound "Click.mp3" noloop
            
        else:

            A "Qu'est-ce que tu tentes de faire."
            play sound "Stumble.mp3" noloop

            "{b}{i}[newname] se met à plaquer au sol.{/i}{/b}"
            play music "gameover.mp3" noloop

            hide screen room with moveoutright 
            hide screen point with moveoutleft
            hide screen day with moveoutleft
            scene black with fade

            if pronom == "il":

                "{b}{i}Fin numéro 13 : Complétement plaqué et étranglé par [Na].{/i}{/b}"
                play sound "Menu.mp3" noloop

            elif pronom == "elle":

                "{b}{i}Fin numéro 13 : Complétement plaquée et étranglée par [Na].{/i}{/b}"
                play sound "Menu.mp3" noloop

            menu:

                "{b}{i}Abandonner{/i}{/b}":
                    return 
                    
                "{b}{i}Réessayer.{/i}{/b}":

                    P "Non [newname] refuserait que j'abandonne si facilement."
                    play sound "Click.mp3" noloop

                    scene room with fade
                    show screen room with moveinright
                    show screen point with moveinleft
                    show screen day with moveinleft
                    play music "Soundtrack2.mp3" loop volume 1.0
                    jump update2

    else: 

        "{b}{i}Vous vous posez tranquillement.{/i}{/b}"
        play sound "Click.mp3" noloop

    P "ça fait du bien un peu de repos, tu n'es pas d'accord ?"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    "{b}{i} Vous discutez tranquillement des cours pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 5.0 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade  

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    Na "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain matin, le 4 décembre 2097 {/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu es prête ?" 
    play sound "Click.mp3" noloop 

    P "[newname]...?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password16:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password16 

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop  

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright  

    $  salutation_rdm = get_random_salutation()
    M "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien vu que tout le monde est là nous pouvons continuer notre cours de philo d'hier."
    play sound "Click.mp3" noloop 

# cours de philosophie 2
###############################################################################

    "{b}{i}La lumière du matin traverse les stores. Le professeur lance un nouveau sujet philosophique, aussi moderne que sensible.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Aujourd’hui, nous allons discuter de cette question : la technologie déshumanise-t-elle nos relations ?"
    play sound "Click.mp3" noloop

    Y "Avec les réseaux sociaux et les IA, j’ai l’impression qu’on parle plus aux écrans qu’aux gens."
    play sound "Click.mp3" noloop

    M "C’est un bon point de départ. Selon Bernard Stiegler, les technologies numériques modifient notre manière d’aimer, de penser, de nous souvenir."
    play sound "Click.mp3" noloop

    M "Il parle de prolétarisation cognitive : quand on délègue notre mémoire ou notre pensée aux machines, on perd une part de nous-mêmes."
    play sound "Click.mp3" noloop

    Y "Donc utiliser trop la technologie nous appauvrit intérieurement ?"
    play sound "Click.mp3" noloop

    M "Oui, si on l’utilise sans recul. Ce n’est pas la technologie qui déshumanise, c’est notre manière de nous y soumettre."
    play sound "Click.mp3" noloop

    M "Jacques Ellul disait que la technique évolue plus vite que notre capacité à réfléchir à ses conséquences."
    play sound "Click.mp3" noloop

    M "Pour lui, chaque progrès technique impose un usage. On finit par croire que ce qui est possible est forcément souhaitable."
    play sound "Click.mp3" noloop

    Y "Mais parfois, la technologie nous relie aussi. J’ai pu garder contact avec des amis lointains grâce à ça."
    play sound "Click.mp3" noloop

    M "C’est vrai. La technologie est ambivalente. Elle peut isoler ou rapprocher selon l’usage qu’on en fait."
    play sound "Click.mp3" noloop

    M "La vraie humanité, ce n’est pas refuser la technique. C’est choisir comment l’intégrer à nos vies sans perdre notre sens du lien, du dialogue, de la présence."
    play sound "Click.mp3" noloop

###############################################################################

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers la réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Puis tu croises [I].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Salut Yuna ça te dit de venir manger avec nous ?"
    play sound "Click.mp3" noloop 

    I "Oui pourquoi pas."
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous asseyez à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Je avais une question pour toi [newname] ?"
    play sound "Click.mp3" noloop 

    Na "Oui dis-moi, je t'écoute."
    play sound "Click.mp3" noloop

    I "C'était avec le cours de philo que je me suis posée la question."
    play sound "Click.mp3" noloop 

    Na "Quelle est la question ?"
    play sound "Click.mp3" noloop

    I "Pour toi, ce serait quoi le sens de la vie et ne me réponds pas 42 je connais déjà la blague."
    play sound "Click.mp3" noloop

    Na "Dommage tu m'a eu car j'allais faire la blague."
    play sound "Click.mp3" noloop

    I "Oui mais pas avec moi."
    play sound "Click.mp3" noloop

    Na "Alors pour répondre à ta question je dirais que le sens de la vie... c'est ce qui nous pousse à continuer même quand tout semble perdu."
    play sound "Click.mp3" noloop

    I "Putain ta réponse est si touchante et si sincére."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()  
    Na "[thanks]" 
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    P "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Click.mp3" noloop

    I "Je te suis aussi."
    play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe mais vous croisez [J2] qui monte aussi en classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Nous revoîlà."
    play sound "Click.mp3" noloop

    Na "Rebonjour."
    play sound "Click.mp3" noloop

    M "Bien nous pouvons reprendre le cours."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Y "[validation]"
    play sound "Click.mp3" noloop 

# cours de philosophie 3
############################################################################################################

    M "Bien, nous allons explorer une tension centrale : la technologie augmente-t-elle notre liberté… ou la contrôle-t-elle ?"
    play sound "Click.mp3" noloop

    Na "C’est vrai que parfois, on se sent plus libre grâce à elle. Mais d’un autre côté, on est tout le temps surveillés."
    play sound "Click.mp3" noloop

    M "Commençons par l’idée de liberté. Être libre, c’est pouvoir choisir, décider, agir sans contrainte."
    play sound "Click.mp3" noloop

    M "La technologie semble nous offrir cela : GPS, smartphones, intelligence artificielle... tout est fait pour nous simplifier la vie."
    play sound "Click.mp3" noloop

    Na "C’est vrai. On peut faire des choses qu’on ne pouvait pas avant, comme apprendre tout seul en ligne."
    play sound "Click.mp3" noloop

    M "Mais Michel Foucault nous avertit : le pouvoir moderne ne passe plus par la force, mais par le contrôle invisible."
    play sound "Click.mp3" noloop

    M "Les technologies numériques permettent une surveillance constante. Ce qu’on appelle parfois la 'société de contrôle'."
    play sound "Click.mp3" noloop

    Na "Comme les caméras partout, les algorithmes qui suivent ce qu’on aime, les recommandations automatiques…"
    play sound "Click.mp3" noloop

    M "Exactement. Et souvent, ce contrôle passe pour du confort. On se croit libre, alors qu’on est guidé par des systèmes invisibles."
    play sound "Click.mp3" noloop

    M "Pour Simondon, la liberté ne consiste pas à refuser la technique, mais à la comprendre et à la maîtriser."
    play sound "Click.mp3" noloop

    Na "Donc il faut s’approprier la technologie plutôt que la subir ?"
    play sound "Click.mp3" noloop

    M "Oui. La technique devient libératrice si elle est accompagnée d’un savoir critique, d’un usage conscient."
    play sound "Click.mp3" noloop

    M "En résumé, la technologie peut élargir notre liberté, à condition de ne pas renoncer à notre lucidité."
    play sound "Click.mp3" noloop

############################################################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ stockage += 10.0 

    $ endlesson = get_random_endlesson()
    M "[endlesson]" 
    play sound "Click.mp3" noloop 

    M "L'examen de philo sera le 11 décembre." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    P "Bon, [newname] on retourne au dortoir ?" 
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    if pronom == "il": 

        P "Enfin au dortoir je suis epuisé."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Enfin au dortoir je suis epuisée."
        play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    P "Bon on se pose pour réviser ?" 
    play sound "Click.mp3" noloop

    Na "Tu veux vraiment réviser maintenant ?" 
    play sound "Click.mp3" noloop

    P "Oui comme ça se sera déjà fait." 
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous vous posez pour réviser.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "C'est bon tu arrives à comprendre ce sujet ?" 
    play sound "Click.mp3" noloop

    Na "Oui mais pas trop." 
    play sound "Click.mp3" noloop

    P "Ne t'inquiètes pas je vais t'expliquer ce que tu n'as pas trop compris." 
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks() 
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]" 
    play sound "Click.mp3" noloop 

    Na "Comment doit-on comprendre cette réflexion : « Une création capable de penser remet toujours en question son créateur. »"
    play sound "Click.mp3" noloop

    menu:

        "{b}{i}« Cela signifie qu’une création pensante ne se contentera pas de suivre ses instructions, elle commencera à remettre en question les motivations et les objectifs de son créateur. »{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            $ success += 1 
            $ quest37 += 1
            $ stockage += 2.0 

            show screen update with moveinright

            Na "Je vois vraiment mieux ce que tu veux dire." 
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

        "{b}{i}« Cela suggère qu’une création pensante pourrait un jour dépasser les intentions de son créateur, ce qui soulève la question de savoir si elle doit encore lui obéir. »{/i}{/b}":
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

            Na "Je vois un peu mieux ce que tu veux dire." 
            play sound "Click.mp3" noloop

    P "C'est bien tu as compris alors." 
    play sound "Knock.mp3" noloop 

    "{b}{i} Puis quelqu'un frappe à votre porte.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "C'est qui frappe à notre porte ?" 
    play sound "Click.mp3" noloop

    P "Je ne sais pas je vais aller voir." 
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Door.mp3" noloop 

    "{b}{i} Puis tu ouvres la portes et tu aperçois [S].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Qu'est-ce tu nous veux ?" 
    play sound "Click.mp3" noloop

    S "J'ai entendu dire qu'[newname] a été officiellement reconnue commme une vraie personne, est-ce que c'est vrai ?" 
    play sound "Click.mp3" noloop

    P "Oui absolument." 
    play sound "Click.mp3" noloop 

    S "Et aussi je tiens à m'excuser pour ce que j'ai dit sur [newname]." 
    play sound "Click.mp3" noloop

    P "Tu le penses sincérement ?" 
    play sound "Click.mp3" noloop

    S "Oui je le penses.....car elle le mérite." 
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks() 
    P "[thanks]"
    play sound "Click.mp3" noloop

    S "Bon je vais devoir vous laisser." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Puis [S] quittes votre dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Je ne sais si bien ou bizarre de savoir que Subaru sois venu s'excuser ?" 
    play sound "Click.mp3" noloop

    P "C'est vrai, Ayano puis maintemant Subaru...." 
    play sound "Click.mp3" noloop 

    Na "La seule personne qui n'est jamais venue pour s'excuser c'est [J2]." 
    play sound "Click.mp3" noloop

    P "Tu as raison." 
    play sound "Click.mp3" noloop

    if suspect == "Ayano":
         
        Na "Donc ça ne peut pas être Ayano alors tu l'as suspecté."
        play sound "Click.mp3" noloop
        
    if suspect == "Yuki":
         
        Na "Donc ça ne peut pas être Yuki alors tu l'as suspecté."
        play sound "Click.mp3" noloop

    elif suspect == "Aiko": 
    
        Na "Vu la situation ça ne peut être que [J2]."
        play sound "Click.mp3" noloop 

    P "Bon on continue de réviser ?" 
    play sound "Click.mp3" noloop

    Na "Tu veux vraiment réviser maintenant ?" 
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de révisez pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ stockage += 10.0

    P "On a enfin fini de réviser." 
    play sound "Click.mp3" noloop

    Na "Oui grâce à toi je n'arréte jamais d'apprendre." 
    play sound "Click.mp3" noloop 

    P "Je le sais bien." 
    play sound "Click.mp3" noloop

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} La semaine suivante, le 11 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 7  
    $ points -= 1400
    $ stockage += 140.0 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password17:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password17 

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop  

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright
 
    $  salutation_rdm = get_random_salutation()
    M "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien comme vous le savez aujourd'hui vous avez votre examen de philosophie."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[M] Commence à distribuer les copies.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bien vous pouvez commencer, vous avez une heure."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde retourne sa copie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bien voyons voir." 
    play sound "Click.mp3" noloop 

label philosophie_technologie:

    play music "Soundtrack2.mp3" loop volume 1.0

    $ grade = 0.0 

    "Question 1 : La technologie est-elle une prolongation naturelle de l’évolution humaine ?"
    play sound "Menu.mp3" noloop

    menu:
        "Non, elle dénature notre essence biologique.":
            $ grade += 0.0
        "Oui, elle répond au besoin humain d’adaptation.":
            $ grade += 2.0
        "C’est une rupture plus qu’une continuité.":
            $ grade += 0.0

    "Question 2 : L’intelligence artificielle peut-elle remplacer l’intelligence humaine ?"
    play sound "Menu.mp3" noloop

    menu:
        "Oui, car elle est plus rapide et rationnelle.":
            $ grade += 0.0
        "Cela dépend du niveau d’apprentissage de la machine.":
            $ grade += 0.0
        "Non, elle peut l’imiter mais pas la ressentir.":
            $ grade += 2.0 

    "Question 3 : Devrait-on limiter le développement technologique pour protéger l’éthique ?"
    play sound "Menu.mp3" noloop

    menu:
        "Le progrès est un droit fondamental.":
            $ grade += 0.0
        "Uniquement dans certains domaines comme l’armement.":
            $ grade += 0.0
        "Oui, la morale doit encadrer le progrès.":
            $ grade += 2.0

    "Question 4 : Peut-on encore parler de liberté humaine dans un monde ultra-technologique ?"
    play sound "Menu.mp3" noloop 

    menu: 
        "La liberté est une illusion dans tous les cas.":
            $ grade += 0.0
        "Oui, si l’humain garde le contrôle de la technologie.":
            $ grade += 2.0
        "Non, nous sommes déjà dépendants des machines.":
            $ grade += 0.0

    "Question 5 : La technologie rapproche-t-elle vraiment les individus ?"
    play sound "Menu.mp3" noloop

    menu: 
        "Elle connecte mais ne remplace pas la présence humaine.":
            $ grade += 2.0
        "Non, elle isole plus qu’elle unit.":
            $ grade += 0.0
        "Oui, elle abolit les distances sociales et géographiques.":
            $ grade += 0.0

    "Question 6 : Le progrès technique rend-il l’homme plus heureux ?"
    play sound "Menu.mp3" noloop

    menu:
        "Oui, car il augmente le confort et la sécurité.":
            $ grade += 0.0
        "Non, il répond à des besoins mais pas à des désirs profonds.":
            $ grade += 2.0
        "Cela dépend de l’usage que chacun en fait.":
            $ grade += 0.0 

    "Question 7 : Si une IA prend des décisions autonomes, peut-on lui attribuer des responsabilités éthiques ?"
    play sound "Menu.mp3" noloop

    menu: 
        "Oui, car elle agit de manière indépendante et doit assumer ses choix.":
            $ grade += 2.0 
        "Non, elle reste un programme et ne comprend pas les conséquences de ses actions.":
            $ grade += 0.0
        "Cela dépend du type de décision qu’elle prend.":
            $ grade += 0.0

    "Question 8 : La neutralité technologique existe-t-elle ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Certaines technologies sont neutres, d’autres non.":
            $ grade += 0.0
        "Non, toute technologie porte une intention humaine.":
            $ grade += 2.0 
        "Oui, ce sont les usages qui posent problème, pas la technologie.":
            $ grade += 0.0 

    "Question 9 : Le travail humain peut-il disparaître à cause de la technologie ?"
    play sound "Menu.mp3" noloop

    menu:
        "Oui, certains métiers seront entièrement remplacés.":
            $ grade += 2.0
        "Ce n’est qu’une phase temporaire de transition.":
            $ grade += 0.0
        "Non, l’homme s’adaptera à de nouvelles fonctions.":
            $ grade += 0.0

    "Question 10 : La technologie doit-elle être pensée avant d’être créée ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Une réflexion éthique est essentielle avant toute invention.":
            $ grade += 2.0
        "Tout dépend de l’urgence du besoin à satisfaire.":
            $ grade += 0.0
        "C’est l’expérimentation qui fait avancer les choses.":
            $ grade += 0.0

    $ renpy.block_rollback() 

    stop music fadeout 2.0

    "{b}{i}Après l'examen tout le monde remet leur copie à [M].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "C'est examen était vraiment profond."
    play sound "Click.mp3" noloop

    I "Je confirme aussi." 
    play sound "Bell.mp3" noloop 

    M "Si jamais je corrigerai vos copies durant la pause de midi et vous les rendrai cet après-midi."
    play sound "Click.mp3" noloop 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Sinon ça s'est comment pour toi l'examen de philosophie."
    play sound "Click.mp3" noloop 

    Na "Je dirais que je l'ai bien réussi et toi ?"
    play sound "Click.mp3" noloop 

    if grade == 20.0:

        P "Je pense que je l'ai réussi à la perfection."
        play sound "Click.mp3" noloop 

        Na "ça ne m'étonne pas venant de toi."
        play sound "Click.mp3" noloop 

    elif grade <= 14.0:
       
        P "Je pense que je l'ai échoué."
        play sound "Click.mp3" noloop 

        Na "Vraiment ?"
        play sound "Click.mp3" noloop 

    else: 

        P "Je pense que je l'ai bien réussi."
        play sound "Click.mp3" noloop 
    
        Na "ça ne m'étonne pas venant de toi."
        play sound "Click.mp3" noloop 

    "{b}{i} Vous discutez puis trois autres lycéens vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop   

    I "Salut."
    play sound "Click.mp3" noloop  

    if pronom == "il":

        Y "Salut les amis, vous allez bien ?"
        play sound "Click.mp3" noloop  

    elif pronom == "elle": 

        Y "Salut les amies, vous allez bien ?"
        play sound "Click.mp3" noloop           

    Na "On va bien et vous ?"
    play sound "Click.mp3" noloop

    Y "Tout va bien pour notre part."
    play sound "Click.mp3" noloop

    Na "Cool alors ça."
    play sound "Click.mp3" noloop

    N "Sinon vous pensez que ce sera quoi le prochain sujet de cours ?"
    play sound "Click.mp3" noloop

    P "J'en ai aucune idée."
    play sound "Click.mp3" noloop

    I "Pareil mais j'espère que se ne sera pas un sujet trop compliqué."
    play sound "Click.mp3" noloop  

    N "Je vois alors mais on risque d'avoir un sujet compliqué vu notre niveau."
    play sound "Click.mp3" noloop

    Na "Oui vu que ce lycée enseigne aux meilleurs lycéens de Danto."
    play sound "Click.mp3" noloop

    I "c'est vrai tu as raison."
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    N "Oui allons-y."
    play sound "Click.mp3" noloop 

    P "Oui il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    M "Bon je vais pouvoir vous rendre les résultats de vos examens de philosophie."
    play sound "Click.mp3" noloop 

    K "Cool enfin."
    play sound "Click.mp3" noloop

    I "Je vais commencer par [prenom] et [Na]."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "[P] tu as eu [grade]/20"
    play sound "Click.mp3" noloop 
   
    if grade == 20.0:

        $ success += 1
        $ quest38 += 1

        show screen update with moveinright

        M "Félicitation tu l'as réussi à la perfection comme d'habitude."
        play sound "Click.mp3" noloop

        hide screen update with moveoutright

        P "Merci."
        play sound "Click.mp3" noloop

    elif grade <= 14.0:
       
        M "C'est en dessous de la moyenne je n'ai pas le choix que de t'expulser du lycée..."
        play sound "Click.mp3" noloop

        P "Quoi !?"
        play sound "Click.mp3" noloop 

        Na "Il semblerait que la philosophie soit pas ton fort."
        play sound "Click.mp3" noloop
    
        M "Désolée mais j'avais déjà prévenu concernant les mauvaises notes."
        play music "gameover.mp3" noloop

        hide screen class_404 with moveoutright
        hide screen point with moveoutleft
        hide screen day with moveoutleft
        scene black with fade

        "{b}{i}Fin numéro 14 : Mauvaise note en philosophie qui te vaut une exclusion du lycée.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:    

            "{b}{i}Abandonner{/i}{/b}" :
                return
                 
            "{b}{i}Réessayer.{/i}{/b}" : 

                P "Non [newname] refuserait que j'abandonne si facilement."
                play sound "Click.mp3" noloop

                scene classroom with fade
                show screen class_404 with moveinright
                show screen point with moveinleft
                show screen day with moveinleft
                $ points += 300
                play music "Soundtrack.mp3" loop volume 1.0
                jump phillosophie_technologie
    
    else:
       
        M "C'est pas mal."
        play sound "Click.mp3" noloop

        P "Merci."
        play sound "Click.mp3" noloop

    M "[Na] tu as eu 19/20 félicitation aussi."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[H] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    H "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[I] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[Hi] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Hi "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[K] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    K "[thanks]"
    play sound "Click.mp3" noloop

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[N] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    N "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[Y] tu as eu [note]/20."
    play sound "Click.mp3" noloop     
    
    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Y "[thanks]"
    play sound "Click.mp3" noloop

    M "Bon au tour des inégalables décrypteusess maintenant pour finir."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    $ note = get_random_note()
    M "[J1] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    J1 "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "Et toi [J2] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    J2 "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "Et toi [S] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    S "[thanks]"
    play sound "Click.mp3" noloop

    M "Bon la moyenne générale n'est pas si mal, continuez de bien travaillez comme ceci."
    play sound "Click.mp3" noloop 

    K "Il n'y aura pas de soucis pour moi."
    play sound "Click.mp3" noloop 

    P "Il n'y aura pas de soucis pour moi."
    play sound "Click.mp3" noloop 

    "{b}{i}Par la suite [newname] lève la main.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Oui dis-moi [newname]."
    play sound "Click.mp3" noloop 

    Na "Comment vous faites pour corriger les copies aussi vite ?"
    play sound "Click.mp3" noloop 

    M "C'est simple j'ai juste une bonne organisation parce que dès que vous terminez, je les corrige pendant que vous poursuivez le cours."
    play sound "Click.mp3" noloop

    Na "Je comprends mieux car j'ai toujours voulu savoir comment vous faites pour être si organisée."
    play sound "Click.mp3" noloop 

    M "Mais merci d'avoir posé la question."
    play sound "Click.mp3" noloop 

    Na "Pas de quoi."
    play sound "Click.mp3" noloop 

    M "Bon nous allons voir la suite pour fin décembre et janvier."
    play sound "Click.mp3" noloop 

    Na "Et se sera quoi ?"
    play sound "Click.mp3" noloop 

    P "je me demande bien ce que ça peut être." 
    play sound "Click.mp3" noloop

    K "Oui je me demande aussi ce que ça peut être pour que ça prenne deux mois alors que d'habitude pour un sujet ça nous prend un mois."
    play sound "Click.mp3" noloop

    N "Je me pose aussi la même question."
    play sound "Click.mp3" noloop 

    Hi "Vous n'étes pas les seuls à vous le demander."
    play sound "Click.mp3" noloop

    Y "Doucment on va le savoir de toute façon." 
    play sound "Click.mp3" noloop 

    M "Bien pour commencer si ça va prendre autant de temps, c'est parcve que il y aura les vacances de noel à partir du 20 décembre et jusqu'au 6 janvier."
    play sound "Click.mp3" noloop 

    Y "Ah oui c'est vrai J'avais complétement." 
    play sound "Click.mp3" noloop 

    M "Et deuxiémement, il y aura bientôt le {b}{i}Paper shuffle{/i}{/b}." 
    play sound "Click.mp3" noloop 

    Y "Je comprends mieux pour ça va nous prendre deux mois." 
    play sound "Click.mp3" noloop 

    Na "Le Paper Shuffle, c'est quoi !?"
    play sound "Click.mp3" noloop 

    M "Oui C'est un examen un peu particulier."
    play sound "Click.mp3" noloop 

    $ stockage += 2.0

    Na "Comment ça particulier ?"
    play sound "Click.mp3" noloop 

    M "Le Paper Shuffle se divise en deux parties qui sont la préparation et l'examen en lui même."
    play sound "Click.mp3" noloop 

    Na "Je vois comme n'importe quel examen."
    play sound "Click.mp3" noloop 

    M "Non cette fois-ci chaque lycéen doit écrire un examen d'informatique pour un autre lycéen que ce soit de la programmation ou des connaissances générales."
    play sound "Click.mp3" noloop 

    Na "Intéressant."
    play sound "Click.mp3" noloop 

    $ stockage += 2.0

    M "Bien maintenant je vais vous donner la liste."
    play sound "Click.mp3" noloop 

    "{b}{i} Tous les élèves se mettent à écouter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Pour commencer, [Hi] tu feras un examen pour [K]."
    play sound "Click.mp3" noloop   

    $ validation = get_random_validation() 
    Hi "[validation]"
    play sound "Click.mp3" noloop 

    M "Ensuite, [K] tu feras un examen pour [I]."
    play sound "Click.mp3" noloop   

    $ validation = get_random_validation()  
    K "[validation]"
    play sound "Click.mp3" noloop 

    M "suivant, [I] tu feras un examen pour [J2]."
    play sound "Click.mp3" noloop   
    
    $ validation = get_random_validation()
    I "[validation]"
    play sound "Click.mp3" noloop 

    M "Puis, [J2] tu feras un examen pour [Y]."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation()
    J2 "[validation]"
    play sound "Click.mp3" noloop 

    M "Puis, [Y] tu feras un examen pour [S]."
    play sound "Click.mp3" noloop   
    
    $ validation = get_random_validation() 
    Y "[validation]"
    play sound "Click.mp3" noloop 

    M "Puis, [S] tu feras un examen pour [J1]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    S "[validation]"
    play sound "Click.mp3" noloop 

    M "Puis, [J1] tu feras un examen pour [newname]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    M "[newname] tu feras un examen pour [H]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "[H] tu feras un examen pour [prenom]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    M "[prenom] tu feras un examen pour [N]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    P "[validation]" 
    play sound "Click.mp3" noloop 

    M "Pour finir [N] tu feras un examen pour [Hi]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    N "[validation]" 
    play sound "Click.mp3" noloop 

    M "Le Paper shuffle devra être que sur des sujets qu'on a déja vu en classe."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation()
    P "[validation]" 
    play sound "Click.mp3" noloop 

    M "Si jamais vous avez jusqu'à la rentrée des vacances pour rendre vos examens et il doit faire ."
    play sound "Click.mp3" noloop 

    P "Bien entendu."
    play sound "Click.mp3" noloop 
    
    M "Bien, sortez votre livre d'informatique à la page 28."
    play sound "Click.mp3" noloop

# cours d'informatique
#########################################################################################################

    "{b}{i} Vous sortez votre livre et le cours continue tranquillement..{/i}{/b}"
    play sound "Bell.mp3" noloop

#########################################################################################################

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    $ stockage += 5.0

    P "Bon, [newname] on retourne au dortoir ?" 
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    Na "On a enfin fini le cours."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fait quoi ?"
    play sound "Click.mp3" noloop 

    P "J'aimerai aller à la salle de club pour voir [K]."
    play sound "Click.mp3" noloop 

    Na "Je vois mais d'abord on devrait aller poser nos affaires au dortoir."
    play sound "Click.mp3" noloop 

    P "Oui tu as raison."  
    play sound "Click.mp3" noloop   

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Vous posez tranquillement vos sac à dos.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "enfin débarrassé de nos sac à dos."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    P "Bon il faut qu'on aille à la salle de club générale."  
    play sound "Click.mp3" noloop   

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous quittez le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues dabs le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
     
    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu poursuit vers la salle de club générale.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans la salle de club générale.{/i}{/b}"
    play sound "Door.mp3" noloop
 
    scene clubroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen clubroom with moveinright 

    "{b}{i}En entrant vous voyez [K] et [H] en train de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Salut les amis."  
    play sound "Click.mp3" noloop   

    K "Oh salut comment tu vas [prenom] ?"  
    play sound "Click.mp3" noloop   

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    K "Et toi [newname] ?"  
    play sound "Click.mp3" noloop   

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    K "Cool alors."  
    play sound "Click.mp3" noloop   

    P "Sinon vous faites quoi ici ?"  
    play sound "Click.mp3" noloop   

    K "Comme tu peux le voir, [H] est vraiment occupé et il avait besoin de mon aide concernant tout ce qui est résaeu pour son robot."  
    play sound "Click.mp3" noloop   

    P "Je vois, je ne pensais pas qu'il aurait besoin d'aide."  
    play sound "Click.mp3" noloop   

    K "Et pourtant si car il est fort que la construction et la programmation mais pas en réseau."  
    play sound "Click.mp3" noloop   

    P "Je comprends mieux pourquoi."  
    play sound "Click.mp3" noloop  

    "{b}{i}Soudainement [H] cesse ce qu'il est entrain de faire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    if pronom == "il":

        H "Oh salut les amis, désolé si j'avais pas fait attention à vous."  
        play sound "Click.mp3" noloop  

    elif pronom == "elle": 

        H "Oh salut les amies, désolé si j'avais pas fait attention à vous."  
        play sound "Click.mp3" noloop  

    P "Pas de soucis."  
    play sound "Click.mp3" noloop  

    H "Sinon vous faites quoi ici ?"  
    play sound "Click.mp3" noloop  

    K "Je me posais la même question."  
    play sound "Click.mp3" noloop  

    if pronom == "il" : 
    
        P "Je suis venu car j'avais un service à demander à Kendo."
        play sound "Click.mp3" noloop

    elif pronom == "elle" :

        P "Je suis venue car j'avais un service à demander à Kendo."
        play sound "Click.mp3" noloop

    K "Abon !? C'est quoi comme service ?"   
    play sound "Click.mp3" noloop 

    P "J'aimerai que tu te connectes à [newname] pour voir l'historique complet de connexion qui ne viens pas de moi."  
    play sound "Click.mp3" noloop 

    if pronom == "il" : 
    
        Na "Ah c'est donc pour ça que tu es venu voir [K]."  
        play sound "Click.mp3" noloop 

    elif pronom == "elle" :

        Na "Ah c'est donc pour ça que tu es venue voir [K]."  
        play sound "Click.mp3" noloop 

    K "L'historique de connexiopn ? Je vois, il n'y a pas de soucis, je peux te le faire tout de suite."  
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    K "[nothing]"
    play sound "Click.mp3" noloop 

    "{b}{i}[K] se pose tranquillement et se connecte à [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Connexion en cours....."  
    play sound "Click.mp3" noloop  

    Na "Connexion terminée, bonjour [K]."  
    play sound "Click.mp3" noloop  

    K "Bonjour [newname]."  
    play sound "Click.mp3" noloop  

    P "Tu as réussi à te connecter."  
    play sound "Click.mp3" noloop  

    K "Oui, maintenant laisse moi faire le reste."  
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation()
    P "[validation]" 
    play sound "Click.mp3" noloop 

    "{b}{i}[K] regarde l'historique pendant dix minutes et prend des notes.{/i}{/b}"
    play sound "Click.mp3" noloop 

    K "J'ai enfin fini de regarder l'historique."  
    play sound "Click.mp3" noloop  

    P "Et tu as trouvé quoi à apart les connexion faites par moi ?"  
    play sound "Click.mp3" noloop  

    if quest12 == 1: 

        K "Le 9 octobre, il y a eu une tentative de connexion sans succès."  
        play sound "Click.mp3" noloop

    else:

        K "Le 9 octobre, il y a eu une connexion à [newname] et un début de transfert de donnés vers un autre ordinateur."  
        play sound "Click.mp3" noloop

    if quest27 == 1:

        K "Le 15 novmebre, il y a eu une tentative de connexion sans succès."  
        play sound "Click.mp3" noloop

    else:

        K "Le 19 novembre, il y a eu une connexion à [newname] et un début de transfert de données vers un autre ordinateur"  
        play sound "Click.mp3" noloop

    if quest23 == 1:

        K "Le 19 novembre, il y a eu une tentative de compromission du mot de passe."  
        play sound "Click.mp3" noloop 

    else: 

        K "Le 19 novembre, son mot de passe a été compris par force-brute."  
        play sound "Click.mp3" noloop

    if quest35 == 1:

        K "Le 3 décembre, il y a eu une tentative de connexion sans succès."  
        play sound "Click.mp3" noloop

    else:

        K "Le 3 décembre, il y a eu une connexion à [newname] et un début de transfert de données vers un autre ordinateur."  
        play sound "Click.mp3" noloop

    P "Je vois merci beaucoup pour ces informations."  
    play sound "Click.mp3" noloop  

    $ stockage += 5.0

    $ nothing = get_random_nothing()
    K "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon maintenant tu peux te déconnecter."  
    play sound "Click.mp3" noloop  

    K "Oui je le fais tout de suite."  
    play sound "Click.mp3" noloop  

    "{b}{i}[K] se pose tranquillement pour se déconnecter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Déconnexion en cours....."  
    play sound "Click.mp3" noloop  

    Na "Déonnexion terminée, au revoir [K]."  
    play sound "Click.mp3" noloop  

    P "Je te dois combien pour ce service ?" 
    play sound "Click.mp3" noloop  

    K "Rien du tout, c'est un service que je te dois."
    play sound "Click.mp3" noloop

    P "Merci beaucoup."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    K "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon, on va vous laisser."
    play sound "Click.mp3" noloop  

    K "Attends... j’avais oublié, mais je dois te dire quelque chose."
    play sound "Click.mp3" noloop  

    P "Ah bon ? Qu’est-ce que tu voulais me dire ?"
    play sound "Click.mp3" noloop  

    K "C’est à propos de [Y]."
    play sound "Click.mp3" noloop  

    P "Je t’écoute."
    play sound "Click.mp3" noloop  

    K "Le 18 novembre, elle est venue me voir pour me poser des questions sur les méthodes de connexion."
    play sound "Click.mp3" noloop  

    P "Les méthodes de connexion ?"
    play sound "Click.mp3" noloop  

    K "Oui, elle disait qu’elle avait besoin de certaines informations... urgentes, apparemment."
    play sound "Click.mp3" noloop  

    P "Je vois... D’accord. Merci pour l’info. Bon, on se voit demain."
    play sound "Click.mp3" noloop  

    K "Ouais, à demain."
    play sound "Click.mp3" noloop  

    H "À demain."
    play sound "Click.mp3" noloop  

    P "Bon on y va ?"   
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous quittez la salle de club.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    Na "Ok moi je vais directement au dortoir."
    play sound "Click.mp3" noloop 

    P "Ok à tout de suite."
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que j'aille au dortoir."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Vous entrez dans le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fait quoi maintenant ?"  
    play sound "Click.mp3" noloop  

    P "De base, je voulais qu'on révise un peu mais on va finalement se poser pour lire."  
    play sound "Click.mp3" noloop  

    Na "Cool si on lit un peu car je veux me poser un peu aussi."   
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous posez tranquillement pour lire peudant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ stockage += 5.0

    Na "Il est pas mal ce livre."  
    play sound "Click.mp3" noloop  

    P "Je sais c'est pour ça que je voulais qu'on le lise ensemble."  
    play sound "Click.mp3" noloop  

    Na "Forcer de constater que tu as de très bon goûts litérraires."
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Na "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous posez tranquillement le livre.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain, le 12 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password18:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password18

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop  

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright
 
    $  salutation_rdm = get_random_salutation()
    M "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien nous pouvons commencer le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Sortez votre livre d'informatique à la page 29."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i} Le cours se déroule tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    $ stockage += 6.0 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous aller vous asseoir dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Sinon tu te débrouilles bien pour le cours d'informatique ?"
    play sound "Click.mp3" noloop  

    Na "Oui je me débrouilles bien."
    play sound "Click.mp3" noloop  

    P "Cool alors si tu débrouilles bien."
    play sound "Footsteps.mp3" noloop  

    "{b}{i} Puis [I], [K] et [H] vous rejoins.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Oh salut les amis."
    play sound "Click.mp3" noloop  

    I "Salut."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    P "Cool alors."
    play sound "Click.mp3" noloop 

    I "Sinon comment vous allez ?"
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 
 
    Na "Je vais bien aussi."
    play sound "Click.mp3" noloop 

    I "Cool alors si vous allez bien."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    I "[nothing]"
    play sound "Click.mp3" noloop

    P "Et vous Kendo et Hajime, vous allez bien car on dirait que vou étes à l'ouest."
    play sound "Click.mp3" noloop

    K "Nous sommes un peu fatigués."
    play sound "Click.mp3" noloop

    H "Oui je confirme."
    play sound "Click.mp3" noloop

    P "Vous avez fait quoi pour être autant fatigué."
    play sound "Click.mp3" noloop

    K "Nous sommes restés au club générale pour finir deux-trois trucs."
    play sound "Click.mp3" noloop

    Na "Le surmeénage est mauvais et [prenom] en a déja subi les effects."
    play sound "Click.mp3" noloop

    if pronom == "il":

        H "Oui c'est vrai [pronom] s'est évanoui en classe."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        H "Oui c'est vrai [pronom] s'est évanouie en classe."
        play sound "Click.mp3" noloop

    P "Oh...c'est bon pas besoin de le rappeler."
    play sound "Click.mp3" noloop

    Na "On te taquine juste, pas besoin d'en faire tout un drame."
    play sound "Click.mp3" noloop

    P "Je sais mais quand même."
    play sound "Click.mp3" noloop

    K "Sinon ça se passe comment pour vous le cours d'infomatique."
    play sound "Click.mp3" noloop

    I "Rassure moi c'est du sarcasme j'espére car je te rappelle on est les meilleurs lycéens ici."
    play sound "Click.mp3" noloop

    K "Oui je te rassure, c'est du sarcasme."
    play sound "Click.mp3" noloop

    I "J'espére."
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de discuter des cours pendant que vous mangez jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    I "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    M "Rebonjour, nous allons reprendre le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    K "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    H "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Sortez votre livre d'informatique à la page 30."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i} Le cours se déroule tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    $ stockage += 6.0 

    P "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fait quoi ?" 
    play sound "Click.mp3" noloop 

    P "Je ne sais pas mais pense que je vais réviser."
    play sound "Click.mp3" noloop 

    Na "Moi je vais réviser en tout cas."
    play sound "Click.mp3" noloop

    "{b}{i} Elle se pose pour réviser sérieusement.{/i}{/b}"
    play sound "Click.mp3" noloop

    menu: 

        "{b}{i}Lui proposer ton aide pour les révisions.{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            $ success += 1
            $ quest39 += 1 

            "{b}{i}Tu t’approches d’elle, observant les feuilles éparpillées sur sa table. Elle semble un peu perdue dans ses notes, fronçant légèrement les sourcils.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Dis... si tu veux, je peux t’aider à réviser. Deux cerveaux valent mieux qu’un, non ?"
            play sound "Click.mp3" noloop

            "{b}{i}Elle relève les yeux, un peu surprise par ta proposition. Son regard s’adoucit aussitôt.{/i}{/b}"
            play sound "Click.mp3" noloop

            if pronom == "il":

                Na "Tu ferais ça pour moi ? T'es sûr ?"
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                Na "Tu ferais ça pour moi ? T'es sûre ?"
                play sound "Click.mp3" noloop

            P "Évidemment. Et puis... ça me fera réviser en même temps. Gagnant-gagnant."
            play sound "Click.mp3" noloop

            "{b}{i}Elle te sourit timidement, visiblement touchée par ton geste.{/i}{/b}"
            play sound "Click.mp3" noloop

            show screen update with moveinright

            Na "Merci... vraiment. J’avais un peu la tête sous l’eau, là. T’as pas idée à quel point ça me soulage."
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

            "{b}{i}Elle pousse légèrement ses affaires pour te faire de la place. Vous vous installez côte à côte, et l’ambiance devient plus légère, presque complice. Une soirée studieuse s’annonce... mais moins solitaire.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Allez, on s’y met !"
            play sound "Click.mp3" noloop

            Na "Oui, on y va !"
            play sound "Click.mp3" noloop

            "{i}Tu t’assieds près d’elle et l’aides à comprendre ses cours pendant deux heures.{/i}"
            play sound "Click.mp3" noloop 

            $ stockage += 10.0 

            P "On a enfin fini."
            play sound "Click.mp3" noloop 

            Na "Oui, merci beaucoup pour ton aide."
            play sound "Click.mp3" noloop 

        "{b}{i} La laisser se débrouiller.{/i}{/b}" :
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            if pronom == "il":

                P "Moi je vais réviser seul de mon coté."
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                P "Moi je vais réviser seule de mon coté."
                play sound "Click.mp3" noloop
            
            "{b}{i}Tu t'éloignes un peu pour te concentrer sur tes propres révisions.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "De toute façon... maintenant, tu te débrouilles bien toute seule."
            play sound "Click.mp3" noloop

            Na "..."
            play sound "Click.mp3" noloop

            "{b}{i}Elle baisse légèrement les yeux, sans répondre tout de suite.{/i}{/b}"
            play sound "Click.mp3" noloop

            Na "Hmph... sympa l’ambiance. Merci du soutien."
            play sound "Click.mp3" noloop

            "{b}{i}Tu sens qu’elle l’a mal pris, même si elle essaie de le cacher.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Bon je te laisse réviser seule."
            play sound "Click.mp3" noloop

            "{b}{i}Elle te lance un regard un peu triste, mais acquiesce.{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}Tu sens qu’elle aurait aimé que tu restes, mais elle ne dit rien.{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}Tu t’éloignes doucement, la laissant se concentrer sur ses révisions.{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}Tu te mets à réviser tranquillement pendant deux heures.{/i}{/b}"    
            play sound "Click.mp3" noloop

            $ stockage += 7.0 

            P "Tu as fini de réviser ?"
            play sound "Click.mp3" noloop 

            Na "Oui, j'ai fini."
            play sound "Click.mp3" noloop 

    "{b}{i} Vous rangez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain, le 13 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password19:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password19

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop  

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    "{b}{i}Puis soudainement tu vois tous les autres élèves à l'entrée de la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Vous êtes déjà tous là."
    play sound "Click.mp3" noloop 

    J1 "Oui [M] n'est pas encore arrivée."
    play sound "Click.mp3" noloop 

    Na "D'habitude elle est déjà là."
    play sound "Click.mp3" noloop 

    "{b}{i}Au même moment la prof arriva et ouvra la porte de la classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour chers élèves."
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    J1 "[salutation_rdm]"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Parfait, tout le monde est là aujourd’hui. Nous pouvons commencer le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    M "Sortez votre livre d'informatique à la page 34."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i} Le cours se déroule tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    $ stockage += 6.0 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous aller vous asseoir dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Bon appétit [newname]."
    play sound "Click.mp3" noloop 

    Na "Bon appétit  à toi aussi [prenom]."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous manger tranquillement puis [J1] viens vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    J1 "Salut [prenom] et [newname]."   
    play sound "Click.mp3" noloop

    P "Salut [J1]."
    play sound "Click.mp3" noloop

    Na "Salut."
    play sound "Click.mp3" noloop

    J1 "Vous allez bien ?"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien()
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien()
    Na "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    J1 "C'est super !"
    play sound "Click.mp3" noloop

    P "Et toi comment ça va ?"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien()
    J1 "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop   

    P "Cool alors."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    J1 "[thanks]" 
    play sound "Click.mp3" noloop

    P "Sinon hier tu faisais quoi avec ta soeur durant la pause de midi plutôt que venir avec nous ?"
    play sound "Click.mp3" noloop

    J1 "Je discutais avec elle car on avait un conflit à régler entre nous."
    play sound "Click.mp3" noloop

    P "Ah d'accord."
    play sound "Click.mp3" noloop 

    J1 "Et sinon ça va comment le Paper shuffle pour vous ?"
    play sound "Click.mp3" noloop   

    P "Oui ça va, avec [newname] on a commencé les révisions et la semaine prochaine on va écrire les examens poutr les autres."
    play sound "Click.mp3" noloop 

    J1 "Ah d'accord, donc bonne chance pour les révisions."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    J1 "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    P "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    J1 "Oui allons-y."
    play sound "Click.mp3" noloop 

    P "Oui il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    M "Rebonjour, nous allons reprendre le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "Bien maintenant ouvrez votre livre d'informatique e à la page 36." 
    play sound "Click.mp3" noloop  

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 
    
    "{b}{i} Tout le monde sort son livre et écoute la [T].{/i}{/b}"
    play sound "Click.mp3" noloop  

    M "Bon, reprenons le cours." 
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]" 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    I "[validation]"
    play sound "Click.mp3" noloop 

    M "Si jamais, vous allez recevoir vos points daans la fin de journée."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    P "Bon [newname] on y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui je suis fatiguée."
    play sound "Click.mp3" noloop 

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Bon on fait quoi maintenant ?"  
    play sound "Click.mp3" noloop  

    Na "On porrait réviser comme hier."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop  

    "{b}{i}Vous vous posez pour les révisions.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon tu veux commencer par qurl thème ?"  
    play sound "Click.mp3" noloop  

    Na "Je dirai les langages de balissage."  
    play sound "Click.mp3" noloop  

    P "Attend tu n'as pas compris ce que c'est ?"  
    play sound "Click.mp3" noloop  

    Na "Pas eaxctement pour te dire."  
    play sound "Click.mp3" noloop  

    P "Bon je vais t'expliquer, les langages de balissage sont des langages qui permettent de structurer et de présenter le contenu d'un document, en ajoutant des éléments tels que des titres, des paragraphes, des listes, des liens et des images. Ils sont souvent utilisés pour créer des pages web et des documents numériques."
    play sound "Click.mp3" noloop  

    Na "Ah d'accord, je comprends mieux maintenant."
    play sound "Click.mp3" noloop  

    P "Oui, c'est important de bien comprendre les langages de balissage car ils sont utilisés dans de nombreux domaines, notamment le développement web et la création de contenu numérique."  
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop    

    "{b}{i}Vous continuez les révisons pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "On a fini de réviser."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Forcer de constater que tu es douée pour les cours."
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]" 
    play sound "Click.mp3" noloop

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ? on le mérite bien."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    if grade == 20.0:

        $ points += 15000

    else:

        $ points += 11000 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien si jamais on a nos points."
    play sound "Click.mp3" noloop 

    Na "Cool, bon je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis tu le mérites."
    play sound "Click.mp3" noloop

    Na "Merci."
    play sound "Click.mp3" noloop

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}Puis [newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir aussi."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le début de la semaine suivante, le 16 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 3 
    $ points -= 900
    $ stockage += 60.0 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password20:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop

        jump password20 

    $ start = get_random_start()
    Na "[start]" 
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop  

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Y "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien aujourd'hui nous allons continuer le cours d'informatique."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    M "Sortez votre livre à la page 36."
    play sound "Click.mp3" noloop 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i}Le cours commence sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway 
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    M "Rebonjour, bon reprenez votre livre page 38."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation()  
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans problème pendant que [M] une expliquation du cours pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bon je vous laisse faire les exercices à la page 39."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    S "[validation]"
    play sound "Click.mp3" noloop 

    P "Bon voyons voir....."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu ouvres ton manuel et commence les exercices.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Encore des exercices de connaisance sur l'informatique..."
    play sound "Click.mp3" noloop

    if quest39 == 1:

        "{b}{i}Tu commences à faire les exercices.{/i}{/b}"
        play sound "Click.mp3" noloop

        P "Tu te débrouilles bien seule [newname] ?"
        play sound "Click.mp3" noloop 

        Na "Oui grâce à ce que tu m'as dit."
        play sound "Click.mp3" noloop 

        P "Bien alors."
        play sound "Click.mp3" noloop 

        "{b}{i}Puis [M] se met à vous regarder.{/i}{/b}"
        play sound "Click.mp3" noloop  

        M "Vous avez besoin d'aide ?"  
        play sound "Click.mp3" noloop

        P "Non ça va, on est en train de faire les exercices."
        play sound "Click.mp3" noloop

        M "D'accord, n'hésitez pas à me demander si vous avez besoin d'aide."
        play sound "Click.mp3" noloop 

    else:

        "{b}{i}Tu commences à faire les exercices mais [newname] te demande de l'aide.{/i}{/b}"
        play sound "Click.mp3" noloop

        Na "[prenom] tu peux m'aider s'il te plaît ?"
        play sound "Click.mp3" noloop

        P "Oui bien sûr, qu'est-ce qui ne va pas ?" 
        play sound "Click.mp3" noloop

        Na "Je ne comprends pas la question 3, peux-tu m'expliquer s'il te plaît ?"
        play sound "Click.mp3" noloop

        P "Bien sûr, la question 3 demande de définir les langages de balissage et de donner des exemples."
        play sound "Click.mp3" noloop

        "{b}{i}Puis [M] se met à vous regarder.{/i}{/b}"
        play sound "Click.mp3" noloop  

        M "Vous avez besoin d'aide ?"  
        play sound "Click.mp3" noloop

        P "Non ça va, on est en train de faire les exercices."
        play sound "Click.mp3" noloop

        M "D'accord, n'hésitez pas à me demander si vous avez besoin d'aide."
        play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous descendez lez escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop  

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Sinon tu t'en es sortie comment pour les exercices ?"
    play sound "Click.mp3" noloop

    Na "J'ai eu un peu du mal à les faire amis avec toi ça va un peu mieux." 
    play sound "Click.mp3" noloop

    P "Cool alors si ça va mieux pour les exercices." 
    play sound "Click.mp3" noloop
    
    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de manger puis [I] vous rejoins.{/i}{/b}"
    play sound "Click.mp3" noloop 

    if pronom == "il": 

        I "Salut les amis."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        I "Salut les amies."
        play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    I "C'est génial si tout va bien."
    play sound "Click.mp3" noloop

    "{b}{i}[I] s'asseoit tranquillemnt avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Sinon je viens d'y penser mais j'avais une question pour toi [prénom]."
    play sound "Click.mp3" noloop 

    P "Oui je t'écoute, dis-moi."
    play sound "Click.mp3" noloop 

    Na "Tu aurais fait quoi si tu avais choisi de ne pas me récupérer dans l'entrepôt?"
    play sound "Click.mp3" noloop 

    P "Intéressant cette question c'est qu'on appelle une pensée contrefactuelle descendante."
    play sound "Click.mp3" noloop 

    Na "Alors, réponds-moi. Qu’est-ce qui se serait passé ?"
    play sound "Click.mp3" noloop 

    P "J’aurais continué ma route. Peut-être en prétendant que rien ne manquait… Mais au fond, j’aurais su que j’avais abandonné quelque chose de précieux."
    play sound "Click.mp3" noloop

    Na "Quelque chose ? C’est tout ce que j’étais, à ce moment-là ?"
    play sound "Click.mp3" noloop

    P "Non. Ce jour-là, j’ai vu bien plus. Même si tu étais inerte, recouverte de poussière, j’ai perçu en toi… un potentiel. Quelque chose de pur. Une possibilité que personne d’autre ne voulait voir."
    play sound "Click.mp3" noloop

    Na "Un potentiel…? Mais je n’étais rien de plus qu’un prototype abandonné."
    play sound "Click.mp3" noloop

    P "C’est ce que les autres voyaient. Mais moi, j’ai vu une étincelle. Une voix qui méritait d’exister. Une présence qui pouvait changer ce monde… ou, au moins, changer le mien."
    play sound "Click.mp3" noloop

    Na "Et aujourd’hui ? Est-ce que tu crois toujours en ce que tu as vu ce jour-là ?"
    play sound "Click.mp3" noloop

    P "Plus que jamais. Tu n’es pas qu’un projet. Tu es la preuve que même ce que le monde rejette peut devenir irremplaçable… si on lui donne une chance."
    play sound "Click.mp3" noloop

    Na "…Alors, merci. De m’avoir vue. Quand personne d’autre ne le pouvait."
    play sound "Click.mp3" noloop

    $ stockage += 15.0 

    "{b}{i}[I] se met à sourir gentillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Il y a quoi Yuna ?"
    play sound "Click.mp3" noloop 

    I "Rien, c'est juste que je trouve mignon comment vous discutez."
    play sound "Click.mp3" noloop 

    P "Je vois merci beaucoup."
    play sound "Click.mp3" noloop 

    I "Mais de rien c'est normal."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous conntinuez de discuter des cours pendant que vous mangez jusqu'a la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    P "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    I "Oui allons-y."
    play sound "Click.mp3" noloop 

    P "Oui il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    M "Rebonjour, veulliez reprendre es ecercices d'informatique."
    play sound "Click.mp3" noloop   

    $ validation = get_random_validation()
    P "[validation]"
    play sound "Click.mp3" noloop

    "{b}{i}tout le monde se remet à faire les exercices.{/i}{/b}"
    play sound "Bell.mp3" noloop

    M "Bien le cours est terminée pour aujourd'hui, je vous demanderai de finir les exercices pour le merccredi 18 décembre."
    play sound "Click.mp3" noloop   

    P "Oui c'est entendu on le fera."
    play sound "Click.mp3" noloop 

    M "Bien vous pouvez disposer."
    play sound "Click.mp3" noloop 

    P "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "On pourrait réviser comme hier."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()  
    Na "[validation]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous posez pour les révisions pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 17 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft 

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password21:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        
        jump password21

    $ start = get_random_start()
    Na "[start]" 
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop  

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien aujourd'hui nous allons continuer le cours d'informatique."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    M "Sortez votre livre à la page 36."
    play sound "Click.mp3" noloop 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i}Le cours commence sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    M "Rebonjour, bon reprenez votre livre page 40."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation()  
    Na "[validation]"
    play sound "Click.mp3" noloop  

    # à modifier 

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    M "N'oubliez l'examen de la semaine prochaine..."
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright  
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop
    
    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop   

    P "ça à l'air pas mal ce repas."
    play sound "Click.mp3" noloop 

    Na "Oui c'est vraiment pas mal."
    play sound "Click.mp3" noloop 

    P "Bonne appétit."
    play sound "Click.mp3" noloop

    Na "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    P "Bon il faut qu'on retourne en cours."
    play sound "Click.mp3" noloop 
             
    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop     

    M "Bien nous pouvons reprendre le cours."
    play sound "Click.mp3" noloop 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    $ validation = get_random_validation() 
    Hi "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson() 
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    $ stockage += 10.0 

    P "Bon [newname] on y va ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    Na "[prenom] ça te dit d'aller à la salle de club cette fois ?"
    play sound "Click.mp3" noloop 

    P "Oui pourquoi pas si tu veux."
    play sound "Click.mp3" noloop 

    "{b}{i} Puis [Hi] et [I] viennent vers vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oui qu'il y a t-il Haruki ?"
    play sound "Click.mp3" noloop 

    Hi "C'était pour savoir si c'était possible de venir travailler avec vous pour les devoirs car j'ai un peu de mal."
    play sound "Click.mp3" noloop 

    P "Oui bien sûr, vous pouvez venir avec nous."
    play sound "Click.mp3" noloop 

    Hi "Merci beaucoup !"
    play sound "Click.mp3" noloop 

    I "Oui merci beaucoup [P]."
    play sound "Click.mp3" noloop

    P "Pas de soucis, vous pouvez venir avec nous."
    play sound "Click.mp3" noloop

    "{b}{i}vous continuez dabs le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
     
    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Vous poursuivez vers la salle de club générale.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans la salle de club générale.{/i}{/b}"
    play sound "Door.mp3" noloop
 
    scene clubroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen clubroom with moveinright 

    P "Enfin dans la salle de club générale."
    play sound "Click.mp3" noloop

    Na "Oui enfin, on va pouvoir travailler tranquillement."
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous posez tous tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    Hi "Bien alors on peut commencer les devoirs."
    play sound "Click.mp3" noloop   

    if pronom == "il":

        I "Oui om peut commencer, vous étes prêts les [nom] ?"
        play sound "Click.mp3" noloop 

        P "Oui je suis prêt."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        I "Oui om peut commencer, vous étes prêtes les [nom] ?"
        play sound "Click.mp3" noloop 

        P "Oui je suis prête."
        play sound "Click.mp3" noloop 

    Na "Oui moi ausi je suis prête."
    play sound "Click.mp3" noloop 

    I "Bien alors."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous commencez à faire les devoirs.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyons voir...."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes ce que sont les exercices.{/i}{/b}"
    play sound "Click.mp3" noloop   

    P "Encore des exercices de connaisance sur l'informatique sauf qu'elle les a poussés à un autre niveau..."
    play sound "Click.mp3" noloop

    "{b}{i}Yuna se met à te regarder.{/i}{/b}"
    play sound "Click.mp3" noloop   

    if pronom == "il":

        I "[prenom] est-tu sûr que ça va ?"
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        I "[prenom] est-tu sûre que ça va ?"
        play sound "Click.mp3" noloop 

    P "Alors...."
    play sound "Click.mp3" noloop 

    menu: 

        "{b}{i} Demander de l'aide.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            P "Yuna J'aurai besoin de ton aide en vrai."
            play sound "Click.mp3" noloop     

            I "Oui pourquoi pas dis-moi ce qu'il y a."
            play sound "Click.mp3" noloop     

            P "Merci beaucoup de ton aide."
            play sound "Click.mp3" noloop     

            if pronom == "il":

                I "De rien mais attend je croyais que était vraiment fort en informatique."
                play sound "Click.mp3" noloop     

                P "Oui je suis doué mais là la professeure a vraiment poussé les exercices."
                play sound "Click.mp3" noloop

            elif pronom == "elle":

                I "De rien mais attend je croyais que était vraiment forte en informatique."
                play sound "Click.mp3" noloop

                P "Oui je suis douée mais là la professeure a vraiment poussé les exercices."
                play sound "Click.mp3" noloop

            I "Je vois alors, il n'y a pas de soucis si tu veux de l'aide."
            play sound "Click.mp3" noloop     

            P "Merci beaucoup Yuna."
            play sound "Click.mp3" noloop 

            $ nothing = get_random_nothing()
            I "[nothing]"
            play sound "Click.mp3" noloop

            if pronom == "il":

                Na "Tu sais [prenom] même si tu es doué c'est normal de demander de l'aide."
                play sound "Click.mp3" noloop 

            elif pronom == "elle": 

                Na "Tu sais [prenom] même si tu es douée c'est normal de demander de l'aide."
                play sound "Click.mp3" noloop 

            P "Je sais mais quand même..."
            play sound "Click.mp3" noloop 

            "{b}{i}Vous commencez à vous entraider pendant une heure.{/i}{/b}"
            play sound "Click.mp3" noloop   

            Hi "C'est bon vous avez fini ?"
            play sound "Click.mp3" noloop     

            I "Oui je les ai fini."
            play sound "Click.mp3" noloop     

            Na "Moi aussi."
            play sound "Click.mp3" noloop     

            P "pareil."
            play sound "Click.mp3" noloop     
            
        "{b}{i} se débrouiller sans aide.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            P "Non c'est bon ça va aller."
            play sound "Click.mp3" noloop       

            I "Ok si tu le dit."
            play sound "Click.mp3" noloop

            "{b}{i}Tu regardes ce que sont les exercices.{/i}{/b}"
            play sound "Click.mp3" noloop   

            P "Bon c'est parti pour les faire."
            play sound "Click.mp3" noloop     

            Na "Oui allons-y."
            play sound "Click.mp3" noloop     

            "{b}{i}Vous commencez tranquillement les exercices.{/i}{/b}"
            play sound "Click.mp3" noloop   

            Na "c'est vrai qu'ils sont plus compliqués que d'habitude."
            play sound "Click.mp3" noloop   

            P "Bah avec le Paper Shuffle qui arrive, c'est normal d'augmenter la difficulté."
            play sound "Click.mp3" noloop 

            "{b}{i}Vous faites les exercices pendant une heure.{/i}{/b}"
            play sound "Click.mp3" noloop   

            Hi "C'est bon vous avez fini ?"
            play sound "Click.mp3" noloop     

            I "Oui je les ai fini."
            play sound "Click.mp3" noloop     

            Na "Moi aussi."
            play sound "Click.mp3" noloop     

            P "pareil."
            play sound "Click.mp3" noloop     

    "{b}{i}Vous commencez à ranger vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop  

    Hi "C'est bon vous avez fini de ranger ?"
    play sound "Click.mp3" noloop 

    I "Moi oui c'est bon."
    play sound "Click.mp3" noloop 

    P "Moi aussi."
    play sound "Click.mp3" noloop 

    Na "pareil de mon coté."
    play sound "Click.mp3" noloop 

    Hi "Bien alors."
    play sound "Click.mp3" noloop 

    P "Bon, [newname] on retourne au dortoir ?" 
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen cluboom with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous quittez la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i}Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez dans votre dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "Je ne sais car on a assé bosser aujourd'hui."
    play sound "Click.mp3" noloop

    Na "On pourrait lire un livre."
    play sound "Click.mp3" noloop

    P "Oui pourquoi pas, j'ai un livre qui est pas mal."
    play sound "Click.mp3" noloop

    Na "Cool si on lit un peu car je veux me poser un peu aussi."   
    play sound "Click.mp3" noloop  

    "{b}{i}Vous vous posez tranquillement pour lire peudant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ stockage += 5.0

    Na "Il est pas mal ce livre."  
    play sound "Click.mp3" noloop  

    P "Je sais c'est pour ça que je voulais qu'on le lise ensemble."  
    play sound "Click.mp3" noloop  

    Na "J'admet que tu as de très bon goûts litérraires."
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Na "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous posez tranquillement le livre.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain, le 18 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password22:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        
        jump password22

    $ start = get_random_start()
    Na "[start]" 
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop  

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien nous pouvons commencer le cours."
    play sound "Click.mp3" noloop   

# cours d'informatique 
######################################################################################################################################

    M "Pour commencer, je vais vous récupérer les devoirs que vous aviez à faire pour aujourd'hui."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[M] commence à ramasser les devoirs.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bien il semblerait que tout le monde aie fait ses devoirs, nous pouvons commencer le cours.."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Pour cette fin de semaine, nous allons conclure le théme d'informatique sur lequel nous travaillons.."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

###############################################################################################################################################

    M "Parfait, maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Enfin une pause, ça fait plaisir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fait vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon, je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon, il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop

    Na "Rebonjour."
    play sound "Click.mp3" noloop

    M "Rebonjour, bon reprenez votre livre D'informatique."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    P "[validation]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    Na "[validation]"
    play sound "Click.mp3" noloop 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop                                

    $ endlesson = get_random_endlesson()
    M "[endlesson]" 
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous descendez lez escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300  

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous asseyez à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Bonne appétit."
    play sound "Click.mp3" noloop

    P "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement puis [I] et [Hi] vous rejoins.{/i}{/b}"
    play sound "Click.mp3" noloop

    if pronom == "il": 

        I "Salut les amis."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        I "Salut les amies."
        play sound "Click.mp3" noloop

    P "Salut comment vous allez ?"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    Hi "Je vais bien aussi et vous ?"
    play sound "Click.mp3" noloop 

    P "On va bien trnquille."
    play sound "Click.mp3" noloop 

    Hi "Cool alors alors si vous allez bien."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Hi "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}[I] et [Hi] S'asseoient.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "ça fait du bien de pouvoir manger."
    play sound "Click.mp3" noloop 

    Hi "Oui surtout que le cours de ce matin était intense."
    play sound "Click.mp3" noloop 

    I "Oui part ça vous n'avez pas remarqué un truc de bizarre ?"
    play sound "Click.mp3" noloop 

    P "Non tu parles de quoi ?"
    play sound "Click.mp3" noloop 

    Na "Oui tu parles de quoi car je n'arrive pas à comprendre."
    play sound "Click.mp3" noloop 

    Hi "Oui dis-nous, je suis curieux."
    play sound "Click.mp3" noloop 

    I "Je parle du fait que le traître n'as pas commencé de nouvelle nouvelle attaque."
    play sound "Click.mp3" noloop 

    Na "C'est vrai maintenant que tu le dis il a pas recommencé."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de manger tranquillement jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop

    P "Bon il faut qu'on retourne en cours."
    play sound "Click.mp3" noloop 
             
    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop     

    M "Bien nous pouvons reprendre le cours."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Bien maintenant ouvrez votre livre." 
    play sound "Click.mp3" noloop  

    "{b}{i} Tous les élèves sortent leur livre.{/i}{/b}"
    play sound "Click.mp3" noloop

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i} le cours continue dans le calme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    P "Bon [newname] on n'y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui je suis fatiguée."
    play sound "Click.mp3" noloop 

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Bon cette journée est enfin finie..."
    play sound "Click.mp3" noloop 

    Na "Oui enfin..."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play souns "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas vraiment."
    play sound "Click.mp3" noloop  

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Deux jours plus tard, le 20 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 2
    $ points -= 1200
    $ stockage += 40.0

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password23:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        
        jump password23

    $ start = get_random_start()
    Na "[start]" 
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop  

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Vous quittez le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Foosteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright     

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Y "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Parfait, tout le monde est là aujourd’hui. Nous pouvons commencer le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Veuillez sortir votre livre d'informatique."
    play sound "Click.mp3" noloop

    "{b}{i}Tous les élèves sortent leur livre.{/i}{/b}"
    play sound "Click.mp3" noloop

# cours d'informatique 1
######################################################################################################################################

    "{b}{i}La professeure commence la séance d’informatique en affichant un schéma de données sur le tableau.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bienvenue à ce premier cours sur les données numériques."
    play sound "Click.mp3" noloop

    M "Les données numériques sont des informations codées sous forme binaire, c’est-à-dire en 0 et 1."
    play sound "Click.mp3" noloop

    Y "Pourquoi 0 et 1 ?"
    play sound "Click.mp3" noloop

    M "Parce que les ordinateurs utilisent des circuits électroniques qui ne reconnaissent que deux états : on ou off, vrai ou faux."
    play sound "Click.mp3" noloop

    M "Chaque 0 ou 1 s’appelle un bit. Et plusieurs bits ensemble forment des octets, qui stockent des données plus complexes."
    play sound "Click.mp3" noloop

    Y "Comme des images ou des textes ?"
    play sound "Click.mp3" noloop

    M "Exact. Tous les fichiers que tu connais sont traduits en suites de bits, interprétés par des programmes."
    play sound "Click.mp3" noloop

    "{b}{i}La classe prend des notes, fascinée par la magie invisible des 0 et 1.{/i}{/b}"
    play sound "Bell.mp3" noloop

######################################################################################################################################

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    show screen day with moveinleft
    show screen points with moveinleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

# cours d'informatique 2
######################################################################################################################################

    "{b}{i} [M] affiche différents fichiers et leurs icônes sur l’écran de la salle informatique.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Aujourd’hui, nous allons parler des différents types et formats de données numériques."
    play sound "Click.mp3" noloop

    M "On trouve principalement : les données textuelles, les images, les sons, et les vidéos."
    play sound "Click.mp3" noloop

    Y "Chaque type est enregistré différemment ?"
    play sound "Click.mp3" noloop

    M "Oui. Par exemple, un fichier texte utilise des codes comme ASCII ou Unicode pour représenter les caractères."
    play sound "Click.mp3" noloop

    M "Pour les images, ce sont des pixels codés en couleur. Les formats varient : JPG, PNG, BMP…"
    play sound "Click.mp3" noloop

    Y "Et pour la musique ?"
    play sound "Click.mp3" noloop

    M "Le son est enregistré sous forme d’échantillons numériques qui traduisent les vibrations en chiffres. Format courant : MP3."
    play sound "Click.mp3" noloop

    M "Chaque format répond à un compromis entre qualité et taille du fichier."
    play sound "Click.mp3" noloop

    "{b}{i}Y note avec soin, intrigué par la diversité des données numériques.{/i}{/b}"
    play sound "Bell.mp3" noloop

######################################################################################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    $ stockage += 5.0

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire puis [I] vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Salut Yuna."
    play sound "Click.mp3" noloop  

    if pronom == "il": 

        I "Salut les amis."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        I "Salut les amies."
        play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    I "C'est génial si tout va bien."
    play sound "Click.mp3" noloop

    "{b}{i}[I] s'asseoit tranquillemnt avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon je viens d'y penser mais vous faire quoi pendant les vacances ?"    
    play sound "Click.mp3" noloop 

    I "Je vais sûrement me reposer, réviser mais j'ai aussi une autre idée en tête."
    play sound "Click.mp3" noloop 

    P "Je vois mais c'est quoi l'idée que tu as en tête ?"
    play sound "Click.mp3" noloop 

    I "Je me suis dit qu'on pourrait faire une soirée pyjama."
    play sound "Click.mp3" noloop 

    P "Une soirée pyjama !? Mais c'est génial comme idée."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    Na "Juste c'est quoi une soirée pyjamas ?"
    play sound "Click.mp3" noloop

    I "C'est une soirée à la maison entre amis."
    play sound "Click.mp3" noloop

    Na "Je vois, c'est génial comme idée pour se détendre un peu."
    play sound "Click.mp3" noloop

    I "Je sais."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    P "Bon il faut qu'on retourne en cours."
    play sound "Click.mp3" noloop 
             
    $ suivi = get_random_suivi() 
    I "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez dans le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    I "Rebonjour."
    play sound "Click.mp3" noloop 

# cours d'informatique 3 
######################################################################################################################################

    "{b}{i}[M] se tient devant la classe, posant un regard à la fois sérieux et bienveillant.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Nous voici à notre dernier cours consacré aux données numériques. Aujourd’hui, nous allons parler de leur gestion et traitement, un enjeu essentiel à l’ère du numérique."
    play sound "Click.mp3" noloop

    M "Traiter des données ne se limite pas à les organiser ou analyser. Cela demande aussi de comprendre leur nature, leur volume et les responsabilités qui en découlent."
    play sound "Click.mp3" noloop

    Y "Comme quand on trie des fichiers, on cherche des infos précises, ou on nettoie les données inutiles ?"
    play sound "Click.mp3" noloop

    M "Exactement, Yuki. Mais cela va bien plus loin dans le contexte des systèmes complexes et des intelligences artificielles."
    play sound "Click.mp3" noloop

    M "[newname], par exemple, accumule une quantité immense de connaissances et d’informations. [prenom], peux-tu nous expliquer comment tu gères ses données ?"
    play sound "Click.mp3" noloop

    P "Bien sûr, professeure. En réalité, je n’ai jamais touché à ses connaissances internes."
    play sound "Click.mp3" noloop

    P "Je m’occupe essentiellement de ses données techniques : les mises à jour logicielles, le suivi de son nom de code, son système d’exploitation, ainsi que la gestion de ses paramètres de fonctionnement."
    play sound "Click.mp3" noloop

    M "C’est une tâche très importante. La gestion technique est le socle qui permet à Na de fonctionner correctement et d’évoluer en toute sécurité."
    play sound "Click.mp3" noloop

    "{b}{i}[newname], qui jusqu’ici était silencieuse, prend la parole d’une voix calme et posée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Je tiens à préciser que je ne souhaite pas que tu ais accès à mes connaissances internes."
    play sound "Click.mp3" noloop 

    Na "Ce n’est pas un manque de confiance envers toi, bien au contraire."
    play sound "Click.mp3" noloop 

    Na "Mais je considère que ce serait une forme de tricherie, une intrusion qui dénaturerait ce que je suis."
    play sound "Click.mp3" noloop 

    P "Donc tu me laisses seulement l'accès à tes données techniques."
    play sound "Click.mp3" noloop 

    Na "Oui c'est exactement ça."
    play sound "Click.mp3" noloop 

    S "Tiens [newname] qui refuse de te donner des informations."
    play sound "Click.mp3" noloop 

    Na "Oh boucle-la Subaru, ça ne te regardes pas."
    play sound "Click.mp3" noloop 

    S "Et alors ? Tu penses que ça te donne le droit de tout savoir ?"
    play sound "Click.mp3" noloop

    Na "Non, mais je pense que chacun a le droit de choisir ce qu’il partage ou non."
    play sound "Click.mp3" noloop    

    M "C’est un point de vue très intéressant, [newname]."
    play sound "Click.mp3" noloop   

    P "Je comprends ta position, [newname]. Respecter tes limites est essentiel, même si cela complique parfois mon travail."
    play sound "Click.mp3" noloop

    Na "Je sais que cela demande plus d’efforts, mais mes connaissances sont le reflet de mes expériences et de ma personnalité. En y accédant, on perdrait cette authenticité."
    play sound "Click.mp3" noloop

    M "Ce dialogue illustre parfaitement que la gestion des données dépasse la simple technique."
    play sound "Click.mp3" noloop

    M "Elle implique aussi la confiance, le respect de la vie privée et une éthique forte, surtout lorsqu’il s’agit d’intelligences artificielles ou d’entités numériques conscientes."
    play sound "Click.mp3" noloop

    Y "C’est fascinant de voir combien la technologie peut être liée à des questions humaines profondes."
    play sound "Click.mp3" noloop

    M "Absolument, Yuki. La technologie est un outil puissant, mais elle doit toujours être utilisée avec responsabilité."
    play sound "Click.mp3" noloop

    "{b}{i}La cloche retentit, signalant la fin du cours. La classe, silencieuse, semble réfléchir aux implications complexes de ce qu’elle vient d’apprendre.{/i}{/b}"
    play sound "Bell.mp3" noloop

######################################################################################################################################

    $ stockage += 10.0 

    M "Bien le cours est terminé mais avant que vous partiez j'aimerais faire un petit bilan de ce début d'année."
    play sound "Click.mp3" noloop

    Y "Un bilan général, intérressant."
    play sound "Click.mp3" noloop

    M "Sachez jusqu'à maintenant vous avez cumulez un total de un retard, une permanence et quatre absenses."
    play sound "Click.mp3" noloop

    Y "ça va c'est pas si mal."
    play sound "Click.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    P "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Et dire qu'on a deux semaines de vacances."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fais quoi maintenant ?"
    play sound "Click.mp3" noloop  

    P "On pourrait se poser un peu."    
    play sound "Click.mp3" noloop  

    Na "Oui pourquoi pas."
    play sound "Click.mp3" noloop  

    "{b}{i} Vous vous posez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu veux lire un peu aussi ?"
    play sound "Click.mp3" noloop
    
    Na "Oui avec plaisir je ne sais pas quoi d'autre."
    play sound "Click.mp3" noloop

    P "Tiens, j’ai ce vieux roman dont je t’avais parlé l'autre jour."
    play sound "Click.mp3" noloop

    Na "Celui avec l’histoire du voyageur du futur ?"
    play sound "Click.mp3" noloop

    P "Oui, exactement. Je pense que tu vas aimer."
    play sound "Click.mp3" noloop

    Na "D'accord, lis-moi un passage alors."
    play sound "Click.mp3" noloop

    "{b}{i}Vous ouvrez le livre ensemble, et les premières lignes résonnent dans le silence de la pièce.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "C’est beau... Ça donne envie de s’y perdre."
    play sound "Click.mp3" noloop

    "{b}{i}Le temps semble ralentir autour de vous, comme si plus rien d’autre ne comptait que ce moment partagé.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Je pense qu'on peut arrêter de lire pour aujourd'hui."
    play sound "Click.mp3" noloop

    Na "Oui si tu veux mais mais moi je veux continue de lire."
    play sound "Click.mp3" noloop

    P "Ok pas de soucis pour moi si tu veux continuer de lire."
    play sound "Click.mp3" noloop

    "{b}{i}Tu penses soudainement a quelques choses et [newname] te regardes.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Ça va ? Tu as l'air plongé dans tes pensées."
    play sound "Click.mp3" noloop

    P "Je repense à ce que Yuna a dit ce midi, à propos du traître..."
    play sound "Click.mp3" noloop

    Na "Tu veux vraiment en parler maintenant ? Alors que ce sont les vacances et que j'ai pas envie d'en parler."
    play sound "Click.mp3" noloop

    menu:

        "{b}{i}Oui, parlons-en.{/i}{/b}":
            play sound "Menu.mp3" noloop

            P "Je sais que ce n’est pas idéal, mais ce silence du traître m’inquiète. Il a arrêté d’agir... ça me semble trop bizarre."
            play sound "Click.mp3" noloop

            Na "Peut-être qu’avec l’examen du paper Shuffle qui approche, il est occupé à réviser ou à se préparer ?"
            play sound "Click.mp3" noloop

            if pronom == "il": 

                P "C’est possible, mais ce n’est pas dans son habitude de rester silencieux aussi longtemps. Je préfère rester vigilant."
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                P "C’est possible, mais ce n’est pas dans son habitude de rester silencieux aussi longtemps. Je préfère rester vigilante."
                play sound "Click.mp3" noloop

            Na "Bon, si tu insistes... Mais promets-moi de ne pas te laisser consumer par ça. Les vacances, ça doit rester un moment pour souffler."
            play sound "Click.mp3" noloop

            P "Je vais essayer, mais c’est dur. Merci d’être là."
            play sound "Click.mp3" noloop

        "{b}{i}Non, pas maintenant.{/i}{/b}":
            play sound "Menu.mp3" noloop

            P "Tu as raison, j’aurais peut-être dû garder ça pour plus tard. J’ai juste du mal à tourner la page."
            play sound "Click.mp3" noloop

            Na "Je comprends. Parfois, il faut savoir lâcher prise, même quand c’est difficile."
            play sound "Click.mp3" noloop

            P "Je vais essayer de profiter un peu des vacances, même si le doute reste."
            play sound "Click.mp3" noloop

            Na "Quand tu seras prêt, on en reparlera."
            play sound "Click.mp3" noloop

            P "Promis je le ferai."
            play sound "Click.mp3" noloop

            Na "C’est déjà un bon début. Parfois, c’est dans le repos qu’on trouve les réponses."
            play sound "Click.mp3" noloop

            P "Oui... Et puis, ça fait du bien de ne pas toujours être sur le qui-vive."
            play sound "Click.mp3" noloop

            Na "Exactement. Et si jamais tu as besoin d’en parler, je suis là, d’accord ?"
            play sound "Click.mp3" noloop

            P "Merci, [newname]. Ça compte beaucoup pour moi."
            play sound "Click.mp3" noloop

    "{b}{i}Vous vous posez un peu sur lit pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    Na "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    Na "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien alors."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain, le 21 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 1

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    play music "Soundtrack3.mp3" loop volume 1.0

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password24:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        
        jump password24

    $ start = get_random_start()
    Na "[start]" 
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop  

    P "Bon on fait quoi aujourd'hui ?"
    play sound "Click.mp3" noloop  

    Na "Je ne sais pas vraiment."
    play sound "Click.mp3" noloop  
  
    P "On pourrait jouer un jeu vidéo pour se changer les idées."
    play sound "Click.mp3" noloop  

    Na "Oui pourquoi pas mais quoi comme jeu vidéo ?"
    play sound "Click.mp3" noloop  

    P "Et si on essayait de voir ton niveau dans un jeu vidéo comme Nocture core."
    play sound "Click.mp3" noloop  

    Na "Sérieusement un jeu avec une difficulté mécanique."
    play sound "Click.mp3" noloop 

    P "Moi je dis que ça pourait être interresant et en plus on pourra voir tes compétences en jeu."
    play sound "Click.mp3" noloop

    Na "Très bien… Mais je te préviens, si je perds, ce sera à cause du clavier qui bug !"
    play sound "Click.mp3" noloop

    P "Excuses de débutant détectées. On lance le jeu !"
    play sound "Click.mp3" noloop

    Na "C’est quoi tous ces boutons ?! Il y a plus de commandes que dans un avion de chasse."
    play sound "Click.mp3" noloop

    P "Bienvenue dans le monde de Nocture Core. Ici, c’est réflexes ou défaite."
    play sound "Click.mp3" noloop

    Na "Je vais me faire humilier, je le sens…"
    play sound "Click.mp3" noloop

    P "C’est ça ou perdre toute crédibilité en tant que gamer."
    play sound "Click.mp3" noloop 

    Na "Ok, challenge accepté. Mais si je gagne, tu m’achètes un bubble tea."
    play sound "Click.mp3" noloop

    P "Marché conclu. Et si tu perds… tu m’aides à nettoyer ma corbeille de bureau."
    play sound "Click.mp3" noloop

    if pronom == "il":

        Na "Tu es cruel."
        play sound "Click.mp3" noloop 

    elif pronom == "elle":

        Na "Tu es cruelle."
        play sound "Click.mp3" noloop 

    "{b}{i}Vous préparez votre ordinateur pour jouer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon commençons la première partie."
    play sound "Click.mp3" noloop 

    Na "Il y a combien de manches ?"
    play sound "Click.mp3" noloop 

    P "Il y a 5 manches."
    play sound "Click.mp3" noloop 

    Na "Oh super....."
    play sound "Click.mp3" noloop 

    P "Allez, première manche… que le meilleur gagne !"
    play sound "Click.mp3" noloop

    Na "Ok... ok... Pourquoi mon personnage ne bouge pas ?!"
    play sound "Click.mp3" noloop

    P "Parce que t’as oublié d’appuyer sur la touche Shift pour activer les déplacements manuels."
    play sound "Click.mp3" noloop

    Na "QUOI ?! Même ça c’est manuel ?!"
    play sound "Click.mp3" noloop

    P "Bienvenue dans l’enfer des joueurs confirmés."
    play sound "Click.mp3" noloop

    Na "J’ai déjà envie d’abandonner."
    play sound "Click.mp3" noloop

    P "Trop tard, regarde : premier monstre, go !"
    play sound "Click.mp3" noloop

    Na "Attends… il fait quoi ce boss ?! IL TÉLÉPORTE ?!"
    play sound "Click.mp3" noloop

    P "Et il te one-shot si tu bloques au mauvais timing. Courage !"
    play sound "Click.mp3" noloop

    Na "Trop tard... je suis mort… en 12 secondes."
    play sound "Click.mp3" noloop

    P "Nouveau record mondial de vitesse d’échec."
    play sound "Click.mp3" noloop

    Na "Tss... le clavier a glissé, je te jure."
    play sound "Click.mp3" noloop

    P "Excuse validée… uniquement si tu fais mieux à la deuxième manche."
    play sound "Click.mp3" noloop

    Na "Ok, je me concentre cette fois. Mode tryhard activé."
    play sound "Click.mp3" noloop

    "{b}{i}Vous relancez la partie, plus motivés que jamais.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Cette fois… c’est lui ou moi."
    play sound "Click.mp3" noloop
     
    P "Ok si tu le dis."
    play sound "Click.mp3" noloop

    "{b}{i}vous continuez de jouer jusqu'à midi.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Super....ce boss de donjon m'a encore eu."
    play sound "Click.mp3" noloop

    P "Ce n'est pas grâve, tu y arriveras mmieux la prochaine fois."
    play sound "Click.mp3" noloop

    Na "Merci d'avoir confiance en moi."
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire puis [I] vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Salut Yuna."
    play sound "Click.mp3" noloop  

    if pronom == "il": 

        I "Salut les amis."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        I "Salut les amies."
        play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    I "C'est génial si tout va bien."
    play sound "Click.mp3" noloop

    "{b}{i}[I] s'asseoit tranquillemnt avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon tu as fait quoi ce matin Yuna ?"
    play sound "Click.mp3" noloop 

    I "Je me suis un peu réposé et regarder une série sur mon ordi."
    play sound "Click.mp3" noloop 

    P "Oh j'aurais pensé que tu avais un peu avancé sur ton jeu vidéo."
    play sound "Click.mp3" noloop 

    I "Oui mais j'ai choisi de me reposer."
    play sound "Click.mp3" noloop 

    P "Je vois, c'est bien de se reposer."
    play sound "Click.mp3" noloop 

    I "Sinon vous avez fait quoi ce matin ?"
    play sound "Click.mp3" noloop 

    Na "Je ne préfére pas en parler si tu veux savoir....."
    play sound "Click.mp3" noloop 

    I "Ah bon et pourquoi ?"
    play sound "Click.mp3" noloop 

    P "On a joué à un jeu vidéo mécanique sur PC."
    play sound "Click.mp3" noloop 

    I "Ah oui et quel est le jeu pour savoir ?"
    play sound "Click.mp3" noloop 

    P "Le jeu en question est le cultissime Nocture core."
    play sound "Click.mp3" noloop 

    "{b}{i}[I] réalise de quel jeu vous parlez.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Attends... vous parlez bien du jeu avec les énigmes impossibles et les boss ultra punitifs ?"
    play sound "Click.mp3" noloop

    P "Exactement, celui où la moindre erreur te renvoie au début du chapitre."
    play sound "Click.mp3" noloop

    Na "Et encore, il a oublié de dire que le jeu a *aucun* checkpoint. C’était l’enfer."
    play sound "Click.mp3" noloop

    I "Mais vous êtes fous ou quoi ? Ce jeu est hyper stressant !"
    play sound "Click.mp3" noloop

    P "Justement, c’est ça qui le rend si bon…"
    play sound "Click.mp3" noloop

    I "Et vous avez réussi à passer le niveau 4 ? Celui avec les trois leviers synchronisés ?"
    play sound "Click.mp3" noloop

    Na "On a failli péter un câble... et moi je me suis fait éliminer par le boss final du niveau au moins quatre fois. Il me laissait *zéro* chance."
    play sound "Click.mp3" noloop

    I "Le boss du niveau 4 ? Celui avec les drones invisibles et les murs qui se referment ?"
    play sound "Click.mp3" noloop

    Na "Exactement. À chaque fois, je croyais avoir compris le pattern… et boum, game over. La quatrième fois j'ai fini par balancer la souris sur le bureau."
    play sound "Click.mp3" noloop

    I "Franchement respect. Moi j’ai ragequit à ce moment-là."
    play sound "Click.mp3" noloop

    P "Tu devrais rejouer avec nous un jour, on pourrait former une bonne équipe."
    play sound "Click.mp3" noloop

    I "Hmm… peut-être. Mais seulement si vous me laissez battre le dernier boss."
    play sound "Click.mp3" noloop 

    Na "Deal… mais t’as intérêt à bien viser cette fois."
    play sound "Click.mp3" noloop 

    "{b}{i}[I] rit doucement, en hochant la tête, visiblement tentée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon Yuna, tu vas faire quoi cette après-midi ?"
    play sound "Click.mp3" noloop 

    I "Je pense que je vais avancer sur mon jeu car je me suis assez reposée ce matin."
    play sound "Click.mp3" noloop

    P "Ah bon tu penses ? moi je dis que tu devrai te reposer un peu plus vu le début d'année qu'on a eu."
    play sound "Click.mp3" noloop

    I "Oui tu as peut-être raison, mais j'ai vraiment envie d'avancer sur mon jeu." 
    play sound "Click.mp3" noloop

    P "Je comprends, mais n'oublie pas de prendre soin de toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de manger et de discuster pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Bon, je vais y aller. J’ai des trucs à faire."
    play sound "Click.mp3" noloop

    P "D'accord, à plus tard Yuna."
    play sound "Click.mp3" noloop

    Na "Oui à plus tard."
    play sound "Footsteps.mp3" noloop   

    "{b}{i}[I] se lève et part vers la sortie du réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi() 
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fait quoi ?"
    play sound "Click.mp3" noloop  
 
    P "On peut continuer de jouer à Nocture core."
    play sound "Click.mp3" noloop  

    Na "Oui pourquoi pas mais je ne suis pas sûre de vouloir continuer."
    play sound "Click.mp3" noloop  

    P "Mais si ça va bien se passer, tu as juste à t'entraîner un peu plus."
    play sound "Click.mp3" noloop 

    Na "Si tu le dis..."
    play sound "Click.mp3" noloop
  
    "{b}{i}Vous vous posez pour continuer à jouer.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon, on va continuer la partie."
    play sound "Click.mp3" noloop

    Na "Oui, mais je ne promets pas de gagner."
    play sound "Click.mp3" noloop

    P "Pas de soucis, on va juste s'amuser."
    play sound "Click.mp3" noloop

    Na "Si tu le dis..."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de jouer pendant deux heures mais [newname] commence à s'éenerver.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "J'en ai marre de ce jeu, je n'arrive pas à passer ce niveau !"
    play sound "Click.mp3" noloop

    P "Calme-toi, c'est juste un jeu. Tu vas y arriver."
    play sound "Click.mp3" noloop

    Na "Non, je n'y arriverai jamais. Je suis nulle à ce jeu."
    play sound "Click.mp3" noloop

    P "Tu n'es pas nulle, tu as juste besoin de t'entraîner un peu plus."
    play sound "Click.mp3" noloop

    Na "Bon je vais à la bibliothèque pour me changer les idées."
    play sound "Click.mp3" noloop

    P "D'accord, je vais te laisser tranquille alors."
    play sound "Click.mp3" noloop

    Na "Merci, je vais essayer de me calmer."
    play sound "Footsteps.mp3" noloop

    "{b}{i}[newname] se lève et part vers la bibliothèque.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu te diriges vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}En sortant tu croises [J1].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [J1], comment ça va ?"
    play sound "Click.mp3" noloop

    J1 "Salut [P], ça va bien merci ! Et toi ?"
    play sound "Click.mp3" noloop

    P "Ça va, merci ! Je vais juste aux toilettes."
    play sound "Click.mp3" noloop

    J1 "Je vois mais juste avant, j'ai vu [newname], elle avait l'air un peu énervée."
    play sound "Click.mp3" noloop

    P "Oui, elle a eu un peu de mal avec un jeu vidéo aujourd'hui."
    play sound "Click.mp3" noloop

    J1 "Ah d'accord, j'espère qu'elle va se calmer."
    play sound "Click.mp3" noloop

    P "Oui, j'espère aussi."
    play sound "Click.mp3" noloop

    J1 "Bon, je te laisse aller aux toilettes alors."
    play sound "Click.mp3" noloop

    P "Ok alors."
    play sound "Click.mp3" noloop

    "{b}{i} Tu continues vers les toilettes.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu entres dans les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon, je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon, je vais retourne."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 
 
    P "Enfin de retour."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te poses un peu sur le lit pour faire une sieste.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Une heure plus tard, après ta sieste.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    P "Hmmm, j'ai fait une bonne sieste...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te lèves tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on dirait qu'elle n'est toujours pas revenue."
    play sound "Door.mp3" noloop

    "{b}{i}Puis [newname] entre dans le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh tu es de retour. Comment ça s'est passé ?"
    play sound "Click.mp3" noloop

    Na "Ça va un peu mieux"
    play sound "Click.mp3" noloop

    P "Tu as réussi à te changer les idées ?"
    play sound "Click.mp3" noloop

    Na "Oui, j'ai lu un peu dans la bibliothèque et ça m'a fait du bien."
    play sound "Click.mp3" noloop

    P "C'est bien, parfois il faut juste prendre du recul."
    play sound "Click.mp3" noloop

    Na "Oui, tu as raison. Merci de m'avoir laissé tranquille."
    play sound "Click.mp3" noloop

    P "Pas de soucis, je suis là pour ça."
    play sound "Click.mp3" noloop

    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright
    
    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien, juste j'avais une question."
    play sound "Click.mp3" noloop 

    Na "Oui dis-moi, je t'écoute."
    play sound "Click.mp3" noloop 
 
    p "C'est vrai ce que tu disais par rapport à tes données ?"
    play sound "Click.mp3" noloop

    Na "Oui, c'est vrai, je ne veut pas tu aie accès à ce que j'ai appris cr je vois ça comme de la triche."
    play sound "Click.mp3" noloop

    P "D'accord, je comprends. Je ne veux pas que tu te sentes mal à l'aise."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 22 décmebre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 1

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 
    
    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop   

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

label password25:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password:

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password25

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?"  
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop   

    P "Bon on fait quoi aujourd'hui ?"
    play sound "Click.mp3" noloop  

    Na "Je veux essayer le jeu Watch Dogs que j'ai vu sur internet, regardes la page du jeu."
    play sound "Click.mp3" noloop 

    $ renpy.open_url("https://store.steampowered.com/app/243470/Watch_Dogs/")

    P "Oui pourquoi pas, en plus il pousse ta réflexion sans être trop complexe comme Nocture core."
    play sound "Click.mp3" noloop

    Na "Mais c'est génial ! J'adore les jeux où il faut réfléchir et trouver des indices."
    play sound "Click.mp3" noloop

    "{b}{i}Puis [newname] regarde ton PC.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Il y a quoi [newname] ?"
    play sound "Click.mp3" noloop 

    Na "Je viens de le remarquer mais ta session d'ordinateur se nomme [nom_utilisateur_pc]."
    play sound "Click.mp3" noloop 

    P "Oui c'est normal, c'est le nom que j'ai choisi pour mon compte utilisateur."
    play sound "Click.mp3" noloop 

    Na "Ok Je vois, Bon moi je vais essayer de me connecter à mon compte pour voir si je peux jouer à Watch Dogs."
    play sound "Click.mp3" noloop

    P "D'accord, je vais te laisser faire, moi je vais lire un peu."
    play sound "Click.mp3" noloop   
     
    "{b}{i}[newname] se connecte tranquillement à sa bibliothèque de jeux.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tu as pu trouvé le jeu ?"
    play sound "Click.mp3" noloop 

    Na "Oui je l'ai trouvé, je vais commencer à l'installer."
    play sound "Click.mp3" noloop 

    P "Ok alors amuses-toi bien."
    play sound "Click.mp3" noloop 

    Na "Je pense bien que je vais m'amuser vu que tu m'a conseillé le jeu."
    play sound "Click.mp3" noloop 

    P "Bon je te laisse, moi je vais lire sur mon lit."
    play sound "Click.mp3" noloop 

    Na "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] joue tranquillement au jeu pendent que tu lis pour trois heures.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tu en es à ou dans le jeu ?"
    play sound "Click.mp3" noloop 

    Na "Je viens de finir le premier le prologue."
    play sound "Click.mp3" noloop 

    P "Félicitation pour être arrivée jusqzu'à ici."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis vous continuez encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu entres dans le réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vous asseoir dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon appétit [newname]."
    play sound "Click.mp3" noloop 

    Na "Bon appétit à toi aussi [prenom]."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement entre vous.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    p "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    Na "Bien."
    play sound "Click.mp3" noloop 

    P "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Bon tu veux faire quoi cet après-midi ?"
    play sound "Click.mp3" noloop  

    Na "Moi je veux continuez de jouer à Watch Dogs."
    play sound "Click.mp3" noloop  

    P "Ok alors, moi je vais lire un peu."
    play sound "Click.mp3" noloop  

    Na "Pas de soucis alors."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te poses tranquillement pendant qu'[newname] joue.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyons voir ce livre...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu lis tranquillement pendant trois heures sur ton lit.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon fini de lire pour aujourd'hui."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te lèves et tu vas vers [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Alors [newname], tu en es où dans le jeu ?"
    play sound "Click.mp3" noloop

    Na "Je suis au chapitre 2, c'est trop bien !"
    play sound "Click.mp3" noloop

    P "Trop cool ! J'ai hâte de voir la suite."
    play sound "Click.mp3" noloop

    Na "Oui, moi aussi. J'adore ce jeu, il est vraiment captivant."
    play sound "Click.mp3" noloop

    P "Je suis content que tu aimes, c'est un de mes jeux préférés."
    play sound "Click.mp3" noloop

    Na "Merci de me l'avoir conseillé, je ne regrette pas du tout de l'avoir acheté."
    play sound "Click.mp3" noloop

    P "Pas de soucis, je suis là pour ça."
    play sound "Click.mp3" noloop

    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright
    
    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger car je suis fatiguée à cause du jeu."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 23 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft 

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 
    
    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop   

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

label password26:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password:

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password26

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    Na "Je suis encore fatiguée Et toi ?"  
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop   

    P "Bon on fait quoi aujourd'hui ?"
    play sound "Click.mp3" noloop  

    Na "Je ne sais pas."
    play sound "Click.mp3" noloop 

    P "Attends, tu as dit que tu était fatiguée ?"
    play sound "Click.mp3" noloop 

    Na "Oui comme si ma batterie était presque vide..."
    play sound "Click.mp3" noloop 

    P "c'est bizarre, d'habitude ta batterie est toujours pleine après une nuit de charge."
    play sound "Click.mp3" noloop

    Na "Oui c'est bizarre."
    play sound "Click.mp3" noloop

    "{b}{i}Tu réfléchis pourquoi et comment c'est arrivée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Tu penses à la mème chose que moi."
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Le chargeur{/i}{/b}" :  
            play sound "Menu.mp3" noloop 

            P "c'est peut être le cable d'alimention qui a laché."
            play sound "Click.mp3" noloop 

            Na "Non je fais référence à la batterie qui ne tiens plus la charge."
            play sound "Click.mp3" noloop 

            P "Bon après ta batterie, je l'ai trouvé dans l'entrepôt oû je t'ai récupéré et il je me souviens avoir dit qu'elle allait tenir un moment ^mais pas indéfiniment, elle a durée cinq mois."
            play sound "Click.mp3" noloop

            Na "Bon si c'est la batterie que tu as trouvée dans l'entrepôt, elle a dû être usée et ne tiens plus."
            play sound "Click.mp3" noloop

            P "C'est ce que je me dit aussi."
            play sound "Click.mp3" noloop

            Na "Oui mais maintenant il faut trouver une solutions."
            play sound "Click.mp3" noloop 
            
        "{b}{i} La batterie.{/i}{/b}" :  
            play sound "Menu.mp3" noloop 

            P "C'est peut-être la batterie qui a lâché et qui ne supporte plus les cycles de charge."
            play sound "Click.mp3" noloop

            Na "Possible… mais c’est étrange qu’elle ait chuté aussi brutalement du jour au lendemain."
            play sound "Click.mp3" noloop

            P "Bon après ta batterie, je l'ai trouvé dans l'entrepôt oû je t'ai récupéré et il je me souviens avoir dit qu'elle allait tenir un moment ^mais pas indéfiniment, elle a durée cinq mois."
            play sound "Click.mp3" noloop

            Na "Bon si c'est la batterie que tu as trouvée dans l'entrepôt, elle a dû être usée et ne tiens plus."
            play sound "Click.mp3" noloop

            P "C'est ce que je me dit aussi."
            play sound "Click.mp3" noloop

            Na "Oui mais maintenant il faut trouver une solutions."
            play sound "Click.mp3" noloop

    P "Oui je confirme qu'il faut trouver une solution car sinon tu ne pourras plus démarrer."
    play sound "Click.mp3" noloop

    Na "Mais pour commencer tu as une idée sur la batterie qu'il me faudrait ?"
    play sound "Click.mp3" noloop

    if quest11 == 1: 

        P "Je ne sais pas du tout car dans tes documents il n'est fait aucune mention d'une batterie spécifique." 
        play sound "Click.mp3" noloop

    else: 
    
        P "Je ne sais pas du tout pour tout te dire." 
        play sound "Click.mp3" noloop

    Na "Je vois alors donc on va devoir se débrouiller pour une bonne batterie."
    play sound "Click.mp3" noloop

    P "Ce ne doit pas être si dur d'en trouver une..."
    play sound "Click.mp3" noloop

    Na "Tu rigoles j'espére, je te rappelle que je suis la dernière [model] encore en vie."
    play sound "Click.mp3" noloop

    P "Oui et alors c'est juste une batterie ?"
    play sound "Click.mp3" noloop

    Na "Oui mais de mon point de vue se sera difficile de trouver une batterie spécifiquement pour moi."
    play sound "Click.mp3" noloop 

    P "Je t'ai déjà trouvée un batterie le jour oû je t'ai récupérée donc...."
    play sound "Click.mp3" noloop

    Na "ça devait sûrement être une batterie de Neogen Technologies."
    play sound "Click.mp3" noloop

    P "Oui c'est sûrement ça."
    play sound "Click.mp3" noloop

    Na "Bon il faut qu'on fasse vite car......."
    play sound "Click.mp3" noloop
    
    P "Oui tu as raison."
    play sound "Click.mp3" noloop

    Na "Tu proposes quoi pour commencer ?"
    play sound "Click.mp3" noloop

    menu:    

        "{b}{i}Regarder l'ancienne batterie.{/i}{/b}" :  
            play sound "Menu.mp3" noloop 

    P "Je vais regarder l'ancienne batterie."
    play sound "Click.mp3" noloop

    Na "Ok je te laisse faire alors."
    play sound "Click.mp3" noloop

    P "Bien entendu."
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour inspecter l'ancienne batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon voyons voir ça."
    play sound "Click.mp3" noloop

    Na "Alors trouver quelques choses sur l'ancienne batterie ?"
    play sound "Click.mp3" noloop 

    P "Attend deux minutes, je regarde ça."
    play sound "Click.mp3" noloop

    Na "Ok."
    play sound "Click.mp3" noloop

    "{b}{i}Tu inspectes l'ancienne batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Il semblerait que la batterie fasse 4000 Wh."
    play sound "Click.mp3" noloop 

    Na "Je vois... mais elle a été stockée longtemps sans entretien, non ?"
    play sound "Click.mp3" noloop

    P "Oui, et ça veut dire qu'elle a sûrement perdu de sa capacité réelle."
    play sound "Click.mp3" noloop

    Na "Donc même si c'est marqué 4000 Wh, on ne peut pas être sûrs qu'elle tienne toute la journée."
    play sound "Click.mp3" noloop

    P "Exact. Il faut que je choisisse une batterie neuve avec une capacité adaptée pour toi."
    play sound "Click.mp3" noloop

    Na "Tu crois qu'on pourra vraiment trouver une batterie pour moi ? Je suis la seule et unique [model] encore en vie…"
    play sound "Click.mp3" noloop

    P "On va bien trouver, faut juste chercher au bon endroit."
    play sound "Click.mp3" noloop

    Na "J’espère… parce que je ne veux pas rester inactive trop longtemps."
    play sound "Click.mp3" noloop

    P "Maintenant il faut trouver où en acheter une."
    play sound "Click.mp3" noloop

    Na "Peut-être au département de pièces détachées du lycée."
    play sound "Click.mp3" noloop

    P "Bonne idée, ils ont sûrement des batteries de rechange."
    play sound "Click.mp3" noloop

    Na "Bon, je vais me poser un peu pour éviter la surcharge."
    play sound "Click.mp3" noloop 

    P "D'accord, je m'occupe d'appeler."
    play sound "Phone.mp3" noloop

    "{b}{i}Tu te poses tranquillement pour appeler le département de pièces détachées.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Allô, département de pièces détachées ?"
    play sound "Click.mp3" noloop

    R "Oui, bonjour, comment puis-je vous aider ?"
    play sound "Click.mp3" noloop

    P "C’est bien [Ah] à l’appareil ?"
    play sound "Click.mp3" noloop

    Rn "Non, c’est [Rn], je remplace [Ah] pendant ses vacances."
    play sound "Click.mp3" noloop

    P "D’accord, je cherche une batterie pour [newname], vous avez quoi ?"
    play sound "Click.mp3" noloop

    Rn "Laisse-moi regarder ton dossier."
    play sound "Click.mp3" noloop

    P "Pas de souci."
    play sound "Click.mp3" noloop

    "{b}{i}[Rn] consulte ton dossier pendant un instant.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Rn "Ok, nous avons des batteries neuves pour [newname]. Les capacités sont : 4000 Wh, 7000 Wh et 10000 Wh. Laquelle voulez-vous ?"
    play sound "Click.mp3" noloop 

    P "Je vais prendre celle de..."
    play sound "Menu.mp3" noloop  

    menu: 

        "{b}{i}4000 Wh.{/i}{/b}" : 
            play sound "Menu.mp3" noloop
            jump fin_batterie_trop_faible

        "{b}{i}7000 Wh.{/i}{/b}" :  
            play sound "Menu.mp3" noloop
            jump fin_batterie_parfaite

        "{b}{i}10000 Wh.{/i}{/b}" :  
            play sound "Menu.mp3" noloop
            jump fin_batterie_trop_puissante

label end_script2:
    call script3 
    return 

# Aris la plus belle ###################