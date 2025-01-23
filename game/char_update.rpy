default char_checkpoint = 0

default char_jay_checkpoint = 0
default char_kit_checkpoint = 0
default char_vida_checkpoint = 0
default char_andrea_checkpoint = 0
default char_manic_update = 0



default char_neda_update = 0




label char_screen_update:
    $ char_checkpoint =+ 1

    if char_checkpoint == 1:
        $ character_button = True
        return

label char_jay_update:
    $ char_jay_checkpoint =+ 1
       
    if char_jay_checkpoint == 1:
        $ persistent.jay_profile = CharacterProfile(name="Jay", imageName="jay profile", desc = "test", trueName = "jay")
        return

label char_kit_update:
    $ char_kit_checkpoint =+ 1
       
    if char_kit_checkpoint == 1:
        $ persistent.kit_profile = CharacterProfile(name="Kit", imageName="kit profile", desc = "test", trueName = "kit")
        return

label char_vida_update:
    $ char_vida_checkpoint =+ 1
       
    if char_vida_checkpoint == 1:
        $ persistent.vida_profile = CharacterProfile(name="Vida", imageName="vida profile", desc = "test", trueName = "vida")
        return

label char_andrea_update:
    $ char_andrea_checkpoint =+ 1
       
    if char_andrea_checkpoint == 1:
        $ persistent.andrea_profile = CharacterProfile(name="Andrea", imageName="andrea profile", desc = "???", trueName = "andrea")
        return

label char_manic_update:
    $ char_manic_checkpoint =+ 1
       
    if char_manic_checkpoint == 1:
        $ persistent.manic_profile = CharacterProfile(name="???", imageName="manic profile", desc = "???", trueName = "manic")
        return
    elif char_manic_checkpoint == 2:
        $ persistent.manic_profile = CharacterProfile(name="Manic", imageName="manic profile", desc = "test", trueName = "manic")
        return




label char_neda_update:
    $ char_neda_checkpoint =+ 1
       
    if char_neda_checkpoint == 1:
        $ persistent.neda_profile = CharacterProfile(name="Neda", imageName="neda profile", desc = "test", trueName = "neda")
        return







