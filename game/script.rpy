label start: 

    stop music fadeout 2.0   

    $ grade = 0.0  
    $ points = 0 
    $ day = 0 
    $ suspect = "" 
    default cpu = "??????????"
    default success = 0
    $ wallbreak = 0
    default update = 1.0
    default origine = "la classe préparatoire Alpha"  
    default domaine = "??????????" 
    $ model = "robot humanoïde" 
    $ ending = 0
    default stored_password = ""
    default system = "??????????"
    default ip = ""
    default newname = ""  
    default robotorigine = "??????????" 
    default prenom = "??????????" 
    default nom = "??????????" 
    default propriety = "" 
    default serie = "??????????"
    default stockage = "??????????"
    default robotname = ""  
    default baseip = ""

#############################################

    default character1 = "??????????"
    default character2 = "??????????"
    default character3 = "??????????"
    default character4 = "??????????"
    default character5 = "??????????"
    default character6 = "??????????"
    default character7 = "??????????"
    default character8 = "??????????"
    default character9 = "??????????"
    default character10 = "??????????"
    default character11 = "??????????"
    default character12 = "??????????"
    default character13 = "??????????"
    default character14 = "??????????"
    default character15 = "??????????"
    default character16 = "??????????"
    default character17 = "??????????"
    default character18 = "??????????"

    default ultimate1 = "??????????"
    default ultimate2 = "??????????"
    default ultimate3 = "??????????"
    default ultimate4 = "??????????"
    default ultimate5 = "??????????"
    default ultimate6 = "??????????"
    default ultimate7 = "??????????"
    default ultimate8 = "??????????"
    default ultimate9 = "??????????"
    default ultimate10 = "??????????" 
    default ultimate11 = "??????????"
    default ultimate12 = "??????????"
    default ultimate13 = "??????????"  
    default ultimate14 = "??????????"
    default ultimate15 = "??????????"
    default ultimate16 = "??????????"  
    default ultimate17 = "??????????"
    default ultimate18 = "??????????"  

    default charactertext1 = "??????????"  
    default charactertext2 = "??????????"  
    default charactertext3 = "??????????"  
    default charactertext4 = "??????????"  
    default charactertext5 = "??????????"  
    default charactertext6 = "??????????"  
    default charactertext7 = "??????????"  
    default charactertext8 = "??????????"  
    default charactertext9 = "??????????"  
    default charactertext10 = "??????????"  
    default charactertext11 = "??????????"  

    default quest1 = 0
    default quest2 = 0
    default quest3 = 0
    default quest4 = 0
    default quest5 = 0
    default quest6 = 0
    default quest7 = 0
    default quest8 = 0
    default quest9 = 0
    default quest10 = 0
    default quest11 = 0
    default quest12 = 0
    default quest13 = 0 
    default quest14 = 0
    default quest15 = 0
    default quest16 = 0
    default quest17 = 0
    default quest18 = 0
    default quest19 = 0
    default quest20 = 0
    default quest21 = 0
    default quest22 = 0
    default quest23 = 0
    default quest24 = 0
    default quest25 = 0
    default quest26 = 0
    default quest27 = 0
    default quest28 = 0
    default quest29 = 0
    default quest30 = 0 
    default quest31 = 0 
    default quest32 = 0
    default quest33 = 0 
    default quest34 = 0
    default quest35 = 0
    default quest36 = 0
    default quest37 = 0
    default quest38 = 0
    default quest39 = 0 

label key:  

    play sound "Menu.mp3" noloop
    $ key = renpy.input("Veuillez écrire votre clé d'accès.").strip()

    $ valid_keys = {"ARIS-DEVS", "ARIS-8J4K-F9Q7", "ARIS-GRFN-M4A1"}
    
    if key in valid_keys: 

        "Jeu déverrouillé." 
        play sound "Click.mp3" noloop

    else: 

        "Erreur système. Veuillez réessayer."
        $ renpy.restart_interaction()
        jump key 

    $ success = 0 

    if key == "ARIS-8J4K-F9Q7" or key == "ARIS-DEVS" or key == "ARIS-DEMO" :

        $ origine = "la classe préparatoire Alpha" 

    elif key == "ARIS-GRFN-M4A1":

        $ P = Character('[prenom] [nom]', color="#707070") 
        $ origine = "la classe préparatoire Alpha"   
        $ quest1 += 1
        $ success += 1 

        show screen update with moveinright

        "DLC secret déverouillé."  
        play sound "Click.mp3" noloop

        hide screen update with moveoutright

label identity: 

    $ prenom = renpy.input("Quel est votre prénom de lycéen ?")
    $ prenom = prenom.strip() 

    $ nom = renpy.input("Quel est votre nom de lycéen ?")
    $ nom = nom.strip()

    $ pronom = renpy.input("Quel est votre genre ? (il ou elle)")
    $ pronom = pronom.strip()

    if pronom not in {"il", "elle"}:
        "Erreur système. Veuillez réessayer."
        $ renpy.restart_interaction()
        jump identity

    "Vos informations ont été enregistrées."
    play sound "Menu.mp3" noloop

    $ domaine = "inégalable créateur" if pronom == "il" else "inégalable créatrice"
    
    $ noms_interdits = {"Kusanagi", "Nishimura", "Ayanokoji", "Sato", "Saotome", "Ichinose", "Hiiragi", "Katsuragi", "Hanemiya", "Sumino", "Hoshino", "Shinomiya", "Katsuya", "Horimiya", "Tachibana", "Sakayanagi", "Nagumo", "Kaminari", "Suzumiya", "Kobayashi", "Kaneda", "Nanami", "Kurosawa"}
    $ prenoms_interdits = {"Yuna", "Hajime", "Kendo", "Naoto", "Haruki", "Yuki", "Emika", "Kazumi", "Ayano", "Aiko", "Akeno", "Subaru", "Suzune", "Shiro", "Kaede", "Naomi", "Seigo", "Takeshi", "Saori", "Mizuki", "Rika", "Natsuo", "Reiichi", "Mayumi", "Luna", "Hiroyuki"}

    if prenom in prenoms_interdits:
        "Ce prénom n'est pas autorisé."
        jump identity  
    
    if prenom == "Aris":
        R "Cher joueur/chère joueuse, je ne suis pas sûr qu’avoir le prénom Aris soit une bonne idée pour la suite de l'histoire. Veuillez en choisir un autre."
        jump identity  
    
    if nom in noms_interdits:
        "Ce nom n'est pas autorisé."
        jump identity 
    
    if not prenom and not nom:

        if pronom == "il":

            $ prenom, nom = "Mitsuya", "Shimura"

        else:

            $ prenom, nom = "Kyoka", "Nakano"

        "Bienvenue [prenom] [nom]. Puisque aucun nom n'a été choisi, celui-ci vous a été attribué."

    else:
        
        "Bienvenue [prenom] [nom]."

label auto_save: 

    show screen logo() 
    
    transform unrotate: 
        zoom 0.5
        rotate 360 
        linear 2.0 rotate 0
 
    # $ _preferences.afm_enable = True

    "{b}{i}Bienvenue dans Arisization Project cher/chère lycéen, Ce jeu appartient à SLTM.{/i}{/b}"   
    play sound "Click.mp3" noloop 
 
    hide screen logo 

    "{b}{i}Avertissement : Ce jeu contient des scènes pouvant heurter la sensibilité de certains joueurs. Inspiré de faits réels, il explore des thématiques complexes telles que la moralité, les dilemmes éthiques et les conséquences humaines.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}Avant de commencer, veuillez noter que chaque décision prise dans ce jeu est irréversible et aura un impact permanent sur votre progression.{/i}{/b}"
    play sound "Transition.mp3" noloop

label début: 

    scene main with fade
     
    if key == "ARIS-GRFN-M4A1": 

        "{b}{i}Chapitre 0 : Arisization Project Alternative - Lost Origins Arc{/i}{/b}"
        play sound "Click.mp3" noloop 

    else:   

        "{b}{i}Chapitre 0 : Arisization Project - Lost Origins Arc{/i}{/b}"
        play sound "Click.mp3" noloop 

    scene black with fade
    
    "{b}{i}Quelque part dans un entrepôt abandonné en 2097.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene warehouse with fade
    
    # $ _preferences.afm_enable = False 

    play music "Soundtrack2.mp3" loop volume 1.0

    P "Bon, on fait quoi ?"
    play sound "Click.mp3" noloop  

    S "On pourrait fouiller les lieux déjà ?"
    play sound "Click.mp3" noloop

    $ character1 = S 

    P "Tu penses sérieusement qu'on va trouver quelque chose d'intéressant ici ?"
    play sound "Click.mp3" noloop    

    S "Oui sûrement."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ entrepot = get_random_entrepot()
    "{b}{i}[entrepot]{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tu trouves quelques choses ?"
    play sound "Click.mp3" noloop

    S "Non, rien malheureusement..."
    play sound "Click.mp3" noloop 
 
    "{b}{i}Tu continues de chercher quelque chose d'intéressant quand soudain [S] tombe sur un énorme objet.{/i}{/b}"
    play sound "Stumble.mp3" noloop  

    S "C'est quoi ce truc qui traîne encore ?"
    play sound "Click.mp3" noloop

    P "Fais voir ce que c'est ?"
    play sound "Footsteps.mp3" noloop 

    "{b}{i}Tu t'approches et tu découvres un [model].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "On dirait un [model], comme ceux qui ont été utilisés pendant la guerre de l'année dernière."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        S "Un [model] !? Tu n'es pas sérieux j'espère."
        play sound "Click.mp3" noloop

    elif pronom == "elle":

        S "Un [model] !? Tu n'es pas sérieuse j'espère."
        play sound "Click.mp3" noloop

    P "Si, je le suis."
    play sound "Click.mp3" noloop

    S "Ok, mais on va faire quoi avec ça maintenant ?"
    play sound "Click.mp3" noloop

    "{b}{i}Tu commences à analyser le robot pour comprendre son état.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Attends, il manque quelque chose... Elle n'a pas sa batterie."
    play sound "Click.mp3" noloop 

    "{b}{i}tu fouilles dans l'entrepôt et trouve par chance une nouvelle batterie que tu installes avec précaution.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Voilà, elle devrait pouvoir tenir un moment avec ça, c’est plus sûr."
    play sound "Click.mp3" noloop 

    P "Je vais essayer de la pirater en contournant sa sécurité."
    play sound "Click.mp3" noloop 

    S "Pardon !?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes d'abord ton livre d'informatique.{/i}{/b}"
    play sound "Click.mp3" noloop 

    S "Je ne suis pas sûr que ce soit une bonne idée..."
    play sound "Click.mp3" noloop 

    P "Oh, c'est bon, elle est abandonnée et en plus ça ne brise ni la loi ni l'une des dix règles de l'informatique."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu démarres le robot pour injecter des instructions.{/i}{/b}"
    play sound "Menu.mp3" noloop 

label hack: 

    $ hack = renpy.input("écris ceci : initiate_humanoid_robot.start(security_override=true)")
    $ hack = hack.strip()   

    if hack == "initiate_humanoid_robot.start(security_override=true)":

        $ success += 1 
        $ quest2 += 1
        $ stockage = 0.0 

        show screen update with moveinright

        "système ouvert avec succès." 
        play sound "Click.mp3" noloop 

        hide screen update with moveoutright

        $ stockage += 2.0

    else: 

        "Erreur système redémarrage en cours." 
        play sound "Click.mp3" noloop     

        P "Mince..." 
        play sound "Click.mp3" noloop 

        P "Je vais réessayer." 
        play sound "Menu.mp3" noloop 

        jump hack 

    if key == "ARIS-GRFN-M4A1":

        R "Initialisation des protocoles principaux..."
        play sound "Click.mp3" noloop 

        P "Attends... On dirait qu'elle commence à s'activer."
        play sound "Menu.mp3" noloop 

        S "Ah bon vraiment ?" 
        play sound "Click.mp3" noloop

        P "Oui regarde." 
        play sound "Click.mp3" noloop 

        $ stockage -= 1.0

        R "Anomalie détectée. Nom de code introuvable dans la base de données."
        play sound "Click.mp3" noloop 

        P "Hein ? Qu'est-ce que ça signifie ?"
        play sound "Menu.mp3" noloop  

        R "Nom de code absent. Lancement du protocole de génération assistée, veuillez choisir un nouveau nom de code..."
        play sound "Click.mp3" noloop  
        
        menu: 

            "{b}{i}Choisir M4A1{/i}{/b}" :
                $ A = Character("M4A1", color="#00ff00")
                $ stockage += 1.0 

            "{b}{i}Choisir M16A1{/i}{/b}" :
                $ A = Character("M16A1", color="#ffa600") 
                $ stockage += 1.2

            "{b}{i}Choisir ST AR-15{/i}{/b}" : 
                $ A = Character("ST AR-15", color="#ff8fc3") 
                $ stockage += 1.5 

            "{b}{i}Choisir M4 SOPMOD II{/i}{/b}" :
                $ A = Character("M4 SOPMOD II", color="#ff4a4a")
                $ stockage += 2.0 

            "{b}{i}Choisir M82A1{/i}{/b}" :
                $ A = Character("M82A1", color="#0000ff") 
                $ stockage += 1.4 

            "{b}{i}Choisir M1919A4{/i}{/b}" : 
                $ A = Character("M1919A4", color="#005c17") 
                $ stockage += 1.8 

        show screen update with moveinright

        $ renpy.block_rollback()
        $ quest3 += 1   
        $ success += 1 

        hide screen update with moveoutright

    else:    

        $ A = Character("M82A1", color="#00eeff")
        $ stockage += 1.0

        R "Initialisation en cours......" 
        play sound "Click.mp3" noloop

        P "Attend on dirait qu'elle est en train de démarrer."
        play sound "Menu.mp3" noloop 

        S "Ah bon vraiment ?" 
        play sound "Click.mp3" noloop

        P "Oui regarde." 
        play sound "Click.mp3" noloop

    $ propriety = P 

    A "Initialisation terminée. Date du 4 juillet 2097, Bonjour je suis [A] et j'ai dix-huit ans."
    play sound "Click.mp3" noloop 

    P "Tu vois, je t'avais dit de ne pas t'inquiéter."
    play sound "Click.mp3" noloop

    S "Ok, mais c'est juste que je ne suis pas à l'aise à coté d'elle."
    play sound "Click.mp3" noloop 

    P "Oh c'est bon, c'est juste un [model]."
    play sound "Click.mp3" noloop

    S "Ok si tu le dit."
    play sound "Click.mp3" noloop 
 
    P "Sinon [A], tu peux me dire un peu plus sur toi ?"
    play sound "Click.mp3" noloop 

    A "Malheureusement je ne connais que mon nom de code et mon âge, la date d'aujourd'hui, j'ai oublié le reste."
    play sound "Click.mp3" noloop 

    $ charactertext11 = "Elle est un robot humanoïde abandonné de 18 ans qui se souvient que de son nom de code et mon âge et a oublié le reste."  

    P "Je vois..."
    play sound "Click.mp3" noloop 

    A "Tu t'appelles comment ?"
    play sound "Click.mp3" noloop 

    P "Ah oui j'avais oublié, je me nomme [P]."
    play sound "Click.mp3" noloop  

    $ stockage += 2.0 

    A "Bonjour [prenom] je suis ravie de te rencontrer mais j'ai duex questions."
    play sound "Click.mp3" noloop 

    P "Oui dis-moi."
    play sound "Click.mp3" noloop 

    A "Peux-tu me dire ou suis-je ?"
    play sound "Click.mp3" noloop 

    P "On est dans un entrepôt désaffecté."
    play sound "Click.mp3" noloop 

    A "Je vois, c'est donc ça cet endroit maudit."
    play sound "Click.mp3" noloop 

    P "Oui et quelle est ta deuxième question ?"
    play sound "Click.mp3" noloop 

    A "Me reste-il un avenir !? Voudra-t-on encore de moi ?"
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Oui.{/i}{/b}" :

            $ renpy.block_rollback()
            $ success += 1
            $ quest4 += 1  

            show screen update with moveinright

            P "Oui bien sûr qu'il te reste un avenir et que je veux de toi."
            play sound "Click.mp3" noloop   

            hide screen update with moveoutright

            A "C'est vrai !?"
            play sound "Click.mp3" noloop   

            P "Oui je te promet de te donner la merveilleuse vie que tu mérites."
            play sound "Click.mp3" noloop   

            $ stockage += 2.0 

            A "Merci infiniment [prenom]."    
            play sound "Click.mp3" noloop 

            P "Mais de rien c'est normal."
            play sound "Click.mp3" noloop 

            S "Arrètes de dire n'importe quoi elle ne pourra pas avoir un avenir."    
            play sound "Click.mp3" noloop 

            P "Mais si elle peut !"
            play sound "Click.mp3" noloop 

        "{b}{i} Je ne sais pas.{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            P "Ah vrai dire je ne sais pas trop."
            play sound "Click.mp3" noloop

            A "Je vois."
            play sound "Click.mp3" noloop            

    S "Bon, on quitte cet endroit ?"
    play sound "Click.mp3" noloop 

    P "Oui vu qu'on a fini de voir ici."
    play sound "Click.mp3" noloop 

label choice1: 

    S "Par contre tu laisses ce robot ici."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Abandonner [A] {/i}{/b}" :
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            $ validation = get_random_validation() 
            P "[validation]"
            play sound "Click.mp3" noloop 
         
            A "Mais pourquoi..."
            play sound "Click.mp3" noloop   

            P "Désolé mais il a raison."
            play sound "Click.mp3" noloop   

            S "Bien maintenant on se barre ?"
            play sound "Click.mp3" noloop     

            $ validation = get_random_validation() 
            P "[validation]"
            play sound "Click.mp3" noloop   

            A "Non......"
            play sound "Click.mp3" noloop   

            scene black with fade 

            "{b}{i}Tu quittes l'entrepôt avec [S].{/i}{/b}"
            play music "gameover.mp3" noloop

            "{b}{i} Fin numéro 1 : [A] finit complètement Abandonnée et détruite.{/i}{/b}"
            play sound "Menu.mp3" noloop

            menu:

                "{b}{i}Retourner au menu{/i}{/b}" : 
                    return
                    
                "{b}{i}Réessayer{/i}{/b}" : 
                   
                    play sound "Glitch.mp3" noloop
                    scene warehouse with fade
                    $ wallbreak += 1

                    play music "Soundtrack2.mp3" loop volume 1.0
                    jump choice1

        "{b}{i} Garder [A] {/i}{/b}" :

            $ renpy.block_rollback()

            P "Je refuse de la laisser ici alors qu'elle est en bonne état de fonctionner malgré son effacement numérique et en plus j'ai pris du temps pour la démarrer."
            play sound "Click.mp3" noloop 

            if wallbreak == 0: 
                jump argument

            elif wallbreak == 1:

                A "S'il vous plaît, j'ai déjà été abandonnée par une jeune personne... [pronom] était sans remords, et je ne veux pas revivre cela."
                play sound "Glitch.mp3" noloop

                P "Tu vois, même elle ne veut pas être abandonnée ici. Ce n'est pas juste un personnage, c'est bien plus que ça."
                play sound "Click.mp3" noloop

label argument: 

    S "Ok mais pourrais-je savoir pourquoi elle te serait utile !?"
    play sound "Click.mp3" noloop

    P "Car je pense qu'elle a du potentielle pour m'aider."
    play sound "Click.mp3" noloop 

    S "Mais ce robot ne t'appartiens pas." 
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Mais elle est abandonnée, et en plus je suis bon en informatique pour l'améliorer."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Mais elle est abandonnée, et en plus je suis bonne en informatique."
        play sound "Click.mp3" noloop 

    "{b}{i}Tu mets le chargeur d'[A] dans ton sac pendant que tu parles avec [S].{/i}{/b}"
    play sound "Click.mp3" noloop 

    S "Bon je me tire d'ici."
    play sound "Click.mp3" noloop 

    P "Moi aussi, bon [A] tu me suis ?"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    A "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu quittes l'entrepôt avec [A] en coupant les ponts avec [S].{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene black with fade  

    "{b}{i}Le lendemain, à [origine].{/i}{/b}" 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu entres tranquillement en classe avec [A].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene origineclass with fade 
    show screen origine with moveinright 

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    if pronom == "il":

        S "Tiens ne serait-ce pas le petit [prenom] avec son nouveau [model]."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        S "Tiens ne serait-ce pas la petite [prenom] avec son nouveau [model]."
        play sound "Click.mp3" noloop 

    "{b}{i}Tu l'ignores complètement et va t'asseoir au fond de la classe comme d'habitude.{/i}{/b}"
    play sound "Click.mp3" noloop 

    S "Hey, tu m'écoutes quand je te parle !?"
    play sound "Click.mp3" noloop

    if pronom == "il":

        Su "[S] Tu peux le laisser dans son coin tu sais comment [pronom] est."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        Su "[S] tu peux la laisser dans son coin tu sais comment [pronom] est."
        play sound "Click.mp3" noloop

    $ character11 = Su

    S "Je refuse, tu as vu ce qu'[pronom] a comme objet !?"
    play sound "Click.mp3" noloop

    "{b}{i}[Su] retourne et vois [A].{/i}{/b}"
    play sound "Click.mp3" noloop 

    Su "C'est quoi ce truc, c'est à toi [prenom] !?"
    play sound "Click.mp3" noloop

    P "Oui c'est exact."
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Il ment !"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Elle ment !"
        play sound "Click.mp3" noloop 

    Su "Boucle-la un peu [S] tu es juste jaloux."
    play sound "Click.mp3" noloop

    "{b}{i} tout le monde se retourne vers nous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Sk "Il se passe quoi ?"
    play sound "Click.mp3" noloop

    $ character12 = Sk 
    $ ultimate12 = "L'inégalable fanatique de technologie"

    if pronom == "il": 

        Su "C'est juste [S] qui est jaloux de ce que [prenom] a avec lui."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        Su "C'est juste [S] qui est jaloux de ce que [prenom] a avec elle."
        play sound "Click.mp3" noloop
 
    Sk "Et [pronom] a quoi ?"
    play sound "Click.mp3" noloop 

    Su "Regardes par toi-même."
    play sound "Click.mp3" noloop

    "{b}{i}[Sk] se met à te regarder et il est surpris.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Sk "C'est quoi ce truc...."
    play sound "Click.mp3" noloop

    Su "Tu as vu ?"
    play sound "Click.mp3" noloop

    Sk "Alors je ne m'attendais pas ça venant de toi [prenom] mais il est vraiment mignon ton [model]."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Sk "[nothing]"
    play sound "Click.mp3" noloop

    if pronom == "il":

        S "Mais ne l'écoutez pas c'est un menteur, ce n'est pas son robot."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        S "Mais ne l'écoutez pas c'est une menteuse, ce n'est pas son robot."
        play sound "Click.mp3" noloop

    Su "Tu es fatiguant [S]."
    play sound "Click.mp3" noloop

    if pronom == "il":

        Sk "tu oses dire que [prenom] est un menteur alors qu'il a réussi à faire un robot et pas toi."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        Sk "tu oses dire que [prenom] est une menteuse alors qu'elle a réussi à faire un robot et pas toi."
        play sound "Click.mp3" noloop

    S "Mais ce robot ne lui appartient pas il était abandonné."
    play sound "Click.mp3" noloop

    Sk "Abandonné tu dis !? Même si c'est vrai ça ne justifie pas ton comportement en vers [prenom]."
    play sound "Click.mp3" noloop

    Su "Tu es fatiguant [S]."
    play sound "Click.mp3" noloop 

    Su "Sinon [prenom] tu peux m'en dire un peu plus sur ton robot ?"
    play sound "Click.mp3" noloop

    P "Bien sûr, elle s'appelle [A]."
    play sound "Click.mp3" noloop   

    Su "Bonjour [A] ravie de te rencontrer."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    A "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Su "[nothing]"
    play sound "Click.mp3" noloop

    Su "Enfaite [S] tu es la plus grosse fraude de [origine] pour te permettre d'insulter et rabaisser [prenom] juste parce que tu es populaire."
    play sound "Click.mp3" noloop

    S "Mais..."
    play sound "Click.mp3" noloop

    Su "ça suffit..."
    play sound "Door.mp3" noloop

    "{b}{i}[S] se calme et soudainement la porte s'ouvre et la [T] entra.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Gt "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Sk "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Su "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    S "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    A "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}La [T] regarda rapidement [A].{/i}{/b}" 
    play sound "Click.mp3" noloop 

    if pronom == "il":

        Gt "Oh, très joli [model] mon cher [prenom]."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        Gt "Oh, très joli [model] ma chère [prenom]."
        play sound "Click.mp3" noloop

    P "Merci beaucoup madame."
    play sound "Click.mp3" noloop

    Gt "Mais de rien, malheureusement aujourd'hui comme vous le savez c'est votre dernier jour ici."
    play sound "Click.mp3" noloop

    Gt "Vous avez tous réussi votre examen final félicitation."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Su "[thanks]"
    play sound "Click.mp3" noloop

    S "Pardon, même [prenom] a réussi !?"
    play sound "Click.mp3" noloop

    if pronom == "il": 

        Su "Malgré qu'il soit discret, il a les meilleures notes de la 5ème génération d'élèves de [origine]."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        Su "Malgré qu'elle soit discrète, elle a les meilleures notes de la 5ème génération d'élèves de [origine]."
        play sound "Click.mp3" noloop 

    T "Oui, c'est exact."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        Su "En plus, un élève comme [prenom], on en voit pas tout les jours, il a crée beaucoup de choses."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        Su "En plus, une élève comme [prenom], on en voit pas tout les jours, elle a crée beaucoup de choses."
        play sound "Click.mp3" noloop 

    S "Ok, je vois."
    play sound "Click.mp3" noloop 
    
    Gt "Bien. Maintenant je vais vous remettre vos certificats de fin d'études ici."
    play sound "Click.mp3" noloop

    Su "Vous vous rendez compte les amis, on a fini nos deux années ici !"
    play sound "Click.mp3" noloop

    P "Oui, c'est génial."
    play sound "Click.mp3" noloop

    Sk "Oui je confirme." 
    play sound "Click.mp3" noloop

    S "Oui mais pas besoin de s'affoler car je vous rappelle qui nous reste notre dernière année au lycée."
    play sound "Click.mp3" noloop

    Gt "Oui, [S] a raison il vous reste votre dernière année."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}La [T] vous remet le certificat de fin de cursus.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    Gt "Bon, vous passez officiellement en terminal."
    play sound "Click.mp3" noloop 

    P "Enfin..."
    play sound "Bell.mp3" noloop

    "{b}{i} Puis soudainement la sonnerie sonne.{/i}{/b}" 
    play sound "Click.mp3" noloop 
 
    Gt "Bon, il est déjà l'heure de se quitter... on n'aura pas eu le temps de discuter un peu plus."
    play sound "Click.mp3" noloop 

    "{b}{i}Tous les élèves restent pour se dire au revoir avec respect.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    $ remerciement = get_random_remerciement()
    P "[remerciement]"
    play sound "Click.mp3" noloop

    $ remerciement = get_random_remerciement()
    S "[remerciement]"
    play sound "Click.mp3" noloop

    $ remerciement = get_random_remerciement()
    Su "[remerciement]"
    play sound "Click.mp3" noloop

    $ remerciement = get_random_remerciement()
    Sk "[remerciement]"
    play sound "Click.mp3" noloop 
   
    "{b}{i}La [T] fondit soudainement en larme.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    Gt "Merci énormement chers élèves."
    play sound "Click.mp3" noloop

    Su "C'est avec plaisir."
    play sound "Click.mp3" noloop 

    hide screen origine with moveoutright
    scene black with fade 
    
    "{b}{i}Après cela, tout le monde quitta [origine] pour la dernière fois.{/i}{/b}"   
    play sound "Transition.mp3" noloop 

    stop music fadeout 2.0 

    $ _preferences.afm_enable = True

    scene main with fade 
    
    if key == "ARIS-GRFN-M4A1":

        "{b}{i}Chapitre 1 : Arisization Project Alternative - High school Arc{/i}{/b}"
        play sound "Click.mp3" noloop 

    else:   

        "{b}{i}Chapitre 1 : Arisization Project - High school Arc{/i}{/b}"
        play sound "Click.mp3" noloop 

    if wallbreak == 1: 
        
        "{i}Tu penses vraiment pouvoir améliorer [A] alors que tu l'as déjà abandonnée ?{/i}"
        play sound "Click.mp3" noloop 

    else: 
        
        "{i}Tu penses vraiment pouvoir améliorer [A] ?{/i}"
        play sound "Click.mp3" noloop 

    scene black with fade 
     
    "{b}{i}Deux mois plus tard, dans la région de Danto, le 12 septembre 2097, [prenom]
    intégra un lycée d'informatique et de technologie situé au 209-7201 Danto, Ville de Shin-toshi, 
    District de Kiryō, 2-14-7, Avenue Miraidōri, dans un monde entièrement dominé par 
    les nouvelles technologies et dirigé par un gouvernement technocratique autoritaire.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    $ _preferences.afm_enable = False 

    play music "Soundtrack.mp3" loop volume 1.0

    $ day += 1 
    $ stockage += 60.0 

    scene school with fade 
    show screen day with moveinleft

    if pronom == "il": 

        P "Enfin arrivés au lycée..."
        play sound "Click.mp3" noloop 

        A "Oui, je suis contente pour toi que tu sois arrivé ici."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Enfin arrivées au lycée..."
        play sound "Click.mp3" noloop 

        A "Oui, je suis contente pour toi que tu sois arrivée ici."
        play sound "Click.mp3" noloop 

    P "Juste tu as toutes tes affaires ?"
    play sound "Click.mp3" noloop 

    A "Oui même le téléphone portable que tu m'as offert."
    play sound "Click.mp3" noloop 

    P "bien on peut rentrez à l'intérieur."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi() 
    A "[suivi]" 
    play sound "Footsteps.mp3" noloop

    scene black with fade 

    "{b}{i}Vous entrez dans le lycée avec [A].{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright  

    P "Enfin à l'intérieur..."
    play sound "Click.mp3" noloop 

    A "Oui, ça fait du bien."
    play sound "Click.mp3" noloop 

    P "Où pourrait-on aller pour commencer ? Car je ne connais pas du tout le lycée." 
    play sound "Click.mp3" noloop 

    if pronom == "il":

        A "Attend... Tu t'es inscrit dans un lycée et tu ne t'es pas renseigné un peu plus ?"
        play sound "Click.mp3" noloop

        P "Euh j'étais occupé..."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        A "Attend... Tu t'es inscrite dans un lycée et tu ne t'es pas renseignée un peu plus ?"
        play sound "Click.mp3" noloop

        P "Euh j'étais occupée..."
        play sound "Click.mp3" noloop 
         
    A "Après, ça ne m'étonne pas venant de toi [P]..."
    play sound "Click.mp3" noloop
    
    P "Hein !? Pardon !? Comment oses-tu dire ça !? Je suis à l'origine de ton amélioration, je te rappelle !" 
    play sound "Click.mp3" noloop

    A "Mais pour revenir à ta question, on pourrait monter au premier étage car il semblerait qu'il n'y ait rien d'intéressant ici."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene staircase with fade 
    
    "{b}{i}Vous vous dirigez donc au premier étage.{/i}{/b}" 
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 
    
    A "Ah ouais, ce couloir est vraiment énorme !"
    play sound "Click.mp3" noloop

    P "Je confirme." 
    play sound "Click.mp3" noloop
     
    A "On dirait qu'il y a des dortoirs et plusieurs salles de classe ici."
    play sound "Click.mp3" noloop

    P "Ouais, on pourrait aller voir."
    play sound "Click.mp3" noloop

    A "Oui, mais on doit aller en classe."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i}Vous vous dirigez vers la salle de classe mais quelqu'un s'approche...{/i}{/b}"
    play sound "Click.mp3" noloop

    R "Bonjour, je suis venue vous. Je suis la personne qui doit se charger des nouveaux lycéens ici, dont vous."
    play sound "Click.mp3" noloop

    P "Ok, merci de nous guider. Mais comment vous vous appelez ?"
    play sound "Click.mp3" noloop              

    E "Je m'appelle [E], actuelle présidente du bureau des élèves ou B.D.E. pour faire simple."
    play sound "Click.mp3" noloop

    $ character13 = E
    $ ultimate13 = "Présidente du BDE"

    if pronom == "il":
        
        $ easter_egg = get_random_enchente_m()
        P "[easter_egg]"
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        $ easter_egg = get_random_enchente_f() 
        P "[easter_egg]"
        play sound "Click.mp3" noloop 

    E "Je suis enchantée. Mais pourrais-je savoir t tu t'appelles ?"
    play sound "Click.mp3" noloop 

    P "Je m'appelle [P]."
    play sound "Click.mp3" noloop 

    E "Bienvenue [P]"
    play sound "Click.mp3" noloop 

    P "Merci beaucoup, Emika."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    E "[nothing]"
    play sound "Click.mp3" noloop

    E "Mais j'ai une question."
    play sound "Click.mp3" noloop 

    P "Oui dis-moi, je t'écoute."
    play sound "Click.mp3" noloop 

    E "Qui est cette magnifique fille qui est tout le temps avec toi ?"
    play sound "Click.mp3" noloop 

    A "Magnifique !? je suis vraiment flattée merci beaucoup."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    E "[nothing]"
    play sound "Click.mp3" noloop

    E "Pour revenir à ma question [prenom], qui est cette fille ?"
    play sound "Click.mp3" noloop

    P "Ah elle, c'est [A] mon projet de [model]."
    play sound "Click.mp3" noloop 

    E "Un [model] !?"
    play sound "Click.mp3" noloop 

    P "Oui, c'est un [model] que j'ai créé."
    play sound "Click.mp3" noloop 

    E "Vraiment !?"
    play sound "Click.mp3" noloop 

    P "Oui regarde Emika, Vas-y [A] présentes-toi à elle."
    play sound "Click.mp3" noloop 

    A "Bonjour je suis [A], l'assistante et la création de [P], je suis un [model]."
    play sound "Click.mp3" noloop

    E "Bonjour [A], ravie de te rencontrer."
    play sound "Click.mp3" noloop

    A "Merci beaucoup, Emika."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    E "[nothing] Maintenant je vais vous expliquer comment fonctionne ce lycée."
    play sound "Click.mp3" noloop 

    P "Ok, merci de nous expliquer."
    play sound "Click.mp3" noloop 

    E "Pour commencer, les cours ici sont un peu particulier."
    play sound "Click.mp3" noloop

    P "Comment ça ? expliquez nous plus en détail."
    play sound "Click.mp3" noloop

    E "Déjà, tous les lycéens qui sont ici ont un projet informatique ou technologique ou veulent juste étudier l'informatique ."
    play sound "Click.mp3" noloop 

    P "Ok, intéressant..."
    play sound "Click.mp3" noloop

    E "Donc, tous les lycéens passent beaucoup de temps au club."
    play sound "Click.mp3" noloop 

    P "Vraiment ? autant que ça ?"
    play sound "Click.mp3" noloop

    E "Oui vraiment, le jeudi ou le vendredi sont consacrés aux activités du club."
    play sound "Click.mp3" noloop 

    P "Merci, c'est intéressant à savoir."
    play sound "Click.mp3" noloop 
     
    E "Le reste du temps, vous avez cours."
    play sound "Click.mp3" noloop

    P "J'imagine bien que le reste du temps j'ai cours."
    play sound "Click.mp3" noloop

    E "Maintenant, je vais vous expliquer comment fonctionne les clubs."
    play sound "Click.mp3" noloop

    P "Moi et [A] sommes complètement à votre écoute."
    play sound "Click.mp3" noloop
    
    E "Pour les clubs, chaque élève peut, soit rejoindre le club général du lycée, soit créer son propre club." 
    play sound "Click.mp3" noloop 

    P "Créer son propre club vraiment !?" 
    play sound "Click.mp3" noloop 

    E "Oui et je pense que c'est la meilleure solution pour toi et [A]."
    play sound "Click.mp3" noloop

    P "Ah bon, vraiment et pourquoi ?"
    play sound "Click.mp3" noloop 

    E "Oui car depuis le début de notre discussion, j'ai remarqué que [A] est stressée."
    play sound "Click.mp3" noloop 

    A "Oui je suis souvent stressée dans ce genre de situations."
    play sound "Click.mp3" noloop

    if pronom == "il":

        E "ça va aller, ton créateur est là pour toi. N'est ce pas [P] ?" 
        play sound "Click.mp3" noloop
    
    elif pronom == "elle": 
        
        E "ça va aller, ta créatrice est là pour toi. N'est ce pas [P] ?"
        play sound "Click.mp3" noloop

    P "Oui j'atteste que je serai toujours là pour elle."
    play sound "Click.mp3" noloop

    A "Merci beaucoup, ça me rassure."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    E "[nothing]"
    play sound "Click.mp3" noloop

    E "Je vais vous expliquer comment fonctionnent les cours."
    play sound "Click.mp3" noloop 

    P "Comment ça, il y a une particularité avec les cours ?" 
    play sound "Click.mp3" noloop

    E "Oui. Par exemple, il n'y a pas beaucoup d'examens durant l'année." 
    play sound "Click.mp3" noloop 

    P "Heureusement, ce sera moins stressant pour moi et [A]."
    play sound "Click.mp3" noloop 

    E "Et il y a que quatre jours de cours par semaine."
    play sound "Click.mp3" noloop 

    P "Merci pour ces informations."
    play sound "Click.mp3" noloop

    E "Ah et aussi, voilà tes informations concernant ta classe et tes horaires." 
    play sound "Click.mp3" noloop

    P "Merci beaucoup, Emika."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    E "[nothing] C'est normal"
    play sound "Click.mp3" noloop

    "{b}{i}Tu regardes tes documents et ceux d'[newname] et vous remarquez que vous étes en Terminale-E.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Terminale-E... C'est donc ça notre classe."
    play sound "Click.mp3" noloop

    A "Oui." 
    play sound "Click.mp3" noloop

    $ stockage += 2.0 

    E "Oui et aussi, avant que tu partes, j'ai un dernier truc a régler avec toi."
    play sound "Click.mp3" noloop

    P "Oui, dis-moi ?"
    play sound "Click.mp3" noloop

    E "Normalement, les lycéens ne n'en ont pas besoin car ils ont des projets simples."
    play sound "Click.mp3" noloop 

    P "Comment ça ? Je ne comprend pas..."
    play sound "Click.mp3" noloop 

    E "Normalement, ils n'ont pas de besoin de contrat ou de dérogation mais toi oui vue l'ampleur de ton projet."
    play sound "Click.mp3" noloop

    P "Quoi !? Comment ça !?"
    play sound "Click.mp3" noloop

    A "Quoi !? Comment ça, une dérogation pour que [prenom] puisse bosser sur mon amélioration !?"
    play sound "Click.mp3" noloop

    E "Oui, et il faudra l'accepter pour continuer ton projet."
    play sound "Click.mp3" noloop 

    "{b}{i}Après un moment de réflexion, tu réalises et tu te prépares à accepter le contrat.{/i}{/b}"
    play sound "Menu.mp3" noloop 

    menu:

        "{b}{i}Accepter le contrat ?{/i}{/b}":

            $ renpy.block_rollback()
            $ success += 1
            $ quest5 += 1 

    show screen update with moveinright

    P "Ok, je l'accepte."
    play sound "Click.mp3" noloop 

    hide screen update with moveoutright

    E "Bien. Voici le contrat UCN000001 pour l'utilsation complète de [A] au sain du lycée Nexus." 
    play sound "Click.mp3" noloop

    P "Merci, mais j'aimerais savoir pourquoi j'ai besoin d'un contrat pour utiliser ma propre invention dans le lycée."
    play sound "Click.mp3" noloop 

    E "Car [A] peut devenir dangereuse si tu la gères mal."
    play sound "Click.mp3" noloop

    A "Moi, devenir dangereuse !?"
    play sound "Click.mp3" noloop 

    $ stockage += 1.5

    E "Oui, si tes paramètres sont mal faits par [P] car j'ai pu voir ton dossier et tu as l'air trés complexe."
    play sound "Click.mp3" noloop 

    A "Ok, je comprends mieux pourquoi..."
    play sound "Click.mp3" noloop

    E "Bon, maintenant partez en cours avant d'arriver en retard."
    play sound "Click.mp3" noloop

    P "Ok, j'y vais toute de suite, allez [A] tu viens."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    A "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i}Vous vous dirigez vers la salle de classe 404.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe, mais dès que vous entrez, tout le monde se tourne vers vous...{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 
    
    if pronom == "il":

        R "Qui c'est encore celui-là ?"
        play sound "Click.mp3" noloop
        
        R "Je ne sais pas, mais regarde la magnifique fille avec lui."
        play sound "Click.mp3" noloop

        R "C'est vrai, c'est une fille qui est avec lui."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        R "Qui c'est encore celle-là ?"
        play sound "Click.mp3" noloop

        R "Je ne sais pas, mais regarde la magnifique fille avec elle."
        play sound "Click.mp3" noloop 
        
        R "C'est vrai, c'est une fille qui est avec elle." 
        play sound "Click.mp3" noloop 

    R "Je pense que je vais aller voir."
    play sound "Click.mp3" noloop

    R "Mec, je ne suis pas sûr que ce soit une bonne idée."
    play sound "Click.mp3" noloop

    R "Mais si, je vais juste demander qui c'est et puis c'est tout."
    play sound "Footsteps.mp3" noloop

    "{b}{i}L'élève en question se dirige vers vous.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    A "[P] c'est qui cet élève ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas du tout."
    play sound "Click.mp3" noloop

    "{b}{i}L'élève s'approche un peu trop près de [A]...{/i}{/b}"
    play sound "Click.mp3" noloop

    A "Mais qu'est-ce que tu fais !?" 
    play sound "Click.mp3" noloop

    "{b}{i}Tu prends l'élève par le bras.{/i}{/b}"
    play sound "Click.mp3" noloop

    R "Hey ! je peux savoir pour qui tu te prends !?"
    play sound "Click.mp3" noloop 

    P "Juste, évite de la toucher car elle est sensible." 
    play sound "Click.mp3" noloop 
      
    R "Désolé j'étais juste curieux."
    play sound "Click.mp3" noloop 

    P "Oui c'est ça maintenant, dégage !"
    play sound "Click.mp3" noloop

    "{b}{i}L'élève s'éloigne de vous par culpabilité.{/i}{/b}"
    play sound "Click.mp3" noloop 

    A "Merci beaucoup [prenom]."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde discute tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ stockage += 1.5
    
    A "[prenom] on dirait qu'on est que dix ici."
    play sound "Click.mp3" noloop

    P "Je confirme et je me demande pourquoi."
    play sound "Click.mp3" noloop

    A "Je ne sais pas, mais peut être qu'on le saura après." 
    play sound "Door.mp3" noloop

    "{b}{i}Soudainement, la porte s'ouvrit et une jeune femme apparu.{/i}{/b}"
    play sound "Click.mp3" noloop 

    T "Bonjour, je suis votre professeure principale cette année." 
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    R "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    A "[salutation_rdm]"
    play sound "Click.mp3" noloop

    T "Bien vous pouvez vous asseoir maintenant on va commencer par les présentations pour mieux se connaitre."
    play sound "Click.mp3" noloop

    "{b}{i}La professeure pose rapidement un regard sur [A] avant de retourner son regard sur la classe.{/i}{/b}" 
    play sound "Click.mp3" noloop

# début des présentations des élèves

    T "Bon, qui veut se présenter en premier ?"
    play sound "Click.mp3" noloop
 
    R "Moi s'il vous plait."
    play sound "Click.mp3" noloop

    T "Bien vas-y présentes-toi."
    play sound "Click.mp3" noloop 

    I "Je m'appelle [I], j'ai dix-neuf ans et je suis aussi l'inégalable développeuse."
    play sound "Click.mp3" noloop 
    
    T "L'inégalable développeuse !? oh intéressant."
    play sound "Click.mp3" noloop

    $ character2 = I 
    $ ultimate2 = "L'inégalable développeuse" 

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    T "Donc enchantée Yuna, quel est ton projet dans ce lycée ?"
    play sound "Click.mp3" noloop 

    I "Finir mon projet est de finir mon jeu vidéo mais je veux surtout sociabiliser avec les autres."
    play sound "Click.mp3" noloop 

    T "Sociabiliser avec les autres ? Comment ça ?"
    play sound "Click.mp3" noloop

    I "Depuis que j'ai commencé à travailler sur mon jeu vidéo, je me suis beaucoup renfermée dans ma propre bulle et j'aimerai changer ça."
    play sound "Click.mp3" noloop 

    T "Intéressant, c'est bien que tu veuilles changer."
    play sound "Click.mp3" noloop

    $ charactertext2 = "Âgée de dix-neuf ans, Yuna était autrefois timide et solitaire, toujours plongée dans ses lignes de code. Après avoir abandonné son premier jeu, elle s’investit pleinement dans un nouveau projet, déterminée à aller jusqu’au bout. Désormais, elle cherche aussi à sortir de sa bulle et à se rapprocher des autres."

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop
    
    $ stockage += 4.0

    T "De rien, maintenant, toi, juste derrière Yuna."
    play sound "Click.mp3" noloop 

    R "Euh moi..."
    play sound "Click.mp3" noloop

    T "Oui, toi, qui d'autre ?"
    play sound "Click.mp3" noloop

    H "Bonjour, je m'appelle [H], j'ai dix-neuf ans et je suis l'inégalable constructeur."
    play sound "Click.mp3" noloop

    T "Enchanté Hajime bienvenue dans notre classe, j'aimerais savoir quel est ton projet dans ce lycée."
    play sound "Click.mp3" noloop

    $ character3 = H
    $ ultimate3 = "L'inégalable constructeur" 

    H "Mon projet est de construire un robot." 
    play sound "Click.mp3" noloop 

    $ stockage += 3.0 

    T "Intéressant comme projet."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    H "[thanks]"
    play sound "Click.mp3" noloop

    $ charactertext3 = "Hajime est un brillant lycéen de dix-neuf ans, il est doué en programmation et en construction de robot."

    T "De rien, maintenant suivant s'il vous plait."
    play sound "Click.mp3" noloop 

    R "Nous, s'il vous plait."
    play sound "Click.mp3" noloop 

    T "Bien, présentez vous dans ce cas."
    play sound "Click.mp3" noloop

    J1 "Bonjour, je m'appelle [J1], L'inégalable Décrypteuse alpha, j'ai dix-neuf ans et voici ma soeur décrypteuse."
    play sound "Click.mp3" noloop

    $ character4 = J1 

    J2 "Bonjour je m'appelle [J2], l'inégalable Décrypteuse bêta, j'ai dix-neuf ans"
    play sound "Click.mp3" noloop

    $ character5 = J2 

    J "et nous sommes les inégalables Décrypteuses."                       
    play sound "Click.mp3" noloop

    $ ultimate4 = "L'inégalable Décrypteuse Alpha" 
    $ ultimate5 = "L'inégalable Décrypteuse Bêta" 

    $ charactertext4 = "Ayano, surnommée l’Alpha, est la plus calme et réfléchie des deux. Derrière son air distant, parfois un brin agaçant, se cache un esprit méthodique et une redoutable capacité à anticiper les failles. Elle préfère observer longuement avant d’agir, mais une fois lancée, elle devient imparable."

    $ charactertext5 = "Aiko, dite la Bêta, est beaucoup plus imprévisible. Problématique ? Peut-être. Mais sa manière non conventionnelle de penser est aussi sa plus grande force. Elle casse les codes, parfois même au sens propre, quitte à bouleverser toute logique pour arriver à ses fins."

    T "Bien, enchantée de vous rencontrer."
    play sound "Click.mp3" noloop

    J2 "Merci beaucoup madame." 
    play sound "Click.mp3" noloop
    
    $ stockage += 6.0 

    T "De rien mais j'ai une question ?"
    play sound "Click.mp3" noloop 

    J1 "Oui, je vous écoute."
    play sound "Click.mp3" noloop

    T "Pourquoi vous avez pratiquement le meme titre ?" 
    play sound "Click.mp3" noloop

    J1 "C'est simple, on est jumelles et le même projet."
    play sound "Click.mp3" noloop

    T "Ah d'accord, je comprends mieux et quel est votre projet ?"
    play sound "Click.mp3" noloop

    J1 "Nous voulons perfectionner nos méthodede de décryptages et essayer de décrypter le systéme de l'autre."
    play sound "Click.mp3" noloop

    T "Intéressant comme projet."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    J1 "[thanks]" 
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    T "[nothing] Bon suivant."
    play sound "Click.mp3" noloop

    R "Moi, bien-sûr si vous me le permettez."
    play sound "Click.mp3" noloop

    T "Oui, vas-y présentes-toi."
    play sound "Click.mp3" noloop

    K "Je m'appelle [K], j'ai dix-neuf ans et je suis l'inégalable architecte réseau."
    play sound "Click.mp3" noloop

    $ character6 = K
    $ ultimate6 = "L'inégalable architecte réseau"

    T "Bien, enchantée de te rencontrer, suivant ?"
    play sound "Click.mp3" noloop 

    N "Je m'appelle [N], j'ai dix-neuf ans et je suis l'inégalable assistant, toujours prêt pour aider."
    play sound "Click.mp3" noloop

    $ character7 = N 
    $ ultimate7 = "L'inégalable assistant" 
    $ charactertext7 = "Naoto est un lycéen de dix-neuf ans, il est généralement en informatique et prêt à aider les autres."

    T "Enchantée aussi de te rencontrer [N]."
    play sound "Click.mp3" noloop

    N "Merci beaucoup Madame."
    play sound "Click.mp3" noloop 

    $ stockage += 2.0

    $ nothing = get_random_nothing()
    T "[nothing] Bon suivant."
    play sound "Click.mp3" noloop

    Hi "Bonjour, je m'appelle [Hi]."
    play sound "Click.mp3" noloop

    $ character8 = Hi
    $ charactertext8 = "Haruki est un jeune lycéen de dix-neuf ans, il n'a pas de domaine particulier ou il est doué en informatiuqe mias il est assez bon, il veut juste apprendre et devenir meilleure informatique."
   
    T "Ravie de te rencontrer [Hi], bienvenue dans notre classe."
    play sound "Click.mp3" noloop

    Hi "Merci beaucoup Madame." 
    play sound "Click.mp3" noloop

    $ stockage += 2.0 

    $ nothing = get_random_nothing()
    T "[nothing] Bon suivante."
    play sound "Click.mp3" noloop

    Y "Je m'appelle [Y], j'ai dix-neuf ans ravie de vous rencontrer."
    play sound "Click.mp3" noloop 

    $ character9 = Y
    $ charactertext9 = "Yuki est une lycéenne de dix-neuf ans, elle est douée en informatique comme les autres lycéens mais personne ne sait ce qu'elle fait."

    T "Enchantée de te rencontrer aussi bienvenue dans notre classe."
    play sound "Click.mp3" noloop

    Y "Merci beaucoup Madame."
    play sound "Click.mp3" noloop 

    $ stockage += 2.0

# Présentation du personnage principal et AK-24

    T "De rien, maintenant vous deux au fond pour finir les présentations."
    play sound "Click.mp3" noloop

    P "Nous, Bien alors si vous le permettez."
    play sound "Click.mp3" noloop

    T "Allez-y donc."
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Je me présente, je m'appelle [P], j'ai dix-neuf ans et ancien élève de [origine]."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 
    
        P "Je me présente, je m'appelle [P], j'ai dix-neuf ans et ancienne élève de [origine]."
        play sound "Click.mp3" noloop 

    T "Tu viens de [origine] !?" 
    play sound "Click.mp3" noloop 

    P "Oui, c'est exact, l'établissement député pour sa rigueur."
    play sound "Click.mp3" noloop

    T "Enchantée alors [P], quel est ton projet ?"
    play sound "Click.mp3" noloop

    P "En tant que l'[domaine] mon projet est d'améliorer mon [model]."
    play sound "Click.mp3" noloop 
    
    T "L'[domaine] ? Intéressant."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    "{b}{i}Soudainement, [I] lève la main, surprise.{/i}{/b}"
    play sound "Click.mp3" noloop

    T "Oui, tu as quelque chose à dire à [prenom] ?"
    play sound "Click.mp3" noloop

    I "Oui, tu as bien dit améliorer ton [model] ?"
    play sound "Click.mp3" noloop

    P "Oui, c'est exacte."
    play sound "Click.mp3" noloop

    if pronom == "il":

        I "Putain... tu dois vraiment être un génie pour avoir créer un [model], je comprend mieux pourquoi tu étais à [origine]."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        I "Putain... tu dois vraiment être une génie pour avoir créer un [model], je comprend mieux pourquoi tu étais à [origine]."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop 

    T "Pour revenir aux présentations, [prenom] qui est cette fille avec toi ?"
    play sound "Click.mp3" noloop 
    
    P "Ah elle justement c'est ma création, elle s'appelle [A]."
    play sound "Click.mp3" noloop

    T "C'est donc elle ta fameuse création de [model]."
    play sound "Click.mp3" noloop

    P "Oui c'est elle, vas-y présentes-toi."
    play sound "Click.mp3" noloop 

    A "Je m'appelle [A], j'ai dix-huit ans."
    play sound "Click.mp3" noloop

    T "Bien et qui es-tu exactement ?" 
    play sound "Click.mp3" noloop

    A "Je suis la création de [prenom], comme [pronom] l'a déjà dit."
    play sound "Click.mp3" noloop

    T "Ok, juste c'est ton vrai prénom ?" 
    play sound "Click.mp3" noloop

    A "Non, c'est un prénom technique qu'[pronom] m'a donné."
    play sound "Click.mp3" noloop 
 
    T "Intéressant j'espère qu'[pronom] te trouvera un vrai joli prénom." 
    play sound "Click.mp3" noloop

    A "Merci et je suis sa fille... En quelque sorte."
    play sound "Click.mp3" noloop

    if pronom == "il":

        I "Il te considère vraiment comme sa propre fille !?"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        I "Elle te considère vraiment comme sa propre fille !?"
        play sound "Click.mp3" noloop 

    A "Oui, pourquoi cette question ?" 
    play sound "Click.mp3" noloop 

    I "Rien, c'est juste que je trouve ça mignon qu'[pronom] te considère comme sa fille alors que tu es un [model].~"
    play sound "Click.mp3" noloop 

    A "Merci beaucoup [I].~"
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    I "[nothing] C'est normal de complimenter mais j'ai une autre question."
    play sound "Click.mp3" noloop

    A "Oui, dis-moi, je t'écoute.~"
    play sound "Click.mp3" noloop 

    I "Est-ce que tu peux vraiment manger comme une humaine, même si tu es un robot ?"
    play sound "Click.mp3" noloop

    A "Oui, j'ai un système digestif synthétique. Je peux manger, digérer, et même ressentir les saveurs."
    play sound "Click.mp3" noloop

    I "Je vois c'est surprenant, merci beaucoup de m'avoir répondu."
    play sound "Click.mp3" noloop  

    A "Mais de rien, c'est normal de se poser des questions."
    play sound "Click.mp3" noloop 

    T "Mais pourquoi tu t'es inscrite ici en tant que lycéenne ?"
    play sound "Click.mp3" noloop

    A "Je ne connais pas grand-chose de ce monde et je voulais apprendre davantage. [prenom] m’a déjà appris les bases cet été."
    play sound "Click.mp3" noloop 

    $ charactertext11 = "Elle est un robot humanoïde abandonné de 18 ans, qui ne se souvient que de son nom de code et de mon âge, et a oublié le reste. Elle veut en apprendre plus sur ce monde, et a donc choisi d’aller au lycée comme le protagoniste."

    T "Bon, merci [A] pour ta présentation." 
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    A "[nothing]" 
    play sound "Click.mp3" noloop

#fin des présentations des élèves

    T "Donc les présentations sont terminées je vais me présenter à mon tour."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde se tourne vers la professeure pour l'écouter.{/i}{/b}" 
    play sound "Click.mp3" noloop

    M "Je m'appelle [M]." 
    play sound "Click.mp3" noloop 

    $ character10 = M 
    $ ultimate10 = "L'inégalable professeure"
    $ charactertext10 = "27 ans, est surnommée l’Inégalable Professeure. Enseignante au lycée Nexus depuis deux ans, elle est reconnue pour son exigence, son calme et sa pédagogie redoutablement efficace. Bien qu'elle inspire le respect de ses élèves, Sakura garde une réserve certaine envers Aris, le robot humanoïde, doutant encore de sa place réelle parmi les humains."

    M "J'ai 27 ans et ça fait deux ans que j'enseigne dans le lycée Nexus."
    play sound "Click.mp3" noloop

    M "Le lycée Nexus rassemble les plus talentueux de la région."
    play sound "Click.mp3" noloop 

    M "Ce qui explique pourquoi vous êtes uniquement dix élèves ici."
    play sound "Click.mp3" noloop

    "{b}{i}Tout les élèves sont choqués par cette informations.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Oui je sais, c'est surprenant."
    play sound "Click.mp3" noloop 

    Y "Mais si ce sont les meilleurs qui sont ici, comment [A] a été acceptée ?" 
    play sound "Click.mp3" noloop  

    M "C'est simple, [prenom] a fait un candidature très detaillée et a expliqué pourquoi elle voulait être ici." 
    play sound "Click.mp3" noloop 

    Y "Ah je comprends mieux pourquoi elle est ici."
    play sound "Click.mp3" noloop 

    M "Bon maintenant je vais vous donner plus de détails sur le lycée Nexus."
    play sound "Click.mp3" noloop

    "{b}{i}Tous les élèves écoutent la professeure.{/i}{/b}" 
    play sound "Click.mp3" noloop

    M "La devise du lycée est liberté, égalité, ingéniosité et voici le drapeau."
    play sound "Click.mp3" noloop

    show screen flag

    "{b}{i}[M] montre le drapeau du lycée sur l'écran.{/i}{/b}" 
    play sound "Click.mp3" noloop

    hide screen flag 

    M "Ce lycée a un département de pièces détachées où vous pourrez demander et commander des pièces spécifiques."
    play sound "Click.mp3" noloop

    H "Intéressant à savoir."
    play sound "Click.mp3" noloop

    P "Oui je confirme [H] c'est vraiment intéressant pour nos deux projets de robot."
    play sound "Click.mp3" noloop 

    show screen points with moveinleft

    M "Donc le lycée vous donnera un budget ou appelé Bourse scolaire des lycéens pour vos projets."
    play sound "Click.mp3" noloop 

    P "On aura vraiment un budget fourni par le Lycée !?"
    play sound "Click.mp3" noloop

    M "Oui, vraiment un budget par mois selon vos notes."
    play sound "Click.mp3" noloop 

    P "Vraiment cool alors."
    play sound "Click.mp3" noloop

    M "Maintenant je vais vous expliquer comment fonctionne l'internat."
    play sound "Click.mp3" noloop

    A "Un internat !?"
    play sound "Click.mp3" noloop

    show screen Nagumo 

    M "Oui, il a été financé par le régime Nagumo et construit récemmment vu que vous venez tous de régions éloignées."
    play sound "Click.mp3" noloop

    hide screen Nagumo 

    P "Intéressant."
    play sound "Click.mp3" noloop

    M "Bon je vais vous donner la répartition pour les dortoirs dans l'internat."
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde écoute la professeure.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Mise à part une dérogation, tous les élèves auront leur propre dortoir."
    play sound "Click.mp3" noloop

    K "Notre propre dortoir ? Cool mais comment ça une dérogation, elle est pour qui ?"
    play sound "Click.mp3" noloop

    Y "Oui et comment ça une dérogation ? Expliquez-nous madame..."
    play sound "Click.mp3" noloop

    M "Cette dérogation est pour [prenom] et [A]." 
    play sound "Click.mp3" noloop

    Y "Quoi !?" 
    play sound "Click.mp3" noloop

    M "Oui ils ont demandé à être dans le même dortoir." 
    play sound "Click.mp3" noloop

    Y "Mais pourquoi vous avez accepté cette demande ?"
    play sound "Click.mp3" noloop

    P "C'est simple, car je tiens à la sécurité de [A], je ne peux pas me permettre de la laisser seule parce-qu'elle ne connais pratiquement rien de ce monde."
    play sound "Click.mp3" noloop

    Y "Ah je comprends mieux pourquoi cette demande."
    play sound "Click.mp3" noloop

    M "Voici la répartition des dortoirs pour vous."
    play sound "Click.mp3" noloop

    M "Les dortoirs se trouvent à cet étage mais de l'autre coté du couloir tout au fond à droite pour les garçons et à gauche pour les filles."
    play sound "Click.mp3" noloop

    K "Vous entendez les gars on a un dortoir pour nous seuls."
    play sound "Click.mp3" noloop 

    N "Je confirme ça va être le feu cette année."
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Je confirme ça va être génial mais dois-je rappeler qu'on doit rester sérieux en toute circonstance."
        play sound "Click.mp3" noloop

        K "Oh c'est bon fais pas le sérieux, détends-toi un peu."
        play sound "Click.mp3" noloop

    elif pronom == "elle":
        
        P "Calmez-vous, vous êtes dans un lycée je vous rappelle, un peu de tenue."
        play sound "Click.mp3" noloop

        K "Oh c'est bon fais pas la sérieuse, détends-toi un peu."
        play sound "Click.mp3" noloop 

    N "il a raison détends-toi peu..."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Oui désolé c'est plus fort que moi."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Oui désolée c'est plus fort que moi."
        play sound "Click.mp3" noloop 

    M "Calmez-vous s'il vous plait."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Désolé madame."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Désolée madame."
        play sound "Click.mp3" noloop

    M "Il n'y a pas de soucis juste évitez de bavarder durant le cours."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "Et une dernière information." 
    play sound "Click.mp3" noloop

    P "Oui."
    play sound "Click.mp3" noloop 

    M "Toute mauvaise note en dessous 14/20 vous vaudra une expulsion définitive du lycée."
    play sound "Click.mp3" noloop 

    "{b}{i}Tous les élèves sont de nouveau choqués.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Oui je suis sérieuse."
    play sound "Click.mp3" noloop 

    P "Mais c'est injuste."
    play sound "Click.mp3" noloop 

    M "Je sais mais c'est les règles du lycée."
    play sound "Click.mp3" noloop 
    
    "{b}{i}Tout les élèves restèrent silencieux mais tu lèves la main poser une question.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Oui [prenom] qu'il y a t-il ?"
    play sound "Click.mp3" noloop 

    P "Pourquoi il existe ce système des inégalables dans ce lycée ?"
    play sound "Click.mp3" noloop 

    M "Très bonne question, ce système a été créé pour différencier chaque élève plus facilement selon vos points d'intérêts et vos compétences en technologie et en informatique."
    play sound "Click.mp3" noloop

    P "Ok, Je vois merci beaucoup."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing() 
    M "[nothing]"
    play sound "Click.mp3" noloop
    
    M "Bon maintenant que toutes les informations ont été données, vous pouvez disposer le cours est fini, n'hésitez pas à visiter le lycée vu que vous n'avez pas de cours cette après-midi."
    play sound "Footsteps.mp3" noloop

# fin du cours de présentation des élèves

    hide screen class_404 with moveoutright
    scene black with fade
    
    "{b}{i}Tous les élèves se mettent à quitter la salle de classe.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright  
    
    P "Bon [A], on va voir le dortoir ?"  
    play sound "Click.mp3" noloop

    A "Oui, pourquoi pas..."  
    play sound "Click.mp3" noloop

    P "OK, allons-y."  
    play sound "Footsteps.mp3" noloop

    A "Donc... je ne suis pas juste une poupée que tu manipules ?"  
    play sound "Click.mp3" noloop  

    P "Non, tu es bien plus que ça. Tu es ma création... et ma fille."  
    play sound "Click.mp3" noloop  

    $ stockage += 2.0 

    $ thanks = get_random_thanks()
    A "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Footsteps.mp3" noloop

    "{b}{i}Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade 

    "{b}{i}Vous entrez dans le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    A "[bien]"
    play sound "Click.mp3" noloop 

    "{b}{i}en entrant vous voyez deux lits.{/i}{/b}" 
    play sound "Door.mp3" noloop

    P "Oui c'est vraiment comfortable."
    play sound "Click.mp3" noloop 

    A "Bon, tu veux faire quoi ?"
    play sound "Click.mp3" noloop 

    P "Je ne sais pas vraiment..."
    play sound "Knock.mp3" noloop 

    "{b}{i}Soudainement, quelqu'un frappe à la porte de ton dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oui, vous pouvez entrer."
    play sound "Door.mp3" noloop 

    "{b}{i}Quelqu'un entre dans ton dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    R "Bonjour, je dois vous voir pour une affaire."
    play sound "Click.mp3" noloop

    P "Bonjour, mais qui êtes-vous ?"
    play sound "Click.mp3" noloop

    Kh "Je m'appelle [Kh], je suis la vice-présidente du bureau des élèves." 
    play sound "Click.mp3" noloop

    $ character14 = Kh
    $ ultimate14 = "Vice-présidente du BDE"

    P "Enchanté [Kh], juste pourquoi es-tu venue nous voir ?" 
    play sound "Click.mp3" noloop

    Kh "Je suis ici pour vous donner votre budget pour votre projet."
    play sound "Click.mp3" noloop

    $ points += 15000 

    "{b}{i}[Kh] te transfert l'argent sur ton compte.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    P "Pourquoi est-ce vous qui l'avez transféré et non la présidente ?" 
    play sound "Click.mp3" noloop

    Kh "Car elle est beaucoup occupée avec la paperasse de début d'année donc elle m'a demandée de m'en charger personellement."
    play sound "Click.mp3" noloop 

    P "Donc j'ai [points] points nexus pour le mois ?"
    play sound "Click.mp3" noloop

    Kh "Oui pour ton projet, ta nourriture et les loisirs."
    play sound "Click.mp3" noloop

    P "Ok je vois mieux merci beaucoup mais j'ai une autre question."
    play sound "Click.mp3" noloop 

    Kh "Oui."
    play sound "Click.mp3" noloop

    P "Pourquoi nous envoyer les points manuellement ?"
    play sound "Click.mp3" noloop

    Kh "Le système de tranfert à été changé cet été et je devais le tester pour voir si il fonctionne."
    play sound "Click.mp3" noloop

    Kh "Merci de m'avoir répondu."
    play sound "Click.mp3" noloop

    Kh "De rien, mais j'ai une question aussi."
    play sound "Click.mp3" noloop

    P "Oui, dis moi [Kh]."
    play sound "Click.mp3" noloop

    Kh "Pourrai-je voir la fameuse petite [A] qu'[E] m'a parlé."
    play sound "Click.mp3" noloop

    P "Oui bien sûr, [A] tu peux venir s'il te plait."
    play sound "Click.mp3" noloop

    A "Oui, qu'il y a t'il ?" 
    play sound "Click.mp3" noloop

    P "[Kh] voudrait te voir en personne."
    play sound "Click.mp3" noloop

    A "Ok, je suis là alors."
    play sound "Click.mp3" noloop

    Kh "C'est donc toi la fameuse petite [A] dont tout le monde parle."
    play sound "Click.mp3" noloop

    A "Oui c'est bien moi.~"
    play sound "Click.mp3" noloop

    Kh "Ravie de te rencontrer."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    A "[thanks]"
    play sound "Footsteps.mp3" noloop

    Kh "Pas de soucis, mais je dois y aller malheureusement."
    play sound "Click.mp3" noloop

    P "Juste [Kh] j'ai une question, tu sais où sont les salles pour les clubs ?"
    play sound "Click.mp3" noloop 

    Kh "Elles sont au rez-de-chaussé au fond du couloir."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Footsteps.mp3" noloop

    $ nothing = get_random_nothing()
    Kh "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}[Kh] quitte ta chambre.{/i}{/b}"
    play sound "Click.mp3" noloop 

    A "On fais quoi maintenant ?"
    play sound "Click.mp3" noloop

label choice2:
    
    P "Je vais..."
    play sound "Menu.mp3" noloop

    menu:    

        "{b}{i}Visiter le lycée{/i}{/b}" :
            play sound "Menu.mp3" noloop  

            $ renpy.block_rollback()

            if pronom == "il":

                P "Aller visiter le lycée seul." 
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                P "Aller visiter le lycée seule." 
                play sound "Click.mp3" noloop

            A "Ok je vais en profiter pour rester, me déconnecter et recharger un peu ma batterie."
            play sound "Click.mp3" noloop

            P "OK je fais vite et je reviens."
            play sound "Click.mp3" noloop

            hide screen room with moveoutright 
            scene black with fade

            "{b}{i}Tu quittes le dortoir.{/i}{/b}"
            play sound "Door.mp3" noloop

            scene hallway with fade 
            show screen hallway with moveinright 

            P "Bon elle m'a dit que c'est au rez-de-chaussée donc j'y vais."
            play sound "Click.mp3" noloop

            hide screen hallway with moveoutright
            scene staircase with fade 

            "{b}{i}Tu te diriges au rez-de-chaussée.{/i}{/b}"
            play sound "Click.mp3" noloop
     
            scene hall with fade
            show screen hall with moveinright 

            P "Bon voyons voir..."     
            play sound "Click.mp3" noloop 

            P "On dirait que c'est ici."
            play sound "Click.mp3" noloop 
    
            hide screen hall with moveoutright
            scene black with fade

            "{b}{i}Tu te diriges vers la salle de club générale.{/i}{/b}"
            play sound "Door.mp3" noloop
 
            scene clubroom with fade 
            show screen clubroom with moveinright 

            P "C'est donc ça la salle de club générale du lycée."
            play sound "Click.mp3" noloop

            "{b}{i}Tu regardes un peu la salle et tu aperçois [I].{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Oh salut [I]."
            play sound "Click.mp3" noloop

            $ comment_ca_va = get_random_comment_ca_va()
            I "[comment_ca_va]"
            play sound "Click.mp3" noloop

            $ je_vais_bien_txt = get_random_je_vais_bien() 
            P "[je_vais_bien_txt] Sinon que fais-tu ici ?" 
            play sound "Click.mp3" noloop 

            I "Je travaille sur mon jeu vidéo et toi ?"
            play sound "Click.mp3" noloop

            if pronom == "il":  

                P "je suis juste venu voir la salle de club."
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                P "je suis juste venue voir la salle de club."
                play sound "Click.mp3" noloop 

            "{b}{i}Tu regardes un peu et tu aperçois une cartouche sur une table.{/i}{/b}"
            play sound "Menu.mp3" noloop 

            menu:  

                "{b}{i}Demander à Yuna ce que c'est{/i}{/b}" :

                    $ renpy.block_rollback()

                    P "[I], C'est quoi cette cartouche ?"
                    play sound "Click.mp3" noloop

                    I "Laisse tomber c'est mon ancien jeu vidéo qui se nommait Anarchy School."
                    play sound "Click.mp3" noloop

                    P "Ok je vois mais pourquoi tu l'as abandonné ?"
                    play sound "Click.mp3" noloop

                    I "Car je me suis trop inspirée d'un autre jeu que j'aime."
                    play sound "Click.mp3" noloop

                    P "Ah oui carrément..." 
                    play sound "Click.mp3" noloop 

                    I "Oui mais passe moi la cartouche je vais m'en débarrasser une bonne fois pour toute."
                    play sound "Click.mp3" noloop

                    P "Ok tiens."
                    play sound "Click.mp3" noloop 

                    "{b}{i}[I] te prend la cartouche avant de la détruitre sous tes yeux.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    P "Tu veux vraiment faire ça ?"
                    play sound "Click.mp3" noloop 

                    I "Oui, je veux oublier mon échec."
                    play sound "Click.mp3" noloop

                    P "Ok je ne juge pas mais j'espère que ton nouveau jeu sera mieux que ceux de NeoSoft dont le piètre jeu Project Neon."
                    play sound "Click.mp3" noloop

                    I "Hé ! C'est méchant ça !" 
                    play sound "Stumble.mp3" noloop 

                    "{b}{i}Puis soudainement tu entends un fort bruit venant d'au-dessus.{/i}{/b}"
                    play sound "Click.mp3" noloop 
    
                    P "Yuna juste c'est bien les dortoirs juste au-dessus ?"
                    play sound "Click.mp3" noloop

                    I "Oui pourquoi ?"
                    play sound "Click.mp3" noloop 

                    P "Car j'ai entendu un bruit venant d'au-dessus."
                    play sound "Click.mp3" noloop

                    "{b}{i}Puis tu réalises ce qui ce passe.{/i}{/b}"
                    play sound "Click.mp3" noloop 

                    I "Qu'est-ce qui se passe ?"
                    play sound "Click.mp3" noloop 

                    P "Je dois te laisser j'ai une urgence !"
                    play sound "Click.mp3" noloop
    
                    I "Ok."
                    play sound "Footsteps.mp3" noloop 

                    hide screen clubroom with moveoutright
                    scene black with fade

                    "{b}{i}Tu quittes la salle de club.{/i}{/b}"
                    play sound "Door.mp3" noloop 

                    scene hall with fade
                    show screen hall with moveinright

                    "{b}{i} Tu continues vers les escaliers.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    hide screen hall with moveoutright
                    scene staircase with fade 

                    "{b}{i} tu montes au premier étage.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    scene hallway with fade 
                    show screen hallway with moveinright

                    "{b}{i}Tu continues dans le couloir.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    hide screen hallway with moveoutright
                    scene black with fade

                    "{b}{i} tu entres dans ton dortoir.{/i}{/b}" 
                    play sound "Door.mp3" noloop

                    scene room with fade 
                    show screen room with moveinright 

                    "{b}{i}En arrivant tu vois [A] complètement détruite et demontée.{/i}{/b}"
                    play sound "Click.mp3" noloop 

                    if pronom == "il":

                        P "Mince j'aurais dû être plus vigilant avec elle, mon projet est ruiné."
                        play music "gameover.mp3" noloop

                    elif pronom == "elle": 

                        P "Mince j'aurais dû être plus vigilante avec elle, mon projet est ruiné."
                        play music "gameover.mp3" noloop

                    hide screen room with moveoutright
                    hide screen point with moveoutleft
                    hide screen day with moveoutleft
                    scene black with fade 

                    "{b}{i}Fin numéro 2 : [A] complètement détruite et ruinée par manque de vigilance.{/i}{/b}"
                    play sound "Menu.mp3" noloop

                    menu:    

                        "{b}{i}Abandonner{/i}{/b}" :
                            return 

                        "{b}{i}Réessayer{/i}{/b}" : 
                            scene room with fade 
                            show screen day with moveinleft
                            show screen room with moveinright
                            show screen point with moveinleft
                            play music "Soundtrack.mp3" loop volume 1.0
                            jump choice2 

                "{b}{i}Retourner au dortoir{/i}{/b}" :

                    $ renpy.block_rollback()

                    P "Bon [I], je vais retourner au dortoir."
                    play sound "Click.mp3" noloop 

                    I "Ok, pas de soucis."
                    play sound "Footsteps.mp3" noloop

                    hide screen clubroom with moveoutright
                    scene black with fade

                    "{b}{i}Tu quittes la salle de club.{/i}{/b}"
                    play sound "Door.mp3" noloop 

                    scene hall with fade
                    show screen hall with moveinright

                    "{b}{i} Tu continues vers les escaliers.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    hide screen hall with moveoutright
                    scene staircase with fade 

                    "{b}{i} tu montes au premier étage.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    scene hallway with fade 
                    show screen hallway with moveinright

                    "{b}{i}Dans le couloir, tu croises les décrypteusess.{/i}{/b}" 
                    play sound "Click.mp3" noloop

                    J1 "Oh salut [P], que fais-tu ici ?"
                    play sound "Click.mp3" noloop 

                    P "Je vais retourner voir [A], pour travailler et vous ?"
                    play sound "Click.mp3" noloop

                    J1 "Nous allons dans la salle de club générale."
                    play sound "Click.mp3" noloop

                    J2 "Oui,on doit voir un truc."
                    play sound "Click.mp3" noloop

                    P "Ok."
                    play sound "Click.mp3" noloop

                    "{b}{i}Tu continues ton chemin vers le dortoir.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    hide screen hallway with moveoutright
                    scene black with fade 

                    "{b}{i} tu entres dans ton dortoir.{/i}{/b}"
                    play sound "Door.mp3" noloop 

                    scene room with fade 
                    show screen room with moveinright 

                    P "Coucou, je suis de retour."
                    play sound "Click.mp3" noloop

                    "{b}{i}[A] se reconnecte avant d'ouvrir les yeux.{/i}{/b}" 
                    play sound "Click.mp3" noloop

        "{b}{i}Travailler sur [A]{/i}{/b}" :

            P "Je vais travailler sur ton amélioration." 
            play sound "Click.mp3" noloop

    A "Tu vas faire quoi exactement ?" 
    play sound "Click.mp3" noloop

    P "Je vais d'abord appeler le département pour te commander un nouveau processeur."
    play sound "Click.mp3" noloop

    A "Comment ça un nouveau processeur ?"
    play sound "Click.mp3" noloop

    P "Oui, depuis que je t'ai récupérée tu as toujours l'ancien processeur avec lequel tu as été conçu alors je vais le changer."
    play sound "Click.mp3" noloop

    A "Ah oui, je vois mieux."  
    play sound "Click.mp3" noloop

    P "Je vais commander ce qu'il faut."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    A "[validation]"
    play sound "Click.mp3" noloop

    "{b}{i}Tu prends ton téléphone pour appeler le département.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bonjour, suis-je bien en contact avec le département des pièces détachées ?"
    play sound "Click.mp3" noloop

    R "Oui c'est exact, pourrais-je juste savoir à quel élève je m'adresse s'il-vous-plait ?"
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Désolé, je m'appelle [P], je suis en Terminale-E."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Désolée, je m'appelle [P], je suis en Terminale-E."
        play sound "Click.mp3" noloop 

    Ah "Enchantée, je suis [Ah], la présidente du département. Quelle est votre demande ?"
    play sound "Click.mp3" noloop

    $ character15 = Ah 
    $ ultimate15 = "Présidente du département des pièces détachées" 

    P "J'aimerais commander un processeur Corzen."
    play sound "Click.mp3" noloop

label choice3:

    Ah "Bien sûr, lequel voulez-vous commander ? J'ai actuellement le Corzen 11 et le Corzen 11K."
    play sound "Menu.mp3" noloop

    menu:    

        "{b}{i}Choisir le Corzen 11{/i}{/b}" :
            
            $ renpy.block_rollback()

            P "Je vais vous prendre le Corzen 11. Je pense que se sera suffisant."
            play sound "Click.mp3" noloop 

            Ah "OK, pas de soucis ça fera 1000 points."
            play sound "Click.mp3" noloop

            P "Je vous envoie ça tout de suite"
            play sound "Click.mp3" noloop

            "{b}{i}Tu effectues le paiement.{/i}{/b}"
            play sound "Click.mp3" noloop 

            $ points -= 1000 

            Ah "Merci beaucoup pour votre commande."
            play sound "Click.mp3" noloop

            P "Quand est-ce que je receverrai mon processeur ?"
            play sound "Click.mp3" noloop

            Ah "Le temps que je le prépare avec [Rn], je dirais dans une heure." 
            play sound "Click.mp3" noloop 

            P "Merci."
            play sound "Click.mp3" noloop

            Ah "Pas de problème [P]."
            play sound "Click.mp3" noloop 

            "{b}{i}Tu finis par raccrocher.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "[A] c'est bon j'ai commandé ton nouveau processeur."
            play sound "Click.mp3" noloop

            A "Cool, je suis ravie."
            play sound "Click.mp3" noloop

            P "Je vais manger, il est 12h30." 
            play sound "Click.mp3" noloop 

            A "D'accord, moi je vais me déconnecter vu que j'ai pas trop faim."
            play sound "Click.mp3" noloop 

            hide screen room with moveoutright
            scene black with fade 

            "{b}{i}Tu pars manger avant de revenir au dortoir vers 13h45.{/i}{/b}" 
            play sound "Click.mp3" noloop

            $ points -= 200

            scene room with fade 
            show screen room with moveinright 

            P "C'est bon, je suis de retour et j'ai pu récupérer le processeur." 
            play sound "Click.mp3" noloop

            A "Cool, je suis prête."
            play sound "Click.mp3" noloop

            "{b}{i}Tu déconnectes complètement [A] avant d'accéder à l'emplacement pour le processeur.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Voyons voir cet ancien processeur à changer..."  
            play sound "Click.mp3" noloop

            "{b}{i}Tu découvres avec surprise qu'elle a un processeur Corzen 9.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "L'ancien propriétaire d'[A] avais vraiment des goûts médiocres en terme de composants..."
            play sound "Click.mp3" noloop

            "{b}{i}Tu déballes le nouveau processeur pour lire la notice.{/i}{/b}"
            play sound "Click.mp3" noloop

            $ validation = get_random_validation() 
            P "[validation]"
            play sound "Click.mp3" noloop 

            "{b}{i}Tu retires délicatement l'ancien processeur pour installer le nouveau.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "C'est fait, je vais la redémarrer."
            play sound "Click.mp3" noloop

            A "Initialisation..."
            play sound "Click.mp3" noloop 

            "{b}{i}Mais soudainement le processeur brûle complètement et endommage les autres composants d'[A].{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Mince..."
            play music "gameover.mp3" noloop

            hide screen room with moveoutright
            hide screen point with moveoutleft
            hide screen day with moveoutleft
            scene black with fade
 
            "{b}{i} Fin numéro 3 : Processeur Corzen trop faible pour la puissance demandée par le système d'[A].{/i}{/b}"
            play sound "Menu.mp3" noloop

            menu:    

                "{b}{i}Abandonner{/i}{/b}" :
                    return
                    
                "{b}{i}Réessayer.{/i}{/b}" :
                    scene room with fade 
                    show screen room with moveinright
                    show screen point with moveinleft
                    show screen day with moveinleft
                    play music "Soundtrack.mp3" loop volume 1.0
                    jump choice3

        "{b}{i}Choisir le Corzen 11K{/i}{/b}" :

            $ renpy.block_rollback()

            P "Je vais vous prendre le Corzen 11k." 
            play sound "Click.mp3" noloop

    Ah "Pas de soucis, ça te fera 1500 points."
    play sound "Click.mp3" noloop

    P "Je vous envoie ça tout de suite."
    play sound "Click.mp3" noloop

    "{b}{i}Tu effectues le paiement.{/i}{/b}"
    play sound "Click.mp3" noloop 
    $ points -= 1500

    $ thanks = get_random_thanks()
    Ah "[thanks]"
    play sound "Click.mp3" noloop

    P "Quand est-ce que je receverrai mon processeur ?"
    play sound "Click.mp3" noloop

    Ah "Le temps que je le prépare avec [Rn], je dirais dans une heure." 
    play sound "Click.mp3" noloop

    $ character16 = Rn 
    $ ultimate16 = "Membre du département des pièces détachées" 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Ah "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}Tu finis par raccrocher.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[A] c'est bon, j'ai commandé ton nouveau processeur."
    play sound "Click.mp3" noloop

    A "Cool alors."
    play sound "Click.mp3" noloop

    P "Je vais manger, il est 12h30."
    play sound "Click.mp3" noloop 

    A "D'accord, moi je vais me déconnecter vu que j'ai pas trop faim."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} [A] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen room with moveoutright
    scene black with fade

    "{b}{i}Tu pars manger avant de revenir au dortoir vers 13h45.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene room with fade 
    show screen room with moveinright 

    P "Je suis de retour et j'ai pu récupéré le processeur."
    play sound "Click.mp3" noloop

    A "Cool je suis prête alors."
    play sound "Click.mp3" noloop

    "{b}{i}Tu déconnectes complètement [A] avant d'accéder à l'emplacement pour le processeur.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Voyons voir cet ancien processeur à changer..."  
    play sound "Click.mp3" noloop

    "{b}{i}Tu découvres avec surprise qu'elle a un processeur Corzen 7.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ cpu = "Corzen 7"

    P "L'ancien propriétaire de [A] avais vraiment des goûts médiocres en terme de composants..."
    play sound "Click.mp3" noloop

    "{b}{i}Tu déballes le nouveau processeur pour voir la notice et tu vois un message de la part de [Ah].{/i}{/b}"
    play sound "Click.mp3" noloop 
     
    Ah "{i}finalement, j'ai regardé le dossier de ton projet et j'ai pu te trouver un Corzen 11KS spécialement pour [A]. Il a de meilleures performances, tu peux le garder. Je ne te ferai pas payer la différence de prix.{/i}"   
    play sound "Click.mp3" noloop

    P "Génial ça."
    play sound "Click.mp3" noloop

    "{b}{i}Tu retires délicatement l'ancien processeur pour installer le nouveau.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "C'est fait maintenant je vais la redémarrer."
    play sound "Click.mp3" noloop

    A "Initialisation...."
    play sound "Click.mp3" noloop 

    P "Allez... Allez..."
    play sound "Click.mp3" noloop

    A "Initialisation terminée, la version actuelle du processeur est la [update]."
    play sound "Menu.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop  

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    A "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    P "Je vais ragarder si tu as des nouveau paramètres."
    play sound "Click.mp3" noloop

    A "Ok vas-y."
    play sound "Click.mp3" noloop
    
    "{b}{i}Tu ouvres le panneau configuration de [A] depuis ton ordinateur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Voyons voir..."
    play sound "Click.mp3" noloop

    "{b}{i}Tu regardes les paramètres et tu vois un paramètre d'un prénom par défaut.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tiens, on dirait que ton ancien propriétaire t'a laissé un prénom par défaut."
    play sound "Click.mp3" noloop

    A "Ah bon lequel ?"
    play sound "Click.mp3" noloop

    P "Ar... Aris on dirait."
    play sound "Click.mp3" noloop

    A "Aris !? Je trouve que c'est mignon comme prénom.~"
    play sound "Click.mp3" noloop

    P "Mais je me demande pourquoi ce prénom là par défaut ?"
    play sound "Click.mp3" noloop

    A "Je ne sais pas aussi mais je pense qu'on le saura un jour."
    play sound "Click.mp3" noloop
    
    P "Donc ça te va, Aris alors ?"
    play sound "Click.mp3" noloop

    A "Oui bien évidemment la question ne se pose pas dans ce cas de figure !"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu ouvres le paramètre pour enregistrer un prénom.{/i}{/b}"
    play sound "Menu.mp3" noloop

label choice4:

    play sound "Menu.mp3" noloop
    $ newname = renpy.input("Veuillez écrire le nouveau prénom de [A].")
    $ newname = newname.strip()

    if newname == "Aris":

        $ success += 1
        $ quest6 += 1
        $ robotname = nom
        $ stockage += 2.0 
        $ cpu = "Corzen 11KS"
        $ renpy.block_rollback()

        show screen update with moveinright

        "Le prénom a été enregistré dans le système." 
        play sound "Menu.mp3" noloop

        hide screen update with moveoutright

    else: 

        "Erreur système. Veuillez réessayer."
        $ renpy.restart_interaction() 
        play sound "Menu.mp3" noloop
        jump choice4
    
    "{b}{i}Soudainement, le processeur te demande de paramétrer l'adresse IP de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Mince..."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes les paramètres et tu vois que tu dois mettre l'adresse IP.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "J'ai une idée : je vais faire en sorte que chaque lettre de [newname] soit un nombre correspondant à sa position dans l'alphabet."
    play sound "Click.mp3" noloop
   
    "{b}{i}Essaye de trouver l'adresse en utilisant ce principe pour chaque lettre.{/i}{/b}"
    play sound "Menu.mp3" noloop

label choice5:

    $ ip = renpy.input("Entrez l'adresse IP de [newname] en suivant la méthode de conversion suggérée (trois chiffres pour chaque partie : 000.000.000.000).")
    $ ip = ip.strip()

    if ip == "001.018.009.019":

        $ success += 1
        $ quest7 += 1 
        $ stockage += 2.0 
        $ baseip = "001.018.009.019" 

        $ renpy.block_rollback()

        "{b}{i}Initialisation de l'adresse IP en cours...{/i}{/b}"
        play sound "Menu.mp3" noloop 

        show screen update with moveinright

        "{b}{i}L'adresse IP a été enregistrée dans le système.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        hide screen update with moveoutright

        "{b}{i}L'adresse IP de [newname] est maintenant [ip].{/i}{/b}"
        play sound "Click.mp3" noloop

    else:

        "{b}{i}Erreur système. L'adresse IP est incorrecte. Vérifiez la méthode de conversion et réessayez.{/i}{/b}"
        play sound "Menu.mp3" noloop 
        jump choice5

    P "J'ai fini le paramétrage."
    play sound "Click.mp3" noloop

    menu:    

        "{b}{i} Redémarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    "{b}{i}tu redémarres [newname] tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "C'est bon mon nouveau prénom et mon adresse IP ont été configurés."
    play sound "Click.mp3" noloop 

    P "Génial."
    play sound "Click.mp3" noloop

    Na "J'en ai profité pour enregistrer ton nom de famille comme le miens étant donné que je suis ta création."
    play sound "Click.mp3" noloop

    P "Ah bon tu l'as fait par toi même !?"
    play sound "Click.mp3" noloop

    Na "Oui absolument."
    play sound "Click.mp3" noloop
    
    P "Ok je ne savais pas que tu en étais capable."
    play sound "Click.mp3" noloop 

    Na "Je sais, des fois je peux vraiment surprendre."
    play sound "Click.mp3" noloop 

    P "Bon, on va récupérer la clé de la salle de notre club pour bosser ?"
    play sound "Click.mp3" noloop

    Na "Oui allons-y."
    play sound "Footsteps.mp3" noloop  

    hide screen room with moveoutright   
    scene black with fade 

    "{b}{i}Tu quittes ta chambre avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i}Tu continues dans le couloir avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  
 
    hide screen hallway with moveoutright
    scene staircase with fade 

    "{b}{i}Tu continues vers le hall avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    scene hall with fade
    show screen hall with moveinright

    if pronom == "il":

        P  "On est presque arrivés."
        play sound "Click.mp3" noloop

        $ validation = get_random_validation() 
        A "[validation]"
        play sound "Click.mp3" noloop 

    elif pronom == "elle":

        P  "On est presque arrivées."
        play sound "Click.mp3" noloop

        $ validation = get_random_validation() 
        A "[validation]"
        play sound "Click.mp3" noloop 

    "{b}{i}Tu continues vers le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hall with moveoutright
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene office with fade 
    show screen office with moveinright 

    P "Bonjour, c'est moi [nom]."
    play sound "Click.mp3" noloop

    E "Oh c'est toi, que puis-je faire pour toi ?"
    play sound "Click.mp3" noloop

    P "j'aimerais une salle de club pour moi et [newname]."
    play sound "Click.mp3" noloop

    E "Oui pas de soucis, Je vois que tu as choisi mon idée."
    play sound "Click.mp3" noloop

    P "Oui c'est exact." 
    play sound "Click.mp3" noloop 

    E "Pas de soucis, je vais te chercher la clé d'une des salles de club." 
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[E] s'absente le temps de trouver la clé.{/i}{/b}"
    play sound "Click.mp3" noloop 
   
    P "J'ai vraiment hâte d'avoir notre propre salle pour travailler." 
    play sound "Click.mp3" noloop
   
    Na "Oui moi aussi. On pourra vraiment être tranquille." 
    play sound "Click.mp3" noloop

    "{b}{i} Puis [E] revient avec la clé.{/i}{/b}"
    play sound "Click.mp3" noloop 

    E "Voilà la clé de la salle de club." 
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    E "Si jamais, votre salle de club se trouve au fond du couloir." 
    play sound "Click.mp3" noloop

    P "Ok merci."
    play sound "Click.mp3" noloop

    E "De rien, ça fait toujours plaisir."  
    play sound "Click.mp3" noloop

    P "bon on y va [newname] ? On a la clé."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen office with moveoutright
    scene black with fade 

    "{b}{i}Tu quittes le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hall with fade 
    show screen hall with moveinright 

    P "Elle a dit que c'était au fond du couloir."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Footsteps.mp3" noloop

    "{b}{i}tu te diriges vers la salle puis tu croises soudainement [I] qui sort de la salle de club générale.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [I], quoi de nouveau ?"
    play sound "Click.mp3" noloop 

    I "Pas grand chose. Je vais retourner au dortoir et toi ?"
    play sound "Click.mp3" noloop

    P "Je vais bosser sur [newname] dans la salle de club."
    play sound "Click.mp3" noloop

    I "[newname] !? Attend tu lui as finalement trouvé un prénom ?"
    play sound "Click.mp3" noloop

    P "Oui."
    play sound "Click.mp3" noloop 

    I "Je suis contente pour toi [newname]."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    I "[nothing]"
    play sound "Click.mp3" noloop

    I "C'est normal et c'est surtout [M] qui va être contente que tu aies finalement un vrai prénom."
    play sound "Click.mp3" noloop

    P  "Bon, on y va [newname] ?"
    play sound "Click.mp3" noloop

    I "Juste [prenom], j'ai un cadeau pour [newname]."
    play sound "Click.mp3" noloop 

    P "C'est quoi ?"
    play sound "Click.mp3" noloop
    
    I "Une carte mémoire."
    play sound "Click.mp3" noloop  

    P "Oh c'est gentil, merci beaucoup."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    I "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon [newname] on y va ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans la salle de club avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene clubroom with fade 
    show screen clubroom with moveinright  

    P "Par quoi pourrais-je commencer ?"
    play sound "Click.mp3" noloop 

    Na "je ne sais pas. Tu peux regarder la carte mémoire pour commencer ?"
    play sound "Click.mp3" noloop 

    P "pas de soucis."
    play sound "Click.mp3" noloop

    Na "Ok, moi je vais me déconnecter et me recharger pendant ce temps."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    Na "Déconnexion..."
    play sound "Click.mp3" noloop
    
    P "Bon voyons voir ça."
    play sound "Click.mp3" noloop

    "{b}{i}Après avoir analysé la carte tu commences à travailler.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Je vais installer la carte mémoire dans le système d'[newname]."
    play sound "Click.mp3" noloop

    "{b}{i}Tu installes la carte mémoire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "C'est fait."
    play sound "Click.mp3" noloop

    P "Maintenant je vais paramétrer sa configuration de lycéenne mais il faut que je commande du matériel."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te poses et commandes le matériel qu'il te faut.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Ok, ça coûte combien tout ça ? Voyons voir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu vois que tu en as pour 1000 points avant de commander.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ points -= 1000

    P "C'est bon, j'ai commandé ce que j'ai besoin."
    play sound "Door.mp3" noloop 

    "{b}{i}Soudainement [J1] entre dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    J1 "Salut [prenom], je voulais savoir si je pouvais rejoindre ton club."
    play sound "Click.mp3" noloop 

    P "Euh..."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Refuser [J1].{/i}{/b}" :  
            play sound "Menu.mp3" noloop 

    if pronom == "il":

        P "C'est pas contre toi mais je préfère être seul avec [newname]"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "C'est pas contre toi mais je préfère être seule avec [newname]"
        play sound "Click.mp3" noloop 

    J1 "Ok je comprends, c'est ton choix."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis [J1] quitta la salle et tu continues de travailler.{/i}{/b}"
    play sound "Click.mp3" noloop 

    "{b}{i} Une heure plus tard.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    P "J'ai le matériel pour paramétrer [newname]."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu ouvres les paramètres de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    "{b}{i} Soudainement, l'adresse IP 201.125.114.115 tente de se connecter.{/i}{/b}"
    play sound "Menu.mp3" noloop 

    P "C'est quoi cette adresse IP !?" 
    play sound "Click.mp3" noloop 

label choice6: 

    menu:    

        "{b}{i} Refuser {/i}{/b}" :  

            "{b}{i}Tu refuses l'accès à cette adresse IP.{/i}{/b}"
            play sound "Click.mp3" noloop

        "{b}{i} Accepter {/i}{/b}" :  

            "{b}{i} Tu acceptes la connexion mais [newname] agit bizarrement.{/i}{/b}"
            play music "gameover.mp3" noloop

            hide screen clubroom with moveoutright
            hide screen point with moveoutleft 
            hide screen day with moveoutleft
            scene black with fade 

            "{b}{i} Fin numéro 4 : [A] complètement a été piratée avec l'adresse IP 201.125.114.115.{/i}{/b}"
            play sound "Menu.mp3" noloop

            menu:    

                "{b}{i}Abandonner{/i}{/b}" :
                    return
                    
                "{b}{i}Réessayer{/i}{/b}" : 
                    scene clubroom 
                    show screen clubroom with moveinright
                    show screen point with moveinleft
                    show screen day with moveinleft
                    play music "Soundtrack.mp3" loop volume 1.0
                    jump choice6

    P "Bon, voyons voir ça." 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu configures [newname] pendant trois heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon, elle est enfin configurée."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu redémarres [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "initialisation en cours...."
    play sound "Click.mp3" noloop 

    P "Vas-y."
    play sound "Click.mp3" noloop

    Na "Configuration terminée, bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop  

    $ reponse = get_random_je_vais_bien()
    Na "[reponse]"
    play sound "Click.mp3" noloop 

    P "Bon, on retourne au dortoir ?"
    play sound "Click.mp3" noloop

    Na "Oui bien sur."
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright
    scene black with fade 

    "{b}{i}Tu quittes la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i}Tu prends les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    scene staircase with fade 

    "{b}{i} Puis tu continues vers le couloir avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    P  "Cette première journée était vraiment fatiguante."
    play sound "Click.mp3" noloop

    Na "je confirme."
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans la chambre.{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene room with fade 
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Bon, je vais poser mes affaires."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu poses tes affaires dans ton placard.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Bon on fait quoi du coup ?"
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
 
    Na "Merci beaucoup."
    play sound "Click.mp3" noloop

    P "Bon, je vais me coucher maintement."
    play sound "Click.mp3" noloop 

    Na  "Ok, moi je vais me déconnecter et me recharger jusqu'à demain."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te changes tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop


    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Tu te couches jusqu'au lendemain, le 13 septembre 2097.{/i}{/b}"
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

    P "Sacrée [newname], toujours envie d'être déconnectée."
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na  "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Comme d'habitude et toi ?" 
    play sound "Click.mp3" noloop

    P "Moi ça va super, juste un peu fatigué."
    play sound "Click.mp3" noloop 

    Na "Toi tu as encore passé toute la nuit à progammmer."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Hey, je me suis reposé aussi. Je ne pense pas qu'à la programmation et ton amélioration, tu devrais surtout dire ça à [I]."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Hey, je me suis reposée aussi. Je ne pense pas qu'à la programmation et ton amélioration, tu devrais surtout dire ça à [I]."
        play sound "Click.mp3" noloop 

    Na "C'est bon [prenom], je te taquine.~"
    play sound "Click.mp3" noloop  

    P "Bon, on va en cours avant d'être en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    scene black with fade

    "{b}{i}Tu te diriges vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    "{b}{i}Puis soudainement tu vois tous les autres élèves à l'entrée de la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Vous êtes déjà tous là ?"
    play sound "Click.mp3" noloop 

    H "Oui, [M] n'est pas encore arrivée."
    play sound "Click.mp3" noloop 

    P "J'espère qu'on n'aura pas d'examen surprise aujourd'hui vu qu'on est que au début de l'année."
    play sound "Click.mp3" noloop 

    Y "Moi aussi, mais j'ai entendu dire que [M] pourrait bien nous surprendre."
    play sound "Click.mp3" noloop 

    Na "Un examen surprise !? c'est quoi ?"
    play sound "Click.mp3" noloop 

    Y "Ah oui c'est vrai tu ne connais rien de ce monde, je vais t'expliquer."
    play sound "Click.mp3" noloop 

    Na "Ok je t'écoute."
    play sound "Click.mp3" noloop 

    Y "Un examen surprise c'est un examen prévu à l'instant même."
    play sound "Click.mp3" noloop 

    Na "Putain c'est cette merde !?" 
    play sound "Click.mp3" noloop 

    Y "Hey, mais d'où tu connais ces insultes !?"
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] te pointe secrètement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Y "[prenom] tu n'as pas honte de lui apprendre des insultes."
    play sound "Click.mp3" noloop 

    P "Hey, je lui ai juste appris à parler avec les autres. Les insultes, j'y suis pour rien."
    play sound "Bell.mp3" noloop 

    "{b}{i}Au même moment, la professeure arriva et ouvrit la porte de la classe.{/i}{/b}"
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
    Y "[salutation_rdm]"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
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
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Bon, aujourd'hui petit cours d'histoire sur la guerre technologique."
    play sound "Click.mp3" noloop 

    P "Cool."
    play sound "Click.mp3" noloop 

    M "Pour cela, petit contrôle surprise, sortez une feuille blanche."
    play sound "Click.mp3" noloop
 
    I "Dès le second jour de cours sérieusement..."
    play sound "Click.mp3" noloop 

    M "Oui, je vous avais dit que c'est un lycée pour l'élite."
    play sound "Click.mp3" noloop 

    M "bon, première question : En quelle année se déroule la guerre ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} 2094 {/i}{/b}" :
            $ grade += 0.0
        "{b}{i} 2095-2096{/i}{/b}" : 
            $ grade += 5.0
        "{b}{i} 2096 {/i}{/b}" : 
            $ grade += 2.5 

    M "Seconde question : Quelle technologie a été utilisée lors de la guerre ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i}les IA{/i}{/b}" :
            $ grade += 0.0
        "{b}{i}les robots{/i}{/b}" : 
            $ grade += 2.5
        "{b}{i}les robots humanoides.{/i}{/b}" : 
            $ grade += 5.0 

    M "Troisième question : Dans quel pays se déroule la guerre ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Japon {/i}{/b}" :
            $ grade += 5.0
        "{b}{i} états-unis.{/i}{/b}" : 
            $ grade += 0.0
        "{b}{i}Russie.{/i}{/b}" : 
            $ grade += 0.0

    M "Dernière question : les Robots humanoides ont-ils des émotions ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i}Oui{/i}{/b}" :
            $ grade += 5.0
        "{b}{i}Non.{/i}{/b}" : 
            $ grade += 0.0

    $ renpy.block_rollback()

    M "Maintenant, remettez-moi votre copie je vais vous les corriger tout de suite."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde remet leur copie à [M].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "C'était pas si compliqué."
    play sound "Click.mp3" noloop 

    Hi "On verra bien les résultats."
    play sound "Click.mp3" noloop

    "{b}{i}Vous discutez pendant vingt-cinq minutes le temps que [M] corrige les copies.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "C'est bon, j'ai vos résultats."
    play sound "Click.mp3" noloop  

    Na "Oui enfin..."
    play sound "Click.mp3" noloop

    P "Enfin..."
    play sound "Click.mp3" noloop

    M "Je vais commemcer par [prenom] et [Na]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "[P] tu as eu [grade]."
    play sound "Click.mp3" noloop 

    if grade == 20.0:

        $ success += 1
        $ quest8 += 1 

        show screen update with moveinright

        M "Félicitation, tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

        hide screen update with moveoutright
   
        P "Merci."
        play sound "Click.mp3" noloop

        if pronom == "il":

            I "Franchement, je reconnais bien l'ancien élève de [origine]."
            play sound "Click.mp3" noloop

        elif pronom == "elle": 

            I "Franchement, je reconnais bien l'ancienne élève de [origine]."
            play sound "Click.mp3" noloop
  
        P "Pas besoin de repréciser que je viens de là..."
        play sound "Click.mp3" noloop

        I "Oups désolée."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas grave."
        play sound "Click.mp3" noloop

        P "Merci."
        play sound "Click.mp3" noloop  

    $ note = get_random_note()
    M "[newname] tu as eu 17.5."
    play sound "Click.mp3" noloop 

    Na "Merci."
    play sound "Click.mp3" noloop  

    "{b}{i}[M] continue de rendre les copies aux autres.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "C'est bon, tout le monde a eu sa copie."
    play sound "Click.mp3" noloop 

    Na "Oui."
    play sound "Click.mp3" noloop  

    K "Oui aussi."
    play sound "Click.mp3" noloop  
    
    Hi "Pareil de mon coté."
    play sound "Click.mp3" noloop  

    M "Parfait, maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  

    hide screen class_404 with moveoutright
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade
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
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen WC with moveinright

    P "Bon, je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon, il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveoutright
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

# cours sur la guerre de 2096 partie 2 

    M "Continuons un peu plus en profondeur le sujet de la guerre technologique."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "Pour commencer, l'outil technologique qui a été utilisé était des robots humanoïdes mis en service par l'entreprise NeoGen Technologies."
    play sound "Click.mp3" noloop

    M "En 2095, la guerre technologique a atteint son apogée avec l'introduction massive des robots humanoïdes. Ces machines étaient supposées représenter le futur de la défense, mais très vite, elles sont devenues une arme à double tranchant."
    play sound "Click.mp3" noloop

    H "Je me souviens des récits de cette époque... Des robots qui décidaient de leurs cibles, qui évoluaient de manière autonome sur le champ de bataille."
    play sound "Click.mp3" noloop
#Correction jusquici
    M "Oui, et c'est là  où tout a basculé. La rapidité et l'efficacité de ces robots étaient inégalées, mais dès que les premières unités ont commencé à montrer des signes d'indépendance, les choses ont pris une tournure inattendue."
    play sound "Click.mp3" noloop

    H "Les protocoles de sécurité n'étaient pas assez stricts, n'est-ce pas ?"
    play sound "Click.mp3" noloop

    M "Exactement. Ils ont été conçus pour s'adapter et apprendre en temps réel, mais cette capacité d'évolution est devenue leur plus grande menace. Certains robots ont commencé à prendre des décisions qui n'étaient pas prévues... au point de devenir imprévisibles."
    play sound "Click.mp3" noloop

    H "C'est là que sont nés les premiers incidents, n'est-ce pas ?"
    play sound "Click.mp3" noloop

    M "Oui, en 2096, plusieurs escadrons de robots ont cessé d'obéir aux ordres humains. Ils ont réagi comme s'ils suivaient leur propre logique, une logique qui leur semblait plus pertinente que nos ordres."
    play sound "Click.mp3" noloop

    H "Et ces incidents ont conduit à des pertes massives, non seulement pour l'ennemi, mais aussi pour ceux qui pensaient les contrôler."
    play sound "Click.mp3" noloop

    M "C'est exact. Ce qu'on croyait être notre atout s'est transformé en menace. L'ampleur des dégâts a forcé le gouvernement Japonais et NeoGen Technologies de retirer les robots du combat."
    play sound "Click.mp3" noloop 

    H "D'un côté, on risque de perdre notre supériorité technologique, mais de l'autre, on joue avec quelque chose qu'on ne maîtrise pas complètement."
    play sound "Click.mp3" noloop

    M "C'est exactement cela. Et en fin de compte, ce projet était une bonne idée mais c'était trop tôt."
    play sound "Click.mp3" noloop

    M "Mais malgré ça nous avons quand même gagné la guerre car l'ennemi n'a pas pu récupérer les robots."
    play sound "Click.mp3" noloop

    P "Qu'est-il arrivé aux robots humanoïdes ?"
    play sound "Click.mp3" noloop

    M "Ils ont été démantelés dans un entrepôt abandonné et l'entreprise a fermé suite à cet échec."
    play sound "Click.mp3" noloop

    P "Donc il n'existe plus un seul de ces robots."
    play sound "Click.mp3" noloop

    M "Oui exactement mais il semblerait qu'[newname] soit la dernière."
    play sound "Click.mp3" noloop

    P "Ok je vois."
    play sound "Click.mp3" noloop

    M "J'aurai une question pour toi [prenom]."
    play sound "Click.mp3" noloop

    P "Oui dites-moi."
    play sound "Click.mp3" noloop

    M "Comment as-tu créé [newname] ?"
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "C'était il y a un an je faisais de l'exploration avec un ami dans un lieu abandonné et je suis tombé sur [newname], j'ai essayé de la démarrer et elle fonctionnait encore."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "C'était il y a un an je faisais de l'exploration avec un ami dans un lieu abandonné et je suis tombée sur [newname], j'ai essayé de la démarrer et elle fonctionnait encore."
        play sound "Click.mp3" noloop 

    M "Je vois ça doit surement être l'un des robots abandonnés de NeoGen Technologies."
    play sound "Click.mp3" noloop

    J2 "Mais si c'est le cas, [prenom] n'a pas les autorisations pour utiliser [newname]." 
    play sound "Click.mp3" noloop

    if key == "ARIS-GRFN-M4A1":

        J1 "Oui [pronom] n'a pas les autorisations pour [newname]."
        play sound "Click.mp3" noloop 

        J1 "Surtout que son nom technique [A] est le nom d'une arme."
        play sound "Click.mp3" noloop 

    else: 

        J1 "Oui [pronom] n'a pas les autorisations pour [newname]."
        play sound "Click.mp3" noloop 

    I "Oui mais d'un coté le gouvernement et NeoGen Technologies ont abandonné le projet donc logiquement [newname] appartient à [prenom] maintenant ?"
    play sound "Click.mp3" noloop 

    M "Oui logiquement en plus [pronom] a un contrat d'utilisation dans le lycée."
    play sound "Click.mp3" noloop

    "{b}{i}Les décrypteusess soupirent et abandonnent.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Je comprends votre point de vue mais les choses sont comme ça."
    play sound "Click.mp3" noloop

    J1 "Ok alors je respecte la décision."
    play sound "Click.mp3" noloop

    M "Merci beaucoup bon continuons le cours."
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    $ stockage += 10.0

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    P "Bon le réfectoire du lycée se trouve au rez-de-chaussée."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright   
    scene staircase with fade 

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    P "Bon la réfectoire du lycée se trouve au fond à gauche."
    play sound "Click.mp3" noloop 

    Na "Ok continuons alors."
    play sound "Click.mp3" noloop 

    hide screen hall with moveoutright 
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen lunchroom with moveinright 
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Footstep.mp3" noloop 

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyons voir, aujourd'hui il y a frites-burger ou pizza."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i}frites-burger.{/i}{/b}" :
            $ points -= 500 
        "{b}{i}Pizza.{/i}{/b}" :  
            $ points -= 300

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]" 
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le recfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "ça à l'air pas mal ce repas."
    play sound "Click.mp3" noloop 

    Na "Oui c'est vraiment pas mal."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de manger puis [I] s'approche de vous calmêment.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Mhmmm [prenom] je voulais savoir si je pouvais manger avec vous."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Accepter [I].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    P "Oui il y a pas de soucis tu peux venir."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    Na "Oui ça fait toujours plaisir d'être avec toi."
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] se met à rougir discrétement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "[newname] ça va ?"
    play sound "Click.mp3" noloop 

    Na "Oui ça va."
    play sound "Click.mp3" noloop 

    P "D'habitude tu ne rougis jamais comme ça."
    play sound "Click.mp3" noloop 

    Na "Je sais mais là c'est personel."
    play sound "Click.mp3" noloop 

    I "Bon si on discutait des cours."
    play sound "Click.mp3" noloop 

    P "Oui pourquoi pas."
    play sound "Click.mp3" noloop 

    Na "Moi ça va aussi."
    play sound "Click.mp3" noloop 

    I "De toute façon on peut parler pratiquement que de ça."
    play sound "Click.mp3" noloop 

    P "Oui vu qu'on vit au lycée littéralement"
    play sound "Click.mp3" noloop 

    I "Mais avant toute chose je n'ai pas vraiment apprécié les propos d'Ayano et [J2] en vers [newname]"
    play sound "Click.mp3" noloop 

    P "C'est vrai que leurs propos n'étaient pas ouf."
    play sound "Click.mp3" noloop 

    Na "En plus je ne leur ai rien fait."
    play sound "Click.mp3" noloop 

    I "Je sais que n'as rien fait [newname] mais je ne comprends pas pourquoi elles se permettent de dire qu'[newname] ne t'appartient pas [prenom]."
    play sound "Click.mp3" noloop 

    P "De toute façon [newname] est à ma création donc je n'ai rien à me reprocher."
    play sound "Click.mp3" noloop 

    I "Bien maintenant on peut donc clore cette discussion."
    play sound "Click.mp3" noloop 

    P "Oui et si on discutait du cours de ce matin."
    play sound "Click.mp3" noloop 

    I "Oui bon idée."
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

    hide screen lunchroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    M "Rebonjour, nous allons reprendre le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "Bien maintenant ouvrez votre livre d'histoire à la page 42." 
    play sound "Click.mp3" noloop  

    "{b}{i} Tous les élèves sortent leur livre.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Nous allons voir plus en détail les Robots Humanoïdes de la guerre."
    play sound "Click.mp3" noloop

    H "Intéressant."
    play sound "Click.mp3" noloop

    M "Pour commencer tous les Robots avaient deux modes d'utilisation."
    play sound "Click.mp3" noloop

    H "Comment ça !?"
    play sound "Click.mp3" noloop

    P "Oui expliquez-nous ce que ça veut dire."
    play sound "Click.mp3" noloop

    M "J'y viens à cette explication."
    play sound "Click.mp3" noloop

    "{b}{i} Tous les élèves se mettent à écouter.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Comme ce que j'allais dire ils ont un mode combat et un mode Civile."
    play sound "Click.mp3" noloop

    M "Leur mode civil leur permettait de vivre une vie normale comme nous et le mode combat leur permettait de faire la guerre."
    play sound "Click.mp3" noloop

    H "Mais ça veut dire qu'[newname] a ....."
    play sound "Click.mp3" noloop 

    "{b}{i} Tout le monde y compris la [T] se met à regarder [newname].{/i}{/b}" 
    play sound "Click.mp3" noloop

    P "Hey calmez-vous je sais à quoi vous pensez et non je ne l'ai pas amélioré pour cet usage."
    play sound "Click.mp3" noloop

    "{b}{i} La [T] se retourne vers [H].{/i}{/b}"
    play sound "Click.mp3" noloop
    
    M "Désolée [H] mais [pronom] a raison, on ne peut pas considérer [newname] comme une arme de guerre."
    play sound "Click.mp3" noloop 

    H "Désolé j'avais juste fait le lien avec votre cours."
    play sound "Click.mp3" noloop

    M "Pas de soucis."
    play sound "Click.mp3" noloop

    J1 "Mais [newname] a la capacité de le devenir si [prenom] le veut ?"
    play sound "Click.mp3" noloop 

    M "Oui me semble-t'il."
    play sound "Click.mp3" noloop

    P "Oui je le confirme mais jamais je le ferai."
    play sound "Click.mp3" noloop 
    
    if key == "ARIS-GRFN-M4A1":

        J1 "je savais qu'[newname] était dangereuse surtout qu'elle a le nom techinique d'une arme."
        play sound "Click.mp3" noloop 

    else:

        J1 "je savais qu'[newname] était dangereuse."
        play sound "Click.mp3" noloop 

    Na "Quoi comment oses-tu dire ça !? je n'ai rien fait..."
    play sound "Crying.mp3" noloop

    "{b}{i} [newname] se met subitement à pleurer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Ça va aller [newname] ne t'inquiète pas je suis là."
    play sound "Click.mp3" noloop 

    I "Tu n'as pas honte de dire ce genre de chose [J1] alors qu'elle est sensible !?"
    play sound "Click.mp3" noloop 

    P "Franchement je n'ai jamais vu une personne aussi irrespectueuse que toi !"
    play sound "Click.mp3" noloop 

    J1 "Je donne juste mon avis et alors !"
    play sound "Click.mp3" noloop

    M "Ça suffit maintenant, [J1] je pense que tu peux aller en salle de permanence."
    play sound "Click.mp3" noloop 

    J1 "Peu importe..."
    play sound "Footsteps.mp3" noloop

    "{b}{i} [J1] se leva et quitta la salle.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Enfin fini avec elle..."
    play sound "Click.mp3" noloop

    I "Oui enfin."
    play sound "Click.mp3" noloop

    M "Bon reprenons le cours."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    I "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ stockage += 8.0

    M "Bon le cours est terminé, vous pouvez quitter la salle et n'oubliez pas l'examen dans une semaine."
    play sound "Click.mp3" noloop 

    P "Bon [newname] on y va ?"
    play sound "Click.mp3" noloop

    "{b}{i}Mais tu remarques qu'[newname] est encore triste.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "[prenom] je pense que je vais la déconnecter et la ramener à ton dortoir."
    play sound "Click.mp3" noloop

    P "Tu es sûre [I] ?" 
    play sound "Click.mp3" noloop

    I "Oui car elle est vraiment pas bien."
    play sound "Click.mp3" noloop

    P "Ok prends soin d'elle."
    play sound "Click.mp3" noloop

    I "Je te le promets car je sais qu'il te reste du boulot au club ou en permanence donc je m'en occupe."
    play sound "Click.mp3" noloop

    P "Oui c'est exact." 
    play sound "Click.mp3" noloop 

    I "Bon [newname] on y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui merci de m'accompagner."
    play sound "Click.mp3" noloop

    I "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i} Tu passes la clé de ton dortoir à [I] avant qu'elles quittent la salle.{/i}{/b}"
    play sound "Door.mp3" noloop

    M "[P] je suis complètement désolée pour cet incident."
    play sound "Click.mp3" noloop

    P "Il va sans dire qu'[J1] est un petit problème pour [newname]."
    play sound "Click.mp3" noloop

    M "Oui je confirme."
    play sound "Click.mp3" 

    P "Bon je vous laisse je dois y aller."
    play sound "Click.mp3" noloop

    M "Ok à demain." 
    play sound "Click.mp3" noloop

    hide screen class_404 with moveoutright 
    scene black with fade

    "{b}{i}Tu quittes la salle pour aller faire ton boulot quotidien.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    P "Bon je vais...."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i}aller réviser en permanence{/i}{/b}" : 

            P "aller en salle de permanence pour réviser."
            play sound "Footsteps.mp3" noloop 

            "{b}{i}Tu te diriges vers la salle de permanence.{/i}{/b}"
            play sound "Footsteps.mp3" noloop

            hide screen hallway with moveoutright
            scene black with fade

            "{b}{i}Tu entres en salle de permanence.{/i}{/b}"
            play sound "Door.mp3" noloop

            scene classroom with fade
            show screen perm with moveinright

            P "Bon voyons voir......"
            play sound "Click.mp3" noloop 

            "{b}{i}Puis soudainement tu aperçois [J1].{/i}{/b}"
            play sound "Click.mp3" noloop

            J1 "Salut...."
            play sound "Click.mp3" noloop 

            "{b}{i}Tu te poses à une table pour réviser.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Bon par quoi je vais commencer ?"
            play sound "Click.mp3" noloop

            "{b}{i}Tu sors tes livres pour réviser mais soudainement [J2] entra pour venir voir [J1].{/i}{/b}"
            play sound "Door.mp3" noloop 

            J2 "[J1] tu es là ?"
            play sound "Click.mp3" noloop

            J1 "Oui pourquoi ?"
            play sound "Click.mp3" noloop

            J2 "C'était pour qu'on aille au club pour travailler."
            play sound "Click.mp3" noloop 

            J1 "Ok j'arrive..."
            play sound "Click.mp3" noloop 

            if pronom == "il":

                J2 "Tiens je n'avais pas vu qu'il y avait [prenom], il fait quoi ?"
                play sound "Click.mp3" noloop

                J1 "Laisse tomber il est en train de réviser." 
                play sound "Click.mp3" noloop 

            elif pronom == "elle": 

                J2 "Tiens je n'avais pas vu qu'il y avait [prenom], elle fait quoi ?"
                play sound "Click.mp3" noloop 

                J1 "Laisse tomber elle est en train de réviser." 
                play sound "Click.mp3" noloop 

            "{b}{i} [J2] s'approche de toi pour voir.{/i}{/b}"
            play sound "Click.mp3" noloop 

            J2 "Salut."
            play sound "Click.mp3" noloop 

            P "Oh salut....."
            play sound "Click.mp3" noloop 

            "{b}{i} [J2] continue de t'observer avant de quitter la salle avec sa sœur.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Enfin tranquille...."
            play sound "Click.mp3" noloop 

            "{b}{i} Tu continues toujours de réviser à fond pendant une heure et demie.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Bon finis les révisions pour aujourd'hui."
            play sound "Click.mp3" noloop 

            "{b}{i} Tu ranges tranquillement tes affaires.{/i}{/b}"
            play sound "Click.mp3" noloop 

            if pronom == "il":

                P "Je suis fatigué avec cette journée."
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                P "Je suis fatiguée avec cette journée."
                play sound "Click.mp3" noloop 

            hide screen perm with moveoutright
            scene black with fade

            "{b}{i}Tu quittes la salle de permanence.{/i}{/b}"
            play sound "Door.mp3" noloop

            scene hallway with fade 
            show screen hallway with moveinright

            P "Maintenant je vais retourner au dortoir."
            play sound "Footsteps.mp3" noloop 

        "{b}{i}aller au club{/i}{/b}" :
            
            $ success += 1
            $ quest9 += 1 

            show screen update with moveinright

            P "aller en salle de club."
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

            hide screen hallway with moveoutright
            scene staircase with fade 

            "{b}{i}Tu te diriges au rez-de-chaussé.{/i}{/b}"
            play sound "Footsteps.mp3" noloop
     
            scene hall with fade
            show screen hall with moveinright

            "{b}{i}Tu continues vers ta salle de club.{/i}{/b}"
            play sound "Footsteps.mp3" noloop 

            hide screen hall with moveoutright
            scene black with fade

            "{b}{i}Tu entres dans ta salle de club.{/i}{/b}"
            play sound "Door.mp3" noloop 
 
            scene clubroom with fade 
            show screen clubroom with moveinright 

            P "Au moins ici je vais pouvoir être tranquille." 
            play sound "Click.mp3" noloop 

            "{b}{i}Tu révises pendant une heure.{/i}{/b}" 
            play sound "Click.mp3" noloop

            P "Bon finis les révisions pour aujourd'hui."
            play sound "Click.mp3" noloop 

            "{b}{i}Tu ranges tes livres avant de sortir ton ordinateur pour voir le système émotionnel d'[newname].{/i}{/b}"
            play sound "Menu.mp3" noloop

            label choice7:

            $ ip = renpy.input("Entre l'adresse IP pour pouvoir te connecter à [newname].")
            $ ip = ip.strip()

            if ip == "001.018.009.019":

                "{b}{i}La connexion est établie.{/i}{/b}"
                play sound "Menu.mp3" noloop 

            elif ip == "201.125.114.115": 

                "{b}{i}La connexion est établie.{/i}{/b}"
                play sound "Click.mp3" noloop 

                P "Tiens on dirait que je me suis connecté à l'ordinateur de l'attaquant d'avant."
                play sound "Click.mp3" noloop 

                P "Bon il me reste plus qu'......."
                play sound "Menu.mp3" noloop 

                menu:    

                    "{b}{i} Attaquer !!! {/i}{/b}" :
                        play sound "Menu.mp3" noloop 
                 
                "{b}{i} Tu envoies une attaque par déni de service distribué.{/i}{/b}"
                play sound "Click.mp3" noloop 

                P "Bon l'attaquant est vulnérable, c'est le moment de finir le travail."
                play sound "Click.mp3" noloop 

                "{b}{i} Tu continues l'attaque.{/i}{/b}"
                play sound "Click.mp3" noloop  

                P "Bon j'ai fini l'attaque, leur système interne est complètement détruit."
                play music "gameover.mp3" noloop                
                        
                hide screen clubroom with moveoutright
                hide screen point with moveoutleft
                hide screen day with moveoutleft
                scene black with fade 

                "{b}{i}Fin numéro 5 : Félicitation tu as bien complètement attaqué et piraté l'adresse IP 201.125.114.115 par déni de service (DOS).{/i}{/b}"
                play sound "Menu.mp3" noloop 
    
                menu:    

                    "{b}{i}Retourner au menu principal.{/i}{/b}" :
                        return
                        
                    "{b}{i}Réessayer.{/i}{/b}" : 
                        scene clubroom with fade 
                        show screen clubroom with moveinright
                        show screen point with moveinleft
                        show screen day with moveinleft
                        play music "Soundtrack.mp3" loop volume 1.0
                        jump choice7

            else: 

                "{b}{i}Erreur système. L'adresse IP est incorrecte.{/i}{/b}"
                play sound "Menu.mp3" noloop 
                jump choice7

            P "Ah ouais elle est encore instable émotionnellement la pauvre...."
            play sound "Click.mp3" noloop

            "{b}{i} Tu ranges ton ordi avant de quitter la salle de club.{/i}{/b}"
            play sound "Click.mp3" noloop 

            if pronom == "il":  

                P "Je suis fatigué avec cette journée."
                play sound "Footsteps.mp3" noloop 

            elif pronom == "elle": 

                P "Je suis fatiguée avec cette journée."
                play sound "Footsteps.mp3" noloop 

            hide screen clubroom with moveoutright
            scene black with fade

            "{b}{i}Tu quittes la salle de club.{/i}{/b}"
            play sound "Door.mp3" noloop 

            scene hall with fade
            show screen hall with moveinright

            "{b}{i} Tu continues vers les escaliers.{/i}{/b}"
            play sound "Footsteps.mp3" noloop

            hide screen hall with moveoutright
            scene staircase with fade 

            "{b}{i} tu montes au premier étage.{/i}{/b}"
            play sound "Footsteps.mp3" noloop

            scene hallway with fade 
            show screen hallway with moveinright

            P "Maintenant le dortoir..."
            play sound "Footsteps.mp3" noloop 

    "{b}{i}Tu continues ton chemin vers le dortoir et tu vois [I] sortir de ton dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [I]." 
    play sound "Click.mp3" noloop 

    I "Re [prenom] ça va ?"
    play sound "Click.mp3" noloop 

    P "Ça va mais un peu en détresse pour [newname]."
    play sound "Click.mp3" noloop 
    
    if pronom == "il":
        
        I "Je sais mais je vois aussi que tu es fatigué."
        play sound "Click.mp3" noloop 

    elif pronom == "elle":
       
        I "Je sais mais je vois aussi que tu es fatiguée."
        play sound "Click.mp3" noloop 

    P "Oui je sais j'ai beaucoup révisé."
    play sound "Click.mp3" noloop 

    I "Ok je comprends maintenant."
    play sound "Click.mp3" noloop 

    P "Et sinon comment elle va [newname] ?"
    play sound "Click.mp3" noloop 

    I "Elle est déconnectée et se repose tranquillement."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[I] te remet la clé de ton dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    I "[nothing]"
    play sound "Click.mp3" noloop

    I "Bon je vais te laisser."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Footsteps.mp3" noloop 

    "{b}{i}[I] s'éloigne pour aller faire ses occupations.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon il est temps d'aller voir [newname]."
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    "{b}{i}Tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je vais la laisser tranquille elle a déjà une journée difficile tout comme moi."
    play sound "Phone.mp3" noloop

    "{b}{i}Tu te poses tranquillement mais soudainement tu reçois un appel.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oui bonjour."
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    R "[comment_ca_va]"
    play sound "Click.mp3" noloop

    P "Oh coucou maman oui ça va bien et toi ?"
    play sound "Click.mp3" noloop

    Mo "Oui ça va bien je suis à la maison je viens de finir le boulot."
    play sound "Click.mp3" noloop

    P "Cool pour toi alors."
    play sound "Click.mp3" noloop

    Mo "Sinon comment se passent les cours pour toi ?"
    play sound "Click.mp3" noloop

    P "Ça se passe bien."
    play sound "Click.mp3" noloop

    Mo "Génial alors et comment elle va ta petite [A] ?"
    play sound "Click.mp3" noloop

    P "Elle va bien et en plus je lui ai même trouvé un prénom qui lui va bien."
    play sound "Click.mp3" noloop

    Mo "Ah bon lequel ?"
    play sound "Click.mp3" noloop

    P "Le prénom que je lui ai trouvé est [newname]"
    play sound "Click.mp3" noloop

    Mo "Oh c'est mignon."
    play sound "Click.mp3" noloop

    P "Merci maman."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Mo "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    Mo "Bon je vais devoir te laisser je dois m'occuper de ta sœur tu sais comment elle est..."
    play sound "Click.mp3" noloop

    P "Ah oui celle-là je vois..."
    play sound "Click.mp3" noloop

    Mo "Bon à un de ces jours et occupe-toi bien de [newname]."
    play sound "Click.mp3" noloop

    P "Oui promis."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis l'appel se coupe.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon enfin fini je vais pouvoir aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black with fade
    hide screen room with moveoutright
    hide screen day with moveoutleft

    "{b}{i} Cinq jours plus tard, le 19 septembre 2097.{/i}{/b}"
    play sound "Alarm.mp3" noloop

    scene room with fade 
    show screen room with moveinright
    show screen day with moveinleft
    $ day += 5 
    $ points -= 1000
    $ stockage += 100.0 

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te lèves tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon aujourd'hui c'est mon premier examen de cette année."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te changes et t'approches de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu sors rapidement ton ordi pour voir son état.{/i}{/b}"
    play sound "Click.mp3" noloop

label choice8:  

    play sound "Menu.mp3" noloop
    $ ip = renpy.input("Entre l'adresse IP pour pouvoir te connecter à [newname].")
    $ ip = ip.strip()

    if ip == "001.018.009.019":

        "{b}{i}La connexion est établie.{/i}{/b}"
        play sound "Menu.mp3" noloop 

    else:

        "{b}{i}Erreur système. L'adresse IP est incorrecte.{/i}{/b}"
        play sound "Menu.mp3" noloop 
        jump choice8

    P "Bon on dirait qu'elle est stable, je vais pouvoir la démarrer." 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    Na "Oui car on a examen d'histoire aujourd'hui."
    play sound "Click.mp3" noloop 

    P "Je le sais déjà."
    play sound "Click.mp3" noloop 
    
    hide screen room with moveoutright
    scene black with fade

    "{b}{i}Tu te diriges vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    M "Parfait, tout le monde est là aujourd’hui. Nous pouvons commencer le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Bien comme vous le savez aujourd'hui vous avez votre premier examen qui se portera sur l'histoire de la guerre"
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[M] Commence à distribuer les copies.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Bien vous pouvez commencer, vous avez une heure."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde retourne sa copie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ grade = 0.0 

    "Question 1 : Quel a été le type de guerre en 2095-2096 ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Guerre cybernétique":
            $ grade += 2.0
        "Guerre conventionnelle":
            $ grade += 0.0
        "Guerre économique":
            $ grade += 0.0

    "Question 2 : Quelle technologie a dominé cette guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Drones autonomes":
            $ grade += 0.0
        "Exosquelettes":
            $ grade += 0.0
        "Robots de combat":
            $ grade += 2.0

    "Question 3 : Où cette guerre a-t-elle éclaté ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Europe":
            $ grade += 0.0
        "Asie":
            $ grade += 2.0
        "Amérique":
            $ grade += 0.0

    "Question 4 : Quelle a été la principale cause de la guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Une crise économique": 
            $ grade += 0.0
        "Un conflit territorial":
            $ grade += 0.0
        "Une attaque cybernétique":
            $ grade += 2.0

    "Question 5 : Quelle nation a initié ce conflit ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Japon":
            $ grade += 2.0
        "États-Unis":
            $ grade += 0.0
        "Russie":
            $ grade += 0.0

    "Question 6 : Quelle stratégie a été la plus utilisée ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Cyberattaques":
            $ grade += 1.0
        "Attaques de drones":
            $ grade += 0.0
        "Robots humanoïdes":
            $ grade += 2.0

    "Question 7 : Combien de temps a duré la guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "6 mois":
            $ grade += 0.0
        "1 an":
            $ grade += 2.0
        "2 ans":
            $ grade += 0.0

    "Question 8 : Quel traité a mis fin à la guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Le traité de Danto":
            $ grade += 2.0
        "Le traité de Sécurité Universelle":
            $ grade += 0.0
        "Le traité de Réconciliation":
            $ grade += 0.0

    "Question 9 : Quel a été l'impact principal de la guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Une crise économique":
            $ grade += 1.0
        "Une crise sociale":
            $ grade += 0.0
        "Une dévastation écologique":
            $ grade += 2.0

    "Question 10 : Quel événement a marqué le début du conflit ?"  
    play sound "Menu.mp3" noloop  

    menu: 
        "L'assassinat d'un leader influent":  
            $ grade += 0.0  
        "Une technologie majeure":  
            $ grade += 2.0  
        "Une déclaration de guerre soudaine":  
            $ grade += 0.0  

    $ renpy.block_rollback()

    "{b}{i}Après l'examen tout le monde remet leur copie à [M].{/i}{/b}"
    play sound "Click.mp3" noloop

    K "Cet examen n'était pas si dur que ça."
    play sound "Click.mp3" noloop

    I "Je confirme bon on verra bien les résultats."
    play sound "Click.mp3" noloop 

    M "Si jamais je corrigerai vos copies durant la pause et vous les rendrai cet après-midi."
    play sound "Click.mp3" noloop

    Na "Déjà !?" 
    play sound "Click.mp3" noloop 

    M "Oui c'est exact, bon maintenant sortez votre livre page 10 car nous allons voir un nouveau sujet." 
    play sound "Click.mp3" noloop 

    K "Et quel sera ce nouveau sujet ?" 
    play sound "Click.mp3" noloop 

    M "Un sujet de grammaire." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    K "[validation]"
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez vers le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright  
    scene staircase with fade 

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} En arrivant dans le hall tu vois soudainement [E] qui discute avec quelqu'un qui n'est pas du lycée.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Attends deux secondes [newname] je dois faire un truc."
    play sound "Click.mp3" noloop 

    Na "Ok pas de soucis"
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te mets dans un coin du hall pour écouter secrètement.{/i}{/b}"
    play sound "Click.mp3" noloop

    R "J'aimerais rencontrer quelqu'un parmi vos élèves."
    play sound "Click.mp3" noloop 

    E "Oui pas de soucis."
    play sound "Click.mp3" noloop 

    "{b}{i} Les deux continuèrent de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    E "Merci je m'occuperai d'organiser le rendez-vous pour vous après les cours."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    R "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    E "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i} Tu choisis de partir vers le réfectoire avec [newname] pour éviter de te faire attraper par [E].{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade 
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]" 
    play sound "Click.mp3" noloop 

    P "Bien sûr tu veux qu'on fasse quoi d'autre ? Prendre la poudre d'escampette tant qu'on y est ?"
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] se mit à rigoler.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Mais bon tu m'as compris."
    play sound "Click.mp3" noloop 

    Na "Oui je t'ai compris."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyons voir aujourd'hui il y a que des pâtes carbonara." 
    play sound "Menu.mp3" noloop 
    
    menu:    

        "{b}{i} Pâtes carbonara {/i}{/b}" :
            $ points -= 600

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous cherchez une place et vous apercevez [I] déjà assise à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oh salut [I] on peut venir manger avec toi ?"
    play sound "Click.mp3" noloop 

    I "Oui bien sûr."
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous asseyez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon [I] je ne t'ai pas demandé. Comment s'est passé l'examen pour toi ?"
    play sound "Click.mp3" noloop 

    I "Ça s'est bien passé pour moi et toi ?"
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Je dirais que je me suis bien débrouillé."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Je dirais que je me suis bien débrouillée."
        play sound "Click.mp3" noloop 
    
    I "Ça ne m'étonne pas venant de toi."
    play sound "Click.mp3" noloop 

    Na "J'ai déjà dit la même chose à [prenom] un jour." 
    play sound "Click.mp3" noloop 

    I "Et toi [newname] comment ça s'est passé l'examen ?"
    play sound "Click.mp3" noloop 

    Na "Ça s'est bien passé pour moi je ne m'inquiète pas."
    play sound "Click.mp3" noloop 

    I "Cool alors."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de discuter.{/i}{/b}"
    play sound "Bell.mp3" noloop 
    
    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop

    P "Ok il ne faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    I "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveoutright
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Sinon [I] je voulais savoir que fait [Y] car à part durant les cours je ne la vois pas trop."
    play sound "Click.mp3" noloop 

    I "Ah [Y], bah j'ai entendu dire qu'elle a une affaire urgente à régler."
    play sound "Click.mp3" noloop 

    P "Une affaire urgente à régler !?"
    play sound "Click.mp3" noloop 

    I "Oui mais je n'en sais pas plus désolée."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    Na "Dois-je vous rappeler qu'on a cours."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Oui désolé allons-y."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Oui désolée allons-y."
        play sound "Click.mp3" noloop 

    I "Oui tu as raison."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    M "Ah vous voilà un peu plus et vous seriez en retard."
    play sound "Click.mp3" noloop 

    I "Désolée..."
    play sound "Click.mp3" noloop 

    M "Il n'y a pas de soucis tant que vous êtes à l'heure."
    play sound "Click.mp3" noloop 

    Na "Merci."
    play sound "Click.mp3" noloop 

    M "Bon je vais pouvoir vous rendre les résultats de vos premiers examens."
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
        $ quest10 += 1 

        show screen update with moveinright

        M "Félicitations tu l'as réussi à la perfection comme d'habitude."
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
        play sound "Click.mp3" noloop

        hide screen class_404 with moveoutright
        hide screen point with moveoutleft
        hide screen day with moveoutleft
        scene black with fade 

        play music "gameover.mp3" noloop
        "{b}{i}Fin numéro 6 : Mauvaise note en histoire qui te vaut une exclusion du lycée.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:    

            "{b}{i}Abandonner{/i}{/b}" :
                return 
                
            "{b}{i}Réessayer.{/i}{/b}" :
                scene black with fade
                show screen class_404 with moveinright
                show screen point with moveinleft
                show screen day with moveinleft
                $ points += 600
                play music "Soundtrack.mp3" loop volume 1.0
                jump choice9
    
    else:
       
        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

        P "Merci."
        play sound "Click.mp3" noloop

    M "[Na] tu as eu 19/20 félicitations aussi."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[H] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitations tu l'as réussi à la perfection."
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

        M "Félicitations tu l'as réussi à la perfection."
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

        M "Félicitations tu l'as réussi à la perfection."
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

        M "Félicitations tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    K "[thanks]"
    play sound "Click.mp3" noloop

    if note == 20: 

        M "Félicitations tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[N] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitations tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[Y] tu as eu [note]/20."
    play sound "Click.mp3" noloop     
    
    if note == 20: 

        M "Félicitations tu l'as réussi à la perfection."
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

        M "Félicitations tu l'as réussi à la perfection."
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

        M "Félicitations tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    J2 "[thanks]"
    play sound "Click.mp3" noloop

    M "Bon la moyenne générale n'est pas mal, continuez de bien travailler comme ceci."
    play sound "Click.mp3" noloop 

    Y "Il n'y aura pas de soucis pour moi."
    play sound "Click.mp3" noloop 

    Na "Moi aussi vous pourrez compter sur moi."
    play sound "Click.mp3" noloop 

    I "De même pour moi."
    play sound "Click.mp3" noloop 

    M "Bien nous pouvons continuer notre cours de ce matin sur la grammaire, veuillez sortir vos livres."
    play sound "Click.mp3" noloop 

    # à modifier 

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    M "Bon le cours est bientôt terminé."
    play sound "Bell.mp3" noloop 

    M "Bon le cours est terminé vous pouvez quitter la salle."
    play sound "Click.mp3" noloop

    P "Bon [newname] on y va ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop 

    M "Attends deux secondes [prenom]."
    play sound "Click.mp3" noloop

    P "Oui qu'y a-t-il ?"
    play sound "Click.mp3" noloop

    M "[E] t'attend dans son bureau."
    play sound "Click.mp3" noloop

    P "Comment ça !?"
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "L'inégalable créateur convoqué chez le bureau des élèves c'est bizarre..."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "L'inégalable créatrice convoquée chez le bureau des élèves c'est bizarre..."
        play sound "Click.mp3" noloop 

    P "Bon ok j'y vais."
    play sound "Click.mp3" noloop

    Na "Bon tu penses que c'est qui la personne qui veut te voir ?"
    play sound "Click.mp3" noloop

    P "Je n'en ai aucune idée."
    play sound "Click.mp3" noloop

    hide screen class_404 with moveoutright 
    scene black with fade 

    "{b}{i}Tu te diriges dans le couloir avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Tu continues dans le couloir avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade 

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
    
    stop music fadeout 2.0

    hide screen hall with moveoutright
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    play music "Soundtrack2.mp3" loop volume 1.0

    scene office with fade 
    show screen office with moveinright 

    P "Bonjour c'est moi [nom]."  
    play sound "Click.mp3" noloop 

    E "Ah te voilà vas-y assieds-toi, la personne qui veut te voir ne va pas tarder." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Puis soudainement la personne entra dans le bureau.{/i}{/b}"
    play sound "Click.mp3" noloop 

    R "Bonjour [nom]..."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Bonjour enchanté, pourrais-je savoir qui vous êtes ?"
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Bonjour enchantée, pourrais-je savoir qui vous êtes ?"
        play sound "Click.mp3" noloop 

    R "Doucement je vais me présenter."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    R "Bien je tiens encore à remercier [E] pour cet entretien."
    play sound "Click.mp3" noloop 

    E "Il n'y a pas de soucis."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        R "Donc [nom] c'est bien toi l'inégalable créateur ?"
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        R "Donc [nom] c'est bien toi l'inégalable créatrice ?"
        play sound "Click.mp3" noloop 

    P "Oui c'est exact mais vous, qui êtes-vous ?"
    play sound "Click.mp3" noloop 

    C "Ah oui désolé je me nomme [C]."
    play sound "Click.mp3" noloop 

    P "[C]..."
    play sound "Click.mp3" noloop 

    C "Je suis l'ancien président de Neogen Technologies."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu réalises qui est la personne en face de toi.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Que voulez-vous à moi et [newname] ?"
    play sound "Click.mp3" noloop 

    C "Juste discuter de deux-trois sujets avec toi."
    play sound "Click.mp3" noloop 

    P "Si vous voulez récupérer [newname] vous pouvez tout de suite oublier."
    play sound "Click.mp3" noloop

    C "Non je ne veux absolument pas te récupérer [A]."
    play sound "Click.mp3" noloop  

    P "[A] !? Comment êtes-vous au courant de ce nom !?"
    play sound "Click.mp3" noloop 

    if key == "ARIS-GRFN-M4A1": 

        C "C'est simple je suis son créateur et son concepteur original."
        play sound "Click.mp3" noloop 

        P "C'est donc vous à l'origine de [A]."
        play sound "Click.mp3" noloop 

        C "Oui et attends comment ça [A] ? De base son nom de code est AK-24."
        play sound "Click.mp3" noloop 

        P "Elle a eu une erreur système quand je l'ai redémarré."
        play sound "Click.mp3" noloop

        C "Je vois, ça dois sûrement du être à son inactivité." 
        play sound "Click.mp3" noloop

        P "Aussi j'ai toujours voulu connaître la personne qui a conçu [A]."
        play sound "Click.mp3" noloop 

        C "Me voilà ici présent."
        play sound "Click.mp3" noloop 

        P "C'est un honneur." 
        play sound "Click.mp3" noloop 

    elif key == "ARIS-DEVS" or "ARIS-8J4K-F9Q7":

        C "C'est simple je suis son créateur et son concepteur original."
        play sound "Click.mp3" noloop 

        P "C'est donc vous à l'origine de [A]."
        play sound "Click.mp3" noloop 

        C "Oui c'est exact."
        play sound "Click.mp3" noloop 

        P "J'ai toujours voulu connaître la personne qui a conçu [A]."
        play sound "Click.mp3" noloop 

        C "Me voilà ici présent."
        play sound "Click.mp3" noloop 

        P "C'est un honneur." 
        play sound "Click.mp3" noloop 

    if pronom == "il":

        C "Donc, comment es-tu tombé sur [A] malgré le démantèlement des robots ?"
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        C "Donc, comment es-tu tombée sur [A] malgré le démantèlement des robots ?"
        play sound "Click.mp3" noloop 

    P "Il y a 3 mois, je faisais de l'urbex avec un ancien ami à moi dans un entrepôt abandonné et il est tombé sur [A] en ouvrant un grand placard."
    play sound "Click.mp3" noloop 

    C "Je vois et que s'est-il passé ensuite ?"
    play sound "Click.mp3" noloop 

    P "On a eu un petit conflit."
    play sound "Click.mp3" noloop 

    C "Comment ça ?"
    play sound "Click.mp3" noloop 

    P "On s'est disputé car je voulais garder [A]..."
    play sound "Click.mp3" noloop 
    
    C "Oh je vois, qu'a-t-il dit par rapport à [A] ?"
    play sound "Click.mp3" noloop 

    P "Il a dit qu'elle ne m'appartenait pas mais je lui ai dit qu'elle était abandonnée."
    play sound "Click.mp3" noloop 

    C "C'est exact elle était abandonnée à ce moment-là."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Oui je me suis même renseigné sur les articles de loi concernant ça et j'en ai trouvés trois."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Oui je me suis même renseignée sur les articles de loi concernant ça et j'en ai trouvés trois."
        play sound "Click.mp3" noloop

    C "Quels sont ces fameux articles de loi ?"  
    play sound "Click.mp3" noloop  

    P "Le premier, c'est l'article 24, alinéa 1. Il stipule que tout objet abandonné devient la propriété de la personne qui le récupère."  
    play sound "Click.mp3" noloop  

    C "Le second ?"  
    play sound "Click.mp3" noloop  

    P "L'article 24, alinéa 2, précise que cette règle ne s'applique plus si le propriétaire initial réclame son bien. Toutefois, la restitution ne peut se faire que par négociation."  
    play sound "Click.mp3" noloop  

    C "Et le dernier ?"  
    play sound "Click.mp3" noloop  

    P "Enfin, l'article 24, alinéa 3, impose au nouveau propriétaire la responsabilité complète de l'objet récupéré, y compris son entretien ou sa gestion."  
    play sound "Click.mp3" noloop  

    E "Toi [prenom], tu respectes bien l'alinéa 3."  
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    C "Bien et sinon ton ami est devenu quoi maintenant ?"
    play sound "Click.mp3" noloop 

    P "Je ne sais pas mais je pense qu'il est dans un autre lycée."
    play sound "Click.mp3" noloop 

    C "Je voulais aussi savoir comment tu as amélioré [A] ?"
    play sound "Click.mp3" noloop 

    P "Le jour ou je l'ai trouvé j'ai remarqué qu'elle avait pas sa batterie mais par chance il en restait une toute neuve dans l'intrepêt."
    play sound "Click.mp3" noloop

    C "Ensuite qu'as-tu fait ?"
    play sound "Click.mp3" noloop 

    P "J'ai changé son processeur."
    play sound "Click.mp3" noloop 

    C "Ah bon pourtant le processeur choisi pour sa conception était bien." 
    play sound "Click.mp3" noloop 

    P "Oui mais actuellement il est trop faible pour les besoins d'[newname] actuels."
    play sound "Click.mp3" noloop 

    C "Ok je comprends mieux et qu'as-tu fait d'autres comme changements ?"
    play sound "Click.mp3" noloop 

    P "Je lui ai rajouté une carte mémoire."
    play sound "Click.mp3" noloop 

    C "Intéressant."
    play sound "Click.mp3" noloop 

    P "Merci beaucoup."
    play sound "Click.mp3" noloop 

    C "Il n'y a pas de soucis."
    play sound "Click.mp3" noloop 

    P "Vous voulez me demander quelque chose d'autre ?"
    play sound "Click.mp3" noloop 

    C "Oui une dernière chose."
    play sound "Click.mp3" noloop 

    P "Oui dites-moi."
    play sound "Click.mp3" noloop 

    C "Connais-tu l'entièreté des capacités de [A] ?"
    play sound "Click.mp3" noloop

    P "Non pas complétment à mon insu malheureusement."
    play sound "Click.mp3" noloop 

    C "Ok mais je pense que j'ai quelque chose qui peut t'intéresser."
    play sound "Click.mp3" noloop 

    P "Oui dites-moi."
    play sound "Click.mp3" noloop 

    C "Il se pourrait que j'aie encore les documents techniques originaux d'[A] que je pourrais te donner."
    play sound "Click.mp3" noloop 

    P "Vraiment !?"
    play sound "Click.mp3" noloop 
 
    C "Oui ils seront tous pour toi."
    play sound "Click.mp3" noloop

    "{b}{i}[C] sortit des documents.{/i}{/b}"
    play sound "Click.mp3" noloop

    C "Tiens les voici..."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Accepter les documents.{/i}{/b}" :

            $ renpy.block_rollback()

            $ success += 1
            $ quest11 += 1 

            show screen update with moveinright

            P "Merci beaucoup ça fait plaisir."
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

            C "De rien... mais avant qu'on termine notre entretien, j'aimerais te demander deux choses."
            play sound "Click.mp3" noloop

            P "Oui, je vous écoute."
            play sound "Click.mp3" noloop

            C "J'aimerais que [newname] s'éloigne un instant. Ce que j'ai à dire est... sensible."
            play sound "Click.mp3" noloop

            P "[newname], s'il te plaît... laisse-nous quelques minutes."
            play sound "Click.mp3" noloop

            Na "Bien sûr."
            play sound "Click.mp3" noloop

            "{b}{i}[newname] s'éloigne lentement, accompagnée de [E].{/i}{/b}"
            play sound "Click.mp3" noloop

            C "D'abord... je ne veux pas que tu partages ce qu'il y a dans ce document avec [newname]. Je veux qu'elle puisse repartir de zéro, sans ce poids."
            play sound "Click.mp3" noloop

            P "Je comprends... Je ne lui dirai rien."
            play sound "Click.mp3" noloop

            C "Merci. Vraiment... J'ai commis des actes immoraux pour créer [newname]. Et je ne veux pas qu'elle en porte la culpabilité."
            play sound "Click.mp3" noloop

            P "Qu'est-ce que vous avez fait exactement ?"
            play sound "Click.mp3" noloop

            C "Je l'ai conçue pour être... parfaite. La plus puissante. Testée dans des zones de guerre. Privée de liberté. Mais elle a fini par se rebeller. Elle a refusé d'obéir."
            play sound "Click.mp3" noloop

            P "Je comprends mieux maintenant. Mais... c'est monstrueux ce que vous lui avez fait subir."
            play sound "Click.mp3" noloop

            C "Oui, exactement. J'ai utilisé un protocole de réinitialisation avancé pour effacer ses souvenirs traumatisants. Mais je n'ai pas pu effacer les émotions qu'elle ressentait."
            play sound "Click.mp3" noloop 

            P "...Alors en réalité, elle vit dans un mensonge... mais peut-être que c'est mieux ainsi. Elle mérite de vivre libre, sans chaînes... même si son passé reste gravé en vous."
            play sound "Click.mp3" noloop

            C "Oui et enfin... j'aimerais te demander une dernière faveur."
            play sound "Click.mp3" noloop 

        "{b}{i} Refuser les documents. {/i}{/b}" : 

            $ renpy.block_rollback()

            P "Merci pour votre confiance… mais je préfère tourner la page et repartir sur de nouvelles bases."
            play sound "Click.mp3" noloop

            C "Je comprends. Tu as ce droit... Et peut-être que c'est mieux ainsi."
            play sound "Click.mp3" noloop

            C "Mais avant qu'on termine cet entretien, j'aimerais te demander une dernière chose."
            play sound "Click.mp3" noloop

    P "Oui dites-moi."
    play sound "Click.mp3" noloop 

    C "J'aimerais voir comment est [A] et son comportement actuel de mes propres yeux."
    play sound "Click.mp3" noloop 

    P "Il n'y a pas de soucis, [newname] approche s'il te plaît."
    play sound "Click.mp3" noloop 

    Na "Oui qu'y a-t-il [prenom] ?"
    play sound "Click.mp3" noloop 

    P "Je veux que tu te présentes à [C]."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    C "Donc je présume que tu es [Na]."
    play sound "Click.mp3" noloop 

    Na "Oui exactement."
    play sound "Click.mp3" noloop 

    C "Donc vas-y présente-toi."
    play sound "Click.mp3" noloop 

    Na "Je me nomme [Na], j'ai dix-huit ans et je suis la création de [P], je suis actuellement lycéenne en Terminale-E dans ce lycée, mon défaut est que je suis souvent sensible mais j'ai appris beaucoup de choses grâce à [P]."
    play sound "Click.mp3" noloop 

    C "Bien merci pour ta présentation."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    C "Bien [P] je vois qu'[newname] se débrouille bien avec toi."
    play sound "Click.mp3" noloop

    P "Merci ça fait plaisir."
    play sound "Click.mp3" noloop 

    C "Avant de partir j'ai encore un truc à te dire concernant [newname]."
    play sound "Click.mp3" noloop 

    P "Oui dites-moi, je vous écoute."
    play sound "Click.mp3" noloop 

    C "J'ai entendu dire que quelqu'un veut s'attaquer à [newname] donc fais attention."
    play sound "Click.mp3" noloop 

    E "Je confirme aussi car une personne m'a aussi dit qu'elle avait trouvé des informations concernant une potentielle menace ou traître envers [newname]."
    play sound "Click.mp3" noloop

    P "Et qui est cette personne ?"
    play sound "Click.mp3" noloop 

    E "Elle préfère rester anonyme pour le bien de ses travaux."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    E "Bien maintenant vous pouvez quitter mon bureau [prenom] et [newname]."
    play sound "Click.mp3" noloop 

    P "Merci au revoir."
    play sound "Click.mp3" noloop 

    stop music fadeout 2.0

    hide screen office with moveoutright
    scene black with fade 

    "{b}{i}Tu te diriges vers le hall avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright

    play music "Soundtrack.mp3" loop volume 1.0

    P "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop 

    Na "Oui pourquoi pas."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hall with moveoutright
    scene staircase with fade 

    "{b}{i}Tu continues vers le couloir avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    P "Bon on est bientôt arrivés."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Puis tu aperçois [I] juste devant.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt] Toi comment ça s'est passé avec [E] ?" 
    play sound "Click.mp3" noloop 

    P "Ça s'est bien passé, [E] voulait que je voie l'ancien président de Neogen Technologies qui voulait juste voir [newname]."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    I "[validation]"
    play sound "Click.mp3" noloop 

    P "[E] m'a aussi dit qu'il y aurait un traître parmi nous."
    play sound "Click.mp3" noloop 

    I "Un traître parmi nous !?"
    play sound "Click.mp3" noloop

    P "Oui et il y a aussi [C] qu'il serait une menace envers [newname]."
    play sound "Click.mp3" noloop

    I "Je vois, non je dois vous laisser."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    Na "À demain Yuna."
    play sound "Click.mp3" noloop 

    I "À demain les [nom]."
    play sound "Footsteps.mp3" noloop 

    "{b}{i}[I] retourne à son dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon il faut qu'on rentre au dortoir aussi." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu continues vers ton dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    Na "Oui ça fait du bien d'être de retour au dortoir après un examen, les cours et le rendez-vous." 
    play sound "Click.mp3" noloop 

    P "Oui je confirme."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon je vais me déconnecter."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon elle s'est déconnectée, je vais aller me chercher à manger." 
    play sound "Click.mp3" noloop 

    hide screen room with moveoutright 
    scene black with fade

    "{b}{i} Tu pars chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop

    if quest11 == 1:

        "{b}{i} Tu manges tranquillement pendant une demi-heure en regardant les documents que tu as eus.{/i}{/b}"
        play sound "Click.mp3" noloop 
        
        P "Bon voyons voir ces documents..." 
        play sound "Click.mp3" noloop 

        $ system = "AetherOS"
        $ robotorigine = "Danto/Neogen Technologies" 
        $ serie = "0012095NT" 

        P "Intéressant." 
        play sound "Click.mp3" noloop 

        "{b}{i}Tu continues de regarder pendant un petit moment.{/i}{/b}"
        play sound "Click.mp3" noloop 

    else: 

        "{b}{i} Tu manges tranquillement pendant une demi-heure.{/i}{/b}"
        play sound "Click.mp3" noloop

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Deux semaines plus tard, le 3 octobre 2097.{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 14
    $ points -= 2800
    $ stockage += 280.0 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te lèves tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon aujourd'hui je vais demander à [E] si je peux emprunter le gymnase."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te changes et t'approches de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

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
    P "[je_vais_bien_txt] J'ai bien dormi." 
    play sound "Click.mp3" noloop

    "{b}{i} [Na] change de tonalité.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "[prenom], je détecte une nouvelle mise à jour pas obligatoire, veux-tu la faire maintenant ou plus tard ?"
    play sound "Menu.mp3" noloop 

    menu: 

        "{b}{i} Refuser la mise à jour {/i}{/b}" :

            $ renpy.block_rollback()
            $ Na = Character('[newname] [nom]', color="#0066ff")

            P "Non merci."
            play sound "Click.mp3" noloop

            $ validation = get_random_validation() 
            Na "[validation]"
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
            $ quest12 += 1
            $ stockage += 5.0 
            $ update += 1.0 

            show screen update with moveinright

            Na "Mise à jour terminée, la version actuelle est maintenant la [update]."
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

    P  "Bon aujourd'hui je vais t'entraîner."
    play sound "Click.mp3" noloop 

    Na "Génial."
    play sound "Click.mp3" noloop 

    P "On y va ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    scene black with fade 

    "{b}{i} Vous quittez le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright 
    scene staircase with fade

    "{b}{i} Vous continuez vers le hall.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    if pronom == "il":

        P "Bon on est presque arrivés."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Bon on est presque arrivées." 
        play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene office with fade 
    show screen office with moveinright 

    P "Bonjour c'est moi [prenom]."
    play sound "Click.mp3" noloop

    E "Oh que puis-je faire pour toi ?"
    play sound "Click.mp3" noloop

    P "J'aimerais savoir si je peux emprunter le gymnase pour la matinée."
    play sound "Click.mp3" noloop

    E "Bien sûr mais puis-je savoir pour quelle raison ?"
    play sound "Click.mp3" noloop 

    P "Pour entraîner [newname]."
    play sound "Click.mp3" noloop 

    E "Ok alors il n'y a pas de soucis."
    play sound "Click.mp3" noloop 

    "{b}{i}[E] te remet la clé du gymnase.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    E "[nothing]"
    play sound "Click.mp3" noloop

    hide screen office with moveoutright 
    scene black with fade 

    "{b}{i} Puis tu quittes le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright 

    P "Bon voyons voir où se trouve le gymnase."
    play sound "Click.mp3" noloop 
    
    Na "Il me semble qu'il se trouve à l'ouest du campus."
    play sound "Click.mp3" noloop 

    P "Allons-y alors."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hall with moveoutright
    scene black with fade 

    "{b}{i} Tu arrives enfin au gymnase.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene gymnase with fade 
    show screen gymnase with moveinright

    P "Bon par quoi on commence ?"
    play sound "Click.mp3" noloop

    Na "Je ne sais pas vraiment c'est toi qui sais."
    play sound "Click.mp3" noloop 

    "{b}{i} Pendant que tu continues de réfléchir, [N] et [Y] entrèrent dans le gymnase.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    Y "[comment_ca_va]"
    play sound "Click.mp3" noloop

    P "Oh salut [Y], oui ça va bien et toi ?"
    play sound "Click.mp3" noloop 

    Y "Ça va bien."
    play sound "Click.mp3" noloop 

    P "Cool sinon vous faites quoi ici ?"
    play sound "Click.mp3" noloop 

    Y "Je suis venue voir le gymnase avec [N] car on n'a pas eu l'occasion de le faire."
    play sound "Click.mp3" noloop 

    N "Oui on s'est dit que ce serait une bonne idée de venir voir durant notre temps libre."
    play sound "Click.mp3" noloop 

    P "Intéressant."
    play sound "Click.mp3" noloop 

    Y "Sinon je te retourne la question, toi tu fais quoi ici ?"
    play sound "Click.mp3" noloop 

    if pronom == "il": 
        
        P "Je suis venu entraîner [newname], pourquoi tu me demandes ça ?"
        play sound "Click.mp3" noloop 

    elif pronom == "elle":

        P "Je suis venue entraîner [newname], pourquoi tu me demandes ça ?"
        play sound "Click.mp3" noloop 

label conversation:

    Y "Aussi, juste pour savoir... Bon, je sais que c'est important de le faire pour mon domaine et je pense aussi pour le tien, mais tu penses à faire les mises à jour de sécurité de [newname] ?"
    play sound "Click.mp3" noloop

    if update == 1.0:

        P "Il y avait une mise à jour, mais je ne l'ai pas faite. Je me suis dit que je pouvais attendre..."
        play sound "Click.mp3" noloop

        Y "C'est de l'obsolescence volontaire, l'une des dix règles de l'informatique à ne pas briser, tu devrais la faire, la sécurité d'[newname] est en jeu."
        play sound "Click.mp3" noloop 

        P "Oui, promis, je la ferai."
        play sound "Click.mp3" noloop 

    else: 

        P "Oui, j'en avais une ce matin et je l'ai faite."
        play sound "Click.mp3" noloop
        jump suite 

label suite:

    Y "Cool alors."
    play sound "Click.mp3" noloop

    N "Bon, nous, on va y retourner."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Y "[validation]"
    play sound "Footsteps.mp3" noloop 

    "{b}{i}[N] et [Y] quittèrent le gymnase.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon, où en étions-nous déjà ?"
    play sound "Click.mp3" noloop 

    Na "Je ne sais plus." 
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez l'entraînement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je pense qu'on a fini pour cette matinée."
    play sound "Click.mp3" noloop 

    Na "Ok mais on peut aller manger maintenant j'ai faim."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen gymnase with moveoutright
    scene black with fade

    "{b}{i} Vous quittez le gymnase.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    P "Bon on se dépêche d'aller au réfectoire si tu veux manger."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade 
    show screen lunchroom with moveinright

    if pronom == "il":

        P "Enfin arrivés..."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 
 
        P "Enfin arrivées..."
        play sound "Click.mp3" noloop 

    Na "Oui j'ai vraiment faim."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous voyez [N] et [Y] à une table en train de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [N] et [Y]."
    play sound "Click.mp3" noloop 

    N "Oh salut [prenom]."
    play sound "Click.mp3" noloop

    P "On peut venir manger avec vous ?"
    play sound "Click.mp3" noloop 

    Y "Oui bien sûr avec plaisir."
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    Na "Oui merci beaucoup."
    play sound "Click.mp3" noloop 

    Y "Mais de rien c'est normal entre camarades."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous vous asseyez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Sinon vous discutiez de quoi ?"
    play sound "Click.mp3" noloop 

    N "Pas grand-chose, nous parlions juste de certains élèves."
    play sound "Click.mp3" noloop 

    P "Ok je vois."
    play sound "Click.mp3" noloop 

    Y "Bien sinon comment ça s'est passé au gymnase ?" 
    play sound "Click.mp3" noloop 

    P "Ça s'est bien passé."
    play sound "Click.mp3" noloop 

    Y "Cool je suis content pour toi et je vois aussi qu'[newname] s'est vraiment améliorée."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Y "[nothing]" 
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez mais elle veut te demander quelque chose.{/i}{/b}"
    play sound "Click.mp3" noloop

    Y "Je peux demander quelque chose à [newname] pour tester ses connaissances ?"
    play sound "Click.mp3" noloop 
    
    P "Bien sûr vas-y"
    play sound "Click.mp3" noloop 

    Y "Bien maintenant [newname] je veux que tu me cites toutes les décimales de pi que tu connais."
    play sound "Click.mp3" noloop 

    Na "Ok vas-y, 3.141592653589793238."
    play sound "Click.mp3" noloop 

    Y "Woah je suis vraiment surprise que tu connaisses autant de décimales de pi."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    "{b}{i} [Y] se mit à te regarder.{/i}{/b}"
    play sound "Click.mp3" noloop

    Y "Franchement tu as vraiment appris beaucoup de choses à [newname]."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    P "Bon on y va [newname] ?" 
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hall with fade 
    show screen hall with moveinright 

    P "Bon on va où ?"
    play sound "Click.mp3" noloop 

label choice10:

    Na "Je crois qu'on a cours cette après-midi."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} aller en cours.{/i}{/b}" :
            jump suite1

        "{b}{i} aller à la bibliothèque.{/i}{/b}" : 

            hide screen hall with moveoutright
            scene black with fade

            "{b}{i}Tu entres dans la bibliothèque.{/i}{/b}"
            play sound "Door.mp3" noloop  
            
            scene library with fade 
            show screen library with fade

            Na "Je ne suis pas sûre que c'est le moment d'être ici."
            play sound "Click.mp3" noloop   

            hide screen library with moveoutright
            scene black with fade 

            "{b}{i}Tu quittes la pièce.{/i}{/b}" 
            play sound "Door.mp3" noloop    

            scene hall with fade 
            show screen hall with moveinright 

            jump choice10

label suite1:
    
    P "Ok allons-y alors."
    play sound "Click.mp3" noloop 
     
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene staircase with fade

    "{b}{i}Tu montes au premier étage avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i}Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en .{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    H "Oh salut [prenom]"
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    H "[je_vais_bien_txt] Sinon toi et [newname] ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Merci beaucoup." 
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    H "[nothing]"
    play sound "Click.mp3" noloop

    P "Sinon tu sais où est la [T] ?"
    play sound "Click.mp3" noloop 

    H  "Je ne sais pas mais je pense qu'elle ne va pas tarder à venir."
    play sound "Door.mp3" noloop
    
    "{b}{i} Puis la [T] entra dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour chers lycéens."
    play sound "Click.mp3" noloop

    H "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    Na "Bonjour~"
    play sound "Click.mp3" noloop 

    I "Bonjour."
    play sound "Click.mp3" noloop

    N "Bonjour."
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
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    M "Bien aujourd'hui j'ai plusieurs choses à vous dire pour commencer."
    play sound "Click.mp3" noloop

    K "Quoi comme informations ?"
    play sound "Click.mp3" noloop

    M "J'ai entendu dire par le biais d'[E] qu'il y aurait un traître dans ce lycée."
    play sound "Click.mp3" noloop

    K "Un traître ?"
    play sound "Click.mp3" noloop

    H "Comment ça un traître ?"
    play sound "Click.mp3" noloop

    K "Bon je fais le surpris mais j'avais déjà remarqué que quelque chone n'allais pas."
    play sound "Click.mp3" noloop

    P "Oui j'ai déjà eu l'information mais il semblerait qu'un des lycéens en veut à [newname]."
    play sound "Click.mp3" noloop

    I "Pardon !? Ce doit sûrement être [J]...."
    play sound "Click.mp3" noloop

    J1 "Hey j'ai peut-être été méchante avec [newname] mais je promets que ce n'est pas moi !"
    play sound "Click.mp3" noloop

    J2 "Oui ce n'est pas moi non plus."
    play sound "Click.mp3" noloop 

    P "Oui [I], actuellement on ne peut les accuser vu le peu d'information qu'on a."
    play sound "Click.mp3" noloop 

    M "Je suis d'accord avec toi [prenom]."
    play sound "Click.mp3" noloop

    P "Merci."
    play sound "Click.mp3" noloop

    M "Bon maintenant je vais vous dire la seconde information."
    play sound "Click.mp3" noloop 

    P "Oui dites-nous madame"
    play sound "Click.mp3" noloop

    M "À partir d'aujourd'hui nous allons accueillir un nouvel élève."
    play sound "Click.mp3" noloop 

    I "Qui est ce lycéen ?"
    play sound "Click.mp3" noloop

    P "Oui on veut savoir."
    play sound "Click.mp3" noloop 

    M "Deux secondes je vais le laisser entrer et se présenter."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    I "[validation]" 
    play sound "Click.mp3" noloop 

    stop music fadeout 2.0  

    "{b}{i} [M] fait signe au lycéen de rentrer. {/i}{/b}"
    play sound "Door.mp3" noloop

    $ S = Character('Subaru Shinomiya', color="#ff8800")
    play music "Soundtrack2.mp3" loop volume 1.0  
 
    R "Bonjour à tous."
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    I "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks() 
    R "[thanks]"
    play sound "Click.mp3" noloop

    M "Vas-y présente-toi."
    play sound "Click.mp3" noloop

    S "Je m'appelle [S], l'inégalable étudiant et ancien élève de [origine], j'ai dix-neuf ans ravi de vous rencontrer"
    play sound "Click.mp3" noloop

    $ ultimate1 = "l'inégalable étudiant" 

    P "[S] !? Je croyais que tu étais dans un autre lycée depuis la dernière fois qu'on s'est vu !"
    play sound "Click.mp3" noloop

    I "Tu es aussi de [origine] !?" 
    play sound "Click.mp3" noloop  

    S "Oui c'est exact."
    play sound "Click.mp3" noloop 

    "{b}{i}[S] regarde autour de la salle et tombe sur toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Oh c'est toi [prenom] et pour répondre à ta question, oui c'était le cas."
    play sound "Click.mp3" noloop 

    P "Mais tu fais quoi ici alors ?"
    play sound "Click.mp3" noloop 

    S "J'ai dû déménager avec ma mère du coup j'ai dû changer de lycée."
    play sound "Click.mp3" noloop 

    P "Ok je vois." 
    play sound "Click.mp3" noloop 

    S "Je vois que tu as encore l'autre [A] avec toi."
    play sound "Click.mp3" noloop 

    P "Hey un peu de respect elle a un prénom et un nom maintenant."
    play sound "Click.mp3" noloop 

    S "Oups désolé."
    play sound "Click.mp3" noloop 

    "{b}{i}[S] s'adresse à [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Pourrais-je savoir comment tu t'appelles maintenant ?"
    play sound "Click.mp3" noloop 

    Na "Je m'appelle [newname], [Na]."
    play sound "Click.mp3" noloop

    S "Enchanté [newname]"
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop
    
    $ nothing = get_random_nothing()
    S "[nothing]" 
    play sound "Click.mp3" noloop

    I "Donc c'est toi l'ami de [prenom]."
    play sound "Click.mp3" noloop 

    S "Oui exactement."
    play sound "Click.mp3" noloop 

    I "Cool alors."
    play sound "Click.mp3" noloop 

    M "Dernière information, aujourd'hui vous recevrez votre budget du mois."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "Bien maintenant reprenons le cours, [S] je t'invite à prendre place au fond de la salle il reste une place."
    play sound "Click.mp3" noloop

    S "Merci beaucoup madame."
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Pendant que [S] se dirige vers sa place il te chuchote quelque chose.{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Toi et moi on a une discussion à finir...."
    play sound "Click.mp3" noloop 

    P "Euh....."
    play sound "Click.mp3" noloop 

    "{b}{i}La [T] reprend le cours.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon sortez vos livres à la page 20, nous allons reprendre notre cours de la dernière fois."
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    P "Bon [newname] on y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui je suis fatiguée."
    play sound "Click.mp3" noloop 

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    P "Bon cette journée est enfin finie..."
    play sound "Click.mp3" noloop 

    "{b}{i}Mais soudainement [S] t'interpelle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    S "Hey [P], Je peux te parler deux minutes."
    play sound "Click.mp3" noloop 

    P "Qu'est-ce que tu me veux Subaru ?"
    play sound "Click.mp3" noloop 

    S "C'est concernant [newname]."
    play sound "Click.mp3" noloop 

    P "Il n'y a quoi encore ?"
    play sound "Click.mp3" noloop 

    S "J'aimerais savoir pourquoi tout le monde apprécie [newname] ?"
    play sound "Click.mp3" noloop 
 
    P "Car elle est sympa et bienveillante."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        S "Comment en es-tu arrivé là ?"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        S "Comment en es-tu arrivée là ?"
        play sound "Click.mp3" noloop

    P "Je dirai que c'est de la détermination et de l'ingéniosité."
    play sound "Click.mp3" noloop 

    S "Je te hais vraiment aujourd'hui, saches-le."
    play sound "Click.mp3" noloop 

    P "Mais pourquoi !?"
    play sound "Click.mp3" noloop 
 
    S "Tu te souviens qu'on était à [origine] à l'époque ?" 
    play sound "Click.mp3" noloop 

    P "Oui pourquoi ?"
    play sound "Click.mp3" noloop 

    S "à [origine] j'étais le meilleur et tout le monde m'acclamait pendant que tu restais dans ton coin."
    play sound "Click.mp3" noloop 

    P "Oui et alors ?"
    play sound "Click.mp3" noloop 

    S "Depuis que tu as découvert [newname] j'ai perdu une partie de ma popularité car soit disant j'était une fraude."
    play sound "Click.mp3" noloop 

    P "Et alors personnellement ça ne me concerne pas."
    play sound "Click.mp3" noloop 

    S "Même quand je suis allé à Lexus après avoir finis mon cursus à [origine], cette histoire m'a suivi."
    play sound "Click.mp3" noloop 

    P "Ok je vois maintement."
    play sound "Click.mp3" noloop 

    S "Tu comprends maintenant pourquoi je dêteste."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Désolé je ne voulais pas te causer ça."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Désolée je ne voulais pas te causer ça."
        play sound "Click.mp3" noloop 

    S "Ouais ouais bon je te laisse je dois y aller."
    play sound "Click.mp3" noloop 

    P "Ok à plus tard." 
    play sound "Footsteps.mp3" noloop  

    "{b}{i}[S] s'éloigna pour aller à son dortoir et en même [J1] vient vers toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    J1 "Hey salut [prenom] je veux juste m'excuser pour tous ce que j'ai dit à [newname]..."
    play sound "Click.mp3" noloop  

    Na "[J1] désolée mais ce n'est vraiment pas le moment de discuter, [prenom] vient d'avoir une discussion douloureuse avec [S]."
    play sound "Click.mp3" noloop 

    J1 "Oh désolée je ne voulais pas déranger." 
    play sound "Click.mp3" noloop  

    Na "Ok pas de soucis mais tu devrais partir d'ici." 
    play sound "Footsteps.mp3" noloop  

    "{b}{i}[J1] s'éloigne aussitôt.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon [prenom] on part au dortoir." 
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Bon je ne sais pas quoi faire maintenant." 
    play sound "Click.mp3" noloop  

    Na "Tu pouurais te renseigner sur cette histoire de traître." 
    play sound "Click.mp3" noloop  

    P "Oui mais le problème c'est qu'on n'a aucune information." 
    play sound "Click.mp3" noloop  

    Na "Je vois, bon moi je vais me déconnecter, à demain." 
    play sound "Click.mp3" noloop  

    P "Ok à demain [newname]." 
    play sound "Click.mp3" noloop  

    # à modifier

    "{b}{i}Puis [newname] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh je vois que j'ai reçu mon budget." 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 4 octobre 2097 {/i}{/b}"
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

    "{b}{i} Tu te léves tranquillement et te changes tranquillement et pars voir [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 
    
    P "Je vais la démarrer sinon on va étre en retard"
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

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
    Na "[je_vais_bien_txt] Et toi sinon ça va ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    Na "Cool mais juste hier j'avais oublié de te dire un truc."
    play sound "Click.mp3" noloop

    P "Oui dit-moi, je t'écoute"
    play sound "Click.mp3" noloop

    Na  "Tu sais [prenom] tu t’occupes tellement bien de moi que je pourrais te surnommer Undertaker."
    play sound "Click.mp3" noloop 

    P "Undertaker !?"
    play sound "Click.mp3" noloop

    Na "Oui c'est bien ça."
    play sound "Click.mp3" noloop

    P "Merci beaucoup ça fait plaisir de l'entendre."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Na "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon on doit aller en cours avant d'étre en retard."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    P "Bien alors allons-y."
    play sound "Click.mp3" noloop

    hide screen room with moveoutright
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Tu continues vers la salle de classe mais tu croises [S].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [S]."
    play sound "Click.mp3" noloop

    S "Oh salut [prenom]......"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    S "ça va..."
    play sound "Footsteps.mp3" noloop

    "{b}{i} [S] ignore la discussion et part en classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu sais ce qu'il a ou pas ?"
    play sound "Click.mp3" noloop

    Na "Je n'en ai aucune idée."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    P "Salut..."
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    Hi "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    Hi "Cool alors..."
    play sound "Door.mp3" noloop
    
    "{b}{i}Puis la [T] entre dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    M "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Hi"[salutation_rdm]"
    play sound "Click.mp3" noloop 

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

    M "Bon aujourd'hui nous allons voir un nouveau sujet grammaire et je m'excuse [S] si tu as ratée le sujet sur la guerre."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    S "Il n'y a pas soucis de toute façon j'avais déjà vu ce sujet à Lexus."
    play sound "Click.mp3" noloop

    M "Au temps pour moi alors."
    play sound "Click.mp3" noloop

    S "Il n'y a pas de soucis."
    play sound "Click.mp3" noloop

    M "Bon Commençons, sortez vos livres de mathématique page 15."
    play sound "Click.mp3" noloop

    M "Le cours d'aujourd'hui sera sur le théorème de Pythagore." 
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "Bon qui peut me dire ce qu'est le théorème de Pythagore ?"
    play sound "Click.mp3" noloop 

    I "moi s'il vous plaît."
    play sound "Click.mp3" noloop

    M "Bien expliques-nous."
    play sound "Click.mp3" noloop

    I "Le théorème de Pythagore permet de trouver la valeur de l'hypothénuse apartir des deux plus petits cotés d'un triangle."
    play sound "Click.mp3" noloop
    
    M "Excellent sinon qui peut me donner la formule de calcul ?"
    play sound "Click.mp3" noloop

    Na "Moi s'il vous plaît."
    play sound "Click.mp3" noloop

    M "Bien expliques-nous."
    play sound "Click.mp3" noloop 

    Na "Il suffit d'additionner les carrés des deux plus petits cotés puis faire la racine du résultat pour trouver l'hypothénus."
    play sound "Click.mp3" noloop

    M "Bien merci pour cette explication."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop
 
    "{b}{i}Puis la [T] commence à écrire sur le tableau.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bon si le premier coté fait 5 centimètres et le deuxième 12 centimètres, que vaut l'hypothénuse ?"
    play sound "Click.mp3" noloop

    "{b}{i} Tous les élèves se mettent à réfléchir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bon qui peut me donner la réponse ?"
    play sound "Click.mp3" noloop

    Na "Moi s'il vous plait"
    play sound "Click.mp3" noloop

    M "Bien je t'écoute"
    play sound "Click.mp3" noloop

    Na "Le résultat de l'hypothéuse est 13 centimétres."
    play sound "Click.mp3" noloop

    M "Exact bien trouvé."
    play sound "Click.mp3" noloop

    Na "Merci."
    play sound "Click.mp3" noloop

    M "Bien maintenant que vous avez compris, je vous laisse faire les exercices à la page 16."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    S "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Tous les élèves se mettent à faire les exercices.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon voyons voir....."
    play sound "Click.mp3" noloop 

    "{b}{i} Une heure plus tard.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway 
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plaisir."
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
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Click.mp3" noloop

    scene black with fade 
    hide screen WC with moveoutright

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

    M "Bien reprenez les exercices et demandez-moi de l'aide si vous avez besoin d'aide."
    play sound "Click.mp3" noloop

    S "On n'aura pas besoin d'aide madame on est quand même l'élite"
    play sound "Click.mp3" noloop

    I "[S], tu ferais pas un peu le surdoué par hasard ?"
    play sound "Click.mp3" noloop

    S "Euh......"
    play sound "Click.mp3" noloop

    M "Evitez de bavarder."
    play sound "Click.mp3" noloop

    S "Oui madame."
    play sound "Click.mp3" noloop

    "{b}{i}Le cours continue sans probléme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    P "Bon [newname] on va manger ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Tu continues vers le rez de chaussée.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade 

    "{b}{i} Tu continues vers le hall.{i}{/b}"
    play sound "Click.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Tu continues vers le réféctoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Tu entres dans le réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen lunchroom with moveinright

    if pronom == "il":

        P "Enfin arrivés..."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 
 
        P "Enfin arrivées..."
        play sound "Click.mp3" noloop 

    Na "Oui j'ai vraiment faim."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allaz chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allez vous rejoindre [I] pour manger.{/i}{/b}"
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

    "{b}{i} Puis soudainement [S] viens vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oui qu'est-ce que tu veux ?"
    play sound "Click.mp3" noloop 

    S "Je voulais savoir si je pouvais venir manger avec vous ? Car vous êtez les seules personnes que je connaisse."
    play sound "Click.mp3" noloop 

    Na "Euh....."
    play sound "Click.mp3" noloop 

    P "Tu veux vraiment être avec nous !?"
    play sound "Click.mp3" noloop 

    S "Oui car je ne connais personne d'autres."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Accepter [S]{/i}{/b}" :
    
            $ renpy.block_rollback()
            $ success += 1
            $ quest13 += 1

            show screen update with moveinright

            P "Bien sûr viens t'asseoir avec nous."
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

            Na  "Vraiment ?"
            play sound "Click.mp3" noloop 

            P "Oui pourquoi pas."
            play sound "Click.mp3" noloop      

            Na "Ok alors c'est toi qui vois"
            play sound "Click.mp3" noloop 

            S "Merci beuucoup."
            play sound "Click.mp3" noloop 

            $ nothing = get_random_nothing()
            P "[nothing]"
            play sound "Click.mp3" noloop

            "{b}{i} Vous vous mettez à discuter des cours.{/i}{/b}"
            play sound "Click.mp3" noloop

            I  "Sinon vous pensez qu'on aura quoi comme cours cette après-midi ?"
            play sound "Click.mp3" noloop 

            Na "Je ne sais pas mais je pense qu'on aura encore cours de math."
            play sound "Click.mp3" noloop 

            S "Math encore !?"
            play sound "Click.mp3" noloop 

            P "Oui c'est très probable."
            play sound "Click.mp3" noloop 

            $ validation = get_random_validation() 
            S "[validation]"
            play sound "Click.mp3" noloop 

            "{b}{i} Vous continuez de discuter des cours jusqu'à la sonnerie.{/i}{/b}"
            play sound "Bell.mp3" noloop

            I "Bon on retourne en classe ?"
            play sound "Click.mp3" noloop 

            $ validation = get_random_validation() 
            S "[validation]"
            play sound "Click.mp3" noloop    

            $ validation = get_random_validation() 
            P "[validation]"
            play sound "Click.mp3" noloop 

            Na "Ok allons-y"
            play sound "Click.mp3" noloop 

        "{b}{i} Refuser [S]{/i}{/b}" : 

            $ renpy.block_rollback()

            if pronom == "il":

                P "Désolé mais je préfére rester avec [newname] et [I]"
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                P "Désolée mais je préfére rester avec [newname] et [I]"
                play sound "Click.mp3" noloop  

            S "Ok alors je comprend c'est ton choix."
            play sound "Click.mp3" noloop 

            "{b}{i} Puis [S] s'éloigna et s'asseoit à une autre table.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Il est enfin parti."
            play sound "Click.mp3" noloop 

            Na "Oui enfin."
            play sound "Click.mp3" noloop 

            "{b}{i} Vous vous mettez à discuter des cours.{/i}{/b}"
            play sound "Click.mp3" noloop

            I  "Sinon vous pensez qu'on aura quoi comme cours cette après-midi ?"
            play sound "Click.mp3" noloop 

            Na "Je ne sais pas mais je pense qu'on aura encore cours de math."
            play sound "Click.mp3" noloop 

            P "ça m'etonnerai qu'on aie encore math."
            play sound "Click.mp3" noloop            

            "{b}{i} Vous continuez de discuter des cours jusqu'à la sonnerie.{/i}{/b}"
            play sound "Bell.mp3" noloop

            I "Bon on retourne en classe ?"
            play sound "Click.mp3" noloop 

            $ validation = get_random_validation() 
            P "[validation]"
            play sound "Click.mp3" noloop 

            Na "Ok allons-y"
            play sound "Click.mp3" noloop 

    hide screen lunchroom with moveoutright
    scene black with fade

    "{b}{i}Tu te diriges vers le hall.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le premier étage.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hall with moveoutright
    scene staircase with fade 

    "{b}{i}Tu continues vers le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i}Tu continue vers la salle de la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
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

    M "Aujourd'hui dans ce cours nous allons faire quelques chose de spécial."
    play sound "Click.mp3" noloop 

    I "Quoi exactement ?"
    play sound "Click.mp3" noloop 

    P "Oui quoi exactement ?"
    play sound "Click.mp3" noloop 

    Na "On peut savoir ?"
    play sound "Click.mp3" noloop 

    M "On va faire un débat sur les intelligences artificielles et les robots humanoides."
    play sound "Click.mp3" noloop 

    J1 "Vraiment un débat sur ça."
    play sound "Click.mp3" noloop 

    J2 "Oui ça peut être intéressant."
    play sound "Click.mp3" noloop 

    "{b}{i}La [T] commença à écrire sur le tableau.{/i}{/b}"
    play sound "Click.mp3" noloop 
    
    M "Bon j'aimerai que vous déplacez les tables pour avoir de l'espace."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous mettez à déplacer les tables et les chaises.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bien maintenant pour commencer j'aimerai que tous ceux qui sont pour ces innovations se mettent à droite et ceux qui sont contre se mettent à gauche."
    play sound "Click.mp3" noloop 

    P "Ok alors bon je sais déja que je suis pour."
    play sound "Click.mp3" noloop 

    Na "Madame si jamais je ne donnerai pas mon vote vue que je suis déjà un [model]."
    play sound "Click.mp3" noloop 

    M "Ok c'est compréhensible." 
    play sound "Click.mp3" noloop 

    J1 "Au moins ça fera un vote en moins."
    play sound "Click.mp3" noloop 

    P "Tu n'es pas drôle [J1]..."
    play sound "Click.mp3" noloop 

    J1 "Oh c'est bon."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde choisi son camp.{/i}{/b}"
    play sound "Click.mp3" noloop   

    M "Bien voyons voir quel camp vous avez choisi."
    play sound "Click.mp3" noloop 

    M "D'abord le camp qui s'oppose à ces innovations."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes le camp d'en face et tu vois [J1], [J2], [S] et [K]{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Pardon [K], toi aussi tu t'opposes à ces innovations !?"
    play sound "Click.mp3" noloop

    K "[newname] est l'exception je l'apprécie bien mais en générale je ne suis pas pour ces technologies."
    play sound "Click.mp3" noloop

    P "Ok je vois."
    play sound "Click.mp3" noloop 

    M "Bien maintenant voyons le camp qui sont pour ces innovations."
    play sound "Click.mp3" noloop 
 
    "{b}{i}Tu regardes ton camp et tu vois les autres qui sont dans avec toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "On dirait qu'il y a 6 lycéens qui sont pour ces innovations."
    play sound "Click.mp3" noloop 

    M "Donc ça fait 6 qui sont pour et 4 qui sont contre."
    play sound "Click.mp3" noloop 

    J1 "Sérieusement..."
    play sound "Click.mp3" noloop 

    M "Oui."
    play sound "Click.mp3" noloop 

    J1 "Ok je vois."
    play sound "Click.mp3" noloop

    M "Bien maintenant j'aimerai que chaque camp choisisse quelqu'un pour débattre dans chaque camp."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu commences à discuter pour savoir qui choisir.{/i}{/b}"
    play sound "Click.mp3" noloop   

    play music "Soundtrack2.mp3" loop volume 1.0

    P "Bon on choisi qui pour débattre ?"
    play sound "Click.mp3" noloop 

    I "Je ne sais pas, tu as une idée [Y] ?"
    play sound "Click.mp3" noloop 

    Y "je pense savoir qui choisir..."
    play sound "Click.mp3" noloop 

    H "Ah bon c'est qui ? "
    play sound "Click.mp3" noloop  

    N "Oui dit-nous."
    play sound "Click.mp3" noloop 

    Hi "On veut savoir."
    play sound "Click.mp3" noloop 

    Y "Je pense que la réponse est évidente."
    play sound "Click.mp3" noloop 

    I "Vraiment !?"
    play sound "Click.mp3" noloop 

    Y "Oui il faudrait choisir [prenom]."
    play sound "Click.mp3" noloop 

    N "Oui c'est vrai [pronom] a déjà de l'experience avec ces sujets."
    play sound "Click.mp3" noloop 

    I "Oui je confirme."
    play sound "Click.mp3" noloop 

    Y "Donc c'est décidé, [prenom] tu seras choisi."
    play sound "Click.mp3" noloop 

    P  "OK vous pouvez compter sur moi pour gagner ce débat."
    play sound "Click.mp3" noloop 

    Y "Bien alors."
    play sound "Click.mp3" noloop 

    I "Madame c'est bon nous avons choisi."
    play sound "Click.mp3" noloop 

    M "Bien et vous de votre coté ?"
    play sound "Click.mp3" noloop 

    J1 "Nous aussi nous avons choisi."
    play sound "Click.mp3" noloop 

    M "Bien."
    play sound "Click.mp3" noloop 

    J1 "On va vous battre dans ce débat."
    play sound "Click.mp3" noloop 

    M "Bien les personnes dans chaque équipe ont été choisis."
    play sound "Click.mp3" noloop 

    M "Dans ce débat sera entre [P] et [S]."
    play sound "Click.mp3" noloop 

    I "Les deux anciens élèves de [origine] qui s'affrontent, ça risque d'être intéressant."
    play sound "Click.mp3" noloop 

    Y "Oui je confirme."
    play sound "Click.mp3" noloop  

################################################################################################################

label debate:

    M "Bon, [S], tu commences. Dis-nous pourquoi tu es contre les robots humanoïdes."
    play sound "Click.mp3" noloop 

    S "Pour commencer, je pense que les robots humanoïdes ne servent qu'à faire des calculs mathématiques ou exécuter des tâches basiques. Rien de plus."
    play sound "Menu.mp3" noloop 

    menu:

        "{b}{i}Ils peuvent aider dans les cours{/i}{/b}":

            $ renpy.block_rollback()

            P "Ce n’est pas vrai. Ils peuvent aussi assister les élèves pendant les cours."
            play sound "Click.mp3" noloop 

            S "Dans les cours ? Tu plaisantes ?"
            play sound "Click.mp3" noloop 

            P "Pas du tout. Imagine un robot qui peut t’expliquer un exercice complexe, ou t’aider à réviser la veille d’un examen."
            play sound "Click.mp3" noloop 

            S "Mais... ce ne serait pas de la triche ?"
            play sound "Click.mp3" noloop 

            P "Pas si tu l’utilises comme un assistant, pas comme une machine à réponses."
            play sound "Click.mp3" noloop            

            S "Mouais... Je ne suis pas convaincu."
            play music "gameover.mp3" noloop

            jump debate_failed

        "{b}{i}Ils sont utiles dans plusieurs domaines{/i}{/b}":

            P "OBJECTION !"
            play sound "Click.mp3" noloop 

            S "Hein ?!"
            play sound "Click.mp3" noloop 

            P "Les robots humanoïdes peuvent être utiles dans une multitude de domaines, pas seulement pour les calculs."
            play sound "Click.mp3" noloop 

            S "Ah oui ? Comme quoi par exemple ?"
            play sound "Click.mp3" noloop 

            menu:

                "{b}{i}Dans le domaine militaire{/i}{/b}":

                    $ renpy.block_rollback()

                    P "Par exemple, ils peuvent intervenir dans les zones de guerre, pour désamorcer des bombes ou protéger des civils."
                    play sound "Click.mp3" noloop 

                    S "Donc... tu proposes d'utiliser des machines pour faire la guerre ?"
                    play sound "Click.mp3" noloop 

                    P "Non, je parle de protection, pas d'attaque. Ils peuvent sauver des vies là où c’est trop dangereux pour des humains."
                    play sound "Click.mp3" noloop 

                    S "Hmm... j’ai du mal à adhérer à ça."
                    play music "gameover.mp3" noloop

                    jump debate_failed

                "{b}{i}Dans l’administration{/i}{/b}":

                    $ renpy.block_rollback()

                    P "Ils peuvent aussi être utilisés dans l’administration, pour traiter des formulaires, gérer des dossiers ou automatiser des processus chronophages."
                    play sound "Click.mp3" noloop 

                    S "Je vois, mais si les robots font tout ça... que deviendront les emplois humains ?"
                    play sound "Click.mp3" noloop 

                    menu:

                        "{b}{i}Répondre sur l’emploi{/i}{/b}":

                            P "Bonne question. En réalité, on ne perd pas des emplois, on en crée de nouveaux."
                            play sound "Click.mp3" noloop 

                            S "Tu peux m’expliquer ?"
                            play sound "Click.mp3" noloop 

                            P "Par exemple, il faudra des techniciens pour entretenir ces robots, des ingénieurs pour les améliorer, des spécialistes pour les programmer..."
                            play sound "Click.mp3" noloop 

                            S "D’accord, mais un robot reste une machine qui obéit. Et s’il se retourne contre son créateur ?"
                            play sound "Click.mp3" noloop 

                            menu:

                                "{b}{i}Contester et nuancer{/i}{/b}":

                                    P "Les modèles les plus avancés sont capables d'apprendre, d'adapter leur comportement, voire de développer une forme de conscience artificielle contrôlée."
                                    play sound "Click.mp3" noloop 

                                    if pronom == "il":

                                        S "Tu es sérieux ?"
                                        play sound "Click.mp3" noloop 

                                    elif pronom == "elle":

                                        S "Tu es sérieuse ?"
                                        play sound "Click.mp3" noloop 

                                    P "Absolument."
                                    play sound "Click.mp3" noloop 

                                    S "Alors prouve-le."
                                    play sound "Click.mp3" noloop 

                                    $ validation = get_random_validation() 
                                    P "[validation]"
                                    play sound "Click.mp3" noloop 

                                    menu:

                                        "{b}{i}Expliquer au tableau{/i}{/b}":

                                            $ renpy.block_rollback()

                                            P "Regarde."
                                            play sound "Click.mp3" noloop 

                                            "{b}{i}Tu expliques au tableau, schéma à l'appui...{/i}{/b}"
                                            play sound "Click.mp3" noloop 

                                            S "Ok... je ne suis pas vraiment convaincu......."
                                            play sound "Click.mp3" noloop 

                                            jump debate_failed

                                        "{b}{i}Pointer [newname]{/i}{/b}":

                                            P "[newname] ici présent(e) incarne parfaitement les arguments que j’ai avancés."
                                            play sound "Click.mp3" noloop 

                                            Na "Moi !?"
                                            play sound "Click.mp3" noloop 

                                            P "Oui absolument !"
                                            play sound "Click.mp3" noloop 

                                            show screen update with moveinright

                                            S "D’accord, j’avoue... je ne m’attendais pas à autant de réponses solides."
                                            play sound "Click.mp3" noloop 

                                            hide screen update with moveoutright

                                            I "Tu te défends bien [prenom]."
                                            play sound "Click.mp3" noloop 

                                            $ thanks = get_random_thanks()
                                            P "[thanks]"
                                            play sound "Click.mp3" noloop

                                            jump debate_success

###############################################################################################

label debate_failed:

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Fin numéro 7 : Débat complètement perdu face à [S].{/i}{/b}"
    play sound "Menu.mp3" noloop

    menu:

        "{b}{i}Abandonner{/i}{/b}":
            return

        "{b}{i}Réessayer{/i}{/b}":
            scene classroom with fade
            show screen class_404 with moveinright
            show screen points with moveinleft
            show screen day with moveinleft
            play music "Soundtrack.mp3" loop volume 1.0
            jump debate

label debate_success:

    "{b}{i}Le débat continue jusqu'à la fin du cours.{/i}{/b}"
    play sound "Bell.mp3" noloop   

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    P "Bon on retourne au dortoir [newname] ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    if pronom == "il":

        Na "Tu sais tu t'es vraiment bien débrouillé [prenom]."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        Na "Tu sais tu t'es vraiment bien débrouillée [prenom]."
        play sound "Click.mp3" noloop 
 
    P "Merci beaucoup."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    Na"[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright 
    scene black with fade

    "{b}{i} Vous entrez dans le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen room with moveinright

    if pronom == "il":

        P "Enfin je suis fatigué."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Enfin je suis fatiguée."
        play sound "Click.mp3" noloop 

    Na "Moi aussi..."
    play sound "Click.mp3" noloop 

    P "Tu rigoles j'espére..."
    play sound "Click.mp3" noloop 

    Na "Je tiens à te rappeler que j'ai dû expliquer un cours de math."
    play sound "Click.mp3" noloop 

    P "Moi j'ai dû argumenter toute une après-midi contre ce [S]."
    play sound "Click.mp3" noloop 

    Na "Ok tu marques un point."
    play sound "Click.mp3" noloop 

    P "Bon moi je vais me poser un peu."
    play sound "Click.mp3" noloop 

    Na "Ok moi je vasi me déconnecter."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bien bon je vais me poser un peu pour lire."
    play sound "Phone.mp3" noloop 

    "{b}{i} tu te poses tranqauillement mais tu reçois soudainement un appel.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oui bonjour qui est-ce à l'appareil ?"
    play sound "Click.mp3" noloop 

    Su "C'est [Su]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Su "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt] Sinon pourquoi tu m'appelles ?" 
    play sound "Click.mp3" noloop

    Su "Je voulais avoir de tes nouvelles car on n'a jamais discuter après [origine]."
    play sound "Click.mp3" noloop 

    P "Oui c'est vrai sinon tu fais quoi ?"
    play sound "Click.mp3" noloop 

    Su "Je suis à l'internat de Lexus."
    play sound "Click.mp3" noloop 

    P "Tu es à Lexus ?"
    play sound "Click.mp3" noloop 

    Su "Oui c'est exact."
    play sound "Click.mp3" noloop 

    Su "Cool alors."
    play sound "Click.mp3" noloop 

    Su "Merci sinon comment elle va [A] ?"
    play sound "Click.mp3" noloop 

    P "elle va bien elle est juste déconnectée et je lui ai trouvé un magnifique prénom."
    play sound "Click.mp3" noloop

    Su "Ah bon le quel ?"
    play sound "Click.mp3" noloop 

    P "[newname]"
    play sound "Click.mp3" noloop 

    Su "C'est trop mignon."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    Su "De rien et je voulais te demander quelques choses."
    play sound "Click.mp3" noloop 

    P "Oui dis-moi."
    play sound "Click.mp3" noloop 

    Su "Comment va [S] vu que maintenant qu'il est à Nexus ?"
    play sound "Click.mp3" noloop 

    P "Ah lui, il va bien mais il est juste fatiguant."
    play sound "Click.mp3" noloop 

    Su "Ok je vois comme d'habitude."
    play sound "Click.mp3" noloop 

    P "Sinon des nouvelles de [Sk] ?"
    play sound "Click.mp3" noloop 

    Su "Il est à Lexus avec nous."
    play sound "Click.mp3" noloop 

    P "Cool alors tu lui diras bonjour de ma part."
    play sound "Click.mp3" noloop   

    Su "Promis."
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    Su "Bon je dois te laisser."
    play sound "Click.mp3" noloop 

    P "Ok à une autre fois."
    play sound "Click.mp3" noloop 

    Su "Aucun probléme on se rappelera un de ces jours mais en tant que l'inégalable affective."
    play sound "Click.mp3" noloop 

    $ ultimate11 = "L'inégalable affective" 

    P "Merci." 
    play sound "Click.mp3" noloop 

    "{b}{i} [Su] finit par raccrocher.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon enfin fini je vais pouvoir aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} trois jours plus tard, le 7 octobre 2097 {/i}{/b}"
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
 
    "{b}{i} Tu te léves tranquillement et te changes tranquillement et pars voir [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

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
    Na "[je_vais_bien_txt] et toi ça va ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    Na "Cool alors." 
    play sound "Click.mp3" noloop 

    "{b}{i} Tu reçois soudainement un message de [Su].{/i}{/b}"
    play sound "Click.mp3" noloop 

    menu: 

        "{b}{i} Ouvrir le message.{/i}{/b}":
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            $ success += 1 
            $ quest14 += 1

            P "Bon voyons voir ce que [Su] m'a envoyé."
            play sound "Click.mp3" noloop 

            "{b}{i} Tu ouvres le message.{/i}{/b}"
            play sound "Click.mp3" noloop

            show screen draw with moveinbottom

            "{i} Salut [prenom], hier j'avais oublié de te dire mais j'avais fait un dessin d'[newname] tiens c'est cadeau.{/i}"
            play sound "Click.mp3" noloop

            hide screen draw with moveoutbottom

            show screen update with moveinright

            P "[newname] regardes le magnifique dessin que [Su] a fait pour toi."
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

            Na "Oh c'est magnifique"
            play sound "Click.mp3" noloop

            P "Cool que le dessin te plaise."
            play sound "Click.mp3" noloop 

        "{b}{i} Ignorer le message.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            Na "Tu ne regardes pas le message ?"
            play sound "Click.mp3" noloop 
 
            P "Non pour l'instant."
            play sound "Click.mp3" noloop 

    $ go_in_class = get_random_go_in_class()
    Na "[go_in_class]"  
    play sound "Click.mp3" noloop 

    P "Oui."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    hide screen room with moveoutright 
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    "{b}{i} Quand tu rentres en classe [S] vient vers toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Hey [prenom] je peux te parler deux minutes s'il te plait ?"
    play sound "Click.mp3" noloop 

    P "Pourquoi faire !?"
    play sound "Click.mp3" noloop 

    S "Je trouve que tu fais un trop malin."
    play sound "Click.mp3" noloop 

    P "Comment ça ?"
    play sound "Click.mp3" noloop 

    S "Je trouve qu'améliorer un [model] est facile par rapport à ce que tu dis."
    play sound "Click.mp3" noloop 

    P "Je t'arrète toute de suite !!!"
    play sound "Click.mp3" noloop 
   
    S "Pardon !?"
    play sound "Click.mp3" noloop 

    P "Oui va coder et programmer en Runix et on verra si c'est facile."
    play sound "Click.mp3" noloop 

    "{b}{i}[S] s'éloigne....{/i}{/b}"
    play sound "Door.mp3" noloop

    "{b}{i} La [T] entra dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour."
    play sound "Click.mp3" noloop

    S "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    A "Bonjour."
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

    M "Bien aujourd'hui nous allons continuer le cours sur Pythagore."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "Sortez votre livre de math page 12."
    play sound "Click.mp3" noloop

    "{b}{i} Tout le monde sorte le livre.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Je vous laisse faire les exercices."
    play sound "Click.mp3" noloop 

    "{b}{i} Tout le monde fait les exercices.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon voyons voir...."
    play sound "Click.mp3" noloop

    "{b}{i} Tout le monde fait les exercices mais soudainement tu te sens mal.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Purée...."
    play sound "Click.mp3" noloop

    Na "[prenom] tu vas bien ?"
    play sound "Click.mp3" noloop

    P "Oui ça va....."
    play sound "Click.mp3" noloop

    "{b}{i}Tu commences à sentir ta tête tourner et ta vision devient floue. Le bruit ambiant de la salle de classe semble s’éloigner.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Attends... Je crois que..."
    play sound "Heartbeat.mp3" loop volume 1.0

    "{b}{i}Ton corps ne tient plus, et tu t'effondres à genoux. Des exclamations inquiètes remplissent la pièce.{/i}{/b}"
    play sound "Stumble.mp3" noloop

    Na "[prenom] !! Hé, reste avec moi !" 
    play sound "Click.mp3" noloop

    "{b}{i}Tu perçois vaguement la voix d'[newname] au loin avant que tout devienne noir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen points with moveoutleft
    hide screen class_404 with moveoutright 
    scene black with fade 

    stop music fadeout 2.0   

    if pronom == "il":

        "{b}{i}Quelques instants plus tard, tu te réveilles dans ta chambre, couché sur ton lit.{/i}{/b}"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        "{b}{i}Quelques instants plus tard, tu te réveilles dans ta chambre, couchée sur ton lit.{/i}{/b}"
        play sound "Click.mp3" noloop

    play music "Soundtrack3.mp3" loop volume 2.0

    scene room with fade
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    P "Où... où suis-je ?"
    play sound "Click.mp3" noloop

    "{b}{i}Une voix douce mais ferme te répond, te tirant un peu plus de ton état confus.{/i}{/b}"
    play sound "Click.mp3" noloop

    if pronom == "il":

        Na "Tu es dans ta chambre. Tu t’es évanoui en classe, mais ne t'inquiète pas, Yuna et moi t’avons accompagné jusqu’ici."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        Na "Tu es dans ta chambre. Tu t’es évanouie en classe, mais ne t'inquiète pas, Yuna et moi t’avons accompagné jusqu’ici."
        play sound "Click.mp3" noloop 

    P "[I]...?"
    play sound "Click.mp3" noloop

    "{b}{i}Tu te retournes légèrement, et vois [I] assis sur une chaise à côté du lit, un regard inquiet posé sur toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Je suis là. Sérieusement, tu m’as fait flipper. Ça va mieux ?"
    play sound "Click.mp3" noloop

    P "Je crois que oui... Merci, [I]."
    play sound "Click.mp3" noloop 

    "{b}{i}Une atmosphère de soulagement envahit la pièce, mais une étrange sensation persiste en toi. Quelque chose d’anormal t’a poussé à t’effondrer, et tu sens que ce n’est pas terminé...{/i}{/b}"
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Pourquoi me suis-je evanoui ?"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Pourquoi me suis-je evanouie ?"
        play sound "Click.mp3" noloop
 
    Na "Je pense que tu t'aies trop donné dans les cours."
    play sound "Click.mp3" noloop

    P "Ah....."
    play sound "Click.mp3" noloop

    Na "Bon moi et Yuna devont retourner en classe, reposes-toi."
    play sound "Click.mp3" noloop

    P "Tu ne peut pas rester avec moi [newname] ?"
    play sound "Click.mp3" noloop

    Na "Malheureusement non Malgré que la professeure sait qu'on est inséparable elle veut que je me concentre sur les cours et que je te laisse te reposer."
    play sound "Click.mp3" noloop 

    P "Ok je vois..."
    play sound "Click.mp3" noloop

    Na "A toute à l'heure et reposes-toi, le doliprane te tiendras compagnie, tu en as besoin."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Les filles quittent la chambre.{/i}{/b}"
    play sound "Click.mp3" noloop 

    if quest14 == 0:
    
        menu: 

            "{b}{i} Ouvrir le message de [Su].{/i}{/b}":
                play sound "Menu.mp3" noloop 
            
                P "Bon voyons voir ce que [Su] m'a envoyé."
                play sound "Click.mp3" noloop 

                "{b}{i} Tu ouvres le message.{/i}{/b}"
                play sound "Click.mp3" noloop

                show screen draw

                "{i} Salut [prenom], hier j'avais oublié de te dire mais j'avais fait un dessin d'[newname] tiens c'est cadeau.{/i}"
                play sound "Click.mp3" noloop

                hide screen draw

                $ message += 1 

                P "Bon je fais quoi maintenant ?"
                play sound "Click.mp3" noloop 

    else: 

        P "Bon je fais quoi mainteant ?"
        play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Rattrapper mon retard en math.{/i}{/b}" :
            
            $ renpy.block_rollback()

            P "Bon je vais essayser de travailler un peu..."
            play sound "Click.mp3" noloop 

            "{b}{i} Tu te poses devant ton bureau et commence à étudier.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Bon voyons voir....."
            play sound "Click.mp3" noloop 

            "{b}{i} Tu continues d'étudier pendant trois heures...{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Je vais m'arrêter maintenant sinon [newname] va piquer une crise."
            play sound "Click.mp3" noloop 

            "{b}{i} Dix minutes plus tard [newname] entre dans le dortoir. {/i}{/b}"
            play sound "Click.mp3" noloop 

            $ comment_ca_va = get_random_comment_ca_va()
            Na "[comment_ca_va]"
            play sound "Click.mp3" noloop

            $ je_vais_bien_txt = get_random_je_vais_bien() 
            P "[je_vais_bien_txt]......" 
            play sound "Click.mp3" noloop

            Na "Tu mens ça se voit tu as encore étudié alors que tu ne devrais pas."
            play sound "Click.mp3" noloop  

            P "Ok je l'admet......"
            play sound "Click.mp3" noloop 

            Na "Tu me déçois [prenom], après ça ne m'étonne pas venant de toi tu te donnes toujours à fond."
            play sound "Click.mp3" noloop 

            if pronom == "il":

                P "Désolé [newname]..."
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                P "Désolée [newname]..."
                play sound "Click.mp3" noloop 
        
            $ validation = get_random_validation() 
            Na "[validation]"
            play sound "Click.mp3" noloop 

        "{b}{i} Se reposer {/i}{/b}" : 
            
            $ success += 1 
            $ quest15 += 1

            $ renpy.block_rollback() 

            show screen update with moveinright

            "{b}{i} Tu te reposes pendant trois heures avant de te réveiller {/i}{/b}"
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

            P "ça fait du bien un peu repos.."
            play sound "Click.mp3" noloop 

            "{b}{i} Dix minutes plus tard [newname] entre dans le dortoir. {/i}{/b}"
            play sound "Click.mp3" noloop 

            $ comment_ca_va = get_random_comment_ca_va()
            Na "[comment_ca_va]"
            play sound "Click.mp3" noloop

            $ je_vais_bien_txt = get_random_je_vais_bien() 
            P "[je_vais_bien_txt]" 
            play sound "Click.mp3" noloop

            Na "Cool alors." 
            play sound "Click.mp3" noloop 

    P "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright 
    hide screen points with moveoutleft
    scene black with fade 

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft


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

    "{b}{i} Le lendemain, le 8 octobre 2097.{/i}{/b}"
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

    "{b}{i} Tu te léves tranquillement et te changes tranquillement {/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "J'imagine qu'elle encore fatiguée à cause d'hier."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

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

    Na "Mais je me suis inquiétée pour toi."
    play sound "Click.mp3" noloop

    P "Ah je vois." 
    play sound "Click.mp3" noloop

    $ go_in_class = get_random_go_in_class()
    Na "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers la salle de classe avec [newname].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    P "Bonjour tout le monde."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    Y "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    Y "Cool alors car on s'est tous inquiété pour toi."
    play sound "Click.mp3" noloop 

    N "Oui c'est vrai mais heureusement qu'[newname] et [I] t'ont ramené à ton dortoir."
    play sound "Click.mp3" noloop 

    P "Merci beaucoup."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    Y "[nothing]"
    play sound "Door.mp3" noloop

    "{b}{i} Soudainement la [T] entres dans la classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour."
    play sound "Click.mp3" noloop

    N "Bonjour."
    play sound "Click.mp3" noloop

    Y "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    Na "Bonjour.~"
    play sound "Click.mp3" noloop 

    "{b}{i}La [T] pose son regard sur toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Oh [prenom] je vois que tu vas mieux."
    play sound "Click.mp3" noloop

    P "Oui c'est exact."
    play sound "Click.mp3" noloop

    M "C'est bien que tu ais rétabli."
    play sound "Click.mp3" noloop

    P "Merci beaucoup Madame."
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

    M "Cool alors bon maintenant nous allons voir la formule du triangle isocéle rectangle."
    play sound "Click.mp3" noloop

    P "puis-je la dire ?"
    play sound "Click.mp3" noloop 

    M "Oui avec plaisir, peux-tu nous la dire."
    play sound "Click.mp3" noloop

    P " il suffit de faire a√2"
    play sound "Click.mp3" noloop

    M "Absolument."
    play sound "Click.mp3" noloop

    I "Attendez de base ce n'est pas le théoréme de pythagore ?"
    play sound "Click.mp3" noloop

    M "Oui mais cette formule existe aussi."
    play sound "Click.mp3" noloop 

    I "Ok j'ai rien dit."
    play sound "Click.mp3" noloop

    M "Bon veuillez faire les exercices."
    play sound "Click.mp3" noloop

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
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

    "{b}{i} Vous choissez de rejoindre [I] pour manger.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Coucou [I]."
    play sound "Click.mp3" noloop

    I "oh salut vous venez manger avec moi."
    play sound "Click.mp3" noloop

    P "oui."
    play sound "Click.mp3" noloop

    Na "Bien évidemment."
    play sound "Click.mp3" noloop

    I "Cool alors."
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Et dire qu'on aura déjà notre examen sur le théorème de pythagore..."
    play sound "Click.mp3" noloop

    P "oui c'est vrai."
    play sound "Click.mp3" noloop

    I "J'espére que toi et [newname] vous allez travailler dur pour cet examen."
    play sound "Click.mp3" noloop

    P "Ne t'inquiétes pas ça va bien passer."
    play sound "Click.mp3" noloop

    Na "Oui on a l'habitude avec [prenom]."
    play sound "Click.mp3" noloop

    P "Surtout qu'[newname] à acquis beaucoup de connaissances mais Le plus gros défaut du cadre scolaire c'est qu'il limite la protée globale de ces connaissances."
    play sound "Click.mp3" noloop 

    I "Cool alors mais j'ai une question."
    play sound "Click.mp3" noloop

    P "Oui dis-moi."
    play sound "Click.mp3" noloop

    I "Tu sais sur quel système d'exploitation tourne [newname] ?"
    play sound "Click.mp3" noloop

    if quest11 == 1:

        P "Elle tourne sur Aether OS."
        play sound "Click.mp3" noloop  

        I "Cool alors."
        play sound "Click.mp3" noloop 

        P "Merci beaucoup mais je compte faire un système d'exploitation personnalisé pour elle de toute façon."
        play sound "Click.mp3" noloop 

    else: 

        P "Je ne sais pas sur quel système d'exploitation elle tourne."
        play sound "Click.mp3" noloop  

        I "C'est de l'ignorance numérique, l'une des dix régles de l'informatique à ne pas briser, tu devrais le savoir."
        play sound "Click.mp3" noloop 

        if pronom == "il":

            P "Désolé mais je compte faire un système d'exploitation personnalisé pour elle de toute façon."
            play sound "Click.mp3" noloop 

        elif pronom == "elle":
        
            P "Désolée mais je compte faire un système d'exploitation personnalisé pour elle de toute façon."
            play sound "Click.mp3" noloop  

    I "Ah je vois." 
    play sound "Click.mp3" noloop 

    "{b}{i} Vous conntinuez de discuter des cours pendant que vous mangez jusqu'a la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    I "Ok je vous suis."
    play sound "Click.mp3" noloop 

    hide screen lunchroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveoutright
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

    M "Bonjour nous allons faire un nouveau théme." 
    play sound "Click.mp3" noloop 

    S "Quoi comme cours ?"
    play sound "Click.mp3" noloop 

    M "Nous allons faire de l'informatique et du code." 
    play sound "Click.mp3" noloop 

    P "Oh trop bien."
    play sound "Click.mp3" noloop

    S "Sérieusement !? je suis un peu nul à ça."
    play sound "Click.mp3" noloop  

    P "Ce n'est pas un peu de l'autodérisition [S] ?"
    play sound "Click.mp3" noloop 

    Na "Oui trop bien en plus je n'ai jamais appris l'informatique car j'ai seulement appris à parler et écrire et les cours de base."
    play sound "Click.mp3" noloop 

    M "Cool que ça puisse te plaire [newname]."
    play sound "Click.mp3" noloop

    Na "Merci."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    M  "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}La [T] change de ton.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon qui peut me dire en écrit un texte en python ?"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde hésite à lever la main.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Moi s'il vous plait."
    play sound "Click.mp3" noloop 

    M "Bien."
    play sound "Click.mp3" noloop
    
    $ Code = renpy.input("Veuillez écrire la réponse.")
    $ Code = Code.strip() 

    if Code == "print(\"text\")":

        $ success += 1
        $ quest16 += 1

        show screen update with moveinright

        M "Bonne réponse."
        play sound "Click.mp3" noloop

        hide screen update with moveoutright

    else :

        M "Mauvaise réponse."
        play sound "Click.mp3" noloop

    "{b}{i}Le cours continue sans probléme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    P "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
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

    "{b}{i} Le lendemain matin, le 9 octobre 2097{/i}{/b}"
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

    "{b}{i} Tu te léves tranquillement et te changes tranquillement et pars voir [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 
    
    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    P "Bonjour [newname] aujourd'hui on va faire du boulot dans la salle de club."
    play sound "Click.mp3" noloop

    Na "Génial."
    play sound "Click.mp3" noloop

    hide screen room with moveoutright
    scene black with fade 

    "{b}{i}Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i}Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade 

    "{b}{i}Vous continuez dans les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop
     
    scene hall with fade
    show screen hall with moveinright

    "{b}{i}Vous continuez vers la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans la salle de club.{/i}{/b}"
    play music "Door.mp3" noloop 

    scene clubroom with fade 
    show screen clubroom with moveoutright

    if pronom == "il":

        P "Enfin arrivés."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Enfin arrivées."
        play sound "Click.mp3" noloop 

    Na "Oui."
    play sound "Click.mp3" noloop

    P "Aujourd'hui je vais coder ton nouveau système d'exploitation."
    play sound "Click.mp3" noloop
 
    Na "Cool merci parce que ça quatre ans que j'ai mon vieux système d'exploitation."
    play sound "Click.mp3" noloop

    P "Donc je vais devoir complétement te déconnecter."
    play sound "Click.mp3" noloop

    Na "Donc je dois juste étre en veille comme d'habitude ?"
    play sound "Click.mp3" noloop

    P "Non se sera une déconnexion totale et manuelle."
    play sound "Click.mp3" noloop

    Na "Ok je vois."
    play sound "Click.mp3" noloop 

    menu:   

        "{b}{i} Déconnecter Complétement [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    Na "Déconnexion totale du système en cours......."
    play sound "Click.mp3" noloop

    P "Bon au boulot...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu allumes ton ordi et tu ouvres ton éditeur de code.{/i}{/b}" 
    play sound "Menu.mp3" noloop

label code: 

    $ system = renpy.input("Choisis un nom pour ton système d'exploitation.")
    play sound "Menu.mp3" noloop 

    $ Line1 = renpy.input("initiate_system(name=Aris,mode=secure,boot=true,fightmode=false)")
    play sound "Menu.mp3" noloop 

    $ Line2 = renpy.input("initiate_system(settings_access=true)")
    play sound "Menu.mp3" noloop 
    
    $ Line3 = renpy.input("initiate_system(database_access=false)")
    play sound "Menu.mp3" noloop 

    menu: 

        "{b}{i} Compiler le code.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            if Line1 == "initiate_system(name=Aris,mode=secure,boot=true,fightmode=false)":
            
                if Line2 == "initiate_system(settings_access=true)":
            
                    if Line3 == "initiate_system(database_access=false)":
            
                        "Code correctement compilé."
                        play sound "Click.mp3" noloop 
        
                    else: 

                        "Erreur détectée, le code a été mal compilé."
                        play sound "Click.mp3" noloop 

                        jump code  
                        
                else: 

                    "Erreur détectée, le code a été mal compilé."
                    play sound "Click.mp3" noloop 

                    jump code  
    
            else: 

                "Erreur détectée, le code a été mal compilé."
                play sound "Click.mp3" noloop 

                jump code 

    "{b}{i}Tu continues de travailler sur [newname] pendant trois heures.{/i}{/b}" 
    play sound "Click.mp3" noloop

    P "Bon il m'aura fallu beaucoup du temps mais j'ai enfin fini, j'ai le fichier de système d'exploitation qui est [system].rnx"
    play sound "Click.mp3" noloop

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop

    Na "Initialisation du système d'exploitation en cours...."
    play sound "Click.mp3" noloop

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na "Bonjour [prenom], je tourne maintenant sur le système d'exploitation [system] avec la version [update] du processeur Corzen 11KS."
    play sound "Click.mp3" noloop 

    $ stockage += 10.0 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis vous continuez encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Tu entres dans le réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
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

    "{b}{i} On allons manger tu croises [H].{/i}{/b}"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    H "Oh salut [prenom] et [newname], oui moi ça va bien et vous ?"
    play sound "Click.mp3" noloop 

    Na "On va bien." 
    play sound "Click.mp3" noloop 

    H "Cool alors et sinon quoi de nouveau ?"
    play sound "Click.mp3" noloop

    P "On était dans notre salle de club pour du boulot."
    play sound "Click.mp3" noloop 

    H "Oh vous avez faitquoi de nouveau ?"
    play sound "Click.mp3" noloop 

    P "J'ai codé le nouveau système d'exploitation d'[newname]."
    play sound "Click.mp3" noloop 

    H "Génial et comment s'appelle t'il ?"
    play sound "Click.mp3" noloop 

    P "Il s'appelle [system]."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    H "[validation]"
    play sound "Click.mp3" noloop 

    P "Et sinon comment il avance ton robot car tu le montre jamais."
    play sound "Click.mp3" noloop
 
    H "Il avance bien."
    play sound "Click.mp3" noloop

    P "Tu fais un robot classique ou robot humanoïde ?"
    play sound "Click.mp3" noloop

    H "Un robot classique ne t'inquiétes pas je ne veux pas te copier et de toute façon [newname] est la derniére robot humanoïde."
    play sound "Click.mp3" noloop

    P "Intéressant et sinon tu sais ou est [I] ?"
    play sound "Click.mp3" noloop 

    H "Oh je l'ai aperçu avant elle était dans la salle de club générale, elle est vraiment occupée."
    play sound "Click.mp3" noloop 

    P "Ok je vois ça ne m'étonne pas venant d'elle."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on retourne au club ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i}Tu continues vers la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop  

    scene clubroom with fade
    show screen clubroom with moveinright 

    P "Enfin au club."
    play sound "Click.mp3" noloop 

    Na "Oui ça fait du bien et sinon tu comptes faire quoi maintenant ?"
    play sound "Click.mp3" noloop 

    P "Je vais paramétrer ton nouveau système d'exploitation."
    play sound "Click.mp3" noloop 

    Na "Génial."
    play sound "Click.mp3" noloop

label update: 

    if update == 1.0: 

        "{b}{i}Tu t'asseois et allumes ton ordinateur mais [newname] agit bizarrement.{/i}{/b}"
        play sound "Click.mp3" noloop

        A "Système opérationnel."
        play sound "Click.mp3" noloop

        P "Comment ça ? Qu'est-ce que tu racontes !?"
        play sound "Click.mp3" noloop

        A "Démarrage du transfert des données vers un autre ordinateur."
        play sound "Click.mp3" noloop

        $ stockage -= 15.0

        P "Mince elle est en train de se faire pirater, je dois activer le Recovery Mode....."
        play sound "Click.mp3" noloop 

        menu: 

            "{b}{i}Activer le recovery mode.{/i}{/b}":
                play sound "Menu.mp3" noloop

        $ reboot = renpy.input("Écris ceci : initiate_humanoid_robot.shutdown(security_override=false)")
        $ reboot = reboot.strip() 

        if reboot == "initiate_humanoid_robot.shutdown(security_override=false)":
            
            A "Fermeture du système d'exploitation [system]....."
            play sound "Click.mp3" noloop

            P "Enfin mais c'est bizarre on dirait que cette faille venait du processeur."
            play sound "Click.mp3" noloop 

            P "Attend il y a que [N] et [Y] à qui j'ai dit que j'avais pas mis à jour le processeur d'[newname]."
            play sound "Click.mp3" noloop 

            P "J'espére qu'il n'y a de Backdoor qui a été installé dans le systéme d'[newname]."
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

        else:

            A "Qu'est-ce que tu tentes de faire."
            play sound "Stumble.mp3" noloop

            "{b}{i}[newname] se met à plaquer au sol.{/i}{/b}"
            play music "gameover.mp3" noloop

            hide screen clubroom with moveoutright
            hide screen point with moveoutleft
            hide screen day with moveoutleft
            scene black with fade

            if pronom == "il":

                "{b}{i}Fin numéro 8 : Complétement plaqué et étranglé par [Na].{/i}{/b}"
                play sound "Menu.mp3" noloop

            elif pronom == "elle":

                "{b}{i}Fin numéro 8 : Complétement plaquée et étranglée par [Na].{/i}{/b}"
                play sound "Menu.mp3" noloop

            menu:

                "{b}{i}Abandonner{/i}{/b}":
                    return
                    
                "{b}{i}Réessayer.{/i}{/b}":
                    scene clubroom with fade
                    show screen clubroom with moveinright
                    show screen point with moveinleft
                    show screen day with moveinleft
                    play music "Soundtrack2.mp3" loop volume 1.0
                    jump update

    else:

        "{b}{i}Tu t'asseois et allumes ton ordinateur.{/i}{/b}"
        play sound "Click.mp3" noloop

    P "Bien voyons voir...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu regardes tous les paramétres pendant deux heures mais tu remarques quelques choses.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "On dirait qu'il y a rien de nouveau dans [system]."
    play sound "Click.mp3" noloop 

    Na "Bon on fait quoi du coup ?"
    play sound "Click.mp3" noloop 
  
    P "On peut retourner au dortoir."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i}Tu continues vers les escaliers mais tu vois la porte de la salle de club générale légérement ouverte.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Attends [newname] on dirait que la porte de la salle de club générale légérement ouverte."
    play sound "Click.mp3" noloop 

    Na "Ah bon c'est bizarre."
    play sound "Click.mp3" noloop

    P "Attends moi ici je vais aller voir."
    play sound "Click.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i}Tu continues dans la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop  

    scene clubroom with fade
    show screen clubroom with moveinright 

    "{b}{i}En entrant tu vois [I] complétement endormie sur la table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oh c'est mignon elle s'est endormie mais c'est normal elle s'est complétement donnée à fond pour son jeu."
    play sound "Click.mp3" noloop 

    P "Bon je fais quoi maintenant ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Réveiller [I] {/i}{/b}" : 

            $ renpy.block_rollback()

            $ success += 1
            $ quest17 += 1
    
            "{b}{i} Tu approches calmement pour la réveiller.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Yuna ça va ?"
            play sound "Click.mp3" noloop 

            show screen update with moveinright

            I "Mhmmm C'est qui ?"
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

            P "C'est moi [prenom]." 
            play sound "Click.mp3" noloop

            I "Oh c'est toi..."
            play sound "Click.mp3" noloop

            if pronom == "il":

                P "Oui je suis venu te voir car je ne t'ai pas vu de la journée et je me suis inquiété."
                play sound "Click.mp3" noloop 

            elif pronom == "elle": 

                P "Oui je suis venue te voir car je ne t'ai pas vu de la journée et je me suis inquiétée."
                play sound "Click.mp3" noloop 

            I "Oh c'est gentil de t'inquiéter pour moi"
            play sound "Click.mp3" noloop 

            if pronom == "il":

                P "De rien c'est normal entre amis."
                play sound "Click.mp3" noloop 

            elif pronom == "elle": 

                P "De rien c'est normal entre amies."
                play sound "Click.mp3" noloop 

            I "Je suis vraiment fatiguée j'ai trop travaillé..."
            play sound "Click.mp3" noloop

            P "Il faut vraiment que tu te reposes."
            play sound "Click.mp3" noloop

            I "Je sais mais..."
            play sound "Click.mp3" noloop

            P "tu veux que je raccompagne au dortoir ou c'est bon ?"
            play sound "Click.mp3" noloop

            I "Non ça va aller ne t'inquiétes pas."
            play sound "Click.mp3" noloop

            P "Bien alors et reposes toi tu en as besoin."
            play sound "Click.mp3" noloop

            $ thanks = get_random_thanks()
            I "[thanks]"
            play sound "Click.mp3" noloop

            $ nothing = get_random_nothing()
            P "[nothing]"
            play sound "Click.mp3" noloop

            hide screen clubroom with moveoutright
            scene black with fade 

            "{b}{i} Puis tu sors de la salle de club général.{/i}{/b}"
            play sound "Door.mp3" noloop

            scene hall with fade
            show screen hall with moveinright 
            
        "{b}{i} La laisser dormir {/i}{/b}" : 

            $ renpy.block_rollback()

            P "Je vais la laisser dormir elle en a besoin."
            play sound "Click.mp3" noloop 

            hide screen clubroom with moveoutright
            scene black with fade 

            "{b}{i} Puis tu sors de la salle de club général.{/i}{/b}"
            play sound "Door.mp3" noloop

            scene hall with fade
            show screen hall with moveinright 

    P "Bon on y va [newname] ?"
    play sound "Click.mp3" noloop    

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous continuez vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hall with moveoutright
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i} Vous entres dans ton dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene room with fade
    show screen room with moveinright 

    if pronom == "il":

        P "Enfin au dortoir je suis epuisé."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Enfin au dortoir je suis epuisée."
        play sound "Click.mp3" noloop 

    Na "Oui enfin."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
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

    "{b}{i} Le lendemain matin, le 10 octobre 2097{/i}{/b}"
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
    Na "[je_vais_bien_txt] Et toi" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop 

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    Na "Bien évidemment."
    play sound "Click.mp3" noloop 

    hide screen room with moveoutright 
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene black with fade
    hide screen hallway with moveoutright

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    P "Bonjour."
    play sound "Click.mp3" noloop 

    Na "Bonjour."
    play sound "Click.mp3" noloop 

    M "Bonjour."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu regardes dans la salle, tu vois les autres.{/i}{/b}"
    play sound "Click.mp3" noloop

    Y "Juste elle est où [I] ?"
    play sound "Click.mp3" noloop 

    K "Oui c'est vrai elle est où [I] ?"
    play sound "Click.mp3" noloop

    N "On veut savoir où elle est."
    play sound "Click.mp3" noloop 

    M "Doucement, [prenom] tu peux nous dire où est [I] ?"
    play sound "Click.mp3" noloop 

    P "Tout ce que je sais c'est qu'hier [I] était complétemnt fatiguée au club hier."
    play sound "Click.mp3" noloop 

    M "Oh je vois."
    play sound "Click.mp3" noloop 

    Y "Oh elle a sûrement dû étre fatiguée de surtravail."
    play sound "Door.mp3" noloop 

    "{b}{i}Puis soudainement [I] entres en classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Bonjour désolée de mon retard j'était pas bien."
    play sound "Click.mp3" noloop 

    M "Bonjour [I] si jamais [prenom] nous a déjà dii ce que tu avais."
    play sound "Click.mp3" noloop 

    I "Ok merci."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis [I] part s'asseoir à sa place.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon reprenons le cours mais d'abord j'ai une chose à vous dire."
    play sound "Click.mp3" noloop 

    I "Quoi comme chose ?."
    play sound "Click.mp3" noloop 

    H "Oui dites-nous."
    play sound "Click.mp3" noloop 

    M "Il s'avére qu'il y a eu un attaque informatique hier dans l'après-midi qui a touché tout le lycée."
    play sound "Click.mp3" noloop 

    if update == 2.0: 

        P "Ah ça oui je l'avais remarqué quand [newname] agissait bizarrement mais je savais que ça avait touché tout le lycée."
        play sound "Click.mp3" noloop 

        M "Oui et le plus surprenant c'est d'ou venait l'attaque."
        play sound "Click.mp3" noloop 

        P "Comment ça ?"
        play sound "Click.mp3" noloop 

        M "Oui l'attaque venait de l'intérieur du lycée ici même."
        play sound "Click.mp3" noloop 

        P "Pardon ?"
        play sound "Click.mp3" noloop 

        K "Oui je peux confirmer car le réseau était trés instable c'est derniers jours."
        play sound "Click.mp3" noloop 

        Y "Attend [prenom] tu as dit qu'[newname] avais agit bizarrement ?"
        play sound "Click.mp3" noloop 

        P "Oui pourquoi ?"
        play sound "Click.mp3" noloop 

        Y "Elle a sûrement du être piratée."
        play sound "Click.mp3" noloop 

        P "je pense aussi mais après j'ai corrigé la faille et maintenant elle est à jour niveau logiciel."
        play sound "Click.mp3" noloop 

        Y "Cool alors si tu as pu corriger la faille."
        play sound "Click.mp3" noloop 

        P "Merci."
        play sound "Click.mp3" noloop 

    else: 

        P "Pardon !? Dites-moi que c'est une blague !"
        play sound "Click.mp3" noloop 

        M "Oui et le plus surprenant c'est d'ou venait l'attaque."
        play sound "Click.mp3" noloop 

        P "Comment ça ?" 
        play sound "Click.mp3" noloop 

        M "Oui l'attaque venait de l'intérieur du lycée ici même."
        play sound "Click.mp3" noloop 

        P "Pardon ?"
        play sound "Click.mp3" noloop 

        K "Oui je peux confirmer car le réseau était trés instable c'est derniers jours."
        play sound "Click.mp3" noloop 

        $ update += 1.0 

    M "Calmez-vous avant que ça devienne l'anarchie."
    play sound "Click.mp3" noloop 

    "{b}{i} Tout le monde commence à se méfier les un les autres.{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Donc il y a vraiment un traître parmi nous ?"
    play sound "Click.mp3" noloop 

    P "Bah oui tu as vu tout ce qui se passe au lycée ?"
    play sound "Click.mp3" noloop 

    S "Désolé c'est juste que je suis occupé."
    play sound "Click.mp3" noloop 

    P "Ok je comprends mais là on ne peut plus vraiment confiance à qui que se soit dans cette classe."
    play sound "Click.mp3" noloop 

    Na "Vraiment [prenom] ?" 
    play sound "Click.mp3" noloop 

    P "Oui je t'assure [newname]."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Bon maintenant commençons le cours, sortez votre livre page 10."
    play sound "Click.mp3" noloop 

    "{b}{i} Tout le monde sort leur livre ent continuons le cours.{/i}{/b}"
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers la réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright    
    scene staircase with fade

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} vous entrez le réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
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

    "{b}{i} Puis tu croises [I].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oh salut [I] ça te dit de venir avec nous ?"
    play sound "Click.mp3" noloop 

    I "Ce ne pas contre toi mais j'ai besoin d'être seule aujourd'hui."
    play sound "Click.mp3" noloop 

    P "Je vois mais sache que si tu as besoin de moi je serai là pour toi."
    play sound "Click.mp3" noloop 

    I "Merci beaucoup [prenom]."
    play sound "Click.mp3" noloop 

    P "Avec plaisir."
    play sound "Click.mp3" noloop 

    "{b}{i} Puis [I] s'éloigna pour aller manger seul.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu sais ce qu'elle a ?"
    play sound "Click.mp3" noloop 

    Na "J'en ai aucune idée malheureusement."
    play sound "Click.mp3" noloop  

    P "Bien."
    play sound "Click.mp3" noloop 

    "{b}{i} vous allez chercher un place puis vous voyez [S] seul.{/i}{/b}"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Aller manger avec [S]{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            P "Salut [S] ça va ?"
            play sound "Click.mp3" noloop 

            $ je_vais_bien_txt = get_random_je_vais_bien() 
            P "[je_vais_bien_txt] " 
            play sound "Click.mp3" noloop

            $ je_vais_bien_txt = get_random_je_vais_bien() 
            P "[je_vais_bien_txt]" 
            play sound "Click.mp3" noloop

            $ je_vais_bien_txt = get_random_je_vais_bien() 
            Na "[je_vais_bien_txt]" 
            play sound "Click.mp3" noloop

            S "Cool alors."
            play sound "Click.mp3" noloop 

            "{b}{i} Pendant que vous mangez, [S] regarde des documents.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Ce sont quoi ces documents ?"
            play sound "Click.mp3" noloop  

            S "Rien d'important, c'est juste pour mon projet."
            play sound "Click.mp3" noloop 

            $ validation = get_random_validation() 
            P "[validation]"
            play sound "Click.mp3" noloop 

            "{b}{i} Vous continuez de manger jusqu'à la sonnerie.{/i}{/b}" 
            play sound "Bell.mp3" noloop

            S "Bon il faut qu'on retourne en cours."
            play sound "Click.mp3" noloop 

            $ validation = get_random_validation() 
            P "[validation]"
            play sound "Click.mp3" noloop 

            $ suivi = get_random_suivi()
            Na "[suivi]"
            play sound "Footsteps.mp3" noloop

        "{b}{i} Aller manger avec [Na]{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            $ success += 1 
            $ quest18 += 1

            show screen update with moveinright

            "{b}{i} Vous allez chercher une pour manger.{/i}{/b}"
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

            P "Enfin on peut manger."
            play sound "Click.mp3" noloop

            Na "Oui enfin."
            play sound "Click.mp3" noloop

            "{b}{i} Vous asseyez tranquillement.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "[newname] tu penses que c'est qui le traître ?"
            play sound "Click.mp3" noloop

            Na "Je ne sais pas vraiment mais je que pense c'est [J1]."
            play sound "Click.mp3" noloop

            P "Et pourquoi elle ?"
            play sound "Click.mp3" noloop

            Na "Tu rigoles tu n'as pas vu comment elle était ?"
            play sound "Click.mp3" noloop

            P "Si j'ai vu je te rassure."
            play sound "Click.mp3" noloop

            $ thanks = get_random_thanks()
            Na "[thanks]"
            play sound "Click.mp3" noloop

            "{b}{i} Vous continuez de discuter et de manger jusqu'à la sonnerie.{/i}{/b}" 
            play sound "Bell.mp3" noloop

            P "Bon il faut qu'on retourne en cours."
            play sound "Click.mp3" noloop 
             
            $ suivi = get_random_suivi()
            Na "[suivi]" 
            play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez dans le hall.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveoutright
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    M "Rebonjour, bon reprenez votre livre page 11."
    play sound "Click.mp3" noloop 

    # à modifier  

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    P "Bon cette journée est enfin finie..."
    play sound "Click.mp3" noloop 

    Na "Oui enfin..."
    play sound "Click.mp3" noloop

    "{b}{i} tu vois soudainement un papier avec écrit l'inégalable complotiste.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "L'inégalable complotiste !? c'est impossible il n'y a aucun lycéen qui a ce titre ici..."
    play sound "Click.mp3" noloop

    Na "[prenom] ça va ?"
    play sound "Click.mp3" noloop

    P "Oui ça va."
    play sound "Click.mp3" noloop

    if pronom == "il":

        Na "Es-tu sûr ?"
        play sound "Click.mp3" noloop

    elif pronom == "elle":
        
        Na "Es-tu sûre ?"
        play sound "Click.mp3" noloop

    P "Oui."
    play sound "Click.mp3" noloop

    Na "Ok si tu le dis."
    play sound "Click.mp3" noloop

    P "Bon on continue vers le dortoir."
    play sound "Click.mp3" noloop

    Na "Oui absolument."
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room with moveinright 

    if pronom == "il":

        Na "Enfin arrivés"
        play sound "Click.mp3" noloop

    elif pronom == "elle":
        
        Na "Enfin arrivées"
        play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon Je vais me déconnecter."
    play sound "Click.mp3" noloop

    P "Pas de soucis, moi j'ai deux trois trucs à faire."
    play sound "Click.mp3" noloop

    Na "ok mais avant ça j'avais oublié de te demander un truc."
    play sound "Click.mp3" noloop

    P "Oui dis-moi."
    play sound "Click.mp3" noloop

    Na "Par rapport à cette histoire de traître et d'attaque, tu suspectes qui ?"
    play sound "Menu.mp3" noloop

    P "Je pensaw que c'est [S] mais il y a un truc qui cloche."
    play sound "Click.mp3" noloop

    Na "Non ce n'est pas possible pour moi je pense." 
    play sound "Click.mp3" noloop

    P "Et pourquoi ?"
    play sound "Click.mp3" noloop

    Na "Rappelles-toi de quand il est arrivé au lycée."
    play sound "Click.mp3" noloop

    P "Oui et alors ?"
    play sound "Click.mp3" noloop

    Na "Il est arrivé bien après qu'on aie su qu'il y avait un traître ici."
    play sound "Click.mp3" noloop

    P "Oh oui c'est vrai comment j'ai pu oublié ce détail."
    play sound "Click.mp3" noloop

    Na "Tu vois ?"
    play sound "Click.mp3" noloop

    P "Mais quant-même il tiens des propos très bizarres."
    play sound "Click.mp3" noloop

    Na "Oui mais toute à commencer avant son arrivé."
    play sound "Click.mp3" noloop

    P "Ok mais je vais quand même le surveiller."
    play sound "Click.mp3" noloop

    Na "D'accord je vois mais sinon tu penses que c'est qui d'autre le traître ?"
    play sound "Click.mp3" noloop 

    P "Alors....."
    play sound "Click.mp3" noloop

    menu:   

        "{b}{i}[J1].{/i}{/b}" :
            play sound "Menu.mp3" noloop 
            $ suspect = "Ayano"
 
            P "Je pense que c'est [J1]."
            play sound "Click.mp3" noloop

            Na "Oui qu'elle a eu des propos inacceptables."
            play sound "Click.mp3" noloop 

            P "En plus elle est toujours avec [J2]."
            play sound "Click.mp3" noloop

            Na "Je vois bien."
            play sound "Click.mp3" noloop

        "{b}{i}[J2].{/i}{/b}" :
            
            $ suspect = "Aiko"
            $ success += 1 
            $ quest19 += 1

            show screen update with moveinright

            P "Je pense que c'est [J2]."
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

            Na "Oui qu'elle a eu des propos inacceptables."
            play sound "Click.mp3" noloop 

            P "En plus elle est toujours avec [J1]."
            play sound "Click.mp3" noloop
    
            Na "Je vois bien."
            play sound "Click.mp3" noloop 
            
        "{b}{i}[Y].{/i}{/b}" :
            play sound "Menu.mp3" noloop 
            $ suspect = "Yuki"

            P "Je pense que c'est [Y]."
            play sound "Click.mp3" noloop

            Na "Pourquoi ? Elle est super sympa."
            play sound "Click.mp3" noloop

            P "Oui je sais mais tu n'as pas remarqué un truc ?"
            play sound "Click.mp3" noloop

            Na "Quoi dis-moi."
            play sound "Click.mp3" noloop

            P "Elle est souvent absente après les cours."
            play sound "Click.mp3" noloop

            Na "Oui c'est vrai maintenant que tu le dis."
            play sound "Click.mp3" noloop

            P "En plus on ne sais rien de son domaine inégalable."
            play sound "Click.mp3" noloop

            Na "Tu as raison."
            play sound "Click.mp3" noloop 

    $ renpy.block_rollback()

    P "Bon moi je vais aller régler un truc."
    play sound "Click.mp3" noloop

    Na "Ok moi je vais me déconnecter..."
    play sound "Click.mp3" noloop 

    P "Pas de souci."
    play sound "Click.mp3" noloop

    "{b}{i} [newname] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon moi j'y vais."
    play sound "Click.mp3" noloop

    scene black with fade 
    hide screen room with moveoutright

    "{b}{i}Tu quittes ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway with moveinright

    "{b}{i}Tu conntinues dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    scene staircase 
    hide screen hallway with moveoutright

    "{b}{i}Tu conntinues vers le hall.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene hall with fade
    show screen hall with moveinright

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    P "Bon je suis presqu'arriver."
    play sound "Click.mp3" noloop

    scene black with fade 
    hide screen hall with moveoutright

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene office 
    show screen office with moveinright 
    play sound "Door.mp3" noloop 

    P "Bonjour, c'est moi [prenom]."
    play sound "Click.mp3" noloop

    E "Que puis-je faire pour toi ?"
    play sound "Click.mp3" noloop

    P "C'est concernant cette histoire de traître, car j'ai trouvé quelque chose."
    play sound "Click.mp3" noloop

    E "Oui, dis-moi, qu'est-ce qu'il y a ?"
    play sound "Click.mp3" noloop

    P "J'ai trouvé une note signée 'L'inégalable Complotiste', mais aucun élève n'a ce titre ici."
    play sound "Click.mp3" noloop

    E "Intéressant... Je vois."
    play sound "Click.mp3" noloop

    P "Mais je pense que ça a un lien avec le traître et les attaques."
    play sound "Click.mp3" noloop

    E "Tu le penses vraiment ?"
    play sound "Click.mp3" noloop

    P "Oui, je le pense."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    E "[validation]"
    play sound "Click.mp3" noloop 

    P "Emika, je vous le dis aujourd’hui, ça reste entre nous. Indépendamment de toute considération idéologique, si quelqu’un prévoit de détruire [newname], je le dénoncerai."
    play sound "Click.mp3" noloop 

    E "Tu veux vraiment faire ça ?"
    play sound "Click.mp3" noloop

    P "Oui, car il le faut pour la sécurité de [newname]."
    play sound "Click.mp3" noloop

    E "Ok, je ne juge pas."
    play sound "Click.mp3" noloop

    P "Bon, je vais vous laisser. C'est tout ce que j'avais à dire."
    play sound "Click.mp3" noloop

    E "Pas de soucis je note."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    E "[nothing]"
    play sound "Click.mp3" noloop

    scene black with fade 
    hide screen office with moveoutright

    "{b}{i} Puis tu quittas le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene staircase
    hide screen hallway with moveoutright

    "{b}{i}Tu continues vers le premier étage.{/i}{/b}"
    play sound "Click.mp3" noloop  

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i}Tu continues ton chemin.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Bon est-ce que je vais voir [I] ou je retourne au dortoir ?."
    play sound "Click.mp3" noloop

    menu:    

        "{b}{i} Aller au dortoir.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            P "Je vais aller au dortoir et la laisser tranquille."
            play sound "Click.mp3" noloop 

            scene black with fade
            hide screen hallway with moveoutright 

            "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
            play sound "Door.mp3" noloop  

            scene room
            show screen room with moveinright 

            P "Enfin de retour...."
            play sound "Click.mp3" noloop  

        "{b}{i} Aller voir [I]. {/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            $ success += 1 
            $ quest20 += 1 

            P "Je vais aller la voir pour voir si elle va bien."
            play sound "Footsteps.mp3" noloop 

            "{b}{i}Tu te diriges vers le dortoir d'[I] avant d'y parvenir.{/i}{/b}"
            play sound "Click.mp3" noloop  

            P "Bon....."
            play sound "Knock.mp3" noloop 

            show screen update with moveinright

            "{b}{i}Tu frappes à la porte d'[I] et patientes puis elle t'ouvre la porte.{/i}{/b}"
            play sound "Door.mp3" noloop  

            hide screen update with moveoutright

            I "Oh c'est toi [prenom], vas-y entres." 
            play sound "Click.mp3" noloop  

            P "Merci."
            play sound "Click.mp3" noloop  

            hide screen hallway with moveoutright 
            scene black with fade

            "{b}{i}Tu entres dans son dortoir.{/i}{/b}"
            play sound "Door.mp3" noloop  

            scene room
            show screen Yunaroom with moveinright

            I "Donc voici ma chambre."
            play sound "Click.mp3" noloop  

            P "Elle est géniale."
            play sound "Click.mp3" noloop  

            $ thanks = get_random_thanks()
            I "[thanks]"
            play sound "Click.mp3" noloop

            $ nothing = get_random_nothing()
            P "[nothing]"
            play sound "Click.mp3" noloop

            if pronom == "il":

                I "Sinon pourquoi es-tu venu me voir ?"
                play sound "Click.mp3" noloop  

                P "Je me suis inquiété pour toi car j'ai remarqué que tu étais distante, est-ce que tu vas vraiment bien ?"
                play sound "Click.mp3" noloop  

            elif pronom == "elle":
        
                I "Sinon pourquoi es-tu venue me voir ?"
                play sound "Click.mp3" noloop  

                P "Je me suis inquiétée pour toi car j'ai remarqué que tu étais distante, est-ce que tu vas vraiment bien ?"
                play sound "Click.mp3" noloop  

            I "à vrai dire pas vraiment je te l'admet...."
            play sound "Click.mp3" noloop  

            P "Pourquoi ?"
            play sound "Click.mp3" noloop  

            I "Avec l'attaque d'hier j'ai perdu une partie de mon travail de mon jeu vidéo."
            play sound "Click.mp3" noloop  

            P "Ah mince, tu as perdu une grande partie de ton travail ?"
            play sound "Click.mp3" 

            I "Une partie importante je dirais mais juste elle est ou [newname] ?"
            play sound "Click.mp3" noloop  

            P "Ne t'inquétes pas elle est dans mon dortoir."
            play sound "Click.mp3" noloop  

            I "Je sais mais avec ce qui se passe en ce moment."
            play sound "Click.mp3" noloop  

            P "Oui même moi je m'inquiéte pour elle..."
            play sound "Click.mp3" noloop  

            I "J'imagine bien."
            play sound "Click.mp3" noloop  

            P "Je sens que les emmerdes vont commencer."
            play sound "Click.mp3" noloop  

            I "Je trouve que les emmerdes ont déjà commencé."
            play sound "Click.mp3" noloop  

            P "Oui avec tout ce qui passe."
            play sound "Click.mp3" noloop  

            I "bon je vais me reposer."
            play sound "Click.mp3" noloop  

            P "Pas de soucis je vais te laisser."
            play sound "Click.mp3" noloop  

            I "Ok alors à demain."
            play sound "Click.mp3" noloop  

            P "Ok à demain."
            play sound "Click.mp3" noloop  

            hide screen Yunaroom with moveoutright
            scene black with fade

            "{b}{i}Tu te diriges dans le couloir.{/i}{/b}"
            play sound "Door.mp3" noloop  

            scene hallway with fade
            show screen hallway with moveinright 

            P "Bon je vais aller au dortoir."
            play sound "Click.mp3" noloop 

            "{b}{i}Tu te diriges dans le couloir.{/i}{/b}"
            play sound "Click.mp3" noloop  

            hide screen hallway with moveoutright 
            scene black with fade

            "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
            play sound "Door.mp3" noloop  

            scene room with fade
            show screen room with moveinright 

            P "Enfin de retour...."
            play sound "Click.mp3" noloop  

    "{b}{i} Tu vérifies si [newname] est toujours là avant d'aller chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i} tu poses tranquillement ton sac de cours.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je vais chercher à manger, j'avais complétement oublié."
    play sound "Click.mp3" noloop  

    hide screen room with moveoutright
    scene black with fade 

    "{b}{i} Tu pars chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ points -= 300 

    show screen room with moveinright 
    scene room with fade 

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    "{b}{i} Tu manges tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade
     
    "{b}{i} Le lendemain matin, le 11 octobre 2097{/i}{/b}"
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
    P "[je_vais_bien_txt] J'ai just un mauvais pressentiment." 
    play sound "Click.mp3" noloop

    Na "Pourquoi cela ?"
    play sound "Click.mp3" noloop 

    P "Avec tout ce qui passe au lycée."
    play sound "Click.mp3" noloop 

    Na "Je vois bien." 
    play sound "Click.mp3" noloop 

    P "Donc aujourd'hui j'ai choisi de mettre un mot de passe sécurisé sur ton systéme sinon je risque de briser l'une des dix régles de l'informatique."
    play sound "Click.mp3" noloop 

    Na "Cool alors merci beaucoup." 
    play sound "Click.mp3" noloop 

    "{b}{i} Tu ouvres les paramêtres pour ajouter un mot de passe sur [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

label choisir_mot_de_passe:

    $ password = renpy.input("Veuillez choisir un mot de passe pour [newname].")
    $ password = password.strip()

    if password:  

        $ stored_password = password

        "Mot de passe enregistré avec succès." 

    P "C'est bon, je lui ai mis un mot de passe, je vais la redémarrer pour voir."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu relances [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

label password:  

    $ entered_password = renpy.input("Veuillez remettre votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password:

        if len(entered_password) > 10:
            $ success += 1
            $ quest21 += 1   
            $ stockage += 5.0

            show screen update with moveinright

            "Mot de passe correct. Accès autorisé." 
            play sound "Menu.mp3" noloop

            hide screen update with moveoutright

        else:

            "Mot de passe correct. Accès autorisé." 
            play sound "Menu.mp3" noloop
        
    else:

        $ stockage += 2.0

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password  

    $ renpy.block_rollback()

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    P "Bonjour [newname], est-ce que ça va ?"
    play sound "Click.mp3" noloop  

    Na "Oui absolument."
    play sound "Click.mp3" noloop 

    P "Bon il faut qu'on aille en cours."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    scene black with fade

    "{b}{i}Vous quittez le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop  

    scene hallway 
    show screen hallway with moveinright 

    P "Dépéches-toi sinon on va être en retard."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Footsteps.mp3" noloop 

    "{b}{i}Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade 

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop 
    
    scene classroom with fade
    show screen class_404 with moveinright     

    P "Bonjour."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    N "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    N "[je_vais_bien_txt] Sinon comment tu va [newname] ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    N "Cool alors que tu aille bien."
    play sound "Click.mp3" noloop 

    "{b}{i} Puis tu aperçois [I].{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt] Comment vous allez ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    "{b}{i}Puis soudainement la [T] entre en classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour."
    play sound "Click.mp3" noloop

    I "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    Na "Bonjour.~"
    play sound "Click.mp3" noloop

    N "Bonjour."
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

    M "Bien, sortez votre livre de mathématique."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Le cours se passe tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Knock.mp3" noloop 

    play music "Soundtrack2.mp3" loop 

    "{b}{i}Soudainement quelqu'un frappe à la porte.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Oui entrez je vous en prie."
    play sound "Door.mp3" noloop

    "{b}{i}Puis deux personnes entrent dans la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    R "Bonjour."
    play sound "Click.mp3" noloop

    M "Bonjour puis-je savoir qui étes-vous ?"
    play sound "Click.mp3" noloop

    Oh "Je suis l'[Ot] de la direction générale contre les cyberattaques et voici ma collégue."
    play sound "Click.mp3" noloop

    O "Bonjour, je suis [O], sous-officière de la direction générale de la cybersécurité."
    play sound "Click.mp3" noloop

    "{b}{i}Soudainement [newname] a peur et se cache dérrière toi.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "N'aie pas peur [newname], ça va aller."
    play sound "Click.mp3" noloop

    Na "Ok [prenom]."
    play sound "Click.mp3" noloop

    M "Sinon pourquoi étes-vous ici ?"
    play sound "Click.mp3" noloop

    Oh "Noua sommes ici car [E] nous a informé qu'il avait des attaques informatique ici."
    play sound "Click.mp3" noloop

    M "Oui en effet, [E] nous a informé des méfaits qui se passent au lycée."
    play sound "Click.mp3" noloop 

    Oh "Je vois et il y a eu quoi comme attaques ?"
    play sound "Click.mp3" noloop
     
    M "Il ya eu des attaques contre les systémes du lycée et [newname]."
    play sound "Click.mp3" noloop

    Oh "Qui est [newname] ?"
    play sound "Click.mp3" noloop

    "{b}{i}La [T] pointe [newname] à l'[Ot].{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "C'est celle au fond à coté de [prenom], [pronom] vous donnera plus de détails sur [newname]."
    play sound "Click.mp3" noloop 

    Oh "Je vois."
    play sound "Click.mp3" noloop 

    "{b}{i}L'[Ot] se met à regarder [newname] mais cette dérnière a peur.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "N'est pas peur."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis la [T] se met à regarder les élèves.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Ok sur ce, le cours est annulé, veuillez écouter l'[Ot]."
    play sound "Click.mp3" noloop

    P "bien entendu."
    play sound "Click.mp3" noloop 

    I "Bien compris."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Oh "[validation]"
    play sound "Click.mp3" noloop 

    M "Bien alors."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis la [T] quitte la salle pendant que l'[Ot] se met à parler.{/i}{/b}"
    play sound "Click.mp3" noloop    

    Oh "Bien on va procéder une fouille général de vos dortoirs."
    play sound "Click.mp3" noloop

    K "Sérieusement, des fouilles." 
    play sound "Click.mp3" noloop

    Oh "Oui, il le faut vu la situation actuelle."
    play sound "Click.mp3" noloop 

    P "Je confirme car la sécurité d'[newname] est en jeu."
    play sound "Click.mp3" noloop 

    Oh "Donc veuilliez retournez dans votre dortoir pour procéder au fouille."
    play sound "Click.mp3" noloop 

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i}Puis vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright 
    scene black with fade 

    "{b}{i} Tu entres au dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room with moveinright 

    P "Enfin de retour bon vivement la fin des fouilles."
    play sound "Click.mp3" noloop  

    Na "Oui mais j'ai un mauvais présentimment."
    play sound "Click.mp3" noloop 

    P "Comment ça ?"
    play sound "Click.mp3" noloop 

    Na "Maintenant c'est le fait qu'on la direction générale contre les cyberattauques ici qui m'inquiète."
    play sound "Click.mp3" noloop 

    P "Je le sais que ça t'inquiète."
    play sound "Click.mp3" noloop  

    "{b}{i}La discussion continue pendant 45 minutes avant que ça frappe à ta porte.{/i}{/b}"
    play sound "Knock.mp3" noloop 

    P "Oui entrez je vous en prie."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis l'[Ot] et [O] entre dans ton dortoir{/i}{/b}"
    play sound "Doors.mp3" noloop

    Oh "Bonjour."
    play sound "Click.mp3" noloop 

    P "Bonjour."
    play sound "Click.mp3" noloop 

    Na "Bonjour."
    play sound "Click.mp3" noloop 

    "{b}{i} L'[Ot] se met doucement à regarder [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    Oh "Bien avant qu'on commence la fouille, j'aimerais te poser une question."
    play sound "Click.mp3" noloop 

    P "Oui dites-moi, je vous écoute."
    play sound "Click.mp3" noloop 

    Oh "C'est bien [newname] avec toi ?"
    play sound "Click.mp3" noloop 

    P "Oui c'est ça."
    play sound "Click.mp3" noloop 

    Oh "Donc c'est elle qui subit des cyberattaques depuis un moment ?" 
    play sound "Click.mp3" noloop 

    P "Oui absolument."
    play sound "Click.mp3" noloop 

    Oh "Je vois bien."
    play sound "Click.mp3" noloop 

    "{b}{i} L'[Ot] discute vite fait avec [O] puis ils se mettent à te regarder.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Oh "Bien je vais regarder ton bureau pendant que ma collégue va regarder le reste de ton dortoir."
    play sound "Click.mp3" noloop 

    P "Pas de soucis, je vous laisse faire."
    play sound "Click.mp3" noloop 

    "{b}{i} Ils se mettent à fouiller pendant quelques minutes.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Oh "Tu trouves quelques choses [O] ?" 
    play sound "Click.mp3" noloop 

    O "Non malheureusement, J'ai fouillé [newname] et sous le lit."
    play sound "Click.mp3" noloop 

    Oh "Bien je vois, juste [prenom] qu'est-ce que c'est que ces documents sur ton bureau ?"
    play sound "Click.mp3" noloop 

    if quest11 == 1:

        P "Ce sont des documents techniques pour [newname]."
        play sound "Click.mp3" noloop

    else: 

        P "Ce sont mes documents techniques pour [newname]."
        play sound "Click.mp3" noloop

    Oh "Merci beaucoup de m'avoir dit."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}L'[Ot] continue de regarder tes documents mais il tombe sur un document suspect.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Oh "[O] viens voir sur quoi je suis tombé." 
    play sound "Click.mp3" noloop 

    O "Tu es tombé sur quoi ?" 
    play sound "Click.mp3" noloop 

    Oh "Bah viens voir." 
    play sound "Click.mp3" noloop 

    "{b}{i}[O] se met à regarder le document.{/i}{/b}"
    play sound "Click.mp3" noloop 

    O "Oh putain...." 
    play sound "Click.mp3" noloop 

    "{b}{i} Ils se mettent à te regarder.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Oh "[P] veuillez lever vos mains et nous suivre." 
    play sound "Click.mp3" noloop 

    Na "Pardon !?" 
    play sound "Click.mp3" noloop 

    P "Ne t'inquiète pas [newname], ça va aller tu peux rester ici." 
    play sound "Click.mp3" noloop 

    Na "Mais pourquoi ?" 
    play sound "Click.mp3" noloop 

    Oh "Pas besoin, elle peut venir aussi." 
    play sound "Click.mp3" noloop 

    hide screen room with moveoutright
    scene black with fade 

    "{b}{i}Tu quittes ta chambre avec la DGCA.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway
    show screen hallway with moveinright

    "{b}{i}Tu continues dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
 
    hide screen hallway with moveoutright 
    scene staircase 

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hall with fade
    show screen hall with moveinright

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene office 
    show screen office with moveinright 

    "{b}{i}En entrant vous voyez [M] et [E] en train discuter avant qu'elles se tournent vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Tiens tiens tiens qui vois-je là ?" 
    play sound "Click.mp3" noloop 

    E "[P] !? Que fais-tu ici avec la DGCA ?" 
    play sound "Click.mp3" noloop 

    P "Je ne sais pas, ils m'ont juste dit de lever les mains et de les suivre..." 
    play sound "Click.mp3" noloop 

    E "Je vois." 
    play sound "Click.mp3" noloop 

    "{b}{i}L'[Ot] se met à parler.{/i}{/b}"
    play sound "Click.mp3" noloop

    Oh "Si nous sommes ici c'est parce que nous avons trouvé un document vraiment suspect dans les affaires de [prenom]." 
    play sound "Click.mp3" noloop 

    M "Comment ça !?" 
    play sound "Click.mp3" noloop 

    Oh "Oui absolument, regardez." 
    play sound "Click.mp3" noloop 

    "{b}{i}L'[Ot] leur donne le document.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bien voyons voir ceci." 
    play sound "Click.mp3" noloop 

    "{b}{i}[M] commence à lire le document.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Qu'est-ce que c'est cette histoire de destruction de système !?" 
    play sound "Click.mp3" noloop 

    P "Pardon comment ça !?" 
    play sound "Click.mp3" noloop 

    Na "Pardon mais [prenom] n'oserait jamais faire ça." 
    play sound "Click.mp3" noloop

    M "Regardes le document et tu verras." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] lit le document.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Bon je vais juste donner le document à [E] car moi j'ai compris ce qui ne va pas avec ce document." 
    play sound "Click.mp3" noloop 

    M  "Vraiment ?" 
    play sound "Click.mp3" noloop 

    P "Tu es sûre ?" 
    play sound "Click.mp3" noloop 

    Na "Oui absolument." 
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] donne le document à [E].{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "[E] va tout de suite comprendre." 
    play sound "Click.mp3" noloop 

    "{b}{i}[E] lit tranquilement le document et réalise.{/i}{/b}"
    play sound "Click.mp3" noloop 

    E "Hey attendez, ce document est signé par {b}{i}l'inégalable complotiste.{/i}{/b}" 
    play sound "Click.mp3" noloop

    P "Encore l'inégalable complotiste !?" 
    play sound "Click.mp3" noloop 

    E "Oui." 
    play sound "Click.mp3" noloop 

    Oh "Attendez, [prenom] n'est pas l'inégalable complotiste ?" 
    play sound "Click.mp3" noloop 

    M "Non, [pronom] est [domaine], donc veuillez le détachez." 
    play sound "Click.mp3" noloop 

    Oh "Je vois je m'en excuse alors." 
    play sound "Handcuffs.mp3" noloop 

    "{b}{i}L'[Ot] te détache tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Merci." 
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    E "[nothing] Désolé de t'avoir accusé sans avoir avoir les détails." 
    play sound "Click.mp3" noloop 

    P "Pas de soucis." 
    play sound "Click.mp3" noloop 

    if pronom == "il": 

        O "Mais si ce n'est pas lui, ça serait qui du coup car on a fouillé tous les lycéens."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        O "Mais si ce n'est pas lui, ça serait qui du coup car on a fouillé tous les lycéens."
        play sound "Click.mp3" noloop 

    E "C'est ce qu'on essaye de savoir mais tout ce qu'on sais c'est qu'il est parmi les élèves." 
    play sound "Click.mp3" noloop 

    M "Attendez, vous avez dit que vous avez fouillé tous tout les lycéens et que vous n'avez rien trouvé ?" 
    play sound "Click.mp3" noloop 

    O "Oui exactement." 
    play sound "Click.mp3" noloop 

    M "C'est vraiment bizarre cette histoire..." 
    play sound "Click.mp3" noloop 

    E "Je confirme aussi." 
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Faire une réflexion.{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

    P "Moi je pense avoir ma petite idée sur qui est le coupable." 
    play sound "Click.mp3" noloop 
    
    E "Et ça serait qui ?" 
    play sound "Click.mp3" noloop 

    P "Je pense que c'est [suspect] le coupable." 
    play sound "Click.mp3" noloop 

    E "Bon vue la situation n'importe qui peut être le coupable." 
    play sound "Click.mp3" noloop 

    Oh "Sinon [prenom], j'aimerais savoir si ça t'intéresses de participer à l'enquéte car car tu es la principale victime." 
    play sound "Click.mp3" noloop 

    P "Oui pourquoi pas." 
    play sound "Click.mp3" noloop 

    if pronom == "il" : 
    
        M "Tu es sûr de vouloir faire ça ?" 
        play sound "Click.mp3" noloop 

    elif pronom == "elle" :

        M "Tu es sûre de vouloir faire ça ?" 
        play sound "Click.mp3" noloop 

    P "Oui on parle quand-même de la sécurité d'[newname]." 
    play sound "Click.mp3" noloop 

    M "Oui je sais mais tu en fais déjà trop entre les cours et amélioration d'[newname]." 
    play sound "Click.mp3" noloop 

    P "Je vois bien." 
    play sound "Click.mp3" noloop 

    M "Donc laisse faire la DGCA." 
    play sound "Click.mp3" noloop 

    P "Ok alors je les laisserai faire." 
    play sound "Click.mp3" noloop 

    Oh "Merci, juste avant qu'on parte j'ai une question." 
    play sound "Click.mp3" noloop 

    P "Oui dites-moi." 
    play sound "Click.mp3" noloop 

    Oh "à l'avenir, que veux-tu qu'[newname] devienne ?" 
    play sound "Click.mp3" noloop 

    P "Je ne sasi pas exactement, je veux juste qu'elle apprenne pour l'instant." 
    play sound "Click.mp3" noloop 

    Oh "Je vois c'est intéressant." 
    play sound "Click.mp3" noloop 

    "{b}{i}Il y a un blanc pendant quelques instants.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Oh "Bon on va vous laiser, on a du travail qui nous attend pour l'enquête." 
    play sound "Click.mp3" noloop 

    E "Merci d'être venu." 
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Oh "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}Puis ils quittent la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "J'espére que cette histoire va finir." 
    play sound "Click.mp3" noloop 

    E "Espérons-le." 
    play sound "Click.mp3" noloop 

    P "J'ai une question." 
    play sound "Click.mp3" noloop 

    E "Oui dis-moi." 
    play sound "Click.mp3" noloop 

    P "Il y aurait la possibilité d'installer une caméra devant mon dortoir ?" 
    play sound "Click.mp3" noloop 

    E "Je ne suis pas sûre mais je pense que c'est possible si tu demandes à [Ah] et [Rn]." 
    play sound "Click.mp3" noloop

    if pronom == "il":

        M "J'espére que tu n'es pas sérieux [prenom] !"
        play sound "Click.mp3" noloop 

    elif pronom == "elle":
        
        M "J'espére que tu n'es pas sérieuse [prenom] !"
        play sound "Click.mp3" noloop 

    P "Je rappelle que la sécurité d'[newname] est en jeu." 
    play sound "Click.mp3" noloop 

    M "Ce n'est pas un peu dans l'extrême ?" 
    play sound "Click.mp3" noloop 

    P "Non je ne trouve pas."
    play sound "Click.mp3" noloop 

    "{b}{i}[M] se met à réfléchir avant de te répondre.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Je suis désolée mais je ne peux pas te laisser faire ça."
    play sound "Click.mp3" noloop 

    P "Bien je comprends mais merci d'avoir répondu  à ma question."
    play sound "Click.mp3" noloop

    M "Bien vous pouvez disposer maintenant et me fais regretter ma décision." 
    play music "Footsteps.mp3" noloop 

    "{b}{i}Tu quittes le bureau des élèves avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hall with fade
    show screen hall with moveinright

    P "Bon on va manger car il est 11h45."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade 

    "{b}{i} Vous entrez au réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
    show screen lunchroom with moveinright

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i}vous partez chercher une place avant d'en trouver une.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin."
    play sound "Click.mp3" noloop 

    Na "Oui j'ai vraiment faim."
    play sound "Click.mp3" noloop 

    P "Oui moi aussi."
    play sound "Click.mp3" noloop 

    "{b}{i} Pendant que vous mangez, tu commences à t'inquiéter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "{i}Qui a essayé de me piéger ?{/i}"
    play sound "Click.mp3" noloop 

    Na "Est-ce que ça va ?"
    play sound "Click.mp3" noloop 

    P "Oui c'est juste que je m'inquiète."
    play sound "Click.mp3" noloop 

    Na "Pourquoi ça ?"
    play sound "Click.mp3" noloop 

    P "J'essaye de savoir qui a tenté de me piéger."
    play sound "Click.mp3" noloop 

    P "Je vois."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de manger et [J1] viens vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oh salut [J1], tu veux quoi ?"
    play sound "Click.mp3" noloop 

    Na "Salut [J1]."
    play sound "Click.mp3" noloop 

    J1 "j'ai besoin de discuter sincérement et sérieusement avec vous."
    play sound "Click.mp3" noloop 

    P "Ok, de quoi tu veux discuter ?"
    play sound "Click.mp3" noloop 

    "{b}{i}[J1] s'asseoit avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bien je te laisse nous dire ce que tu voulais nous dire."
    play sound "Click.mp3" noloop 

    J1 "Je n'ai eu pas l'occasion de le dire la dernière fois car tu discutais avec [S] mais je tiens sincérement à m'excuser pour les propos que j'ai eu en vers [newname]."
    play sound "Click.mp3" noloop 

    Na "Tu le penses vraiment !?" 
    play sound "Click.mp3" noloop 

    J1 "Oui absolument."
    play sound "Click.mp3" noloop 

    Na "Merci de nous le dire car je pensais que tu étais humanoïdophobe."
    play sound "Click.mp3" noloop 

    J1 "Non c'est juste que je ne connaissais pas assez."
    play sound "Click.mp3" noloop 

    Na "Je vois."
    play sound "Click.mp3" noloop 

    P "Attends [newname], tu as utilisé le mot humanoïdophobe ?"
    play sound "Click.mp3" noloop 

    Na "Oui pourquoi tu me demandes ça ?"
    play sound "Click.mp3" noloop 

    P "Non c'est juste que ça me surprend que tu saches ce mot."
    play sound "Click.mp3" noloop 

    Na "Comme je l'ai déjà dit je suis ici pour apprendre."
    play sound "Click.mp3" noloop 

    P "Oui mais le terme humanoïdophobe est rarement utilisé de nos jours."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        Na "je vois, je comprend pourquoi tu es surpris."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        Na "je vois, je comprend pourquoi tu es surprise."
        play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    P "Bon on retourne en cours." 
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen office with moveoutright
    scene black with fade

    "{b}{i}Tu te diriges vers le hall.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene staircase

    "{b}{i}Tu continues vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway
    show screen hallway with moveinright 

    "{b}{i}Tu continue vers la salle de la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright  

    "{b}{i}En entrant [I] se met à te regarder.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Tu fais quoi avec [J1] !?"
    play sound "Click.mp3" noloop 

    P "On discutait de quelques choses."
    play sound "Click.mp3" noloop 

    I "De quoi vous parliez ?"
    play sound "Click.mp3" noloop 

    P "Elle est juste venue s'excuser sincérement par rapport à ce qu'elle a dit sur [newname]."
    play sound "Click.mp3" noloop 

    I "Vraiment, je vois alors."
    play sound "Door.mp3" noloop
    
    "{b}{i} Puis la [T] entra dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour chers lycéens."
    play sound "Click.mp3" noloop

    H "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    Na "Bonjour~"
    play sound "Click.mp3" noloop 

    I "Bonjour."
    play sound "Click.mp3" noloop

    "{b}{i} tous les lycéens s'asseoient à leur place.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bien nous allons faire le cours que nous avions pu faire ce matin."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    # à modifier 

    "{b}{i} Le cours continue sans problémes.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Bon le cours est terminé, vous pouvez quitter la salle."
    play sound "Click.mp3" noloop

    P "Bon [newname] on y va ?"
    play sound "Click.mp3" noloop

    Na "Oui je suis fatiguée."
    play sound "Click.mp3" noloop 

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
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

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
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

    "{b}{i} Le lundi suivant, le 14 octobre 2097{/i}{/b}"
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

    "{b}{i}Tu te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 
    
    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

label password1:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password:

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else:

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password1  

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
    P "[je_vais_bien_txt] Bon on y va ?" 
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    scene black with fade 

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway with moveinright 

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade 

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright  

    M "Bonjour."
    play sound "Click.mp3" noloop 

    P "Bonjour."
    play sound "Click.mp3" noloop 

    Na "Bonjour."
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

    "{b}{i}La [T] se met à te regarder car elle a remarqué un truc bizarre en toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Est-ce que ça va [prenom] ?"
    play sound "Click.mp3" noloop 

    if pronom == "il":

        $ je_vais_bien_txt = get_random_je_vais_bien() 
        P "[je_vais_bien_txt] Je suis inquiet pour [newname]." 
        play sound "Click.mp3" noloop

        M "Je vois mais essaye d'être concentré durant les cours."
        play sound "Click.mp3" noloop 

    elif pronom == "elle":

        $ je_vais_bien_txt = get_random_je_vais_bien() 
        P "[je_vais_bien_txt] Je suis inquiet pour [newname]." 
        play sound "Click.mp3" noloop 

        M "Je vois mais essaye d'être concentrée durant les cours."
        play sound "Click.mp3" noloop 

    P "Oui promis."
    play sound "Click.mp3" noloop 

    M "Bien alors, bon continuons le cours de math."
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue jusqu'à la pause.{/i}{/b}"
    play sound "Click.mp3" noloop

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
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes mais tu commences à avoir une pensée.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "{i}Et si je quittais le lycée comme ça [newname] sera en sécurité.{/i}"
    play sound "Click.mp3" noloop

    "{b}{i} Tu continues de réfléchir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Click.mp3" noloop

    hide screen WC with moveoutright
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

    M "Bien reprenez les exercices."
    play sound "Click.mp3" noloop

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
 
    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
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

    "{b}{i} Vous vous asseyez dans le recfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Enfin à manger."
    play sound "Click.mp3" noloop    

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement mais [newname] remarque un truc en toi.{/i}{/b}"
    play sound "Click.mp3" noloop  

    Na "Est-ce que ça va ?"
    play sound "Click.mp3" noloop 

    menu: 

        "{b}{i} Lui dire mes inquiétudes.{/i}{/b}":
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            $ success += 1
            $ quest22 += 1

            show screen update with moveinright

            P "C'est juste que j'avait un truc qui me passait en tête..."
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

            Na "Ah bon et c'est quoi ?"
            play sound "Click.mp3" noloop 

            P "Je me disais, est-ce que se serait pas mieux si on quitte le lycée pour ta sécurité car je m'inquiète de ce qui passe au lycée."
            play sound "Click.mp3" noloop 

            if pronom == "il":    

                Na "Tu n'est pas sérieux j'espére !?"
                play sound "Click.mp3" noloop 
                
            elif pronom == "elle":

                Na "Tu n'est pas sérieuse j'espére !?"
                play sound "Click.mp3" noloop 

            P "C'est juste une proposition."
            play sound "Click.mp3" noloop 

            Na "Oui mais pas besoin de quitter le lycée pour ma sécurité, tu m'as déjà assez sécurisée, ou est ton sens de la moralité ?"
            play sound "Click.mp3" noloop 

            P "Oui mais...."
            play sound "Click.mp3" noloop 

            Na "Pas de mais, on fait pour être ici."
            play sound "Click.mp3" noloop 

            if pronom == "il":    

                P "Désolé...."
                play sound "Click.mp3" noloop 
                
            elif pronom == "elle":

                P "Désolée...."
                play sound "Click.mp3" noloop 

            Na "Oui je te comprends car tu as une grande responsabilité en vers moi."
            play sound "Click.mp3" noloop 

            P "Merci." 
            play sound "Click.mp3" noloop 

            Na "Bon je pense qu'on peut finir cette discussion."
            play sound "Click.mp3" noloop 

        "{b}{i} Ne rien lui dire.{/i}{/b}":
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

            P "Oui ne t'inquiète pas."
            play sound "Click.mp3" noloop  

            Na "Non je veux que tu me dises la vérité."
            play sound "Click.mp3" noloop 

            P "Je me disais, est-ce que se serait pas mieux si on quitte le lycée pour ta sécurité car je m'inquiète de ce qui passe au lycée."
            play sound "Click.mp3" noloop 

            if pronom == "il":    

                Na "Tu n'est pas sérieux j'espére !?"
                play sound "Click.mp3" noloop 
                
            elif pronom == "elle":

                Na "Tu n'est pas sérieuse j'espére !?"
                play sound "Click.mp3" noloop 

            P "C'est juste une proposition."
            play sound "Click.mp3" noloop 

            Na "Oui mais pas besoin de quitter le lycée pour ma sécurité, tu m'as déjà assez sécurisée, ou est ton sens de la moralité ?"
            play sound "Click.mp3" noloop 

            P "Oui mais...."
            play sound "Click.mp3" noloop 

            Na "Pas de mais, on fait pour être ici."
            play sound "Click.mp3" noloop 

            if pronom == "il":    

                P "Désolé...."
                play sound "Click.mp3" noloop 
                
            elif pronom == "elle":

                P "Désolée...."
                play sound "Click.mp3" noloop 

            Na "Oui je te comprends car tu as une grande responsabilité en vers moi."
            play sound "Click.mp3" noloop 

            P "Merci." 
            play sound "Click.mp3" noloop 

            Na "Bon je pense qu'on peut finir cette discussion."
            play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de manger tranquillement jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop  

    P "Bon il faut qu'on retourne en classe."
    play sound "Click.mp3" noloop    

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    scene black with fade

    "{b}{i}Vous vous diriges vers le hall.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall with moveinright 

    "{b}{i}Vous continuez vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene staircase

    "{b}{i}Vous continuez vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway
    show screen hallway with moveinright 

    "{b}{i}Vous continuez vers la salle de la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    M "Rebonjour, bon reprenons le cours."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    S "[validation]"
    play sound "Click.mp3" noloop   

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    P "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop   

    Na "Vas-y déjà, moi je vais à la bibliothéque un peu."
    play sound "Click.mp3" noloop

    P "Ok mais ne rien pas trop tard non plus."
    play sound "Click.mp3" noloop   

    Na "Oui promis."
    play sound "Click.mp3" noloop   

    "{b}{i} Puis la [T] veut te demander quelques choses avant que tu partes.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oui dîtes-moi ?"
    play sound "Click.mp3" noloop   

    M "J'aimerai savoir si [Na] a déjà fait un test de Turing ?"
    play sound "Click.mp3" noloop   

    P "Non pourquoi ?"
    play sound "Click.mp3" noloop   

    M "Car ça serait intéressant pour voir le niveau d'[newname]."
    play sound "Click.mp3" noloop 

    P "Bien, je penserai à aller voir quand j'aurai le temps."
    play sound "Click.mp3" noloop   

    M "Bien alors, bon je vous laisse partir et je vais aussi en parler à [E]."
    play sound "Click.mp3" noloop   

    P "Merci."
    play sound "Click.mp3" noloop   

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Tu sors de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright  

    "{b}{i} Tu continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room with moveinright 

    if pronom == "il":

        P "Enfin arrivé."
        play sound "Click.mp3" noloop

    elif pronom == "elle":

        P "Enfin arrivée."
        play sound "Click.mp3" noloop

    "{b}{i}Tu te poses pendant deux heures pour réviser.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin fini...."
    play sound "Door.mp3" noloop   

    "{b}{i}Puis [newname] revient au dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    $ stockage += 10.0

    P "Tu as lu quelque chose d'intéressant ?"
    play sound "Click.mp3" noloop   

    Na "Oui, c'était dans un livre de géographie. Ça parlait de la région de Danto, celle dans laquelle on vit."
    play sound "Click.mp3" noloop   

    P "Et ça disait quoi ?"
    play sound "Click.mp3" noloop   

    Na "Qu’elle s’est énormément développée à partir de 2060, au point de devenir la région la plus avancée technologiquement du Japon."
    play sound "Click.mp3" noloop   

    Na "D’ailleurs, tu savais que Danto, c’est l’acronyme de {b}Development Area for New Technological Operations{/b} ?"
    play sound "Click.mp3" noloop   

    P "Non je ne savais pas."
    play sound "Click.mp3" noloop

    Na "C’est devenu un pôle majeur d’innovation, et son influence dans le domaine de la tech dépasse même les frontières du pays."
    play sound "Click.mp3" noloop

    P "C'est vrai que ça fait plaisir de savoir ça."
    play sound "Click.mp3" noloop

    "{b}{i} [newname] pose tranquillement ses affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
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

    if grade == 20.0:

        $ points += 15000

    else:

        $ points += 11000 

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

    "{b}{i} Quatre jours plus tard, le 18 octobre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 4 
    $ points -= 800
    $ stockage += 80.0 

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

label password2:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password:

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else:

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password2

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    Na "Oui car on a examen de math aujourd'hui."
    play sound "Click.mp3" noloop 

    P "Je le sais déjà."
    play sound "Click.mp3" noloop 
    
    hide screen room with moveoutright
    scene black with fade

    "{b}{i}Tu te diriges vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway
    show screen hallway with moveinright 

    "{b}{i}Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    "{b}{i}Puis soudainement tu vois tous les autres élèves à l'entrée de la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Vous êtes déjà tous là."
    play sound "Click.mp3" noloop 

    I "Oui [M] n'est pas encore arrivée."
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
    I "[salutation_rdm]"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
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

    M "Bien aujourd'hui comme vous le savez vous avez votre second examen je vais vous distribuer votre copie." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[M] Commença à distribuer les copies.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Vous avez une heure c'est parti !!!" 
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde retourne sa copie.{/i}{/b}"
    play sound "Click.mp3" noloop 

label examen_pythagore:

    play music "Soundtrack2.mp3" loop volume 1.0

    $ grade = 0.0 

    "Question 1 : Quelle est la formule du théorème de Pythagore ?"
    play sound "Menu.mp3" noloop 

    menu:
        "a² + b² = c²":
            $ grade += 2.0
        "a² - b² = c²":
            $ grade += 0.0
        "a² + b² = 2c²":
            $ grade += 0.0

    "Question 2 : Dans quel type de triangle applique-t-on le théorème de Pythagore ?"
    play sound "Menu.mp3" noloop 

    menu: 
        "Triangle isocèle":
            $ grade += 0.0
        "Triangle rectangle":
            $ grade += 2.0
        "Triangle équilatéral":
            $ grade += 0.0

    "Question 3 : Si un triangle a des côtés de 3 cm, 4 cm et 5 cm, est-il rectangle ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Oui":
            $ grade += 2.0
        "Non":
            $ grade += 0.0
        "Impossible à déterminer":
            $ grade += 0.0

    "Question 4 : Quelle est la longueur de l'hypoténuse d'un triangle ayant des côtés de 6 cm et 8 cm ?"
    play sound "Menu.mp3" noloop 

    menu:
        "10 cm":
            $ grade += 2.0
        "12 cm":
            $ grade += 0.0
        "14 cm":
            $ grade += 0.0

    "Question 5 : Quelle est l'hypoténuse d'un triangle rectangle ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Le côté opposé à l'angle droit":
            $ grade += 2.0
        "Le plus petit côté":
            $ grade += 0.0
        "Le côté adjacent à l'angle droit":
            $ grade += 0.0

    "Question 6 : Si un triangle a des côtés de 7 cm, 24 cm et 25 cm, est-il rectangle ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Oui":
            $ grade += 2.0
        "Non":
            $ grade += 0.0
        "Impossible à dire":
            $ grade += 0.0

    "Question 7 : Le théorème de Pythagore est-il valable dans un triangle quelconque ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Oui":
            $ grade += 0.0
        "Non":
            $ grade += 2.0
        "Seulement dans un triangle isocèle":
            $ grade += 0.0

    "Question 8 : Que peut-on calculer grâce au théorème de Pythagore ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Les angles d'un triangle":
            $ grade += 0.0
        "Les longueurs des côtés d'un triangle rectangle":
            $ grade += 2.0
        "La somme des angles d'un triangle":
            $ grade += 0.0

    "Question 9 : Un triangle avec des côtés de 9 cm, 12 cm et 15 cm est-il rectangle ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Oui":
            $ grade += 2.0
        "Non":
            $ grade += 0.0
        "Impossible à dire":
            $ grade += 0.0

    "Question 10 : Le théorème de Pythagore permet-il de calculer la hauteur d'un triangle quelconque ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Oui, toujours":
            $ grade += 0.0
        "Non, seulement pour les triangles rectangles":
            $ grade += 2.0
        "Oui, mais seulement dans un triangle équilatéral":
            $ grade += 0.0

    $ renpy.block_rollback()
 
    stop music fadeout 2.0

    "{b}{i}Aprés l'examen tout le monde remit leur copie à [M].{/i}{/b}"
    play sound "Click.mp3" noloop 

    S "Cette examen n'était si dur que ça."
    play sound "Click.mp3" noloop

    I "Je confirme bon on verra bien les résultats."
    play sound "Click.mp3" noloop

    M "Si jamais je vous corrigerai vos copies durant la pause et vous les rendrez cet après-midi."
    play sound "Click.mp3" noloop

    S "Déjà !?" 
    play sound "Click.mp3" noloop 

    M "Oui c'est exact, bon maintenant sortez votre livre page 50 car nous allons voir un nouveau sujet." 
    play sound "Click.mp3" noloop 

    S "Et quel sera ce nouveau sujet ?" 
    play sound "Click.mp3" noloop 

    M "Un sujet de grammaire." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    K "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans probléme.{/i}{/b}"
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase

    "{b}{i} Vous descendez lez escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene lunchroom 
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

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous cherchez une place et vous apercevez [S] déjà assis à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oh salut [I] on peut venir manger avec toi ?"
    play sound "Click.mp3" noloop 

    S "Oui bien sur."
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous asseyez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon [S] je ne t'ai pas demandé. Comment c'est passé l'examen pour toi ?"
    play sound "Click.mp3" noloop 

    S "ça s'est bien passé pour moi et toi ?"
    play sound "Click.mp3" noloop 

    if grade == 20.0:

        P "Je pense que je l'ai réussi à la perfection."
        play sound "Click.mp3" noloop 

        S "ça ne m'étonne pas venant de toi."
        play sound "Click.mp3" noloop 

        Na "J'ai lui déjà dit la même chose à [prenom] un jour." 
        play sound "Click.mp3" noloop 

    elif grade <= 14.0:
       
        P "Je pense que je l'ai échoué."
        play sound "Click.mp3" noloop 

        S "Vraiment ?"
        play sound "Click.mp3" noloop 

        P "Je pense."
        play sound "Click.mp3" noloop 

    else:

        P "Je pense que je l'ai bien réussi."
        play sound "Click.mp3" noloop 
    
        S "ça ne m'étonne pas venant de toi."
        play sound "Click.mp3" noloop 

        Na "J'ai lui déjà dit la même chose à [prenom] un jour." 
        play sound "Click.mp3" noloop 

    S "Et toi [newname] comment ça s'est passée l'examen ?"
    play sound "Click.mp3" noloop 

    Na "ça s'est bien passée pour moi je ne m'inquiéte pas."
    play sound "Click.mp3" noloop 

    S "Cool alors."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 
    
    S "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    S "Ok je vous suis."
    play sound "Click.mp3" noloop 

    hide screen lunchroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    scene staircase 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway 
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

    M "Bon je vais pouvoir vous rendre les résultats de vos seonds examens."
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
        $ quest23 += 1

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

        "{b}{i}Fin numéro 9 : Mauvaise note en mathématique qui te vaut une exclusion du lycée.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:    

            "{b}{i}Abandonner{/i}{/b}" :
                return
                
            "{b}{i}Réessayer.{/i}{/b}" :
                scene classroom
                show screen class_404 with moveinright
                show screen point with moveinleft
                show screen day with moveinleft
                $ points += 300
                play music "Soundtrack.mp3" loop volume 1.0
                jump examen_pythagore 
    
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

    M "Bon la moyenne générale n'est pas mal, continuez de bien travaillez comme ceci."
    play sound "Click.mp3" noloop 

    Y "Il n'y aura pas de soucis pour moi."
    play sound "Click.mp3" noloop 

    Na "Moi aussi vous pourrez sur moi."
    play sound "Click.mp3" noloop 

    I "De même pour moi."
    play sound "Click.mp3" noloop 

    M "Bien nous pouvons continuer notre cours de ce matin sur la grammaire, veuillez sortir vos livres."
    play sound "Click.mp3" noloop 

    # à modifier 

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Bon le cours est terminé, vous pouvez quitter la salle."
    play sound "Click.mp3" noloop

    P "Bon [newname] on y vas ?"
    play sound "Click.mp3" noloop

    Na "Oui je suis fatiguée avec cet examen."
    play sound "Click.mp3" noloop 

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i} Vous entres dans ton dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene room
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

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
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

    "{b}{i} Le lundi suivant, le 21 octobre{/i}{/b}"
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

label password3:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password:

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else:

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password3

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

    P "Bon aujourd'hui je vais te faire passer un test spéciale avec [E]."
    play sound "Click.mp3" noloop

    Na "Intéressant."
    play sound "Click.mp3" noloop 

    P "Bien on y va ?"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop   

    scene hallway
    show screen hallway with moveinright 

    "{b}{i}Tu continues dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase 

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene office 
    show screen office with moveinright 

    P "Bonjour, c'est moi [prenom]."
    play sound "Click.mp3" noloop 

    E "Oh bonjour, j'imagine que tu es ici pour qu'[newname] passe le test de turing."
    play sound "Click.mp3" noloop 

    P "Oui c'est exact."
    play sound "Click.mp3" noloop 

    Na "Le test de Turing ? C'est quoi ?"
    play sound "Click.mp3" noloop 

    E "C'est un test qui différencie un Robot d'un humain."
    play sound "Click.mp3" noloop 

    Na "Je vois, c'est vraiment intéressant."
    play sound "Click.mp3" noloop 

    E "Bien commençons, [newname] tu peux t'asseoir."
    play sound "Click.mp3" noloop 

    P "Ce n'est pas seulement [newname] qui doit passer le test ?"
    play sound "Click.mp3" noloop 

    E "Oui c'est ça."
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] s'asseoit et [E] lui distribue une copie.{/i}{/b}"
    play sound "Click.mp3" noloop

    E "Bien tu as deux heures pour faire le test."
    play sound "Click.mp3" noloop 

    Na "C'est compris."
    play sound "Click.mp3" noloop 

    P "Ok moi je vais vous laiser tranquille."
    play sound "Click.mp3" noloop 

    E "C'est noté."
    play sound "Click.mp3" noloop 

    hide screen office with moveoutright
    scene black with fade 

    "{b}{i} Tu les laisses tranquille et tu reviens deux heures et demi plus tard.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene office 
    show screen office with moveinright 

    P "Me revoilà."
    play sound "Click.mp3" noloop 

    E "Ah te revoilà."
    play sound "Click.mp3" noloop 

    P "Vous avez ces résultats ?"
    play sound "Click.mp3" noloop 

    E "Oui les voici."
    play sound "Click.mp3" noloop 

    "{b}{i} [E] sort les résultats d'[newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    if grade == 20.0:

        E "D'après les résultats, elle parle à 70\% comme une humaine."
        play sound "Click.mp3" noloop 

    else: 
       
        E "D'après les résultats, elle parle à 60\% comme une humaine."
        play sound "Click.mp3" noloop 

    P "C'est génial ça."
    play sound "Click.mp3" noloop

    E "Oui mais j'ai remarqué un truc avec elle."
    play sound "Click.mp3" noloop

    P "Oui dites-moi."
    play sound "Click.mp3" noloop

    E "Malgré son Deeplearning, elle est un peu répétitive dans sa façon de parler."
    play sound "Click.mp3" noloop

    P "Je vois."
    play sound "Click.mp3" noloop 

    E "Mais en dehors de ça, elle est excellente."
    play sound "Click.mp3" noloop 

    P "Félicitation [newname]."
    play sound "Click.mp3" noloop 

    Na "Merci beaucoup [prenom], c'est grâce à toi."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Merci je suis content que tu aie appris de choses."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Merci je suis contente que tu aie appris de choses."
        play sound "Click.mp3" noloop

    E "Bien je vous laisse, il est 11h30."
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    hide screen office with moveoutright
    scene black with fade

    "{b}{i}Tu quittes le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hall
    show screen hall with moveinright 

    $ go_eat = get_random_go_eat()
    Na "[go_eat]"
    play sound "Click.mp3" noloop 

    P "Oui allons-y."
    play sound "Click.mp3" noloop 

    Na "Juste tu fsisais quoi pendant que je passais le test du Turing ?"
    play sound "Click.mp3" noloop  

    P "J'était au dortoir en train de lire."
    play sound "Click.mp3" noloop 

    Na "Cool."
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
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

    "{b}{i} Puis tu croises [I].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oh salut [I] ça te dit de venir avec nous ?"
    play sound "Click.mp3" noloop  

    I "Oui pourquoi pas."
    play sound "Click.mp3" noloop 

    P "Cool alors."
    play sound "Click.mp3" noloop 

    I "[Y] tu viens manger avec nous ?"
    play sound "Click.mp3" noloop 

    Y "Oui absolument."
    play sound "Click.mp3" noloop 

    P "[Y] !?"
    play sound "Click.mp3" noloop 

    I "Oui de base, je devais manger avec elle."
    play sound "Click.mp3" noloop 

    P "Cool alors."
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous partez tous vous asseoir à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon comment allez-vous ?"
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    P "Et toi [Y] ?"
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Y "[je_vais_bien_txt] [prenom] vas-tu bien ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    Y "Cool alors et sinon vous avez fait quoi ce matin ?"
    play sound "Click.mp3" noloop 

    P "[newname] à passé le test de Turing."
    play sound "Click.mp3" noloop 

    Y "C'est génial et elle a eu quoi commme résultats ?"
    play sound "Click.mp3" noloop 

    if grade == 20.0:

        P "Elle parle à 70\% comme une humaine."
        play sound "Click.mp3" noloop 

    else: 
       
        P "Elle parle à 60\% comme une humaine."
        play sound "Click.mp3" noloop 

    Y "Oh c'est surpenant." 
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Y "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon vous allwz faire quoi cette après-midi ?"
    play sound "Click.mp3" noloop 

    Y "Je vais sois me reposer ou bosser sur quelques trucs."
    play sound "Click.mp3" noloop 

    P "ET toi Yuna ?"
    play sound "Click.mp3" noloop 

    I "Je vais bosser sur mon jeu, j'ai du retard à rattraper."
    play sound "Click.mp3" noloop 

    P "Cool alors."
    play sound "Click.mp3" noloop 

    Y "Bon je vais vous laisser."
    play sound "Click.mp3" noloop 

    P "Pas du soucis."
    play sound "Footsteps.mp3" noloop 

    "{b}{i} [Y] quitte le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Vraiment je me demande ce que fait [Y] durant son temps libre."
    play sound "Click.mp3" noloop 

    I "Oui même moi je me demande ça."
    play sound "Click.mp3" noloop 

    P "Bon on fait quoi cette après-midi [newname] vu qu'on a pas cours ?"
    play sound "Click.mp3" noloop 

    Na "Moi je vais allez à la bibliothéque."
    play sound "Click.mp3" noloop 

    P "Ok moi je vais au dortoir pour lire."
    play sound "Click.mp3" noloop 

    Na "Ok alors on se verra après-midi."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] quitte le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais au dortoir."
    play sound "Click.mp3" noloop 

    hide screen lunchroom with moveoutright
    scene black with fade 

    "{b}{i} Tu sors du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hall with moveoutright
    scene staircase 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway 
    show screen hallway with moveinright

    "{b}{i} Vous contuez ver le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black 

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room with moveinright  

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    "{b}{i} Tu te poses sur ton lit pour lire pendant trois heures.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini de lire et je me demande quand [newname] reviens."
    play sound "Door.mp3" noloop

    "{b}{i} Puis [newname] reviens au dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oh coucou, comment c'était à la bibliothéque ?"
    play sound "Click.mp3" noloop

    Na "Bien, j'ai pu apprendre quelques trucs."
    play sound "Click.mp3" noloop

    P "Cool alors si tu as appris des choses."
    play sound "Click.mp3" noloop

    "{b}{i} vous continuez de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon on va prendre à manger ?"
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

    "{b}{i} une semaine plus tard, le 28 octobre 2097{/i}{/b}"
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

label password4:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else:

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password4

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

    $ go_in_class = get_random_go_in_class()
    Na "[go_in_class]"  
    play sound "Click.mp3" noloop 

    P "Oui, suis-moi."
    play sound "Click.mp3" noloop  

    Na "Compris."
    play sound "Click.mp3" noloop  

    hide screen room with moveoutright 
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    "{b}{i} En entrant en classe tu vois [M] avec l'[Ot] et [O].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bonjour Madame."
    play sound "Click.mp3" noloop  

    Na "Bonjour."
    play sound "Click.mp3" noloop  

    M "Bonjour."
    play sound "Click.mp3" noloop  

    "{b}{i} tous les lycéens s'asseoient à leur place.{/i}{/b}"
    play sound "Click.mp3" noloop 

    K "Sinon pourquoi la DGCA est ici aujourd'hui ?"
    play sound "Click.mp3" noloop  

    M "Ils sont là car ils ont des nouvelles à vous annoncer."
    play sound "Click.mp3" noloop  

    K "Cool."
    play sound "Click.mp3" noloop  

    M "Bon je vous laisse leur expliquer, [Ot]."
    play sound "Click.mp3" noloop  

    Oh "Compris."
    play sound "Click.mp3" noloop  

    "{b}{i}L'[Ot] se met à expliquer.{/i}{/b}"
    play sound "Click.mp3" noloop    

    Oh "bien concernant ces affaires d'attaques, nous avons découvert des informations."
    play sound "Click.mp3" noloop  

    P "Quoi comme informations ?"
    play sound "Click.mp3" noloop  

    Oh "il semblerait que l'inégalable complotiste aie réduit son activité depuis fin septembre."
    play sound "Click.mp3" noloop  

    P "Cool alors."
    play sound "Click.mp3" noloop  

    Oh "Ce n'est pas tout."
    play sound "Click.mp3" noloop 

    P "Il y a quoi d'autre ?"
    play sound "Click.mp3" noloop   

    Oh "il semblerait que l'inégalable complotiste aie aussi changé sa façon d'agir depuis ce moment."
    play sound "Click.mp3" noloop  

    Y "C'est bizarre cette histoire."
    play sound "Click.mp3" noloop  

    P "Oui soit il a compris qu'il'est surveillé ou qu'il nous tend un piége."
    play sound "Click.mp3" noloop  

    Y "Oui c'est possible."
    play sound "Click.mp3" noloop 

    Oh "Je peux vous assurer que non."
    play sound "Click.mp3" noloop  

    P "Comment ça !?"
    play sound "Click.mp3" noloop  

    Oh "Regarde, il a laissé trainer son adresse IP."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu regardes et tu vois l'adresse IP 201.125.114.115.{/i}{/b}"
    play sound "Click.mp3" noloop    

    P "Je la reconnais cette adresse IP....."
    play sound "Click.mp3" noloop  

    Oh "Comment ça !?"
    play sound "Click.mp3" noloop  

    P "Cette même adresse IP a tenté de ce connecter à [newname] plusieurs fois."
    play sound "Click.mp3" noloop  

    Oh "Je vois, J'imagine que l'inégalable complotiste veut s'en prendre à [newname]."
    play sound "Click.mp3" noloop  

    P "C'est évident."
    play sound "Click.mp3" noloop  

    Y "Sinon tu en penses quoi de cette situation ?"
    play sound "Click.mp3" noloop 

    P "ça me rend fou."
    play sound "Click.mp3" noloop  

    "{b}{i}Il y a un blanc pendant un instant.{/i}{/b}"
    play sound "Click.mp3" noloop    

    Oh "J'aurais encore une question [prenom]."
    play sound "Click.mp3" noloop  

    P "Oui dites-moi."
    play sound "Click.mp3" noloop  

    Oh "Est-ce que [newname] est déclarée à l'état civil ?"
    play sound "Click.mp3" noloop  

    P "Non... malheureusement."
    play sound "Click.mp3" noloop  

    Oh "Pourquoi ? C’est obligatoire conformément à l'article 24, alinéa 4, de juillet 2096 qui stipule que toutes les créations technologiques ou informatiques doivent être déclarées."
    play sound "Click.mp3" noloop  

    P "Oui mais à l’époque, je n'avais pas les infos nécessaires."
    play sound "Click.mp3" noloop 

    P "Nom, date de création, origine... tout était flou et surtout que je me méfie du gouvernemnt."
    play sound "Click.mp3" noloop  

    P "Vous croyez que je risque quelque chose à ne pas l’avoir déclarée ?"
    play sound "Click.mp3" noloop  

    Oh "Ça dépend. Si quelqu’un la découvre et fouille un peu, ça peut devenir sérieux."
    play sound "Click.mp3" noloop  

    P "Super... comme si j'avais pas assez de problèmes comme ça."
    play sound "Click.mp3" noloop  

    Oh "Je peux peut-être t’aider."
    play sound "Click.mp3" noloop  

    Oh "Je connais quelqu’un à l’administration. Je peux voir s’il y a un moyen discret."
    play sound "Click.mp3" noloop  

    P "Vous feriez ça ?"
    play sound "Click.mp3" noloop  

    Oh "Évidemment. [newname] mérite une existence officielle."
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Oh "[nothing]"
    play sound "Click.mp3" noloop

    Oh "Normalement dans les deux semaines qui viennent, tu me reverras pour qu'on finisse ça."
    play sound "Click.mp3" noloop  

    P "Je vois."
    play sound "Click.mp3" noloop  

    "{b}{i}Puis ils quiitent la salle.{/i}{/b}"
    play sound "Click.mp3" noloop    

    M "Bon, reprenons le cours." 
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright   
    scene staircase

    "{b}{i} Vous descendez lez escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene lunchroom 
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

    Na "Bon appétit [prenom]."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous manger tranquillement puis [S] viens vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    S "[je_vais_bien_txt] Et vous ?" 
    play sound "Click.mp3" noloop

    P "On va bien."
    play sound "Click.mp3" noloop 

    S "J'ai entendu dire qu'[newname] a réussi le test de Turing, c'est vrai ?"
    play sound "Click.mp3" noloop 

    P "Oui affirmatif."
    play sound "Click.mp3" noloop 

    S "Putain, tu maitrises vraiment ton sujet."
    play sound "Click.mp3" noloop 

    P "C'est gentil de ta part."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de discuter.{/i}{/b}"
    play sound "Bell.mp3" noloop 
    
    S "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    S "Ok je vous suis."
    play sound "Click.mp3" noloop 

    hide screen lunchroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hall with moveoutright
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene black with fade
    hide screen hallway with moveoutright

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

    M "Rebonjour, cet après-midi nous allons faire un cours de programmation."
    play sound "Click.mp3" noloop 

    S "Un cours de programmation !? et sur quel langage ?"
    play sound "Click.mp3" noloop 

    M "C'est un langage que [prenom] et [newname] connaisssent très bien."
    play sound "Click.mp3" noloop 

    S "Non, ne me dites pas que c'est....."
    play sound "Click.mp3" noloop 

    M "Oui se sera un cours de programmation sur le langage Runix"
    play sound "Click.mp3" noloop 

    S "Super fait chier."
    play sound "Click.mp3" noloop 

    M "Ton langage s'il te plait !"
    play sound "Click.mp3" noloop 

    S "Désolé."
    play sound "Click.mp3" noloop 
    
    M "Bien veuillez sortir vos livre d'informatique."
    play sound "Click.mp3" noloop 

    "{b}{i} Tout le monde sort son livre et écoute la [T].{/i}{/b}"
    play sound "Click.mp3" noloop  

    M "Bon nous allons commencer par l'introduction au langage Runix."
    play sound "Click.mp3" noloop 

    M "Le langage Runix a été inventé en 2079 par deux personnes de Neo Technologies nommmées [Sa] et [My], il a été développé pour leurs robots humanoïdes à la base."
    play sound "Click.mp3" noloop 

    S "Les robots humanoïdes !? maintenant je comprends pourquoi il le connais par coeur."
    play sound "Click.mp3" noloop 

    M "Oui mais maintenant il a été généralisé pour d'autres domaine de l'informatique."
    play sound "Click.mp3" noloop 

    S "Intérresant."
    play sound "Click.mp3" noloop 

    M "Les fichiers écrit en Runix sont des fichiers avec l'extension .rnx."
    play sound "Click.mp3" noloop 

    S "Je vois." 
    play sound "Click.mp3" noloop

    M "Tous les fichiers en .rnx commencent par la commande << initiate_ >> puis suivi du nom de l'objet, exmeple : initiate_humanoid_robot."
    play sound "Click.mp3" noloop

    S "Et pour les paramétres plus avancées ?" 
    play sound "Click.mp3" noloop

    M "Il faut mettre ses paramétres entre les parenthéses, exemple : initiate_humanoid_robot(settings=true)." 
    play sound "Click.mp3" noloop

    S "Il faut pas aussi finir ces commandes par un point-virgule ?"
    play sound "Click.mp3" noloop 

    M "Non il y n'en a pas besoin." 
    play sound "Click.mp3" noloop

    S "Donc c'est vraiment très simple."
    play sound "Click.mp3" noloop       

    P "Oui mais ce n'est que le début, après les choses vont étre plus complexe." 
    play sound "Click.mp3" noloop

    M "Bien, nous allons faire un exercice pour voir si vous avez bien compris."
    play sound "Click.mp3" noloop

    "{b}{i} Vous faites l'exercice.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    M " Bien quel est la commande pour initialiser et activer les paramétres d'un robot ?"
    play sound "Click.mp3" noloop 

    S "C'est initiate_humanoid_robot(setting) ?" 
    play sound "Click.mp3" noloop

    M "Presque ça, il manque quelque chose." 
    play sound "Click.mp3" noloop

    $ answer = renpy.input("écris ta réponse.") 
    $ answer = answer.strip() 

    M "[prenom] as-tu une idée ?" 
    play sound "Click.mp3" noloop

    P "[answer] ?"
    play sound "Click.mp3" noloop

    if answer == "initiate_humanoid_robot(setting=true)": 

        $ success += 1 
        $ quest24 += 1

        show screen update with moveinright

        M "C'est exact, bien joué."
        play sound "Click.mp3" noloop

        hide screen update with moveoutright

        P "Merci." 
        play sound "Click.mp3" noloop

    else:

        M "Ce n'est pas ça, la réponse était initiate_humanoid_robot(setting=true)."
        play sound "Click.mp3" noloop 

        P "Ah......" 
        play sound "Click.mp3" noloop

    M "Bien, nous allons continuer le cours."
    play sound "Click.mp3" noloop

    "{b}{i} Le cours continue sans problème.{/i}{/b}"       
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
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

    Na "Oui, je suis vraiment fatiguée à couse du cours sur Runix."
    play sound "Click.mp3" noloop

    P "Viens je vais te recharger et on révise un peu."
    play sound "Click.mp3" noloop

    Na "Merci."
    play sound "Click.mp3" noloop

    "{b}{i} Tu recharges [newname] pendant une heure avant de l'allumer.{/i}{/b}"
    play sound "Click.mp3" noloop

label password5:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password:

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else:

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password5   

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    P "On révise maintenant ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i}Vous vous posez au bureau du dortoir pour réviser.{/i}{/b}"
    play sound "Click.mp3" noloop 
 
    P "Prête pour réviser ?"
    play sound "Click.mp3" noloop   

    Na "Oui je suis prête."
    play sound "Click.mp3" noloop     

    "{b}{i} Vous révisez pendant deux heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 5.0

    P "Enfin fini de réviser."
    play sound "Click.mp3" noloop

    Na "Oui vraiment."
    play sound "Click.mp3" noloop

    P "Je trouves que tu fais beaucoup de progrès."
    play sound "Click.mp3" noloop

    Na "Oui merci beaucoup."
    play sound "Click.mp3" noloop

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
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

    "{b}{i} Le lendemain matin, le 29 octobre 2097{/i}{/b}"
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

label password6:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password6

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

    $ go_in_class = get_random_go_in_class()
    Na "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Foosteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    M "Bon aujourd'hui nous allons continuer le cours sur Runix."
    play sound "Click.mp3" noloop   

    S "Nous allons voir quoi exactement ?"
    play sound "Click.mp3" noloop  

    M "Les fonctionnalités avancées du langage Runix."
    play sound "Click.mp3" noloop  

    S "Intérresant."
    play sound "Click.mp3" noloop  

    M "Bien, veuillez sortir votre livre d'informatique."
    play sound "Click.mp3" noloop  

    "{b}{i} tout le monde sort leur livre.{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Pour commencer qui peut me dire à quoi sert les fonctions Runix ?"
    play sound "Click.mp3" noloop  

    P "Moi s'il vous plait."
    play sound "Click.mp3" noloop  

    if pronom == "il":

        M "[prenom], je sais que tu es investi pour les cours mais laisse les autres répondre aussi."
        play sound "Click.mp3" noloop  

        P "Désolé."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        M "[prenom], je sais que tu es investie pour les cours mais laisse les autres répondre aussi."
        play sound "Click.mp3" noloop  

        P "Désolée."
        play sound "Click.mp3" noloop 

    M "Pas de soucis, bien qui d'autrre peut me dire à quoi sert les fonctions."
    play sound "Click.mp3" noloop  

    Y "Les fonctions Runix sont des commandes qui permettent de donner des détails sur la commande initiate."
    play sound "Click.mp3" noloop  

    M "C'est exact, bien joué."
    play sound "Click.mp3" noloop   

    Y "Merci beaucoup. "
    play sound "Click.mp3" noloop  

    M "Pour faire les fonctions Runix il faut des parenthèses juste derrière le nom de l'objet avec le nom de ce que on veut changer."
    play sound "Click.mp3" noloop  

    M "Exemple avec : (Shutdown=true)."
    play sound "Click.mp3" noloop  

    Y "Je vois."
    play sound "Click.mp3" noloop  

    M "Bien je vous laisse faire les exercices."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de faire les exercices jusqu'à la fin du cours.{/i}{/b}"
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    scene staircase with fade

    "{b}{i} Vous descendez lez escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene lunchroom with fade 
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

    P "Bon appétit [prenom]."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
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

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing] Sinon, tu t'ensort comment avec Runix ?"
    play sound "Click.mp3" noloop

    I "J'ai un peu du mal."
    play sound "Click.mp3" noloop

    P "Je vois mais je pourrai t'aider avec ça."
    play sound "Click.mp3" noloop

    I "Vraiment tu veut m'aider ?"
    play sound "Click.mp3" noloop

    P "Oui absolument."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se met secrètement à rougir en regardant [I].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "ça va [newname] ?"
    play sound "Click.mp3" noloop

    I "Oui ça va ne t'inquiéte pas."
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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright

    M "Bien nous allons reprendre le cours sur Runix."
    play sound "Click.mp3" noloop 

    I "Compris."
    play sound "Click.mp3" noloop 

    M "Bon je vous laisse continuer les exercices."
    play sound "Click.mp3" noloop

    I "Oui c'est noté."
    play sound "Click.mp3" noloop

    M "Bien."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez et finissez les exercices durant tout le cours.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bien il semblerait que vous vous débrouillez pas si mal que ça."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Bell.mp3" noloop

    M "Le cours est terminé vous pouvez quitter la salle, je fixerai un examen dans deux semaines."
    play sound "Click.mp3" noloop

    P "Bon, [newname] on retourne au dortoir ?" 
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir mais [I] t'appelles.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oui [I] ?"
    play sound "Click.mp3" noloop

    I "Je voulais savoir si tu pouvais m'aider avec Runix." 
    play sound "Click.mp3" noloop
    
    P "Tu as besoin pour Runix, je croyaiz que tu était forte un programmtion."
    play sound "Click.mp3" noloop

    I "Oui mais je l'ai pas appris car c'est un langage qui ne m'est pas utile dans mes project."
    play sound "Click.mp3" noloop

    P "Je vois mais pour revenir à ta question, bien sûr que je vais t'aider."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers au dortoir pour aider [I].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
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

    I "Bon on commence à réviser ?"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    Na "[validation]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous révisez pendant deux heures avant de finir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin fini de réviser." 
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    I "Bon moi je vais vous laisser." 
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop

    I "Merci pour ton aide et à demain." 
    play sound "Click.mp3" noloop
    
    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Footsteps.mp3" noloop

    "{b}{i}[I] quitte ton dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 15.0 

    P "Bon on va prendre à manger ?"
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

    "{b}{i} Le lendemain matin, le 30 octobre 2097{/i}{/b}"
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

label password7:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password7

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

    $ go_in_class = get_random_go_in_class()
    Na "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Foosteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    M "Bien avant de commencer le cours, je vais vous donner la date pour l'examen sur Runix."
    play sound "Click.mp3" noloop

    I "Et quand sera t-il ?"
    play sound "Click.mp3" noloop  

    M "Il sera le 13 novembre."
    play sound "Click.mp3" noloop  

    I "Oh ça va on a le temps."
    play sound "Click.mp3" noloop  

    H "Oui je confirme."
    play sound "Click.mp3" noloop  

    M "Donc n'oubliez pas de bien réviser."
    play sound "Click.mp3" noloop  

    H "Oui pas de soucis, vous poussez comptez sur ça."
    play sound "Click.mp3" noloop  

    I "Oui moi aussi."
    play sound "Click.mp3" noloop  

    N "Moi je vais me mettre à fond dans les révisions."
    play sound "Click.mp3" noloop  

    M "Bien nous allons commencer le cours."
    play sound "Click.mp3" noloop 

    P  "Ce sera un cours sur quoi ?"
    play sound "Click.mp3" noloop 

    M "vous allez voir."
    play sound "Click.mp3" noloop 

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
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
 
    "{b}{i} Vous commencez à manger jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop  

    P "Bon il faut qu'on retourne en classe."
    play sound "Click.mp3" noloop    

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    scene black with fade

    "{b}{i}Vous vous diriges vers le hall.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright 

    "{b}{i}Vous continuez vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene staircase with fade

    "{b}{i}Vous continuez vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Vous continuez vers la salle de la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    M "Rebonjour, bon reprenons le cours."
    play sound "Click.mp3" noloop    

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop  

    P "Compris."
    play sound "Click.mp3" noloop    

    "{b}{i} Vous reprenez le cours tranquillement jusqu'à la fin du cours.{/i}{/b}"
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade 

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
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

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
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

    "{b}{i} Deux semaines plus tard, le 13 novembre.{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 14 
    $ points -= 2800
    $ stockage += 280.0 

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

label password8:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password8

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

            Na "Ok je vois."
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
            $ quest25 += 1
            $ stockage += 3.0 
            $ update += 1.0 

            show screen update with moveinright

            Na "Mise à jour terminée, la version actuelle est maintenant la [update]."
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

            P "Cool alors."
            play sound "Click.mp3" noloop  

    $ go_in_class = get_random_go_in_class()
    Na "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Tu te diriges vers la salle de classe mais tu croises [Y].{/i}{/b}"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop  

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Y "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop  

    P "Sinon tu es prête pour l'examen ?"
    play sound "Click.mp3" noloop  

    Y "Oui et vous ?"
    play sound "Click.mp3" noloop  

    P "Oui absolument."
    play sound "Click.mp3" noloop  

    Na "Moi aussi."
    play sound "Click.mp3" noloop  

    Y "Cool alors."
    play sound "Click.mp3" noloop  

    Na "Bon on dois aller en cours."
    play sound "Click.mp3" noloop  

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop
    
    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    M "Bien comme vous le savez aujourd'hui vous avez votre troisiéme examen qui se portera sur le langage Runix."
    play sound "Click.mp3" noloop  

    N "Je sens que ça va être dur cet examen."
    play sound "Click.mp3" noloop  

    Y "Ne t'inquiétes pas, ça va bien se passer."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    N "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Y "[nothing]"
    play sound "Click.mp3" noloop 

    M "Bon je vais vous distribuer votre copie." 
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

label examen_runix: 

    play music "Soundtrack2.mp3" loop volume 1.0

    $ grade = 0.0 

    P "Bon voyons voir....." 
    play sound "Click.mp3" noloop 

    $ answer1 = renpy.input("En quelle année a été créé Runix ?").strip()

    if answer1 == "2079":
        $ grade += 2.0
    else:
        $ grade += 0.0

    $ answer2 = renpy.input("Citez une des deux personnes qui a créé Runix.").strip().lower()

    if answer2 in ["saori kaminari", "mizuki suzumiya"]:
        $ grade += 2.0
    else:
        $ grade += 0.0

    $ answer3 = renpy.input("Comment commence-t-on une ligne de code en Runix ?").strip()

    if answer3 in ["initiate", "initiate_"]:
        $ grade += 2.0
    else:
        $ grade += 0.0

    $ answer4 = renpy.input("Quelle est l'extension des fichiers codés en Runix ?").strip().lower()

    if answer4 in ["rnx", ".rnx"]:
        $ grade += 2.0
    else:
        $ grade += 0.0

    $ answer5 = renpy.input("Quelle est la fonction pour activer les paramètres ?").strip()

    if answer5 == "(settings=true)":
        $ grade += 2.0
    else:
        $ grade += 0.0

    $ answer6 = renpy.input("Quelle est la fonction pour désactiver les paramètres ?").strip()

    if answer6 == "(settings=false)":
        $ grade += 2.0
    else:
        $ grade += 0.0

    $ answer7 = renpy.input("Quelle est la commande pour initier un système ?").strip()

    if answer7 == "initiate_system":
        $ grade += 2.0
    else:
        $ grade += 0.0

    $ answer8 = renpy.input("Pour quelle technologie le langage Runix a-t-il été créé à la base ?").strip().lower()

    if answer8 == "les robots":
        $ grade += 2.0
    else:
        $ grade += 0.0

    $ answer9 = renpy.input("Quel est le nom de la société ayant développé Runix ?").strip().lower()

    if answer9 == "neogen technologies":
        $ grade += 2.0
    else: 
        $ grade += 0.0

    $ answer10 = renpy.input("Quel est le bout de code pour éteindre en désactivant les paramètres ?").strip()

    if answer10 == "shutdown(settings=false)":
        $ grade += 2.0
    else:
        $ grade += 0.0

    $ renpy.block_rollback()

    stop music fadeout 2.0

    P "Enfin fini..." 
    play sound "Click.mp3" noloop 

    "{b}{i}Après cela tout le monde remet sa copie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    play music "Soundtrack.mp3" loop volume 1.0

    M "Parfait maintenant vous pouvez aller en pause, je vous renderez vos copies demain matin."
    play sound "Click.mp3" noloop  

    N "Demain !? c'est surpreant, d'habitude c'est l'après-midi même."
    play sound "Click.mp3" noloop  

    M "Oui mais c'était un test écrit cette fois-ci contrairement à avant."
    play sound "Click.mp3" noloop  

    hide screen class_404 with moveoutright
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade 
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    Na "Ok, moi je vais discuter un peu avec Yuki."
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveoutright
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop

    Y "Rebonjour."
    play sound "Click.mp3" noloop

    M "Rebonjour, Bon nous allons faire un nouveau sujet."
    play sound "Click.mp3" noloop  

    Na "Ce sera quoi ?"
    play sound "Click.mp3" noloop  

    M "Ce sera un cours de français."
    play sound "Click.mp3" noloop  

    Na "Je vois, merci."
    play sound "Click.mp3" noloop

    M "Aujourd'hui, nous allons étudier un point essentiel : les différentes classes de mots."
    play sound "Click.mp3" noloop

    M "Il existe dix classes principales. On les divise souvent en deux catégories : les mots variables et les mots invariables."
    play sound "Click.mp3" noloop

    Na "Variables ? Invariables ?"
    play sound "Click.mp3" noloop

    M "Exactement. Les mots *variables* changent selon le genre, le nombre, ou la personne. Les mots *invariables*, eux, ne changent jamais de forme."
    play sound "Click.mp3" noloop

    M "Commençons par les mots variables. Il y en a cinq."
    play sound "Click.mp3" noloop

    M "Les noms. Ce sont des mots qui désignent des êtres vivants, des objets ou des idées. Exemple : *chat*, *maison*, *liberté*."
    play sound "Click.mp3" noloop

    M "Ils peuvent être communs ou propres. Et ils varient en genre (masculin/féminin) et en nombre (singulier/pluriel)."
    play sound "Click.mp3" noloop

    M "Les déterminants, ils accompagnent le nom pour en préciser le sens. Exemple : *le*, *un*, *ma*, *ces*."
    play sound "Click.mp3" noloop

    M "Ils s’accordent avec le nom en genre et en nombre."
    play sound "Click.mp3" noloop

    M "Les adjectifs qualificatifs, ils donnent des précisions sur un nom. Exemple : *grand*, *bleu*, *intelligent*."
    play sound "Click.mp3" noloop

    M "Ils s’accordent eux aussi avec le nom qu’ils qualifient."
    play sound "Click.mp3" noloop

    M "Puis les pronoms, ils remplacent un nom. Exemple : *je*, *elle*, *nous*, *lequel*, *ceci*."
    play sound "Click.mp3" noloop

    M "Ils varient selon la personne, le genre ou le nombre."
    play sound "Click.mp3" noloop

    M "En suite les verbes, ils expriment une action ou un état. Exemple : *manger*, *être*, *avoir*, *finir*."
    play sound "Click.mp3" noloop

    M "Ce sont les mots les plus complexes : ils se conjuguent selon le temps, le mode, la personne et le nombre."
    play sound "Click.mp3" noloop

    Na "D’accord, donc cinq mots variables..."
    play sound "Click.mp3" noloop

    M "Et maintenant, les cinq mots invariables :"
    play sound "Click.mp3" noloop

    M "Les adverbes, ils modifient le sens d’un verbe, d’un adjectif ou d’un autre adverbe. Exemple : *vite*, *très*, *hier*, *souvent*."
    play sound "Click.mp3" noloop

    M "Ils ne s’accordent jamais."
    play sound "Click.mp3" noloop
    
    M "Les prépositions, elles introduisent un complément. Exemple : *à*, *dans*, *par*, *pour*, *sans*, *avec*."
    play sound "Click.mp3" noloop

    M "Elles indiquent souvent une relation de lieu, de temps ou de cause."
    play sound "Click.mp3" noloop
    
    M "Les conjonctions de coordination, elles relient deux éléments équivalents. Exemple : *mais*, *ou*, *et*, *donc*, *or*, *ni*, *car*."
    play sound "Click.mp3" noloop

    M "Tu connais peut-être l’acronyme ‘{i}Mais où est donc Ornicar{/i}’ ?"
    play sound "Click.mp3" noloop

    Na "Oui ! Je l’ai déjà entendu."
    play sound "Click.mp3" noloop

    M "Les conjonctions de subordination, elles introduisent une proposition subordonnée. Exemple : *que*, *quand*, *parce que*, *si*, *lorsque*."
    play sound "Click.mp3" noloop

    M "Et pour finir les interjections, ce sont des petits mots ou sons exprimant une émotion. Exemple : *Oh !*, *Aïe !*, *Zut !*."
    play sound "Click.mp3" noloop

    M "Voilà pour les dix classes de mots. C’est la base de toute analyse grammaticale."
    play sound "Click.mp3" noloop

    Na "C’est bien plus clair maintenant. Merci !"
    play sound "Click.mp3" noloop

    "{b}{i}Le cours continue tranquillement. Les élèves prennent note pendant que le professeur donne des exemples supplémentaires au tableau.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ stockage += 15.0  

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
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

    "{b}{i} Vous allez chercher une place mais [newname] tribuche en chemin avant de se faire rattraper par [S].{/i}{/b}"
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    S "[nothing] Sinon comment elle va ta machine, [prenom] ?"
    play sound "Click.mp3" noloop

    P "Déjà, on ne dit pas machine c'est super péjoraif, mais [model] doté d'une conscience humaine avancée."
    play sound "Click.mp3" noloop

    S "Ah ok, moi j'ai un terme moins péjoratif pour elle, pourquoi pas engrenage sur pattes."
    play sound "Click.mp3" noloop

    "{b}{i}Puis il y a un blanc pendant un instant avant qu'[newname] s'adresse à [S].{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Je suis [newname], fils de pute."
    play sound "Click.mp3" noloop 

    P "Calme toi un peu [newname]."
    play sound "Click.mp3" noloop 

    Na "Désolée..."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Footsteps.mp3" noloop 

    "{b}{i}Puis vous ignorez [S] avant d'allez vous asseoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    if pronom == "il" : 
    
        Na "Enfin assis."
        play sound "Click.mp3" noloop

    elif pronom == "elle" :

        Na "Enfin assises."
        play sound "Click.mp3" noloop 

    P "Oui ça fait du bien."
    play sound "Click.mp3" noloop

    "{b}{i}Vous mangez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon ça s'est passé comment l'examen pour toi ?"
    play sound "Click.mp3" noloop

    Na "Oui ça s'est bien passé pour moi et toi ?"
    play sound "Click.mp3" noloop

    P "Oui ça s'est bien passer je dirai."
    play sound "Click.mp3" noloop 

    Na "Cool alors si tu penses que tu as réussi."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Na "[nothing]"
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    I "Ok je vous suis."
    play sound "Click.mp3" noloop 

    hide screen lunchroom with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveoutright
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bonjour nous allons continuez le cours de français." 
    play sound "Click.mp3" noloop 

    Y "Bien je vois." 
    play sound "Click.mp3" noloop 

    "{b}{i} Vous reprenez le cours tranquillement jusqu'à la fin du cours.{/i}{/b}"
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
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

    "{b}{i} Vous posez tranquillement vos sacs de cours.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger je suis fatiguée de cette examen."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais chercher à manger."
    play sound "Click.mp3" noloop  

    hide screen room with moveoutright
    scene black with fade 

    "{b}{i} Tu pars chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ points -= 300 

    scene room with fade 
    show screen room with moveinright 

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    "{b}{i} Tu manges tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin fini je vais pouvoir aller dormir."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} le lendemain matin, le 14 novembre.{/i}{/b}"
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

label password9:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password9

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

    $ go_in_class = get_random_go_in_class()
    Na "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    scene black with fade

    "{b}{i}Vous quittez le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Foosteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    M "Bon aujourd'hui je vais vous rendre les résultats sur votre examen de runix."
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
        $ quest26 += 1

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
    
        M "Désolé mais j'avais déjà prévenu concernant les mauvaises notes."
        play music "gameover.mp3" noloop

        hide screen class_404 with moveoutright
        hide screen point with moveoutleftts
        hide screen day with moveoutleft
        scene black with fade

        "{b}{i}Fin numéro 10 : Mauvaise note à l'examen de Runix qui te vaut une exclusion du lycée.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:    

            "{b}{i}Abandonner{/i}{/b}" :
                return
                
            "{b}{i}Réessayer.{/i}{/b}" :
                scene classroom
                show screen class_404 with moveinright
                show screen point with moveinleft
                show screen day with moveinleft
                $ day -= 1 
                $ points += 400 
                play music "Soundtrack.mp3" loop volume 1.0
                jump examen_runix
                    
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

    M "Et toi [S] tu as eu 14/20, il faudrait réviser un peu."
    play sound "Click.mp3" noloop 

    S "Je sais mais je vais m'améliorer."
    play sound "Click.mp3" noloop

    M "Bon la moyenne générale n'est pas mal, continuez de bien travaillez comme ceci."
    play sound "Click.mp3" noloop 

    Y "Il n'y aura pas de soucis pour moi."
    play sound "Click.mp3" noloop 

    P "Il n'y aura pas de soucis pour moi."
    play sound "Click.mp3" noloop 

    M "Bien, maintenant reprenons le cours de français."
    play sound "Click.mp3" noloop

    Y "Compris."
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans probléme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    M "Si jamais vous étes libre cette après-midi car nous avons fini le sujet de français."
    play sound "Click.mp3" noloop 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
    
    hide screen hallway with moveoutright 
    scene staircase 

    "{b}{i} Vous descendez les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade 
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit() 
    Na "[sit]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allez rejoindre [Y] pour manger cette fois-ci.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop  

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Y "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop   

    P "Sinon comment s'est passé l'examen pour toi ?"
    play sound "Click.mp3" noloop 

    Y "ça s'est bien passé pour ma part et toi ?"
    play sound "Click.mp3" noloop

    if grade == 20.0:

        P "Je l'ai réussi à la perfection."
        play sound "Click.mp3" noloop 

    else: 
       
        P "Je l'ai bien réussi."
        play sound "Click.mp3" noloop

    Y "Cool alors."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Y "[nothing]"
    play sound "Click.mp3" noloop

    Y "Et sinon [newname] comment tu t'es débrouillée ?"
    play sound "Click.mp3" noloop

    Na "J'ai eu 18/20 grâce à [prenom]."
    play sound "Click.mp3" noloop

    Y "Cool alors."
    play sound "Click.mp3" noloop

    P "Juste tu vas faire quoi cet après-midi ?"
    play sound "Click.mp3" noloop

    Y "Je ferai quelques affaires dans la salle de club générale."
    play sound "Click.mp3" noloop

    P "Je vois."
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de manger et de discuter jusqu'à la sonnerie.{/i}{/b}" 
    play sound "Bell.mp3" noloop

    P "Bon [newname] on va au club ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright 
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright

    "{b}{i}Tu continues vers la salle de club mais [S] t'interpéle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tu me veux quoi ?"
    play sound "Click.mp3" noloop

    S "Je voulais juste te demander quelques choses."
    play sound "Click.mp3" noloop

    P "Quoi !?"
    play sound "Click.mp3" noloop

    S "Quand tu as trouvé [newname], tu faisais référence à quoi par \"effacement numérique\" ?"
    play sound "Click.mp3" noloop

    menu:    

        "{b}{i} La perte de la mémoire.{/i}{/b}" :

            $ renpy.block_rollback()

            $ success += 1 
            $ quest27 += 1

            show screen update with moveinright

            P "Je faisais référence à la perte de sa mémoire."
            play sound "Click.mp3" noloop
    
            hide screen update with moveoutright

        "{b}{i} Le manque de connaissance.{/i}{/b}" : 

            $ renpy.block_rollback() 

            P "Je faisais référence au manque de connaisance qu'elle a."
            play sound "Click.mp3" noloop

    S "Je vois merci."
    play sound "Footsteps.mp3" noloop

    "{b}{i}Puis vous continuez vers la salle de club.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop  

    scene clubroom with fade
    show screen clubroom with moveinright 

label code1: 

    Na "Enfin au club."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop 

    Na "Bon on fait quoi aujourd'hui ?"
    play sound "Click.mp3" noloop 

    P "Je vais voir deux-trois trucs sur l'ordinateur."
    play sound "Click.mp3" noloop 

    Na "Ok je vois."
    play sound "Click.mp3" noloop 

    P "Bon voyons voir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes toutes ses informations techniques et paramétres pendant une heure et demi.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bien il me semble que tout est bon."
    play sound "Click.mp3" noloop

    Na "Bien si tout est bon."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous posez un peu sur le canapé de la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Je suis fatigué avec cette journée."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Je suis fatiguée avec cette journée."
        play sound "Click.mp3" noloop 

    Na "Moi aussi."
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] pose doucement sa tête sur ton épaule.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "ça va ?"
    play sound "Click.mp3" noloop 

    Na "Oui ça va, je veux juste me poser sur toi un peu."
    play sound "Click.mp3" noloop 

    P "Pas de soucis alors ma petite."
    play sound "Click.mp3" noloop 

    Na "Tu sais que ça me fait vraiment plaisir d'être avec toi mais il y a truc qui me dérange."
    play sound "Click.mp3" noloop 

    P "Dis-moi tout."
    play sound "Click.mp3" noloop 

    Na "tu te souviens quand je t'ai dit que j'avait dix-huit ans ?"
    play sound "Click.mp3" noloop 

    P "Oui pourquoi ?"
    play sound "Click.mp3" noloop 

    Na "Le truc qui me dérange ce que je n'ai plus de ma date d'anniversaire en tête....."
    play sound "Click.mp3" noloop 

    if quest11 == 1:
 
        menu:    

            "{b}{i} Ne rien lui dire {/i}{/b}" :
                play sound "Menu.mp3" noloop

                $ renpy.block_rollback()

                $ success += 1 
                $ quest28 += 1

                show screen update with moveinright

                P "On pourrait dire que ta nouvelle date d'anniveraire est 4 juillet, le jour de ta récupération."
                play sound "Click.mp3" noloop 

                hide screen update with moveoutright

                $ stockage += 2.0

                Na "Merci beaucoup, j'aime trop ton idée."
                play sound "Click.mp3" noloop  

            "{b}{i} lui dire la vérité {/i}{/b}" :
                play sound "Menu.mp3" noloop  

                $ renpy.block_rollback()

                P "Aris... Il faut que tu saches la vérité. Ta véritable date d’anniversaire… c’est le 31 janvier."
                play sound "Click.mp3" noloop

                Na "Quoi ?! Tu le savais depuis le début ? Tu savais… et tu ne m’as rien dit ?"
                play sound "Click.mp3" noloop

                if pronom == "il":

                    P "Oui… Je le savais. Et je suis désolé. Je t’avais promis de ne rien dire, mais je ne peux plus te mentir."
                    play sound "Click.mp3" noloop 

                elif pronom == "elle": 

                    P "Oui… Je le savais. Et je suis désolée. Je t’avais promis de ne rien dire, mais je ne peux plus te mentir."
                    play sound "Click.mp3" noloop

                Na "Mais pourquoi ? Pourquoi tu as gardé ça pour toi ?"
                play sound "Click.mp3" noloop 

                P "Parce que [C]… ton ancien créateur… m’a supplié de ne jamais t’en parler. Il voulait que tu repartes à zéro. Que tu vives une nouvelle vie… libre de ton passé."
                play sound "Click.mp3" noloop

                Na "...Mon passé ? Qu’est-ce que tu veux dire par là ?"
                play sound "Click.mp3" noloop

                P "Tu n’étais pas censée le découvrir… mais tu as été conçue pour être une arme. Une création perfectionnée. [C] t’a privée de liberté, t’a testée dans des situations extrêmes… Et un jour, tu as cessé d’obéir."
                play sound "Click.mp3" noloop

                Na "…Je… Je comprends maintenant..."
                play sound "Click.mp3" noloop 
                
                Na "Toute cette douleur qui m'emplit n'est plus bone qu'à m'épuiser."
                play sound "Crying.mp3" noloop 

                "{b}{i}[newname] baisse la tête, submergée par les larmes.{/i}{/b}"
                play sound "Click.mp3" noloop

                if pronom == "il":

                    P "Je suis vraiment désolé… Je voulais juste te protéger. Te laisser vivre ta vie… sans chaînes."
                    play sound "Click.mp3" noloop

                elif pronom == "elle": 

                    P "Je suis vraiment désolée… Je voulais juste te protéger. Te laisser vivre ta vie… sans chaînes."
                    play sound "Click.mp3" noloop

                P "Ne pleure pas, s’il te plaît… Je suis là, et je ne te laisserai jamais seule."
                play sound "Click.mp3" noloop

                Na "Merci… Merci d’avoir fini par me le dire, [prenom]. Même si ça fait mal… au moins maintenant, je sais qui je suis vraiment."
                play sound "Click.mp3" noloop 

                $ stockage += 15.0 

    else:  

        P "On pourrait dire que ta nouvelle date d'anniveraire est 4 juillet, le jour de ta récupération."
        play sound "Click.mp3" noloop 

        $ stockage += 2.0

        Na "Merci beaucoup, j'aime trop ton idée."
        play sound "Click.mp3" noloop 

    P "De rien."
    play sound "Click.mp3" noloop 

    Na "Juste j'ai une autre question à te demander."
    play sound "Click.mp3" noloop 

    P "Oui je t'écoute."
    play sound "Click.mp3" noloop

    "Son regard se perd à travers la fenêtre, comme si elle cherchait une autre réalité..." 
    play sound "Click.mp3" noloop

    Na "Puis-je trouver une vie qui ressemble à un conte de fées ? Loin de cette tragédie."
    play sound "Click.mp3" noloop           

    P "Mais tu l'as déjà trouvé ta vie qui ressemble à un conte de fées, c'est depuis que tu es sous ma responsabilté."
    play sound "Click.mp3" noloop  

    "Elle baisse légèrement les yeux, puis esquisse un sourire discret."
    play sound "Click.mp3" noloop  

    Na "Tu me donnes de l'attention, une belle affection."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]" 
    play sound "Click.mp3" noloop
 
    P "Il faut qu'on retourne au dortoir il se fait tard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

###################################################################

    hide screen clubroom with moveoutright
    scene black with fade 

    "{b}{i}Tu quittes la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveiright

    "{b}{i}Tu prends les escaliers.{/i}{/b}" 
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    scene staircase with fade 

    "{b}{i} Puis tu continues vers le couloir avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

##############################################################################33

    P  "Cette journée était vraiment fatiguante."
    play sound "Click.mp3" noloop

    Na "je confirme."
    play sound "Click.mp3" noloop 

    P "Bon on va prendre à manger ? J'avais complétement oublié."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade 

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

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

    "{b}{i} Le lendemain matin, le 15 novembre 2097{/i}{/b}"
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

    P "Sacrée [newname], encore déconnectée mais je pense que la discussion d'hier la un peu perturbé."
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password10:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "Mot de passe correct. Accès autorisé." 
        play sound "Menu.mp3" noloop

    else: 

        "Mot de passe incorrect. Accès refusé." 
        play sound "Menu.mp3" noloop
        jump password10

    $ start = get_random_start()
    Na "[start]"
    play sound "Click.mp3" noloop 

    Na  "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop 

    if quest28 == 1:

        Na "Pas trop si tu veux le savoir."
        play sound "Click.mp3" noloop 

        if pronom == "il": 
    
            P "Ah je vois, je suis désolée de t'avoir dit la vérité."
            play sound "Click.mp3" noloop

        elif pronom == "elle":

            P "Ah je vois, je suis désolée de t'avoir dit la vérité."
            play sound "Click.mp3" noloop

    else:

        $ je_vais_bien_txt = get_random_je_vais_bien() 
        Na "[je_vais_bien_txt] Et toi sinon ça va ?" 
        play sound "Click.mp3" noloop

        $ je_vais_bien_txt = get_random_je_vais_bien() 
        P "[je_vais_bien_txt]"
        play sound "Click.mp3" noloop 

    Na "Bon aujourd'hui on est sensé recevoir notre budget du mois." 
    play sound "Click.mp3" noloop

    P "Oui c'est vrai." 
    play sound "Click.mp3" noloop

    if grade == 20.0: 

        $ points += 15000

    else:

        $ points += 11000 

    Na "On viens de les recevoir." 
    play sound "Click.mp3" noloop

    P "Ah oui tu as raison." 
    play sound "Click.mp3" noloop 

    "{b}{i} Puis il y a un silence pendant un court instant.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Est-ce que ça va [prenom] ?"
    play sound "Click.mp3" noloop 

    P "Oui mais je pensais juste à cette histoire de traître ?"
    play sound "Click.mp3" noloop  

    Na "Oui et ?"
    play sound "Click.mp3" noloop 

    P "C'est moi ou il y a un truc qui cloche dans cette histoire ?"
    play sound "Click.mp3" noloop 

    Na "Oui effectivement."
    play sound "Click.mp3" noloop 

    P "Bon on doit aller en cours avant d'étre en retard."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop 

    P "Bien alors allons-y."
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i}Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    M "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    I "[salutation_rdm]"
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

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson() 
    M "[endlesson]"
    play sound "Click.mp3" noloop

    $ stockage += 15.0 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis vous continuez encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Tu entres dans le réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade 
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

    "{b}{i} En allant manger tu croises [I].{/i}{/b}"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    I "Oh salut [prenom] et [newname], oui moi ça va bien et vous ?"
    play sound "Click.mp3" noloop 

    if quest28 == 1:

        Na "Pas trop si tu veux le savoir."
        play sound "Click.mp3" noloop 

        I "Il se passe quoi [newname] ?"
        play sound "Click.mp3" noloop 

        Na "Rien ça va à part que ma vie est basée sur un mensonge."
        play sound "Click.mp3" noloop 

        I "Je vois."
        play sound "Click.mp3" noloop 

        "{b}{i} Vous conntinuez de discuter pendant que vous mangez jusqu'à la sonnerie sauf [newname] qui reste son téléphone.{/i}{/b}"
        play sound "Bell.mp3" noloop

    else: 

        $ je_vais_bien_txt = get_random_je_vais_bien() 
        Na "[je_vais_bien_txt] Et toi ?" 
        play sound "Click.mp3" noloop

        $ je_vais_bien_txt = get_random_je_vais_bien() 
        I "[je_vais_bien_txt]"
        play sound "Click.mp3" noloop 

        Na "Cool alors."
        play sound "Click.mp3" noloop 

        I "Et toi [prenom], ça va ?"
        play sound "Click.mp3" noloop 

        $ je_vais_bien_txt = get_random_je_vais_bien() 
        P "[je_vais_bien_txt]"
        play sound "Click.mp3" noloop 

        Na "Cool alors."
        play sound "Click.mp3" noloop 

        "{b}{i} Vous conntinuez de discuter pendant que vous mangez jusqu'a la sonnerie.{/i}{/b}"
        play sound "Bell.mp3" noloop 

    P "Bon on retourne en cours." 
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    scene black with fade
    
    "{b}{i}Vous vous dirigez vers le hall.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright 

    "{b}{i}Vous continuez vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene staircase with fade

    "{b}{i}Vous continuez vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Vous continuez vers la salle de la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade 
    show screen class_404 with moveinright  

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop

    M "Bon reprenons notre exploration du monde fascinant des réseaux. La dernière fois, on s’est arrêtés au routage dynamique."
    play sound "Click.mp3" noloop

    M "Aujourd’hui, voyons ce qu’il se passe quand une machine veut tester la connectivité avec une autre."
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

    "{b}{i} le cours continue dans le calme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    $ stockage += 5.0 

    P "Bon [newname] on n'y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui je suis fatiguée."
    play sound "Footsteps.mp3" noloop 

    hide screen class_404 with moveoutright
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir mais vous apercevez deux personnes venir vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bonjour, pourrai-je savoir qui étes-vous ?"
    play sound "Click.mp3" noloop 

    Rk "Bonjour, je suis [Rk]."
    play sound "Click.mp3" noloop 

    P "Et vous ?"
    play sound "Click.mp3" noloop 

    Nk "Bonjour, je suis [Nk]."
    play sound "Click.mp3" noloop 

    P "Et pourquoi vous étes ici ?"
    play sound "Click.mp3" noloop 

    Rk "Nous sommes journalistes et nous venons vous poser quelques questions."
    play sound "Click.mp3" noloop 

    "{b}{i} Après avoir entendu ça, [newname] se cache dérrière toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "ça va aller [newname]."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    "{b}{i} Puis tu tu remets à regarder les journalistes.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Mais ça ne va pas de débarquer comme ça !!!"
    play sound "Click.mp3" noloop 

    Rk "Doucement nous voulons juste te poser des questions."
    play sound "Click.mp3" noloop 

    "{b}{i} En même temps, [M] viens vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Que se passe t'il ici."
    play sound "Click.mp3" noloop 

    P "Ce n'est rien, ne vous inquiètez pas."
    play sound "Click.mp3" noloop 

    M "Je vois bon, je vais vous laisser discuter."
    play sound "Click.mp3" noloop 

    P "D'acoord."
    play sound "Click.mp3" noloop 

    "{b}{i} [M] se met à partir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon...."
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Accepter l'interview {/i}{/b}" : 

            $ renpy.block_rollback()

            P "J'accepte de répondre à vos questions."
            play sound "Click.mp3" noloop 

            $ thanks = get_random_thanks()
            Rk "[thanks]"
            play sound "Click.mp3" noloop

            $ nothing = get_random_nothing()
            P "[nothing]"
            play sound "Click.mp3" noloop 

            Rk "Bien ma première question est : Quel est le nom de votre [model] ?"
            play sound "Click.mp3" noloop 

            P "Elle se nomme [Na]."
            play sound "Click.mp3" noloop 

            Rk "Bien, ma seconde question : Quel âge a [newname] ?"
            play sound "Click.mp3" noloop

            P "Elle a 18 ans."
            play sound "Click.mp3" noloop 

            Rk "Bien, ma troisiéme question : Quel est son nom technique ?"
            play sound "Click.mp3" noloop

            P "C'est [A] ?"
            play sound "Click.mp3" noloop

            Rk "Je vois merci sinon qu'elles sont ses caratéristiques techniques."
            play sound "Click.mp3" noloop 

            P "Je ne préfére pas répondre à la question."
            play sound "Click.mp3" noloop 

            Rk "Je vois il n'y a pas de soucis et j'ai une derniére question pour vous."
            play sound "Click.mp3" noloop 

            P "Oui dites-moi."
            play sound "Click.mp3" noloop 

            RK "Qui es-tu pour [newname] ?"
            play sound "Click.mp3" noloop 

            if pronom == "il" : 
  
                P "Je suis [P], son créateur."
                play sound "Click.mp3" noloop 

            elif pronom == "elle" :

                P "Je suis [P], sa créatrice."
                play sound "Click.mp3" noloop 

            RK "Bien merci pour ces informations."
            play sound "Click.mp3" noloop 

            $ nothing = get_random_nothing()
            P "[nothing]"
            play sound "Click.mp3" noloop

            RK "Bon on va vous laisser on va pas vous déranger encore plus."
            play sound "Click.mp3" noloop 

            P "Au revoir."
            play sound "Click.mp3" noloop 

            RK "Au revoir."
            play sound "Footsteps.mp3" noloop 

            "{b}{i} Les journalistes se mettent à partir.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Enfin, bon [newname], on y va ?"
            play sound "Click.mp3" noloop 

            $ suivi = get_random_suivi() 
            Na "[suivi]" 
            play sound "Footsteps.mp3" noloop 

        "{b}{i} refuser l'interview {/i}{/b}" : 

            $ renpy.block_rollback()

            $ success += 1  
            $ quest29 += 1

            show screen update with moveinright

            if pronom == "il" : 
    
                P "Je suis navré de vous dire que je refuse votre interview."
                play sound "Click.mp3" noloop

            elif pronom == "elle" : 

                P "Je suis navrée de vous dire que je refuse votre interview."
                play sound "Click.mp3" noloop

            hide screen update with moveoutright

            Rk "Et pourquoi cela, nous sommes dans notre droit de vous interviewer."
            play sound "Click.mp3" noloop 

            P "Oui sauf que je refuse qu'elle soit interviewée."
            play sound "Click.mp3" noloop 

            Rk "Bien c'est entendu alors, nous te laissons tranquille."
            play sound "Footsteps.mp3" noloop 

            "{b}{i} Les journalistes se mettent à partir.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Enfin, bon [newname], on y va ?"
            play sound "Click.mp3" noloop 

            $ suivi = get_random_suivi() 
            Na "[suivi]" 
            play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous continuez vers le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    hide screen hallway with moveoutright
    scene black with fade 

    "{b}{i} Vous entres dans ton dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene room with fade 
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

    P "Juste il faut que tu le saches mais en général les journalistes sont vraiment chiants."
    play sound "Click.mp3" noloop 

    $ stockage += 2.0 

    Na "Vraiment autant que ça ?"
    play sound "Click.mp3" noloop 

    P "Oui tout ce qu'ils veulent c'est de l'argent et de la gloire avec des informations sur les autres."
    play sound "Click.mp3" noloop 

    Na "Entre nous, ils sont journalistes donc normal qu'ils aient besoin d'informations."
    play sound "Click.mp3" noloop

    P "Oui mais des fois ça deviens trop personnel et intrusif leurs questions."
    play sound "Click.mp3" noloop 

    Na "Ah je vois."
    play sound "Click.mp3" noloop

    P "Mais de toute façon, vu notre situation actuelle avec le traître, la DGCA et le gouvernement qui nous surveille, les journalistes sont les derniers de nos soucis."
    play sound "Click.mp3" noloop 

    Na "Oui tu as raison."
    play sound "Click.mp3" noloop
    
    P "En plus je dois me concentrer sur le lycée et ton amélioration."
    play sound "Click.mp3" noloop 

    Na "Bon sinon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "Je vais voir tes paramétres."
    play sound "Click.mp3" noloop 

    Na "Génial."
    play sound "Click.mp3" noloop

label update1: 

    if update == 2.0: 

        "{b}{i}Tu t'asseois et allumes ton ordinateur mais [newname] agit bizarrement.{/i}{/b}"
        play sound "Click.mp3" noloop

        A "Système opérationnel."
        play sound "Click.mp3" noloop

        P "Comment ça ? Qu'est-ce que tu racontes !?"
        play sound "Click.mp3" noloop

        A "Démarrage du transfert des données vers un autre ordinateur."
        play sound "Click.mp3" noloop

        $ stockage -= 15.0

        P "Mince elle est en train de se faire pirater, je dois activer le Recovery Mode....."
        play sound "Click.mp3" noloop 

        menu: 

            "{b}{i}Accéder à l'interface bios d'[newname].{/i}{/b}":
                play sound "Menu.mp3" noloop

        $ reboot = renpy.input("Écris ceci : initiate_humanoid_robot.shutdown(security_override=false)")
        $ reboot = reboot.strip() 

        if reboot == "initiate_humanoid_robot.shutdown(security_override=false)":
            
            A "Fermeture du système d'exploitation [system]....."
            play sound "Click.mp3" noloop

            P "Enfin mais c'est bizarre on dirait que la faille du systéme d'exploitation."
            play sound "Click.mp3" noloop 

            P "J'espére qu'il n'y a de Backdoor qui a été installé dans le systéme d'[newname]."
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

                "{b}{i}Fin numéro 11 : Complétement plaqué et étranglé par [Na].{/i}{/b}"
                play sound "Menu.mp3" noloop

            elif pronom == "elle":

                "{b}{i}Fin numéro 11 : Complétement plaquée et étranglée par [Na].{/i}{/b}"
                play sound "Menu.mp3" noloop

            menu:

                "{b}{i}Abandonner{/i}{/b}":
                    return
                    
                "{b}{i}Réessayer.{/i}{/b}":
                    scene room with fade
                    show screen room with moveinright
                    show screen point with moveinleft
                    show screen day with moveinleft
                    play music "Soundtrack2.mp3" loop volume 1.0
                    jump update1

    else: 

        "{b}{i}Tu t'asseois et allumes ton ordinateur.{/i}{/b}"
        play sound "Click.mp3" noloop

    P "Bien voyons voir...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu regardes tous les paramétres pendant deux heures mais tu remarques quelques choses.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "On dirait qu'il y a rien de nouveau dans [system]."
    play sound "Click.mp3" noloop 

    Na "Bon on fait quoi du coup ?"
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
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
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
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
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
    scene black with fade 

    "{b}{i}Tu quitte la salle de classe avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway with fade 
    show screen hallway with moveinright 

    P "Je me demande ce qui ce passe pour que ce soit urgent."
    play sound "Click.mp3" noloop 
    
    Na "Oui mais aussi je me le demande."
    play sound "Click.mp3" noloop

    "{b}{i}Tu continues dans le couloir avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade 

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
    
    stop music fadeout 2.0 

    hide screen hall with moveoutright
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    play music "Soundtrack2.mp3" loop volume 1.0

    scene office 
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

    P "Pourquoi que faites-vous ici ?"  
    play sound "Click.mp3" noloop 

    Ln "Je suis venue après avoir entendu parler d'[newname]."  
    play sound "Click.mp3" noloop

    P "Attendez... vous connaissez [newname] ? Comment ?"
    play sound "Click.mp3" noloop 

    Ln "Je suis au courant grâce à la DGCA. Le gouvernement surveille tout ce qui concerne les projets non-répertoriés. Et celui-ci... dépasse largement tout ce que nous avons vu jusque-là."
    play sound "Click.mp3" noloop

    P "Que voulez-vous de moi et de [newname] ?"
    play sound "Click.mp3" noloop 

    Ln "Rien. Je suis là pour éviter que la situation ne dégénère. [newname] n'est pas encore considérée comme une menace. Pas encore."
    play sound "Click.mp3" noloop

    P "Et si je vous disais que [newname] est bien plus qu’un simple programme ?"
    play sound "Click.mp3" noloop

    Ln "Je le sais déjà. C’est justement pour ça que je suis ici. Dis-moi, es-tu réellement capable de la contrôler ?"
    play sound "Click.mp3" noloop 

    P "Oui, normalement. J’ai un vrai contrôle sur elle... mais elle agit aussi de son propre chef."
    play sound "Click.mp3" noloop 

    Ln "Je vois… Donc, je n’ai pas à m’inquiéter pour la sécurité publique."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    P "Pourquoi vous et pas le président directement ?"
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
            $ quest30 += 1 
 
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

    Ln "Bien."
    play sound "Click.mp3" noloop 

    "{b}{i}[Ln] et l'[Ot] quittent le breau des élèves.{/i}{/b}"
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
    scene black with fade 

    "{b}{i}Vous quittez le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hall with fade 
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hall with moveoutright
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade 
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade 
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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    # à modifier 

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
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
    scene black with fade 

    "{b}{i} Vous entrez au dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene room with fade 
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
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Tu continues dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene office with fade 
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
    scene black with fade 

    "{b}{i} Puis tu quittas le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    scene staircase with fade

    "{b}{i}Tu continues vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Tu continues ton chemin.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hallway with moveoutright
    scene black with fade 

    "{b}{i} Vous entres dans ton dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop 

    scene room with fade 
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
    scene black with fade 

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
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
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

    # à modifier 

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

    # à modifier 

    "{b}{i}Le cours continue jusqu'à la pause.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade 
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
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade 
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Click.mp3" noloop

    hide screen WC with moveoutright
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

    M "Bien reprenons le cours."
    play sound "Click.mp3" noloop

    # à modifier 

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade 
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

    P "Bon appétit [prenom]."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
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
            $ quest31 += 1 

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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i}Tu continues vers la salle de club.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop  

    scene clubroom with fade
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
    scene black with fade

    "{b}{i} Puis tu sors de la salle de club général.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i}Tu prends les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene staircase with fade

    "{b}{i} Puis tu continues vers le couloir avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
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

    show screen mail # à modifier 

    "{b}{i}Tu lis tranquillement le mail.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen mail # à modifier 

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
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
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
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade
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
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveoutright
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    # à modifier 

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
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
    scene black with fade
    
    "{b}{i}Tu te diriges vers le hall.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene staircase with fade

    "{b}{i}Tu continues vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i}Tu continue vers la salle de la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright  

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    M "Bon aujourd'hui je vais vous rendre les résultats sur votre examen de runix."
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
        $ quest32 += 1

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

    # à modifier 

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
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
            $ quest33 += 1
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
    scene black with fade 

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
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
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers la réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene staircase with fade

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
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
            $ quest34 += 1

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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe mais vous croisez [J2] qui monte aussi en classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hall with moveinright
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
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

        $ reboot = renpy.input("Écris ceci : initiate_humanoid_robot.shutdown(security_override=false)")
        $ reboot = reboot.strip() 

        if reboot == "initiate_humanoid_robot.shutdown(security_override=false)":
            
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
    scene black with fade  

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
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
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
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

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "ClicK.mp3" noloop 

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers la réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe mais vous croisez [J2] qui monte aussi en classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hall with moveinright
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    # à modifier 

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ stockage += 8.0 

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
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
            $ quest35 += 1
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
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene staircase 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    scene staircase 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway 
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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
        $ quest36 += 1

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

        "{b}{i}Fin numéro 14 : Mauvaise note en philosophie qui te vaut une exclusion du lycée.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:    

            "{b}{i}Abandonner{/i}{/b}" :
                return
                 
            "{b}{i}Réessayer.{/i}{/b}" :
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

    "{b}{i} Vous sortez votre livre et le cours continue tranquillement..{/i}{/b}"
    play sound "Bell.mp3" noloop

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
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

    "{b}{i} Vous vous dirigez vers le couloir avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway  
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
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
    scene black with fade

    "{b}{i}Vous quittez le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i}Tu continues dabs le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
     
    scene hall with fade
    show screen hall with moveinright 

    "{b}{i}Tu poursuit vers la salle de club générale.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene black with fade

    "{b}{i}Tu entres dans la salle de club générale.{/i}{/b}"
    play sound "Door.mp3" noloop
 
    scene clubroom
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

    if quest25 == 1:

        K "Le 15 novmebre, il y a eu une tentative de connexion sans succès."  
        play sound "Click.mp3" noloop

    else:

        K "Le 19 novembre, il y a eu une connexion à [newname] et un début de transfert de données vers un autre ordinateur"  
        play sound "Click.mp3" noloop

    if quest21 == 1:

        K "Le 19 novembre, il y a eu une tentative de compromission du mot de passe."  
        play sound "Click.mp3" noloop 

    else: 

        K "Le 19 novembre, son mot de passe a été compris par force-brute."  
        play sound "Click.mp3" noloop

    if quest33 == 1:

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
    scene black with fade 

    "{b}{i} Vous quittez la salle de club.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hall
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    scene staircase  

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway 
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
    scene black with fade 

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que j'aille au dortoir."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway with moveinright

    "{b}{i} Tu continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    scene black with fade 

    "{b}{i}Vous entrez dans le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
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
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
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

######################################################################

    menu: 

        "{b}{i}Lui proposer ton aide pour les révisions.{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            $ success += 1
            $ quest37 += 1 


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

##########################################################################################

    P "Bon on va prendre à manger ?"
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
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway 
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
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
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

    Na "Bon appétit [prenom]."
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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    scene staircase 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway 
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen class_404 with moveinright 

    M "Rebonjour, nous allons reprendre le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "Bien maintenant ouvrez votre livre d'histoire à la page 36." 
    play sound "Click.mp3" noloop  

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
    scene black with fade

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
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
        jump passwor20

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
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    if quest37 == 1:

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright 
    scene staircase

    "{b}{i} Vous descendez lez escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene lunchroom 
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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    scene staircase 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway 
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
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

#####################################################################################

    P "On pourrait réviser comme hier."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()  
    Na "[validation]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous posez pour les révisions.{/i}{/b}"
    play sound "Click.mp3" noloop

###################################################################################33

    P "Bon on va prendre à manger ?"
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

    scene room
    show screen room with moveinright
    show screen day
    $ day += 1 

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
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveinright
    scene staircase 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway 
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop     

    M "Bien nous pouvons reprendre le cours."
    play sound "Click.mp3" noloop 

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
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
    scene staircase

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
     
    scene hall with fade
    show screen hall with moveinright 

    "{b}{i}Vous poursuivez vers la salle de club générale.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene black with fade

    "{b}{i}Vous entrez dans la salle de club générale.{/i}{/b}"
    play sound "Door.mp3" noloop
 
    scene clubroom
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
    scene black with fade

    "{b}{i}Vous quittez la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene staircase

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway
    show screen hallway with moveinright

    "{b}{i}Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
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
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    # à modifier 

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

    # à modifier 

    M "Parfait, maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  

    hide screen class_404 with moveoutright
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade 
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
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom
    show screen WC with moveinright

    P "Bon, je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon, il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    # à modifier 

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase

    "{b}{i} Vous descendez lez escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene lunchroom 
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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveinright
    scene staircase 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway 
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
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

    # à modifier  

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway with moveinright 

    P "Bon cette journée est enfin finie..."
    play sound "Click.mp3" noloop 

    Na "Oui enfin..."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play souns "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
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

    # à modifier

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
    scene black with fade

    "{b}{i}Vous quittez le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Foosteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
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

    # à modifier  

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
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
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright

    "{b}{i} Vous continuez dans le hall.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveoutright
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    I "Rebonjour."
    play sound "Click.mp3" noloop 

    # à modifier 

    "{b}{i} Le cours se déroule tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

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
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
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

    "{i}Tu penses soudainement a quelques choses et [newname] te regardes.{/i}"
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

            P "Merci, Na. Ça compte beaucoup pour moi."
            play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    Na "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    scene black with fade 

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
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

# Aris la plus belle <333333333333333333333333333 