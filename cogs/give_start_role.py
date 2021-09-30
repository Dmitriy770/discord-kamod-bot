import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option
from info import serverinfo


class GiveStartRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.START_ROLE_ID = serverinfo.START_ROEL_ID

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.START_ROLE_ID != 0 and member.guild.get_role(self.START_ROLE_ID) is not None:
            role = discord.utils.get(member.guild.roles, id=self.START_ROLE_ID)
            await member.add_roles(role)


def setup(bot):
    bot.add_cog(GiveStartRole(bot))
