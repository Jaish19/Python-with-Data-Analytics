from winreg import*
import winreg

keyVal = r'SOFTWARE\\pyth'

key = CreateKey(HKEY_LOCAL_MACHINE, keyVal)
SetValueEx(key, "Start Page", 0, REG_SZ, "skill")
SetValueEx(key, "Start Page 2", 0, REG_SZ, "skill")
CloseKey(key)






