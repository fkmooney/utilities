import win32com.client
import datetime
import os

path = os.path.expanduser("D:/Information_Machine/IM_daily_connection_reports")
today = datetime.date.today()

# get messages in subfolder
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
root_folder = namespace.Folders.Item(1)
subfolder = root_folder.Folders['Archived'].Folders['IM Reports']
messages = subfolder.Items

# cycle through messages to find unread daily reports and pull attachments
for message in messages:
    if message.Unread and "Video Connections Report" in message.Subject:
        print("Pulling attachemnt for:", message.Subject)
        attachments = message.Attachments
        attachment = attachments.Item(1)
        for attachment in message.Attachments:
            attachment.SaveAsFile(os.path.join(path, str(attachment)))
            if message.Unread:
                message.Unread = False
            break
