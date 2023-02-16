from winreg import*
import winreg

keyVal = r'SOFTWARE\\Wow6432Node\\pyth'

key = CreateKey(HKEY_LOCAL_MACHINE, keyVal)
SetValueEx(key, "Python_Status", 0, REG_SZ, "0")
SetValueEx(key, "VBAI_Status", 0, REG_SZ, "0")
SetValueEx(key, "VBAI_ROI", 0, REG_SZ, "0,0,0,0,0")
SetValueEx(key, "Python_ROI", 0, REG_SZ, "0,0,0,0,0")



name1, value1, type = EnumValue(key, 0)
print("name:",name1,"value:", value1)
name2, value2, type = EnumValue(key, 1)
print("name:",name2,"value:", value2)
name3, value3, type = EnumValue(key, 2)
print("name:",name3,"value:", value3)
name4, value4, type = EnumValue(key, 3)
print("name:",name4,"value:", value4)
#CloseKey(key)

while True:
	name1, value1, type = EnumValue(key, 0)
	#print("name:",name1,"value:", value1)
	if (value1 == "1"):
		print ("change in registry")
		SetValueEx(key, "Python_Status", 0, REG_SZ, "0")


CloseKey(key)










# key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,key_name)
# subkey = winreg.CreateKey(key, "ContextMenuHandlers")
# subkey2 = winreg.CreateKey(subkey, "PythonSample")
# winreg.SetValueEx(subkey2, None, 0, winreg.REG_SZ, ShellExtension._reg_clsid_)
# print (ShellExtension._reg_desc_, "registration complete." )


# key_name = r'SOFTWARE\\pyth_1'

# try:
#       key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_name)
#       # Merely creating LocalDumps is sufficient to enable the defaults.
#       winreg.CreateKey(key, "LocalDumps")
#       # Disable the WER UI, as documented here:
#       # https://msdn.microsoft.com/en-us/library/windows/desktop/bb513638.aspx
#       winreg.SetValueEx(key, "DontShowUI", 0, winreg.REG_DWORD, 1)
#     # Trap OSError instead of WindowsError so pylint will succeed on Linux.
#     # Catching errors is important because some build machines are not elevated
#     # and writing to HKLM requires elevation.
#     except OSError:
#       pass 


# # Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
# # RawKey = OpenKey(Registry, "SOFTWARE\\pyth")

# # #print (EnumValue(RawKey,1))
# # try:
# # 	i = 0
# # 	while 1:
# # 		name, value, type = EnumValue(RawKey, i)
# # 		print(name, value, i)
# # 		i += 1
# # except WindowsError:
# # 	print("some")