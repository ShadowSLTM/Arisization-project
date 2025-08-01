﻿################################################################################
## Initialisation
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Écrans de jeu
################################################################################


## Écran des dialogues #########################################################
##
## L’écran des dialogues est utilisé pour afficher les dialogues du joueur. Il
## prend deux paramètres, who(qui) et what(quoi) qui sont respectivement le
## nom du personnage en train de parler et le texte à afficher. (Le paramètre
## who(qui) peut être None si aucun nom n’est donné.)
##
## Cet écran affiche le texte correspondant à what. Il peut également créer un
## texte avec le paramètre who et l’identifiant « window » est utilisé pour
## déterminer les styles à appliquer.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Si il y a une side image, l'afficher au-dessus du texte. Ne pas
    ## l'afficher sur la version téléphone - pas assez de place.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Rendre la boîte du nom personnalisable à travers l'objet Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Écran de saisie #############################################################
##
## Cet écran est utilisé pour afficher renpy.input. Le paramètre prompt est
## utilisé pour passer le texte par défaut.
##
## Cet écran doit créer une entrée affichable avec l'id "input" pour accepter
## les différents paramètres.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Écran des choix #############################################################
##
## Cet écran est utilisé pour afficher les choix qui seront fait par le joueur
## dans le jeu. Le premier paramètre, items, est une liste d'objets contenant
## chacun des champs de texte et d'action.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Écran des menus rapides #####################################################
##
## Les menus rapides sont affichés dans le jeu pour permettre un accès rapide à
## certaines fonctions.

define quick_menu = True

screen quick_menu():

    ## Assure qu'il apparaît au-dessus des autres screens.
    zorder 100

    if quick_menu:

        hbox: 
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Retour") action Rollback()
            textbutton _("Historique") action ShowMenu('history')
            textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Snapshot") action ShowMenu('save')
            textbutton _("Snapshot R.") action QuickSave()
            textbutton _("Snapshot R.") action QuickLoad()
            textbutton _("Préf.") action ShowMenu('preferences')
            textbutton _("Succès") action ShowMenu('success')
            textbutton _("[A]") action ShowMenu("robot") 

## Ce code garantit que le menu d’accès rapide sera affiché dans le jeu, tant
## que le joueur n’aura pas explicitement demandé à cacher l’interface.
init python:
    config.overlay_screens.append("quick_menu") 

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Screens du menu principal et du menu de jeu
################################################################################

## Écran de navigation #########################################################
##
## Cet écran est disponible dans le menu principal et dans le menu de jeu. Il
## fournit l’accès aux autres menus et permet le démarrage du jeu.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Nouvelle partie") action Start() 

        else: 

            textbutton _("Historique") action ShowMenu("history")

            textbutton _("Snapshot") action ShowMenu("save")

        textbutton _("Charger") action ShowMenu("load")

        textbutton _("Préférences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Fin de la rediffusion") action EndReplay(confirm=True)

        elif not main_menu: 

            textbutton _("Menu principal") action MainMenu()
            
        textbutton _("À propos") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## L'aide n’est ni nécessaire ni pertinente sur les appareils
 
            textbutton _("Aide") action ShowMenu("help")

            textbutton _("Boutique") action ShowMenu("Shop")

            textbutton _("Succès") action ShowMenu("success")  

            textbutton _("Ton robot") action ShowMenu("robot") 

            textbutton _("Personnages") action ShowMenu("characters")

            textbutton _("Crédits") action ShowMenu("credit")

        if renpy.variant("pc"): 

            textbutton _("Quitter ton robot") action Quit(confirm=not main_menu) 

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Écran du menu principal #####################################################
##
## Utilisé pour afficher le menu principal quand Ren'Py démarre.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Ceci assure que tout autre screen de menu est remplacé.
    tag menu

    add gui.main_menu_background

    ## Cette frame vide obscurcit le menu principal.
    frame:
        style "main_menu_frame"

    ## L'instruction use inclut un autre écran à l'intérieur de celui-ci. Le
    ## vrai contenu du menu principal se trouve dans l'écran "navigation".
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Écran du menu de jeu ########################################################
##
## Ceci présente la structure commune de base d'un écran du menu de jeu. Il est
## appelé en lui passant le titre de l'écran, et il affiche l'arrière-plan, le
## titre et la navigation.
##
## Le paramètre de défilement peut être None, ou "viewport" ou "vpgrid". Cet
## écran est destiné à être utilisé avec un ou plusieurs enfants, qui sont
## transclus (placés) à l'intérieur de l'écran.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Réserve de l'expace pour la section de navigation.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Retour"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

## Écran de chargement et de Snapshot ########################################
##
## Ces écrans permettent au joueur d’enregistrer le jeu et de le charger
## à nouveau. Comme ils partagent beaucoup d’éléments communs, ils sont
## tous les deux implémentés dans un troisième écran, appelé fichiers_slots
## (emplacement_de_fichier).
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Snapshot"))


screen load():

    tag menu

    use file_slots(_("Charger"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Snapshots automatiques"), quick=_("Snapshots rapides"))

    use game_menu(title):

        fixed:

            ## Cette instruction s’assure que l’évènement enter aura lieu avant
            ## que l’un des boutons ne fonctionne.
            order_reverse True

            ## Le nom de la page, qui peut être modifié en cliquant sur un
            ## bouton.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La grille des emplacements de fichiers.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A %d %B %Y, %H:%M"), empty=_("emplacement vide")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Boutons pour accéder aux autres pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) donne les nombres de 1 à 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Uploader Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Télécharger Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Écran des préférences #######################################################
##
## L’écran de préférences permet au joueur de configurer le jeu pour mieux
## correspondre à ses attentes.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Préférences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Affichage")
                        textbutton _("Fenêtre") action Preference("display", "window")
                        textbutton _("Plein écran") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Avance rapide")
                    textbutton _("Texte non lu") action Preference("skip", "toggle")
                    textbutton _("Après les choix") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Des boites vbox additionnelles de type "radio_pref" ou
                ## "check_pref" peuvent être ajoutées ici pour ajouter des
                ## préférences définies par le créateur du jeu.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Vitesse du texte")

                    bar value Preference("text speed")

                    label _("Avance automatique")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Volume de la musique")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volume des sons")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Volume des voix")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Couper tous les sons"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Écran de l'historique #######################################################
##
## Il s’agit d’un écran qui affiche l’historique des dialogues au joueur. Bien
## qu’il n'y ait rien de spécial sur cet écran, il doit accéder à l’historique
## de dialogue stocké dans _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Cette instruction permet d’éviter de prédire cet écran, car il peut être
    ## très large
    predict False

    use game_menu(_("Historique"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Cela positionne correctement l'écran si history_height est
                ## initialisé à None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Utilise pour la couleur du texte, la couleur par
                        ## défaut des dialogues du personnage si elle a été
                        ## initialisée.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("L'historique des dialogues est vide.")


## Ceci détermine quels tags peuvent être affichés sur le screen de
## l'historique.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Écran d'aide ################################################################
##
## Cet écran fournit des informations sur les touches et les boutons de souris.
## En interne, il utilise d’autres écrans (keyboard_help, mouse_help et
## gamepad_help) pour afficher une aide dédiée.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Aide"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Clavier") action SetScreenVariable("device", "keyboard")
                textbutton _("Souris") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Manette") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():

    hbox:
        label _("Entrée")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Espace")
        text _("Avance dans les dialogues sans effectuer de choix.")

    hbox:
        label _("Flèches directionnelles")
        text _("Permet de se déplacer dans l’interface.")

    hbox:
        label _("Echap.")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Ctrl")
        text _("Fait défiler les dialogues tant que la touche est pressée.")

    hbox:
        label _("Tab")
        text _("Active ou désactive les «sauts des dialogues».")

    hbox:
        label _("Page Haut")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Page Bas")
        text _("Avance jusqu'au prochain dialogue.")

    hbox:
        label "H"
        text _("Cache l’interface utilisateur.")

    hbox:
        label "S"
        text _("Prend une capture d’écran.")

    hbox:
        label "V"
        text _("Active la {a=https://www.renpy.org/l/voicing}{size=24}vocalisation automatique{/size}{/a}.")

    hbox:
        label "Shift+A"
        text _("Ouvre le menu d'accessibilité.")


screen mouse_help(): 

    hbox:
        label _("Bouton gauche")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Bouton central")
        text _("Cache l’interface utilisateur.")

    hbox:
        label _("Bouton droit")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Molette vers le haut")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Molette vers le bas")
        text _("Avance jusqu'au prochain dialogue.")


screen gamepad_help():

    hbox:
        label _("Bouton R1\nA/Bouton du bas")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Gâchettes gauche")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Bouton R1")
        text _("Avance jusqu'au prochain dialogue.")

    hbox:
        label _("Boutons directionnels, stick gauche")
        text _("Permet de se déplacer dans l’interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Y/Bouton du haut")
        text _("Cache l’interface utilisateur.")

    textbutton _("Calibrage") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Écrans additionnels
################################################################################


## Écran de confirmation #######################################################
##
## Cet écran est appelé quand Ren'Py souhaite poser une question au joueur dont
## la réponse est oui ou non.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Cette instruction s’assure que les autres écrans resteront en arrière
    ## plan tant que cet écran sera affiché.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Oui") action yes_action
                textbutton _("Non") action no_action

    ## Le clic bouton droit et la touche Echap. correspondent à la réponse
    ## "non".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Écran de l’indicateur d'avance rapide #######################################
##
## L’écran skip_indicator est affiché pour indiquer qu’une avance rapide est en
## cours.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Avance rapide")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Cette transformation est utilisé pour faire clignoter les flèches l’une après
## l’autre.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Nous devons utiliser une police qui a le glyphe BLACK RIGHT-POINTING
    ## SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Écran de notification #######################################################
##
## Cet écran est utilisé pour affiché un message au joueur. (Par exemple, quand
## une Snapshot rapide a eu lieu ou quand une capture d’écran vient d’être
## réalisée.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Écran NVL ###################################################################
##
## Cet écran est utilisé pour les dialogues et les menus en mode NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Les dialogues sont affichés soit dans une vpgrid soit dans une vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Si fourni, affiche le menu. Le menu peut s’afficher de manière
        ## incorrecte si config.narrator_menu est initialisé à True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Ce paramètre contrôle le maximum d’entrée dans le mode NVL qui peuvent être
## affichée simultanément.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Screen des bulles ###########################################################
##
## Le screen des bulles est utilisé pour afficher des dialogues en utilisant des
## bulles de dialogue. Ce screen prend les mêmes paramètres que le screen say,
## doit prévoir un displayable avec l'id "what", et peut créer des displayables
## avec les ids "namebox", "who", et "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window: 
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Variantes pour les mobiles
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Comme la souris peut ne pas être présente, nous remplaçons le menu rapide
## avec une version qui utilise des boutons plus gros et qui sont plus faciles à
## toucher du doigt.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Retour") action Rollback()
            textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

# screen du jeu 

screen lunchroom():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "réfectoire":
            size 50
            xalign 0.5 

screen class_404():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "Classe 404":
            size 50
            xalign 0.5 

screen room():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "Chambre":
            size 50
            xalign 0.5 

screen hallway():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "Couloir":
            size 50
            xalign 0.5 

screen hall():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "Hall":
            size 50
            xalign 0.5 

screen office():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "Bureau des élèves":
            size 50
            xalign 0.5 

screen clubroom():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "Salle de club":
            size 50
            xalign 0.5 

screen Dev():
    frame:
        xalign 0.5
        ypos 10 
        has vbox  

        text "Developper mode":
            size 20
            xalign 0.5 

screen logo():
    frame:
        yalign 0.5
        xalign 0.5  
        add "Images/logo.JPG" at unrotate

screen points():
    frame:
        xalign 0 
        ypos 10 
        has vbox  

        text "[points] points":
            size 30
            xalign 0.5 

screen perm():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "salle de permanence":
            size 50
            xalign 0.5 

screen origine():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "[origine]":
            size 50
            xalign 0.5 

screen WC():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "Toilettes":
            size 50
            xalign 0.5 

screen gymnase():
    frame:
        xalign 0.999
        ypos 10 
        has vbox  

        text "gymnase":
            size 50
            xalign 0.5

screen Yunaroom():
    frame:
        xalign 0.99
        ypos 10 
        has vbox  

        text "Chambre de Yuna":
            size 50
            xalign 0.5 

screen library():
    frame:
        xalign 0.99
        ypos 10 
        has vbox  

        text "Bibliothèque":
            size 50
            xalign 0.5 

screen day():
    frame: 
        xalign 0
        ypos 60
        has vbox  

        text "Jour [day]":
            size 30
            xalign 0.5 

screen draw():
    frame:
        yalign 0.3
        xalign 0.5 
        add "Images/Draw.Jpeg"

screen mail():
    frame:
        yalign 0.3
        xalign 0.5 
        add "Images/mail.png"

screen Nagumo():
    frame:
        yalign 0.3
        xalign 0.5 
        add "Images/Nagumo.png"

screen flag():
    frame: 
        yalign 0.3
        xalign 0.5 
        add "Images/Nexus.png"

screen update():
    frame: 
        yalign 0.08
        xalign 0.999
        add "success.jpg"

screen Shop():

    tag menu

    ## Cette déclaration concerne l’écran game_menu. L’élément vbox est ensuite
    ## inclus dans la fenêtre de l'écran game_menu.
    use game_menu(_("Boutique"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "{b}{i}— Clés d'accès —\n{/i}{/b}" 

            text _("Clé officielle : ARIS-8J4K-F9Q7\n")

            text _("Cette clé d'accès est à inscrire lors que vous lancez une nouvelle partie.\n")

            label "{b}{i}— DLC —\n{/i}{/b}"

            if key == "ARIS-GRFN-M4A1": 

                text _("DLC Arisization Project - Alternative : (installé)\n")

            else:   

                text _("DLC Arisization Project - Alternative : (non installé)\n") 

style about_label is gui_label 
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text: 
    size gui.label_text_size 

screen credit():

    tag menu

    ## Cette déclaration concerne l’écran game_menu. L’élément vbox est ensuite
    ## inclus dans la fenêtre de l'écran game_menu.
    use game_menu(_("Crédits"), scroll="viewport"):

        style_prefix "about"

        vbox: 

            label "{b}{i}— Crédits —\n{/i}{/b}"

            text _("Développement global et narration : [Dc] (Shadow_SLTM)\n")

            text _("Consultant en scénarisation : [Dc] (Shadow_SLTM)\n")

            text _("Dialogues des personnages : [Dc] (Shadow_SLTM)\n")

            text _("Gestion des musiques  : [Dc] (Shadow_SLTM)\n")
  
            text _("Interface joueur : [Dc] (Shadow_SLTM)\n") 

            text _("Animations du jeu : [Dc] (Shadow_SLTM)\n") 

            text _("Concepts : [Dc] (Shadow_SLTM)\n") 

            text _("Système des succès : [Dc] (Shadow_SLTM)\n") 

            text _("Création du personnage AK-24 et ses variantes : [Dc] (Shadow_SLTM)\n") 

            text _("Création des autres personnages : [Dc] (Shadow_SLTM)\n")  

            text _("Illustration du drapeau du régime Nagumo : [Dc] (Shadow_SLTM)\n")

            text _("Illustration du drapeau du lycée Nexus : [Dc] (Shadow_SLTM)\n")

            text _("Illustration de l'interface Windows : [Dc] (Shadow_SLTM)\n")

            text _("Illustration du menu : [Dc] (Shadow_SLTM)\n") 

            text _("Programmation : [Dc] (Shadow_SLTM)\n") 

            text _("Correction du jeu : [Dc] (Shadow_SLTM)\n")

            text _("Gestion des fichiers du jeu : [Dc] (Shadow_SLTM)\n") 
            
            label "{b}{i}— Contributions secondaires —\n{/i}{/b}" 

            text _("Phrase « Bon après ça ne m'étonne pas venant de toi » : Sararnbb\n") 

            text _("Dessin de [Su] : Sararnbb\n") 

            text _("Idée du personnage de [Sk] : Kama\n") 
             
            text _("Idée du personnage de Seigo : Kama\n") 

            text _("Idée de la variante AK-25 : Kama\n")  

            text _("Correction partielle de l’orthographe du chapitre 0 : Kama\n") 

            text _("Idée des textes de narration : Louks\n") 

            text _("Terme « Engrenage sur pattes » : Nathanaël (Loki)\n")

            text _("Fonctions aléatoires : [Dc] (Shadow_SLTM) et Nathanaël (Loki)\n") 

            label "{b}{i}— Remerciements —\n{/i}{/b}"  
            
            text _("Musiques utilisées sous licence libre.\n") 

            text _("Décors utilisés sous licence libre.\n") 

            label "{b}{i}— Propriété —\n{/i}{/b}"   

            text _("DLC Arisization Project - Alternative : [Dc] (Shadow_SLTM)\n")

            text _("Arisization Project (The Realization Project of Aris) appartient à [Dc] (Shadow_SLTM)\n")   

            text _("Éditeur : SLTM\n") 

style about_label is gui_label  
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text: 
    size gui.label_text_size 

screen success(): 

    tag menu

    use game_menu(_("Succès"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "{b}{i}— Progression —\n{/i}{/b}" 

            text _("Succès : [success]/42\n") 

            label "{b}{i}— liste des succès —\n{/i}{/b}" 

            text _("Une autre clé ? : [quest1]/1\n") 
            text _("Premier piratage : [quest2]/1\n")
            text _("Nouveau nom de code : [quest3]/1\n")     
            text _("L'espoir fait vivre : [quest4]/1\n") 
            text _("Acceptation : [quest5]/1\n")  
            text _("Nouvelle identité : [quest6]/1\n")
            text _("Nouvelle adresse : [quest7]/1\n")
            text _("Ce n’est que le début : [quest8]/1\n")
            text _("Au club !!! : [quest9]/1\n")
            text _("Maître de guerre : [quest10]/1\n")
            text _("Vive la documentation : [quest11]/1\n")
            text _("Première mise à jour : [quest12]/1\n")  
            text _("Oublier le passé : [quest13]/1\n") 
            text _("J'ai raison : [quest14]/1\n")       
            text _("Lis-mon message : [quest15]/1\n") 
            text _("Le repos avant tout : [quest16]/1\n")
            text _("Petit exercice de python : [quest17]/1\n")
            text _("Nouveau système : [quest18]/1\n")      
            text _("Affection pour les autres : [quest19]/1\n")
            text _("Entre connaissances : [quest20]/1\n")
            text _("le bon présumé : [quest21]/1\n")
            text _("Affection pour les autres partie 2 : [quest22]/1\n")
            text _("Mot de passe solide : [quest23]/1\n")
            text _("La vérité avant tout : [quest24]/1\n")
            text _("Génie des maths : [quest25]/1\n") 
            text _("Petit exercice de Runix : [quest26]/1\n") 
            text _("Seconde mise à jour : [quest27]/1\n")
            text _("Génie de l’informatique : [quest28]/1\n")
            text _("Détail du passé : [quest29]/1\n")
            text _("Mentir n’est pas si mal : [quest30]/1\n")
            text _("Journalistes de merde : [quest31]/1\n")
            text _("Dire les termes : [quest32]/1\n")           
            text _("Silence brutal : [quest33]/1\n") 
            text _("Molière c'est toi ? : [quest34]/1\n") 
            text _("Jamais deux sans trois : [quest35]/1\n")  
            text _("Sa vraie valeur : [quest36]/1\n") 
            text _("Faire de la philosophie : [quest37]/1\n") 
            text _("Bon philosophe : [quest38]/1\n") 
            text _("L'entraide scolaire : [quest39]/1\n") 
            text _("Nouvelle batterie : [quest40]/1\n")             
            text _("Quatrième mise à jour : [quest41]/1\n")
            text _("Maître du chaos ordonné : [quest42]/1\n") 

style about_label is gui_label   
style about_label_text is gui_label_text
style about_text is gui_text 

style about_label_text: 
    size gui.label_text_size 

screen robot():                   

    tag menu

    use game_menu(_("Ton robot"), scroll="viewport"):

        style_prefix "about" 

        vbox:

            label "{b}{i}— Description —\n{/i}{/b}" 

            text _("[charactertext11]\n")

            label "{b}{i}— Informations techniques —\n{/i}{/b}"

            text _("Nom de code : [A]\n") 

            text _("Identité : [newname] [robotname]\n")

            text _("Mot de passe : [stored_password]\n") 

            text _("Système d'exploitation : [system]\n")

            text _("Mise à jour : [update]\n") 

            text _("Adresse IP : [baseip]\n")
 
            text _("Origine : [robotorigine]\n")  

            text _("Numéro de série : [serie]\n")  

            text _("stockage utilisé : [stockage] Go\n")

            text _("Processeur : [cpu] \n") 

            text _("Propriétaire : [propriety] \n") 

style about_label is gui_label 
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text: 
    size gui.label_text_size 

screen characters():                   

    tag menu

    use game_menu(_("Personnages"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "{b}{i}— Vous —\n{/i}{/b}" 

            text _("{b}[P] — [domaine]\n{/b}") 

            label "{b}{i}— Personnages Principaux —\n{/i}{/b}" 

            text _("{b}[character1] — [ultimate1]{/b}\n") 
        
            text _("[charactertext1]\n") 

            text _("{b}[character2] — [ultimate2]{/b}\n") 

            text _("[charactertext2]\n") 

            text _("{b}[character3] — [ultimate3]{/b}\n") 

            text _("[charactertext3]\n") 

            text _("{b}[character4] — [ultimate4]{/b}\n") 

            text _("[charactertext4]\n") 

            text _("{b}[character5] — [ultimate5]{/b}\n") 

            text _("[charactertext5]\n") 

            text _("{b}[character6] — [ultimate6]{/b}\n") 

            text _("[charactertext6]\n") 

            text _("{b}[character7] — [ultimate7]{/b}\n") 

            text _("[charactertext7]\n") 

            text _("{b}[character8] — [ultimate8]{/b}\n") 

            text _("[charactertext8]\n") 

            text _("{b}[character9] — [ultimate9]{/b}\n")

            text _("[charactertext9]\n") 

            text _("{b}[character10] — [ultimate10]{/b}\n") 

            text _("[charactertext10]\n") 

            label "{b}{i}— Personnages Secondaires —\n{/i}{/b}" 

            text _("[character11] — [ultimate11]\n") 
            text _("[character12] — [ultimate12]\n")
            text _("[character13] — [ultimate13]\n") 
            text _("[character14] — [ultimate14]\n") 
            text _("[character15] — [ultimate15]\n") 
            text _("[character16] — [ultimate16]\n") 
            text _("[character17] — [ultimate17]\n") 
            text _("[character18] — [ultimate18]\n") 

style about_label is gui_label 
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text: 
    size gui.label_text_size 

screen about():

    tag menu

    ## Cette déclaration concerne l’écran game_menu. L’élément vbox est ensuite
    ## inclus dans la fenêtre de l'écran game_menu.
    use game_menu(_("À propos"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "{b}{i}— [config.name!t] —\n{/i}{/b}"
            text _("Version [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _("Conçu avec {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]\n")

            label "{b}{i}— Catégorie du jeu —\n{/i}{/b}" 

            text _("Sci-Fi\n")
            text _("Mystery\n")
            text _("Cyberpunk\n")
            text _("Thriller\n")
            text _("School Life\n")
            text _("Science fiction\n")
            text _("Hacking\n") 
            text _("dystopie technologique\n")

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size