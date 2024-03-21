from getpass4 import getpass
p = getpass.getpass(prompt = "Enter the password:")
if(p == "ram"):
    print("Go to Haven")
else:
    print("NO")