import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(5) 
# "6" refers to the index of a folder - in this case, the inbox. 
# "5" is Sent items


messages = inbox.Items
message = messages.GetLast()
props = message.ItemProperties

for prop in props:
	print(prop)