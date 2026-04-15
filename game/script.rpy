# Declare variables used by this game. 
define P = Character("[player_name]")
default player_name = "Protag" # Provide a default value
default player_pronoun = "hehim"
default player_pronoun_personal = "he"
default player_pronoun_object = "him"
default player_pronoun_possessive = "his"
define r = Character("[rocket_name]")
define m = Character("[matilda_name]")
define M = Character("[mawce_name]")
define f = Character("[ferris_name]")

default matilda_name = "???"
default mawce_name = "???"
default rocket_name = "???"
default ferris_name = "???"

define config.main_menu_music = "audio/music/MainMenu.mp3"

$import Math

transform halfsize:
    zoom 0.5
    center




# The game starts here!
 
label start:
    $ start_time = build.time
    stop music fadeout 2.0
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
    
    show kindlifemushroom
    with easeinbottom

    hide evildeathmushroom
    show shroom_one behind kindlifemushroom at truecenter
    P "You gotta be kidding..."
    
    

    hide kindlifemushroom
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


    show matilda happy at center:
        matrixcolor BrightnessMatrix(-1.0)
    with dissolve
    m "Oh dear… "

    "A soft voice from above speaks to you."
    
    show matilda happy at center:
        matrixcolor BrightnessMatrix(0.0)
    with dissolve
    m "That isn’t pretty, now is it?"

    "The toadstool crouches down, her spindly finger moving to wipe the liquid from your lip. 
    Her hands are cold and firm, the texture akin to flower stems."

    "As your vision starts to blur and your eyes flutter shut, you feel as your body lifts..."
    
    hide matilda happy 
    show rocket angry 1 at left
    show matilda happy at right
    with Fade(1, 0.1, 2)
    # $ music_time = (build.time-start_time)
    # play music "<from >Pause_menu_lmao.mp3"

    
    
    r "Matilda?"
    
    m "Yes?"

    show rocket angry 2 
    r "..."

    show rocket angry 1 
    r "Yes!? Yes about what? How about yes that you explain who this is?!"

    show rocket angry 2 
    M "That doesn’t make any sense..."

    show matilda neutral
    m "They mistook me for another mushroom;
    The effects should wear off soon."

    show rocket angry 1
    r "They ATE you???"

    show rocket angry 2
    show matilda shocked
    m "On accident!"

    show matilda neutral
    M "Did it hurt?"

    f "What's the pain scale, 1 – 10?"

    show matilda shocked
    m "Shh-! They’re awake."

    P "Good morning?"

    show matilda happy
    show rocket happy 2
    "Good morning!!"

    show rocket happy 1
    P "Who are you?!"

    show matilda neutral
    f "No need to freak out..."

    show matilda happy
    m "I'm glad to see you're recovering well."
    
    f "You consider looking like THAT \"well\"?"

    show rocket happy 2
    r "I'd consider them being alive as a miracle."

    show rocket happy 1
    M "Can we at least wait a few minutes before getting mean?"

    show rocket angry 1
    r "I wasn't--"

    show rocket neutral 1
    P "Shut uppppp! My heart hurts."
    
    show rocket neutral 2
    show matilda shocked
    P "{size=+30}WHO ARE YOU!?{/size}" with hpunch

    show matilda neutral
    show rocket neutral 1
    m "Right, I apologize. We are the Overgrowth."

    show matilda happy
    $ matilda_name = "Matilda"
    m "I'm Matilda."

    show rocket happy 2
    $ rocket_name = "Rocket"
    r "Rocket."

    show rocket happy 1
    $ mawce_name = "Mawce"   
    M "Mawce!"
    
    $ ferris_name = "Ferris"
    f "Ferris."

    show matilda shocked
    m "And-- well, Simon should be around here somewhere..."

    show matilda neutral
    f "We should be happy he’s not here, it would make this whole thing a nightmare."

    show rocket neutral 2
    r "If you find a snake man, try to bring him back to camp. I’m tired of dragging him back myself." 

    show rocket neutral 1
    f "Quit being lazy, we have to get firewood anyways, we’ll probably find him."

    m "You could have tea with Mawce and I, it’ll help rest your body."

    M "I picked fresh herbs this morning!"

    menu: 
        "Get firewood with Ferris & Rocket":
            pass
        "Have tea with Matilda and Mawce":
            pass
        "Try to find Simon":
            pass

    "continue development here please, thanks guys"

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
                    show youdied at truecenter:
                        zoom 3.3
                    with Dissolve(3.0)
                    ""
                    return
                        






    P "Owie my stomach ow ow ouch"
    "YOU DIED"
    return
    