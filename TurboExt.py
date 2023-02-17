import sys, os, shutil

args = sys.argv

if len(args)<2:
    print("Use: python TurboExt.py <your_file>.exe")
elif not os.path.isfile(args[1]):
    print("Error: File not found!")
elif not args[1].endswith(".exe"):
    print("Error: File should be executable!")
else:
    os.system(f"python pyinstxtractor.py {args[1]}")

    try:
        file = f"{args[1].split('.')[0]}.pyc"

        shutil.copy(f"{os.getcwd()}/{args[1]}_extracted/{file}", os.getcwd())
    except:

        files = os.listdir(f"{os.getcwd()}/{args[1]}_extracted")

        for x in files:
            if x.endswith(".pyc"):
                if not "pyi" in x and not "struct" in x:
                    file = x
                    shutil.copy(f"{os.getcwd()}/{args[1]}_extracted/{file}", os.getcwd())
    os.system(f"decompyle3 {file}")