from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def shutdown(self, ctx):
        await ctx.send("Extinction du bot…")
        await self.bot.close()


async def setup(bot):
    await bot.add_cog(Admin(bot))
