# Heavy Journal

Adds the functionality of the "blog updating" weapon to TF2:

![Comic page about the weapon](https://i.imgur.com/Hf8fLHB.png)

*unlike the comic, this script will not make your bullets biodegrade, or set up a blog for you*

# INSTALLATION

1. Be sure that you have Python installed (Python3 crashes when it finds some characters (e.g.: Japanese characters). Use Python2 if you can)
2. Edit the script.py file according to the instructions below
3. Add `-condebug -conclearlog -console` in your TF2 Launch Options
4. Start the game first, then the script
5. Congrats, now the `kills.db` file will update with every kill you get! You can use another script to watch this file and update an *actual blog* easily!

# EDITING THE FILE

You just need to edit the first 2 variables

`name` = Your Steam account name. Running `name` command in in-game console will automatically update your name within the script.

`installpath` = Your TF2 Installation folder. Must direct to `Team Fortress 2` folder and must not end with a `/` or `\`

# IS THIS VAC BANNABLE?

No.

# HOW TO UPDATE BLOG

This script only records your kills into a SQLite file. You can watch the SQLite file for changes to update an *actual* blog.
