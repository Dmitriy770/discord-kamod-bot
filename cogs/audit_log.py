import datetime as dt
import discord
from info import serverinfo

from discord.ext import commands

class AuditLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ID_AUDIT_CHANNEL = serverinfo.ID_AUDIT_CHANNEL

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if self.ID_AUDIT_CHANNEL is not None and self.bot.get_channel(self.ID_AUDIT_CHANNEL) is not None:
            # join voice
            if before.channel is None:
                emb = discord.Embed(colour=discord.Colour.green(),
                                    description=f'Пользователь {member} подключился к голосовому каналу **{after.channel}**')
                emb.set_author(name=member, icon_url=member.avatar_url)
                emb.timestamp = dt.datetime.utcnow()
                await self.bot.get_channel(self.ID_AUDIT_CHANNEL).send(embed=emb)
            # left voice
            elif after.channel is None:
                emb = discord.Embed(colour=discord.Colour.red(),
                                    description=f'Пользователь {member} отключился от голосового канала **{before.channel}**')
                emb.set_author(name=member, icon_url=member.avatar_url)
                emb.timestamp = dt.datetime.utcnow()
                await self.bot.get_channel(self.ID_AUDIT_CHANNEL).send(embed=emb)
            # teleport
            elif before.self_mute == after.self_mute:
                emb = discord.Embed(colour=discord.Colour.from_rgb(r=254, g=254, b=34),
                                    description=f'Пользователь {member} отключился от голосового канала **{before.channel}** и подключился к **{after.channel}**')
                emb.set_author(name=member, icon_url=member.avatar_url)
                emb.timestamp = dt.datetime.utcnow()
                await self.bot.get_channel(self.ID_AUDIT_CHANNEL).send(embed=emb)


def setup(bot):
    bot.add_cog(AuditLog(bot))
