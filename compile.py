# 请配置环境变量！
# python32 为 Python x86 路径
# python64 为 Python x64 路径
import os
import linecache
import zipfile
PATH = os.environ.get("PATH").split(";")
major = int(linecache.getline("ScratchOff.py", 28)[8:])
minor = int(linecache.getline("ScratchOff.py", 29)[8:])
releases = int(linecache.getline("ScratchOff.py", 30)[11:])
build = int(linecache.getline("ScratchOff.py", 31)[8:])
typenum = int(linecache.getline("ScratchOff.py", 32)[10:])
x = int(linecache.getline("ScratchOff.py", 33)[4:])
if int(typenum) <= 6:
    DEBUG = True
else:
    DEBUG = False
version = str(major) + "." + str(minor) + "." + str(releases) + \
    "." + str(build) + "." + str(typenum) + "." + str(x)
python64 = os.environ.get("python64")
python32 = os.environ.get("python32")
print(python32)
print(python64)
print()
os.system("md python")
os.system("\"" + python64 + "\\python\" -m venv python\\python64")
os.system("python\\python64\\Scripts\\python -m pip install --upgrade pip")
os.system("python\\python64\\Scripts\\pip install pywin32")
os.system("python\\python64\\Scripts\\pip install pygame==1.9.6")
os.system("python\\python64\\Scripts\\pip install pillow")
os.system("python\\python64\\Scripts\\pip install pyinstaller")
os.system("\"" + python32 + "\\python\" -m venv python\\python32")
os.system("python\\python32\\Scripts\\python -m pip install --upgrade pip")
os.system("python\\python32\\Scripts\\pip install pywin32")
os.system("python\\python32\\Scripts\\pip install pygame==1.9.6")
os.system("python\\python32\\Scripts\\pip install pillow")
os.system("python\\python32\\Scripts\\pip install pyinstaller")
if DEBUG:
    os.system("md Releases\\ScratchOff_" + version)
    os.system("python\\python64\\Scripts\\pyinstaller -F -w -i SO.ico ScratchOff.py")
    os.system(
        "move dist\\ScratchOff.exe Releases\\ScratchOff_" +
        version +
        "\\ScratchOff64_RLS.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")
    os.system("python\\python32\\Scripts\\pyinstaller -F -w -i SO.ico ScratchOff.py")
    os.system(
        "move dist\\ScratchOff.exe Releases\\ScratchOff_" +
        version +
        "\\ScratchOff32_RLS.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")
    with open("ScratchOff.py", "r", encoding="utf-8") as file:
        text = file.readlines()
    text[23] = "DEBUG = True\n"
    with open("ScratchOff.py", "w", encoding="utf-8") as file:
        for i in text:
            file.write(i)
    os.system("python\\python64\\Scripts\\pyinstaller -F -c -i SO.ico ScratchOff.py")
    os.system(
        "move dist\\ScratchOff.exe Releases\\ScratchOff_" +
        version +
        "\\ScratchOff64_DBG.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")
    os.system("python\\python32\\Scripts\\pyinstaller -F -c -i SO.ico ScratchOff.py")
    os.system(
        "move dist\\ScratchOff.exe Releases\\ScratchOff_" +
        version +
        "\\ScratchOff32_DBG.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")
    with open("ScratchOff.py", "r", encoding="utf-8") as file:
        text = file.readlines()
    text[23] = "DEBUG = False\n"
    with open("ScratchOff.py", "w", encoding="utf-8") as file:
        for i in text:
            file.write(i)
else:
    os.system("md Releases\\ScratchOff_" + version)
    os.system("python\\python64\\Scripts\\pyinstaller -F -w -i SO.ico ScratchOff.py")
    os.system(
        "move dist\\ScratchOff.exe Releases\\ScratchOff_" +
        version +
        "\\ScratchOff64.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")
    os.system("python\\python32\\Scripts\\pyinstaller -F -w -i SO.ico ScratchOff.py")
    os.system(
        "move dist\\ScratchOff.exe Releases\\ScratchOff_" +
        version +
        "\\ScratchOff32.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del ScratchOff.spec")

with open("temp.txt", "w") as file:
    file.write("D")
os.system(
    "xcopy website Releases\\ScratchOff_" +
    version +
    "\\website <temp.txt")
os.system("xcopy pictures Releases\\ScratchOff_" +
          version + "\\pictures /E <temp.txt")
os.system("del temp.txt")
os.system("copy font.ttc Releases\\ScratchOff_" + version + "\\font.ttc")
os.system("copy SO.ico Releases\\ScratchOff_" + version + "\\SO.ico")
os.system("copy about.png Releases\\ScratchOff_" + version + "\\about.png")
os.system("rd /s /q python")
z = zipfile.ZipFile(
    "Releases\\ScratchOff_" +
    version +
    ".zip",
    'w',
    zipfile.ZIP_DEFLATED)
for dir_path, dir_names, file_names in os.walk(
        "Releases\\ScratchOff_" + version):
    f_path = dir_path.replace("Releases\\ScratchOff_" + version, "")
    f_path = f_path and f_path + os.sep or ""
    for filename in file_names:
        z.write(os.path.join(dir_path, filename), f_path + filename)
z.close()
