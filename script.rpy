# Image Declaration
    # Backgrounds
image bg1st = im.Scale("", 1280, 720)
image bg2nd = im.Scale("", 1280, 720)
image bg3rd = im.Scale("", 1280, 720)

# Music and Sound Declaration
    # Background Music
define audio.name1 = ""
define audio.name2 = ""
define audio.name3 = ""

    # Sound Effects
define audio.sound1 = "audio/punch.mp3"
define audio.sound2 = "audio/macquack.mp3"
define audio.sound3 = "audio/outrosong.mp3"

# Game Characters Declaration
    # Narration
define narrator = Character("Narrator", color= "#870989ff", image= None)

    # Objects / General Characters
define intercom = Character("Intercom", color= "#ffffff", image= "intercom")

# Specific Characters Declaration
    # Buddy
default nickmc = "??"
define mc = Character("[nickmc]", color= "#eabc25ff", image= "mc", dynamic= True)

    # Best Friend
default nickbff = "??"
define bff = Character("[nickbff]", color= "#91e3b2", image= "bff", dynamic= True)

    # Boss
define boss = Character("Dr. Montgomery", color= "#ff0000", image= "boss")

# Functions
    # cleanName() function to process and clean player input for names
    # askName() function to prompt the player for their name and return the cleaned version
init python:
    def cleanName(nickraw):
        allowedchars = " '-()~"
        nickfixed = "".join([c for c in nickraw if c.isalnum() or c in allowedchars])

        processednick = ""
        capitalize_next = True

        for char in nickfixed:
            if capitalize_next and char.isalpha():
                processednick += char.upper()
                capitalize_next = False
            else:
                processednick += char.lower()

            if char in " (":
                capitalize_next = True

        return processednick or "Buddy" # default name if nothing is entered

    def askName():
        nickraw = renpy.input("              Enter your name: ", length=50).strip()
        return cleanName(nickraw) or "Buddy" # default name if nothing is entered

label start:
    window hide
    scene bg1st
    show mc at left
    with moveinleft

    jump randomtest

label testpositive:
    $renpy.pause(2.5)
    play music name1
    window show
    with dissolve

    "(The screen is black as a new game is started.)"
    "(The sounds of computer typing and paper printer beeping are heard as text and background begin appearing.)"
    
    mc "Today is Tuesday, and I'm almost finished with my shift.\n\n(Press any button to continue)"
    mc "Stamp here… Signature there…"
    mc "..."
    
    "(MC loses faith; expression is waning.)"
    
    mc "I'm almost finished with my shift."
    mc "..."
    
    "(MC frowns.)"
    
    mc "I've been checking the clock fifty times now, and I'm certain it no longer works."
    
    "(MC regains some faith, glances at his computer.)"
    
    mc "Hmm, at least it's a slow day; I can just relax a bit while I type in numbers."
    mc "..."
    
    "(MC gives up, head falling onto the desk surface.)"
    
    mc "I wish something exciting would happen for once."
    mc "Is this really what my life has come to? Just sitting here, doing the same thing every day?"
    mc "Typing numbers into a spreadsheet for just enough to scrape by?"
    
    "(MC sits back upright, reflecting.)"
    
    mc "No, no, it's not just enough for me alone to scrape by, though."
    
    "(The background changes to a shot showing the little sister in the corner of a framed photo, and a sticky note next to it, written down: “Do it for her.”)"
    "(The scene shifts back to the original background.)"
    
    mc "I'm almost finished with my shift."
    
    "(The sound of a news blast or those 'promo videos' you see for companies begins to play loudly, causing the player's character to bump their desk and their name card to fall to the floor.)"
    
    mc "Dang it! This thing always falls off."
    mc "Let's get that fixed--"

    $ nickmc = askName() # Player declares their name!

    "(MC picks up the name card and puts it back on the desk.)"
    
    mc "There we go, that's better!"
    
    "(A chime plays.)"
    
    intercom "Will [nickmc] please come to the head office immediately? Thank you."
    
    mc "..."
    mc "Please, no..."

    window hide
    with dissolve

label theoffice:
    scene bg2nd
    show mc at left
    with moveinleft
    show boss at right
    $renpy.pause(2.5)
    play music name2
    window show
    with dissolve

    "(Cut to boss's office, showing MC and Boss.)"
    
    boss "Ah, [nickmc], there you are. Please, have a seat."
    boss "I have some news for you."
    boss "You've been promoted!"
    
    mc "<I thought for sure The Incident would have gotten me fired!>"
    mc "What would be my new position?"
    
    boss "Ah..."
    boss "Well, it's a bit of a... unique position."
    boss "You've been moved to the Coral Branch."
    
    mc "The Coral Branch?"
    
    boss "Yes, it's a new branch that just opened up."
    boss "It's located on a remote island. An experimental branch."
    boss "But trust me, it looks like a great opportunity for you!"
    
    "(Zoom in on MC, sweating.)"
    
    mc "..."
    
    boss "And you won't have anymore paperwork to worry about!"

    window hide
    with dissolve

label backtoyourseat:
    scene bg1st
    show mc at left
    with moveinleft
    show boss at right
    with moveinleft
    $renpy.pause(2.5)
    play music name1
    window show
    with dissolve

    "(Back to a scene at the office with MC and Boss.)"
    
    boss "Alright, now you'll be stationed on the third island in the archipelago."
    mc "What's its name?"
    boss "Does it really matter?"
    "(The boss looks mildly annoyed.)"
    boss "Listen, you aren't there to make friends. You're there because you have a mission to fulfill."
    mc "And what is that mission?"
    boss "Your task will be to locate and retrieve a certain item for the company."
    boss "We refer to it as 'The Heartstone.'"
    mc "What does it do?"
    boss "Snap out of it, [nickmc]. It's not your job to know what it does."
    boss "Just relocate the object and bring it back to us."
    boss "One of our business partners is very interested in acquiring it."
    boss "You're familiar with GyroMaxx, I'm sure."
    mc "GyroMaxx? Yeah, I've heard of them. They're a big energy company, right?"
    boss "That's right. And no doubt they'd love to use this lovely treasure in their ongoing fuel project."
    boss "Listen, this deal's on you. If it falls through, you'll get much worse than just a demotion, if you know what I mean."
    boss "So, I suggest you get to work on this right away. The sooner you find it, the better."
    mc "..."
    boss "Come on, [nickmc]! We're family! Wouldn't want to let your family down, would you?"
    "(A sudden jab at MC's heart, reminding him of his sister.)"
    boss "The board thinks you're awfully useless, but I know you have potential!"
    boss "... I just don't know exactly what it is yet."
    boss "..."
    boss "Consider this your second chance, [nickmc]. Don't mess it up."
    "(MC takes a deep breath, trying to process everything.)"
    mc "So when do I start?"
    boss "You start tomorrow. I'll have someone take you to the island in the morning."
    mc "<Guess I'd better get packing...>"
    "(Screen fades to black.)"
    mc "<All a big family>"
    mc "<...You're doing this for your family>"
    "(Title card is displayed.)"

    window hide
    with dissolve

label randomtest:
    # This is a test label to try out some random things, such as sound effects and music.
    # It will be deleted later, but for now it's just a sandbox for testing things out.

    # TESTS:
    
    $renpy.pause(1)
    play sound sound1
    $renpy.pause(1)
    play sound sound2
    $renpy.pause(1)
    play sound sound3
    $renpy.pause(10)

    # If nothing is here, ignore!
    # END OF TESTS.

    jump testpositive


    return
