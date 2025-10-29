# Jolie is setting up an art installation for her cat, Millie. The art installation will be made up of multiple LEDs.
# Jolie has decided that she needs a specific number of red LEDs, green LEDs, and blue LEDs. After rummaging through her desk, she has found some of each. She can buy two special types of LEDs, one which can be either red or green, and another which can be either green or blue.
# How many of the special LEDs will Jolie need to buy to finish her installation?

# ## Input
# The first line of input contains three integers r, g, and b which are the numbers of red LEDs, green LEDs, and blue LEDs Jolie needs.
# The second line contains three integers cr, cg, and cb, which are the numbers of red LEDs, green LEDs, and blue LEDs Jolie already owns.
# The third line contains two integers crg, cgb, which are the numbers of special LEDs that can be either red or green, and the number of special LEDs that can be either green or blue, that are available for Jolie to buy.

# ## Output
# Output a single integer, which is the total number of LEDs Jolie needs to buy to make her installation.
# Output -1 if there aren't enough LEDs for her to complete her installation.

[r, g, b] = [int(x) for x in input().split()] # Get the number of required r/g/b LEDs
[cr, cg, cb] = [int(x) for x in input().split()] # Get the number of available r/g/b LEDs
[crg, cgb] = [int(x) for x in input().split()] # Get the number of purchasable rg/gb LEDs

# A running count of the number of rgb LEDs bought
purchased = 0

# Use the available r/g/b LEDs
r -= min(r, cr)
g -= min(g, cg)
b -= min(b, cb)

# Check if enough rg/gb LEDs
if crg < r or cgb < b:
    print(-1)
    exit()

# Purchase rg LEDs for just r requirement
purchased += r
crg -= r
r = 0

# Purchase gb LEDs for just b requirement
purchased += b
cgb -= b
b = 0

# rg available, purchase as many as needed
if crg > 0:
    available = min(g, crg)
    g -= available
    purchased += available

# gb available, purchase as many as needed
if crg > 0:
    available = min(g, cgb)
    g -= available
    purchased += available

if r == 0 and g == 0 and b == 0:
    print(purchased)
else:
    print(-1)
