word = input ("type word")
if word.endswith ("а"):
    print ("nom.sg")
elif word.endswith ("я"):
    print ("nom.sg")
elif word.endswith ("ы"):
    print ("gen.sg or nom.pl or acc.pl")
elif word.endswith ("и"):
    print ("gen.sg or nom.pl or acc.pl")
elif word.endswith ("е"):
    print ("dat.sg or loc.sg")
elif word.endswith ("у"):
    print ("acc.sg")
elif word.endswith ("ю"):
    print ("acc.sg")
elif word.endswith ("й"):
    print ("instr.sg")
elif word.endswith ("ь"):
    print ("gen.pl or acc.pl")
elif word.endswith ("м"):
    print ("dat.pl")
elif word.endswith ("ми"):
    print ("instr.pl")
elif word.endswith ("ах"):
    print ("loc.pl")
elif word.endswith ("ях"):
    print ("loc.pl")
else:
    print ("gen.pl or acc.pl")
