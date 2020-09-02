import time
import sqlite3
import os
import sys
import atexit

installpath = "/home/espriminati/.steam/steam/steamapps/common/Team Fortress 2" # Change this to your TF2 Install Directory. MUST NOT END WITH "/" OR "\"
name = "" # (optional) Change this to your IGN
saveEveryXKills = 10 # Save the file every X kills. Setting this to 1 or lower will save every kill (Recommended: Over 5)

saveEveryXKills = max(1, saveEveryXKills)
remainingKillsToSave = saveEveryXKills
logpath = "/tf/console.log" # DO NOT CHANGE THIS
killedText = "Just killed {victim} using my {weapon}. Feeling good! {crit}"
critText = "critted them btw lol"
db = sqlite3.connect("kills.db")
sqlcommand = "INSERT INTO kills (victim,weapon,crit) VALUES (?,?,?);"

# i have no idea what this is i just stole it from stackoverflow lmao
def watch(fn, words):
	fp = open(fn, 'r')
	while True:
		new = fp.readline()

		if new:
			for word in words:
				if word in new:
					yield (word, new)
		else:
			time.sleep(0.5)

def saveBeforeExit():
	db.commit()
	db.close()

atexit.register(saveBeforeExit)

# Called whenever you kill someone. Change this however you want.
# victim: (string) The name of the player you just killed
# weapon: (string) The ID of the weapon you just killed with
# crit:  (boolean) Was the last hit a critical hit?
def killed(victim, weapon, crit):
	if crit:
		finalText = killedText.format(
			victim=victim, weapon=weapon, crit=critText)
	else:
		finalText = killedText.format(victim=victim, weapon=weapon, crit="")
	print(finalText)

	db.execute(sqlcommand, (victim, weapon, (1 if crit else 0)))

	remainingKillsToSave -= 1
	if (remainingKillsToSave == 0):
		print("%s kills since last save, saving..." % saveEveryXKills)
		db.commit()

# Check if the installation directory is valid and exists
if not (os.path.exists(installpath) and os.path.isdir(installpath)) or (sys.platform.startswith("win") and installpath.startswith("/")):
	print("Installation directory is invalid. Please make sure the installpath variable is correct")
	sys.exit(1)

# Check if we have an actual 'console.log' file
if not os.path.exists(installpath + logpath):
	print("console.log file doesnt exist. Please make sure that you started TF2 using '-condebug -conclearlog -console' arguments")
	sys.exit(1)

for triggeredWord, log in watch(installpath + logpath, ['killed', '"name" =']):
	if log.startswith('"name" ='): # do not check triggeredWord because if someone has '"name" =' in their name, we dont want to change the name again 
		name = log.replace('"', "").replace('name = ', "").replace(" ( def. unnamed )", "").replace("\n", "")
		print(name)
	else:
		replacedArray = log.replace(
			name + " killed ", "").replace(".\n", "").split(" with ")
		killed(" with ".join(replacedArray[0:len(replacedArray)-1]), replacedArray[-1].replace(
			". (crit)\n", ""), log.endswith("(crit)\n"))

