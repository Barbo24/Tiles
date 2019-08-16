text1 = "wallBOT"
for x in range(50):
    print(text1 + str(x), "=", "(" + str(16*x) + ",", str(0) + ")")
else: print("###########################################################################################")

text2 = "win.blit(wall, lvl1lay.wallBOT"
text3 = ")"
for x in range(50):
        print("   ", text2 + str(x) + text3)
else: print("###########################################################################################")


for x in range(101):
    print("healthpercentage" + str(x) ,"=", "font.render(",'"' + str(x) + "HP" + '"', ", True, white, black)")
else: print("###########################################################################################")
	
for x in range(101):
    print("HPstr =", '"' + str(x) + '"')
else: print("###########################################################################################")
	
for x in range(101):
    print("   ", "if hp.HPint ==", str(x) + ":") 
    print("       ", 'hp.HPstr = "' + str(x) + '"')
else: print("###########################################################################################")