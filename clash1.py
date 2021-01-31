# One of the things coders regularly need to do, is to check if brackets/braces/parenthesis are used correctly. Many languages' IDE provide assistance for that task, but yours doesn't...
#
# You want to write a parser that does the checking for you.
# Your program should check the following syntax rules:
# - There can't be more [ than ] or vice versa. Same for ( and ).
# - There can't be a ) or ] before it's opening counterpart.
# - Any other characters can be ignored.
# - Pairs can't be "separated", e.g. ( [ ) ] is wrong, because the ] is outside the encapsulating ()

cadena="{{{{}}[]{}}}}"
var1=cadena.find("}")
print(var1)
cantidad_llaves=0
for i in cadena:
    cantidad_llaves=cadena.find("}")
print(cantidad_llaves)
