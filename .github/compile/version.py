import json
import os
import linecache
major = int(linecache.getline("ScratchOff.py", 28)[8:])
minor = int(linecache.getline("ScratchOff.py", 29)[8:])
releases = int(linecache.getline("ScratchOff.py", 30)[11:])
build = int(linecache.getline("ScratchOff.py", 31)[8:])
typenum = int(linecache.getline("ScratchOff.py", 32)[10:])
x = int(linecache.getline("ScratchOff.py", 33)[4:])
version = str(major) + "." + str(minor) + "." + str(releases) + \
    "." + str(build) + "." + str(typenum) + "." + str(x)
rb = json.loads(os.environ["MSG"])[-1].split("\n\n")
ver = rb[0][4:]
log = rb[1]
with open("version.ps1", "w", encoding="utf8") as file:
    file.write("\"VERSION=" + "ScratchOff v" + ver +
               " (Version " + version + ") \" >> $env:GITHUB_ENV\n")
    file.write("\"VER=" + ver + "\" >> $env:GITHUB_ENV\n")
    file.write("\"FILEPATH=Releases\\ScratchOff_" +
               version + ".zip\" >> $env:GITHUB_ENV\n")
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("```plain\n" + log + "\n```")
