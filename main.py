#for-system-built
import discord
from discord import Intents, Profile
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import time
import random
#in-system-built    
from module import hasRole
from module import isOwner
from module import isOwnerServer



#global variables
counter = -1
mins = 0
hours = 0
debounce = 0
moreThanNine = False
#end of global variables


client = commands.Bot(command_prefix='`')
# status = cycle(['with your expectations',
#                'the .Help command to see all the commands',
#                'Don`t forget it is a capital H in the help command'])


@client.event
async def on_ready():
    #reminder.start()
    print('Bot is ready!')
    print('Logs:')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="IN DEVELOPMENT: FiveM on RETRO Romania RP   discord.link/retrorp"))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingRole):
        await ctx.send('You don`t have the role to do that')
#ERROR HANDLER - AICI PUN ERORI IN CAZ DE

@tasks.loop(seconds=3600)
async def reminder():
    global debounce
    guild = client.get_guild(708725972920303656)
    userRole = guild.get_role(767481279079776266)
    if debounce > 0:
        general_chat = client.get_channel(799309457233543201)
        embed = discord.Embed(
        title='Retro Romania Roleplay',
        description=f'Pentru ajutor contactati un {userRole.mention} Acestia o sa va ajute cu orice fel de problema cu care va confruntati.',
        colour=discord.Colour.purple()
    )
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
        embed.set_footer(
            text=f'©️ 2021 RETRO All Rights Reserved')
        await general_chat.send(embed=embed)
    debounce += 1

@client.command()
async def ping(ctx):
    print(f'{ctx.author.name} checked the ping at {time.asctime()}')
    await ctx.send(f'Pinged {round(client.latency * 1000)}ms')

@client.command()
async def closeClient(ctx):
    if ctx.author.id == 518331788880510979 or ctx.author.id == 815302587393245206:
        await client.close()
@client.command()
async def add(ctx, rankToAdd: discord.Role, member: discord.Member):
    guild = ctx.guild
    channelToAddRoles = guild.get_channel(822412196314611752)
    targetRoles = member.roles
    developer = await ctx.guild.fetch_member(518331788880510979)
    first = None
    canGiveMafia = False
    if ctx.channel == channelToAddRoles:
        try:
            targetRoles.index(rankToAdd)
            embed = discord.Embed(
            title='Retro Romania Roleplay',
            description=f'{member.mention} are deja acel rol. Daca ti se pare ca este o greseala apeleaza developer-ul {developer}.',
            colour=discord.Colour.red()
            )
            embed.set_thumbnail(
             url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
            embed.set_footer(
             text=f'©️ 2021 RETRO All Rights Reserved')
            await ctx.send(embed=embed)
        except Exception:
            staffRetro = guild.get_role(767481287203618837)
            trialhelper = guild.get_role(767481284175200275)
            helper = guild.get_role(767481283063971841)
            helperavansat = guild.get_role(811707329119649862)
            moderator = guild.get_role(767481282006745138)
            supermoderator = guild.get_role(803962152032534558)
            admin = guild.get_role(767481279758336030)
            superadmin = guild.get_role(819613493246165003)
            lidermoderator = guild.get_role(819614130310611024)
            lideradmin = guild.get_role(819613488208674897)
            headofstaff = guild.get_role(767481279079776266)
            cofondator = guild.get_role(767481270355361793)
            developer = guild.get_role(791428646840696832)
            managerdiscord = guild.get_role(767481274922696725)
            accesgrade = guild.get_role(767481286369214486)
            fondator = guild.get_role(767481269998190612)
            liderfactiune = guild.get_role(776556061779951657)

            if rankToAdd == staffRetro:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == trialhelper:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == helper:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == helperavansat:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == moderator:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == supermoderator:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == admin:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == superadmin:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == lidermoderator:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == lideradmin:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == headofstaff:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == managerdiscord:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == cofondator:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == fondator:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            if rankToAdd == accesgrade:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
                return
            topRoleWriter = ctx.author.top_role
            for role in guild.roles:
                if role == topRoleWriter:
                    first = topRoleWriter
                if role == rankToAdd:
                    first = rankToAdd
            if first == rankToAdd:
                embed = discord.Embed(
                title='Retro Romania Roleplay',
                description=f'{member.mention} nu ai functia suficient de mare pentru asta. Daca crezi ca este o greseala apeleaza developerul bot-ului. [Chihiro#7105]',
                colour=discord.Colour.red()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                embed.set_footer(
                    text=f'©️ 2021 RETRO All Rights Reserved')
                await ctx.send(embed=embed)
            if first == topRoleWriter:
                bypass = False
                for actualRole in member.roles:
                    if actualRole == liderfactiune:
                        canGiveMafia = True
                    if actualRole == fondator:
                        bypass = True
                    if actualRole == headofstaff:
                        bypass = True
                    if actualRole == cofondator:
                        bypass = True
                    if actualRole == managerdiscord:
                        bypass = True
                if canGiveMafia == True or bypass == True:
                    if rankToAdd.name[7:12] == 'MAFIA' or rankToAdd.name[7:14] == 'POLITIA' or rankToAdd.name[7:13] == 'AGENT' or rankToAdd.name[7:16] == 'INSPECTOR' or rankToAdd.name[7:14] == 'COMISAR' or rankToAdd.name[10:19] == 'PLUTONIER' or rankToAdd.name[10:23] == 'SUBLOCOTENENT' or rankToAdd.name[10:20] == 'LOCOTENENT' or rankToAdd.name[10:15] == 'MAIOR' or rankToAdd.name[10:17] == 'COLONEL' or rankToAdd.name[10:25] == 'GENERAL LOCOTEN' or rankToAdd.name[7:13] == 'TESTER' or rankToAdd.name[7:15] == 'CO-LIDER':
                        print(f'{time.asctime()}:   {ctx.author.name} i-a dat grad de {rankToAdd} lui {member.name}')
                        await member.add_roles(rankToAdd)
                        embed = discord.Embed(
                        title='Retro Romania Roleplay',
                        description=f'Gradul {rankToAdd.name.strip()} a fost adaugat cu succes lui {member.mention}',
                        colour=discord.Colour.green()
                        )
                        embed.set_thumbnail(
                            url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                        embed.set_footer(
                            text=f'©️ 2021 RETRO All Rights Reserved')
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(
                        title='Retro Romania Roleplay',
                        description=f'Acesta nu este grad de factiune sau nu se poate da prin bot-ul nostru.',
                        colour=discord.Colour.red()
                        )
                        embed.set_thumbnail(
                            url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                        embed.set_footer(
                            text=f'©️ 2021 RETRO All Rights Reserved')
                        await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                    title='Retro Romania Roleplay',
                    description=f'Nu ai lider factiune. Ne pare rau nu poti face asta.',
                    colour=discord.Colour.red()
                    )
                    embed.set_thumbnail(
                        url='https://cdn.discordapp.com/attachments/800379324460695572/822416819839041546/Retro.png')
                    embed.set_footer(
                        text=f'©️ 2021 RETRO All Rights Reserved')
                    await ctx.send(embed=embed)

@client.command()
async def remove(ctx, rankToDelete: discord.Role, member: discord.Member):
    guild = ctx.guild
    channelToRemoveRoles = guild.get_channel(822412196314611752)
    targetRoles = member.roles


@client.command()
async def clear(ctx, numberOfClear):
    try:
        await ctx.channel.purge(limit=int(numberOfClear))
    except Exception:
        await ctx.channel.send('Nu ai introdus un numar.')

@client.command()
async def test1(ctx, rank: discord.Role):
    print(rank.name[7:15])


    


client.run('')