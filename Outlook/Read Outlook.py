import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) 
# "6" refers to the index of a folder - in this case, the inbox. 
# You can change that number to reference any other folder

messages = inbox.Items
message = messages.GetFirst()
while message:
    print(message.Subject)
    # print(message.body)
    message = messages.GetNext()

