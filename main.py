import json
import discord

BunnybebesBot = discord.Client(intents=discord.Intents.all())


#Button stuff - in future must go to slash commands or something, had problem with it not seeing Menu class
class Menu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

                        #id required for persistent view/ buttons to work on bot reset
    @discord.ui.button(custom_id = '1', label='Yes', style=discord.ButtonStyle.blurple)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name = "The Test")
        # This will get the role you want to edit^
        await interaction.user.add_roles(role) # adds the role
        await interaction.response.send_message("*Look through the OpenProj category and find a task you can do..*", ephemeral=True) 

    @discord.ui.button(custom_id = '2', label='No', style=discord.ButtonStyle.blurple)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("*cries*", ephemeral=True)    

@BunnybebesBot.event
async def on_ready():
    #How to make buttons work after bot restart = You need to make the view persistent
    #Give every element in that view a unique ID, set the timeout to None and inside the setup_hook you need to do bot.add_view(YourView())
    BunnybebesBot.add_view(Menu())
    print(f'{BunnybebesBot.user} has connected to Discord!')

    channel = BunnybebesBot.get_channel(1049419765267038251)

    #Creating Whitelist Task Embed
    bunnybebesBlue = discord.Colour.from_str('#2854dd')
    theTestEmbed0 = discord.Embed(title="The Test", color=bunnybebesBlue)

    theTestEmbed1 = discord.Embed(title="", description= '"Before we let you join the rest of the contributors, you must pass **The Test**.."', color=bunnybebesBlue)
    theTestEmbed1.set_thumbnail(url = "https://i.postimg.cc/Pf1jV3Y5/Hidden-Bebe-100.jpg")

    theTestEmbed2 = discord.Embed(title="", description= '"Bunny Bebes uses a bot called **OpenProj** to allow the community to **contribute** to the project and earn **shares** in the projects **profit**.."', color=bunnybebesBlue)
    theTestEmbed2.set_thumbnail(url = "https://i.postimg.cc/Pf1jV3Y5/Hidden-Bebe-100.jpg")

    theTestEmbed3 = discord.Embed(title="", description= '"A member can **contribute** by doing **tasks** for the project and can **release** their earnings from the server at the end of every month.."', color=bunnybebesBlue)
    theTestEmbed3.set_thumbnail(url = "https://i.postimg.cc/Pf1jV3Y5/Hidden-Bebe-100.jpg")

    theTestEmbed4 = discord.Embed(title="", description= '"Prove your worthy of joining our community by **completing 1 task**.."', color=bunnybebesBlue)
    theTestEmbed4.set_thumbnail(url = "https://i.postimg.cc/Pf1jV3Y5/Hidden-Bebe-100.jpg")

    
    # listOfEmbeds = []
    # listOfEmbeds.append(theTestEmbed0)
    # listOfEmbeds.append(theTestEmbed1)
    # listOfEmbeds.append(theTestEmbed2)
    # listOfEmbeds.append(theTestEmbed3)
    # listOfEmbeds.append(theTestEmbed4)
    # await channel.send(embeds=listOfEmbeds)

    # view = Menu()
    # message = ""

    # bunnybebesBlue = discord.Colour.from_str('#2854dd')
    # theTestEmbed4 = discord.Embed(title="Begin the Test?", description= "", color=bunnybebesBlue)
    # await channel.send(message, embed = theTestEmbed4, view=view)



f = open("tokens")
s = f.read()
tokensDict = json.loads(s)
BunnyBebesToken = tokensDict["BunnyBebesToken"]


BunnybebesBot.run(str(BunnyBebesToken))
