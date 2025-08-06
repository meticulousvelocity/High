import discord
import const

db = const.db

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
# intents.moderation = True
intents.reactions = True

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    with db:
        db.execute(query("create_ticket_staff_table"))


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    pass


@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    pass


@bot.event
async def on_message(message: discord.Message):
    assert isinstance(message, discord.Message)
    if message.author.id == const.TICKET_KING_ID:
        if len(message.embeds) < 1:
            return
        embed = message.embeds[0]
        assert isinstance(embed, discord.Embed)
        if embed.title != "Ticket Claimed":
            return
        claim = embed.description
        assert isinstance(claim, str)
        claimer = between(claim, "<@", ">")
        claimer_id = int(claimer)
        with db:
            db.execute(query("update_ticket_count"), (claimer_id,))
        print(f"Ticket claimed by {claimer_id}. Adding +1 to their ticket count.")


def query(command: str):
    return (const.SQL / f"{command}.sql").read_text()


def between(text: str, start: str, end: str):
    return text.split(start, 1)[1].split(end, 1)[0]


def main():
    bot.run(const.TOKEN.read_text().strip())


if __name__ == "__main__":
    main()
