import discord
from discord import guild
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_choices;

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)
token = "OTk2MTQ1Mjc5OTEwODEzNzc2.GPdTto.f_FCHy1E5alVIakbyFQUO5h7_dVCGOxsWFDNB4"


@slash.slash(
    name = "releases",
    description="Here you can see new releases",
    guild_ids = [996146306751926293],
    options=[
        create_option(
            name="option",
            description="This is a description",
            required=True,
            option_type=3,
            choices=[
                create_choice(
                    name="Nike",
                    value="Nike"    
                )
            ]
        )
    ]   
)
async def _releases(ctx:SlashContext, option:str):
    await ctx.send(option)

@slash.slash(
    name="bought",
    description="Here you can see what you've bought",
    guild_ids = [996146306751926293],
)

async def _bought(ctx:SlashContext):
    await ctx.send("Here you'll be able to see what you've bought")





client.run(token)