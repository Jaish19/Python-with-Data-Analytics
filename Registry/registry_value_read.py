from winreg import*

Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
RawKey = OpenKey(Registry, "SOFTWARE\\pyth")

name, value, type = EnumValue(RawKey, 0)
print("name:",name,"value:", value)
