#Developed by WilliamNT (Sculman#9270)


import os
import sys
import logging

#logging
logging.basicConfig(filename='kvgenerator_log.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)
try:
    1/0
except ZeroDivisionError as err:
    logger.error(err)

def restartSelf():
        print("Configuration cleared. You may start again now.")
        os.execv(sys.executable, ['python'] + sys.argv)

print("KV File Generator for CS:GO written in Python by WilliamNT (Sculman#9270)")

#Asking for a map name. Also we're eliminating the possibility of giving a name ending with .bsp
while True:
    try:
        mapName = input("Map name > ").lower()
        while mapName.endswith(".bsp"):
            print('Invalid map name. Map names with the ending ".bsp" are not allowed.')
            break
        if mapName == "":
            mapName = "map"
            break
        else:
            break
    except ValueError:
        print('Invalid map name. Map names with the ending ".bsp" are not allowed.')


#Asking the user for details
mapAuthor = input("Author name > ")

while True:
    try:
        charType_T = int(input('''Please choose a terrorist type:
        [1] Anarchist
        [2] Balkan
        [3] Leet
        [4] Phoenix
        [5] Pirate
        [6] Professional
        [7] Separatist
        > '''))      
        if charType_T < 1 or charType_T > 7:
            raise ValueError
        break
    except ValueError:
        print('Invalid terrorist type. Please choose between 1-7.')

while True:
    try:
        charType_CT = int(input('''Please choose a counter terrorist type:
        [1] FBI
        [2] GIGN
        [3] GSG
        [4] IDF
        [5] SAS
        [6] SEALS
        [7] SWAT
        > '''))
        if charType_T < 1 or charType_T > 7:
            raise ValueError
        break
    except ValueError:
        print('Invalid counter terrorist type. Please choose between 1-7.')


#convert number to type name
if charType_T == 1:
    friendlyCharName_T = "Anarchist"
elif charType_T == 2:
    friendlyCharName_T = "Balkan"
elif charType_T == 3:
    friendlyCharName_T = "Leet"
elif charType_T == 4:
    friendlyCharName_T = "Phoenix"
elif charType_T == 5:
    friendlyCharName_T = "Pirate"
elif charType_T == 6:
    friendlyCharName_T = "Professional"
elif charType_T == 7:
    friendlyCharName_T = "Separatist"

if charType_CT == 1:
    friendlyCharName_CT = "FBI"
elif charType_CT == 2:
    friendlyCharName_CT = "GIGN"
elif charType_CT == 3:
    friendlyCharName_CT = "GSG"
elif charType_CT == 4:
    friendlyCharName_CT = "IDF"
elif charType_CT == 5:
    friendlyCharName_CT = "SAS"
elif charType_CT == 6:
    friendlyCharName_CT = "SEALS"
elif charType_CT == 7:
    friendlyCharName_CT = "SWAT"

while True:
    try:
        print("##########" + "\n" + "Map name: " + mapName + "\n" + "Author: " + mapAuthor + "\n" + "T type: " + friendlyCharName_T + "\n" + "CT type: " + friendlyCharName_CT + "\n" "##########")
        configConfirm = input("Are these correct? [Y/N] > ").upper()
        while configConfirm not in ("Y", "N", ""):
            print('Invalid answer. Please choose between yes [Y] and no [N].')
            break

        else:
            break #Még meg kell csinálni hogy újra kezdje az inputokat
    except ValueError:
        break

if charType_T == 1: #Anarchist
    tline = '		"tm_anarchist"""\n		"tm_anarchist_variantA"""\n		"tm_anarchist_variantB"""\n		"tm_anarchist_variantC"""\n		"tm_anarchist_variantD"""\n'
    charArm_T = 'models/weapons/t_arms_anarchist.mdl'

elif charType_T == 2: #Balkan
    tline = '		"tm_balkan_variantA"""\n		"tm_balkan_variantB"""\n		"tm_balkan_variantC"""\n		"tm_balkan_variantD"""\n		"tm_balkan_variantE"""\n'
    charArm_T = 'models/weapons/t_arms_balkan.mdl'

elif charType_T == 3: #LEET
    tline = '		"tm_leet_variantA"""\n		"tm_leet_variantB"""\n		"tm_leet_variantC"""\n		"tm_leet_variantD"""\n		"tm_leet_variantE"""\n'
    charArm_T = 'models/weapons/t_arms_leet.mdl'

elif charType_T == 4: #Phoenix
    tline = '		"tm_phoenix"""\n		"tm_phoenix_variantA"""\n		"tm_phoenix_variantB"""\n		"tm_phoenix_variantC"""\n		"tm_phoenix_variantD"""\n'
    charArm_T = 'models/weapons/t_arms_phoenix.mdl'

elif charType_T == 5: #Pirate
    tline = '		"tm_pirate"""\n		"tm_pirate_variantA"""\n		"tm_pirate_variantB"""\n		"tm_pirate_variantC"""\n		"tm_pirate_variantD"""\n'
    charArm_T = 'models/weapons/t_arms_pirate.mdl'

elif charType_T == 6: #Professional
    tline = '		"tm_professional"""\n		"tm_professional_var1"""\n		"tm_professional_var2"""\n		"tm_professional_var3"""\n		"tm_professional_var4"""\n'
    charArm_T = 'models/weapons/t_arms_professional.mdl'

elif charType_T == 7: #Separatist
    tline = '		"tm_separatist"""\n		"tm_separatist_variantA"""\n		"tm_separatist_variantB"""\n		"tm_separatist_variantC"""\n		"tm_separatist_variantD"""\n'
    charArm_T = 'models/weapons/t_arms_separatist.mdl'

#end of T models list ------  end of T models list ------  end of T models list ------  end of T models list ------  end of T models list ------  end of T models list ------  end of T models list ------  

if charType_CT == 1: #FBI
    ctline = '		"ctm_fbi"""\n		"ctm_fbi_variantA"""\n		"ctm_fbi_variantB"""\n		"ctm_fbi_variantC"""\n		"ctm_fbi_variantD"""\n'
    charArm_CT = 'models/weapons/ct_arms_fbi.mdl'

elif charType_CT == 2: #GIGN
    ctline = '		"ctm_gign"""\n		"ctm_gign_variantA"""\n		"ctm_gign_variantB"""\n		"ctm_gign_variantC"""\n		"ctm_gign_variantD"""\n'
    charArm_CT = 'models/weapons/ct_arms_gign.mdl'

elif charType_CT == 3: #GSG
    ctline = '		"ctm_gsg9"""\n		"ctm_gsg9_variantA"""\n		"ctm_gsg9_variantB"""\n		"ctm_gsg9_variantC"""\n		"ctm_gsg9_variantD"""\n'
    charArm_CT = 'models/weapons/ct_arms_gsg9.mdl'

elif charType_CT == 4: #IDF
    ctline = '		"ctm_idf"""\n		"ctm_idf_variantB"""\n		"ctm_idf_variantC"""\n		"ctm_idf_variantD"""\n		"ctm_idf_variantE"""\n		"ctm_idf_variantF"""\n'
    charArm_CT = 'models/weapons/ct_arms_idf.mdl'

elif charType_CT == 5: #SAS
    ctline = '		"ctm_sas"""\n		"ctm_sas_variantA"""\n		"ctm_sas_variantB"""\n		"ctm_sas_variantC"""\n		"ctm_sas_variantD"""\n		"ctm_sas_variantE"""\n'
    charArm_CT = 'models/weapons/ct_arms_sas.mdl'

elif charType_CT == 6: #SEALS
    ctline = '		"ctm_st6"""\n		"ctm_st6_variantA"""\n		"ctm_st6_variantB"""\n		"ctm_st6_variantC"""\n		"ctm_st6_variantD"""\n'
    charArm_CT = 'models/weapons/ct_arms_st6.mdl'

elif charType_CT == 7: #SWAT
    ctline = '		"ctm_swat"""\n		"ctm_swat_variantA"""\n		"ctm_swat_variantB"""\n		"ctm_swat_variantC"""\n		"ctm_swat_variantD"""\n'
    charArm_CT = 'models/weapons/ct_arms_swat.mdl'

finalprint = '"'+mapName+'"\n' '{\n' '     "name"  ' '"'+mapName+'"\n' '     "imagename"     ' '"'+mapName+'"\n'  '     "t_arms"    '  '"'+charArm_T+'"\n'	'   "ct_arms"   '	'"'+charArm_CT+'"\n'	    '   "t_models"\n' '    {\n' +tline+ '}\n' 	'   "ct_models"\n' '    {\n' +ctline+ '    }\n' '}\n'


#Generate a file, if the user confirms that the settings are correct they gave
if configConfirm.upper() == "Y"or "":
    with open(mapName + ".kv", 'w') as outputTxt:
         outputTxt.write(finalprint)
    print('File' + '"' + mapName + ".kv" + '"successfully generated.')
elif configConfirm.upper() == "N" or "R":
    restartSelf()

input("Press enter to exit. > ")