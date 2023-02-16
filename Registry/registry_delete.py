from winreg import*
import winreg

keyVal = r'SOFTWARE\\pyth'

Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
OpenKey(Registry, "SOFTWARE\\pyth")
DeleteKey(HKEY_LOCAL_MACHINE,keyVal)


