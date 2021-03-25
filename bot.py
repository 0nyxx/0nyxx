

import os
import random
import re

import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    activity = discord.Game(name="Parancsokért -help / Swift by 0nyx", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Sikeres bejelentkezés")



@bot.command(
	help="Ugy tunik segitsegre van szukseged",

	brief="Törli az összes üzenetet az adott csatornán."
)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount = 10000):
    embed = discord.Embed(title="ÜZENETEK TÖRLÉSE...", description="Üzenetek törölve:gear:.",colour=discord.Colour.dark_gray())
    await ctx.channel.send(embed=embed)
    await ctx.channel.purge(limit=amount)

@bot.event
async def on_member_join(member):
    await message.channel.send(f'Szia{member.mention},köszi hogy csatlakoztál!')


@bot.command(
	
	help="Megnézheted vele milyen parancsok vannak",
	
	brief="Visszairja hogy pong"
)
async def ping(ctx):

	await ctx.channel.send("pong")

@bot.command(
    help=".",

    brief="Visszaküldi azt,amit megadtál neki."
)
async def print(ctx, *args):
	response = ""

	
	for arg in args:
		response = response + "   " + arg

	await ctx.channel.send(response)


@bot.command()
@commands.has_permissions(send_messages=True)
async def smile(ctx):
   embed = discord.Embed(title="`Smile.`", description=f"> :sunglasses:",colour=discord.Colour.dark_orange())
   await ctx.send(embed=embed)


@bot.command(
	help="Ugy tunik segitsegre van szukseged.",

	brief="Elküldi a Bot jelenlegi verzióját.")
@commands.has_permissions(send_messages=True)
async def ver(ctx):
   embed = discord.Embed(title="VERZIO.", description="> `4.1` :gear:",colour=discord.Colour.dark_blue())
   await ctx.channel.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('`Hibát észleltem, próbáld meg újra` :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("`Nincsenek meg a szükséges engedélyeid` :angry:")

@bot.command(
	help="Ugy tunik segitsegre van szukseged.",

	brief="Ha jó személy használja,akkor bannolja az adott embert."
)

@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.channel.send('bannolva')
    await ctx.author.send('ki lettél bannolva')

class HelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.dark_red(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

bot.help_command = HelpCommand()

@bot.command(
	help="Ugy tunik segitsegre van szukseged.",

	brief="Unbannolja az adott embert,ha jó személy használja."
)
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member :  discord.Member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'UNBANNED {user.mention}')
            return

@bot.command(
	help="Ugy tunik segitsegre van szukseged",

	brief="Lenémitja az adott embert,ha megfelelő ember használja."
)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=False, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention}**némitva**", colour=discord.Colour.dark_blue())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" lenémitott: {guild.name} reason: {reason}")

@bot.command(
	help="Ugy tunik segitsegre van szukseged.",

	brief="Unmute-olja az adott embert,ha megfelelő személy használja."
)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f"Unmuteolta: - {ctx.guild.name}")
   embed = discord.Embed(title="`UNmute.`", description=f"> Unmuteolva lettél,** {member.mention}",colour=discord.Colour.dark_blue())
   await ctx.send(embed=embed)
  
@bot.command(
	
	help="Megnézheted vele milyen parancsok vannak",
	
	brief="Visszairja hogy **jang**"
)
async def jing(ctx):

	await ctx.channel.send("**jang**")


@bot.command(
	help="Ugy tunik segitsegre van szukseged.",

	brief="Ha jó személy használja,akkor kickeli az adott embert."
)

@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    embed = discord.Embed(title="`Kick`", description=f"> *Kickelve lett** {member.mention}",colour=discord.Colour.dark_blue())
    await member.kick(reason = reason)
    await ctx.channel.send(embed=embed)

@bot.command(
	help="Ugy tunik segitsegre van szukseged.",

	brief="Figyelmezteti az adott embert.")
@commands.has_permissions(administrator=True)
async def warn(ctx, member : discord.Member, *, reason = None):
   embed = discord.Embed(title="`FIGYELMEZTETÉS.`", description=f"{member.mention} `figyelmeztetve lett.`:gear:",colour=discord.Colour.dark_green())
   await ctx.channel.send(embed=embed)

@bot.command(
    help="> Küld egy privát üzenetet.",

    brief="> Ugy tunik segitsegre van szukseged."
)
async def pü(ctx):
    embed = discord.Embed(title="`Privát üzenet elküldve.` :gear:", description="> Nézd meg a Privát üzeneteidet!:eyes:", colour=discord.Colour.light_gray())
    embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)
    await ctx.channel.send(embed=embed)
    await ctx.author.send("Itt a **PÜ-d**:eyes:")

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def delrole(ctx, role: discord.Role):
    await bot.delete_role(role)
    await bot.say("A {} jelvény sikeresen törölve lett!".format(role.name))

@bot.command()
async def addtext(ctx, channelName, roleName):
    guild = ctx.guild
    member = ctx.author
    role = await guild.create_role(name=roleName)
    admin_role = get(guild.roles, name=roleName)

    embed = discord.Embed(title="`Szöveges Csatorna létrehozva!`", description="> What we think, we become.", colour=discord.Colour.dark_gold())
    embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(name=channelName, overwrites=overwrites)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role("Tag")
async def addrole(ctx, member:discord.Member, *, role:discord.Role):
    moderator_role = get(guild.roles, name="Moderátor")
            await member.add_roles(role)
            await ctx.send(f"{member} kapott egy {role} rangot!")
            

@bot.command()
@commands.has_role("Tag")
async def takerole(ctx, member:discord.Member = None, *, role:discord.Role = None):
            await member.remove_roles(role)
            await ctx.send(f"A {role} rang el lett távolitva tőled, {member}!")

@bot.command()
async def addvoice(ctx, channelName, roleName):
    guild = ctx.guild
    member = ctx.author
    role = await guild.create_role(name=roleName)
    admin_role = get(guild.roles, name=roleName)

    embed = discord.Embed(title="`Hang Csatorna létrehozva!`", description="> What we think, we become.", colour=discord.Colour.dark_gold())
    embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_voice_channel(name=channelName, overwrites=overwrites)
    await ctx.send(embed=embed)


bot.run('your_token')

//bot created by onyx//