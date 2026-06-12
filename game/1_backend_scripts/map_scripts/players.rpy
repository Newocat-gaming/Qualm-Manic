python early:
    class Player:
        def __init__(self, name = "", icon_pos = (), icon_last_pos = (), icon = "", history = []):
            self.name = name
            self.icon_pos = icon_pos
            self.icon_last_pos = icon_last_pos
            self.icon = "map/" + icon + ".webp"
            self.history = history





default player_1 = Player(name = "Jay", icon_pos = (), icon_last_pos = (), icon = "player_dot", history = [])

default player_2 = Player(name = "Kit", icon_pos = (), icon_last_pos = (), icon = "player_dot", history = [])


default active_player = player_1



