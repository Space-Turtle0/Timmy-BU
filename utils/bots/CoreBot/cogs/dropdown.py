import discord
from discord.ext import commands


class Dropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(
                label="Math Helpers",
                description="If you need help with Math, click here!",
                emoji="โ๏ธ",
            ),
            discord.SelectOption(
                label="Science Helpers",
                description="If you need help with Science, click here!",
                emoji="๐งช",
            ),
            discord.SelectOption(
                label="Social Studies Helpers",
                description="If you need help with Social Studies, click here!",
                emoji="๐",
            ),
            discord.SelectOption(
                label="English Helpers",
                description="If you need help with English, click here!",
                emoji="๐",
            ),
            discord.SelectOption(
                label="Essay Helpers",
                description="If you need help with an Essay, click here!",
                emoji="โ๏ธ",
            ),
            discord.SelectOption(
                label="Language Helpers",
                description="If you need help with a Language, click here!",
                emoji="๐ฃ",
            ),
            discord.SelectOption(
                label="Computer Science Helpers",
                description="If you need help with Computer Science, click here!",
                emoji="๐ป",
            ),
            discord.SelectOption(
                label="Fine Art Helpers",
                description="If you need help with Fine Arts, click here!",
                emoji="๐จ",
            ),
            discord.SelectOption(
                label="Other Helpers",
                description="If you need help with anything else, click here!",
                emoji="๐ง",
            ),
        ]

        super().__init__(
            placeholder="Select a subject you need help with!",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        self.view.stop()


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        DropdownClass = Dropdown()

        self.add_item(DropdownClass)
        self.InteractionClass = DropdownClass


class DropdownDemo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticketdropdown(self, ctx):
        view = DropdownView()
        await ctx.send("Select a ticket via the dropdown here!:", view=view)
        await view.wait()

        dropdownclass = view.InteractionClass.values
        await ctx.send(dropdownclass)


def setup(bot):
    bot.add_cog(DropdownDemo(bot))
