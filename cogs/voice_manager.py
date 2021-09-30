from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option
from info import serverinfo


class VoiceManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ID_VOICE_CHANNEL = serverinfo.ID_VOICE_CHANNEL
        self.SERVER_ID = serverinfo.SERVER_ID

    '''@cog_ext.cog_slash(name='start_voice_manager', description='Запуск voice manager',
                       guild_ids=[serverinfo.SERVER_ID])
    @commands.has_permissions(administrator=True)
    async def start_voice_manager(self, ctx):
        dbserver = DBServer(ctx.guild)
        category = await ctx.guild.create_category(name='VOICE CHANNEL')
        voice_channel = await ctx.guild.create_voice_channel(name='create voice channel', category=category)
        dbserver.set_channel('voice_create_channel', voice_channel.id)
        await ctx.send('voice manager запущен')'''

    # set voice limit
    '''@cog_ext.cog_slash(name='set_voice_limit', description='Задаёт ограниечение канала', guild_ids=[serverinfo.SERVER_ID],
                       options=[
                           create_option(name="limit", description="0-99", option_type=4, required=False)
                       ], )
    async def set_voice_limit(self, ctx, limit: int = 0):
        dbuser = DBUser(ctx.guild, ctx.author)
        if limit > 99:
            limit = 99
        elif limit < 0:
            limit = 0
        dbuser.set_voice_limit(limit)
        if ctx.author.voice is not None and ctx.author.voice.channel.name == dbuser.get_voice_name():
            await ctx.author.voice.channel.edit(reasone=None, user_limit=limit)
        await ctx.send("Лимит установлен")'''

    # set voice name
    '''@cog_ext.cog_slash(name='set_voice_name', description='задаёт имя войса',
                       guild_ids=[serverinfo.SERVER_ID], options=[
            create_option(name='name', description='укажите имя', option_type=3, required=True)])
    async def set_voice_name(self, ctx, name: str = None):
        dbuser = DBUser(ctx.guild, ctx.author)
        dbserver = DBServer(ctx.guild)
        if name is None:
            ctx.send(f'{ctx.author.mention} введите новоё название канала')
        else:
            if dbuser.get_cash() < dbserver.get_cost('RENAME_CHANNEL'):
                await ctx.send(f'{ctx.author.mention} у вас не достаточно средств')
            elif len(name) > 30:
                await ctx.send(f'{ctx.author.mention}, слишком длинное название')
            elif not moderation(name):
                await ctx.send(f'{ctx.author.mention} в название канал содержатся запрещённые слова')
            else:
                last_name = dbuser.get_voice_name()
                dbuser.set_voice_name(name)
                dbuser.set_cash(-dbserver.get_cost('RENAME_CHANNEL'))
                if ctx.author.voice is not None and ctx.author.voice.channel.name == last_name:
                    await ctx.author.voice.channel.edit(reasone=None, name=name)
                await ctx.send('Канал переименован')'''

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        #dbserver = DBServer(member.guild)
        #dbuser = DBUser(member.guild, member)
        #self.ID_VOICE_CHANNEL = dbserver.get_channel('voice_create_channel')
        if self.ID_VOICE_CHANNEL is not None and self.bot.get_channel(self.ID_VOICE_CHANNEL) is not None:
            category = self.bot.get_channel(self.bot.get_channel(self.ID_VOICE_CHANNEL).category_id)
            # join voice
            if after.channel is not None and after.channel.id == self.ID_VOICE_CHANNEL:
                channel = await member.guild.create_voice_channel(name=str(member.name),
                                                                  user_limit=0,
                                                                  category=category)
                await member.move_to(channel)
            # left voice
            if before.channel is not None and before.channel.id != self.ID_VOICE_CHANNEL and before.channel.category_id == self.bot.get_channel(
                    self.ID_VOICE_CHANNEL).category_id and not before.channel.members:
                await before.channel.delete()


def setup(bot):
    bot.add_cog(VoiceManager(bot))
