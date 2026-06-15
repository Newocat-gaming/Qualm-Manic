default quickbutton_party = False
default quickbutton_history = True
default quickbutton_save = False
default quickbutton_Qsave = False

default quickbutton_inventory = False
default quickbutton_back = False
default quickbutton_options = True
default quickbutton_Qload = False

# unlock quickbuttons
default quickbutton_party_unlock = False
default quickbutton_inventory_unlock = False

default skipping_disabled = False

# battle state
label battle_start:
    $ in_combat = True
    $ quickbutton_save = False
    $ quickbutton_Qsave = False
    $ quickbutton_Qload = False
    $ renpy.block_rollback()
    return

label battle_end:
    $ in_combat = False
    $ quickbutton_save = True
    $ quickbutton_Qsave = True
    $ quickbutton_Qload = True
    $ renpy.block_rollback()
    return


# vn state
label vn_start:
    $ skipping_disabled = False
    $ quickbutton_back = True
    $ renpy.block_rollback()
    $ config.rollback_enabled = True
    return

label vn_end:
    $ skipping_disabled = True
    $ quickbutton_back = False
    $ renpy.block_rollback()
    $ config.rollback_enabled = False
    return
