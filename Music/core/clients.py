from pyrogram import Client

from config import Config

from .logger import LOGS


class HellClient(Client):
    def __init__(self):
        self.app = Client(
            "HellMusic",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="Music.plugins"),
            workers=100,
        )

        self.user = Client(
            "HellClient",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            session_string=Config.HELLBOT_SESSION,
            no_updates=True,
        )

    async def start(self):
        LOGS.info(">> Booting up HellMusic...")
        if Config.BOT_TOKEN:
            await self.app.start()
            me = await self.app.get_me()
            self.app.id = me.id
            self.app.mention = me.mention
            self.app.name = me.first_name
            self.app.username = me.username
            LOGS.info(f">> {self.app.name} is online now!")
        if Config.HELLBOT_SESSION:
            await self.user.start()
            me = await self.user.get_me()
            self.user.id = me.id
            self.user.mention = me.mention
            self.user.name = me.first_name
            self.user.username = me.username
            try:
                await self.user.join_chat("Its_HellBot")
                await self.user.join_chat("https://t.me/joinchat/LUzuM9rrEdIwZTFl")
            except:
                pass
            LOGS.info(f">> {self.user.name} is online now!")
        LOGS.info(">> Booted up HellMusic!")

    async def logit(self, hash: str, log: str):
        log_text = f"#{hash.upper()} \n\n{log}"
        try:
            await self.app.send_message(
                Config.LOGGER_ID, log_text, disable_web_page_preview=True
            )
        except Exception as e:
            LOGS.warning(f"Error in Logger: {e}")


hellbot = HellClient()