from discord.ext import commands

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx):
        await ctx.send("🛒 Commande shop ok !")


async def setup(bot):
    await bot.add_cog(Shop(bot))
