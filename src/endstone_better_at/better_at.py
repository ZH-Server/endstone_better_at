from endstone.plugin import Plugin
from endstone.event import event_handler, PlayerChatEvent

class BetterAt(Plugin):
    api_version = "0.5"

    def on_enable(self) -> None:
        self.register_events(self)
        # match "@ + {server.player.namelist}" with {player.chat.message}, if true -> title matched playername {message}; else -> do nothing
    
    @event_handler
    def on_chatting(self, event: PlayerChatEvent) -> None:
        #i=0
        pl_list=self.server.online_players
        self.logger.info(f"pl_list: {pl_list}")
        """
        for f"@{pl_list[i]}" in event.message:
            pl_target=pl_list[i]
            pl_target.send_message(f"{event.player.name} mentioned you!")
            if i > len(pl_list):
                break
            else:
                i+1
        """