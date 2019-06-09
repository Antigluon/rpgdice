from redbot.core import commands
from dice import roll

def cleanroll(formula):
  result = roll(formula)
  try:
    result = sum(result)
  except TypeError:
    #already an int - this is fine
    pass
  return result

class RPGDice(commands.Cog):
    """An RPG dice roller"""

    @commands.command(name="roll", aliases=["r"])
    async def diceroll(self, ctx, formula, times=1):
      "Rolls RPG dice." 
      try:       
        result = str(cleanroll(formula))
        for time in range(1, int(times)):
          result += ", {}".format(cleanroll(formula))
        await ctx.send("`{}` = `{}`".format(formula, result))
      except (dice.ParseException, dice.DiceException):
        await ctx.send("Invalid expression.")

    @commands.command(name="statroll5e", 
      aliases=["5estatroll", "statroll", "statgen5e", "5estatgen", "statgen"])
    async def statroll5e(self, ctx, arg="4d6 drop lowest"):
      """Rolls d&d stats."""
      formulas = {"default": "4d6h3t", "4d6 drop lowest": "4d6h3t", 
      "forgiving": "4d6rr1h3", "harsh": "3d6"}
      if arg in formulas.keys():
        formula = formulas[arg]
      else:
        formula = arg
      try:
          await ctx.send("{}: `{}, {}, {}, {}, {}, {}`".format(arg, 
        cleanroll(formula), cleanroll(formula), cleanroll(formula), 
        cleanroll(formula), cleanroll(formula), cleanroll(formula)))
      except Exception:
        await ctx.send("Invalid expression.")
