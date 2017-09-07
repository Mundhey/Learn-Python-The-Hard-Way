tabby_cat="\t I am tabbed in"
persian_cat="I'm split\non line"
backslash_cat="I'm \\ a \\ cat"

fat_cat="""
I'll do a list
\t* Cat food\a
\t* fishes\a
\t* catnip\n\t* Grass\a
"""


catty='''
I'll do a list
\t* Cat food\a
\t* fishes\a
\t* catnip\n\t* Grass\a
'''


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print catty

while True:
 for i in ["/","- ","|","\\","|"]:
  print "%s\r" % i,