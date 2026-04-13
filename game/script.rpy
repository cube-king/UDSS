# Declare variables used by this game. 
define P = Character("[player_name]", image="postaldude")
default player_name = "Protag" # Provide a default value
default player_pronoun = "hehim"
default player_pronoun_personal = "he"
default player_pronoun_object = "him"
default player_pronoun_possessive = "his"
define m = Character("[matilda_name]")
default matilda_name = "???"
define matilda_1 = Image("matilda_1",oversample=1)

define config.main_menu_music = "audio/music/MainMenu.mp3"

$import Math

transform halfsize:
    zoom 0.5
    center







# The game starts here!
 
label start:
    $ start_time = build.time
    # stop music
    # play music pause_menu_lmao
    scene bg room

    # $ player_name = renpy.input("What is your name?")
    # $ player_name = player_name.strip() # Removes accidental extra spaces

    # menu:
    #     "He/Him":
    #         "Set successfully!"
    #     "She/Her":
    #         "Set successfully!"
    #         $ player_pronoun = "sheher"
    #         $ player_pronoun_personal = "she"
    #         $ player_pronoun_object = "her"
    #         $ player_pronoun_possessive = "hers"

    #     "They/Them":
    #         "Set successfully!"
    #         $ player_pronoun = "theythem"
    #         $ player_pronoun_personal = "they"
    #         $ player_pronoun_object = "their"
    #         $ player_pronoun_possessive = "theirs"

    P "Okay, I should have that manual around here somewhere..."

    show evildeathmushroom
    with easeinbottom

    P "..."
    
    show shroom_one behind evildeathmushroom at truecenter
    P "You gotta be kidding..."
    
    

    hide evildeathmushroom
    with easeoutbottom


    
    P "I need food, but I'm not quite sure if this is safe..."

    menu:
        "Take the mushroom":
            P "I'll take the mushroom, I guess..."
        "Don't take it":
            jump starve_death
    label take_mushroom:

    hide shroom_one with dissolve
    "You start to feel a bit woozy, and the environment around you starts to shift."

    "You feel lightheaded, your knees buckling under your weight."

    "You settle yourself onto the ground so as to not have a hard landing."

    "You never thought your life would be taken in a 50/50, but here we are."

    "You rest your back on a fallen log, your head lulling back to stare at the skyline."
    
    with Fade(1, 0.1, 1)


    show matilda_1 at halfsize:
        matrixcolor BrightnessMatrix(-1.0)
    with dissolve
    m "Oh dear… "

    "A soft voice from above __"
    
    show matilda_1 at halfsize:
        matrixcolor BrightnessMatrix(0.0)
    with dissolve
    $ matilda_name = "Matilda"
    m "That isn’t pretty, now is it?"

    "The toadstool crouches down, her spindly finger moving to wipe the liquid from your lip. 
    Her hands are cold and firm, the texture akin to flower stems."

    "As your vision starts to blur and your eyes flutter shut, you feel as your body lifts"
    
    with Fade(1, 0.1, 1)
    $music_time = (build.time-start_time)
    play music "<from >Pause_menu_lmao.mp3"

    # scene change ? probably idk

    
    return
    
label starve_death:
    "If you don't take the mushroom you WILL starve to death"
    menu:
        "Take the mushroom":
            jump take_mushroom
        "Starve to death":
            P "ohh man boy am i hungry"
            "Are you SURE you don't want to take the mushroom?"
            menu:
                "Take the mushroom":
                    jump take_mushroom
                "Literally starve and die from starvation (this option kills you)":
                    P "Owie my stomach ow ow ouch"
                    show YOUDIED
                    with dissolve
                    ""
                    return
                        






    P "Owie my stomach ow ow ouch"
    "YOU DIED"
    return
    