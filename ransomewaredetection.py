import smtplib
import time
import os
import shutil
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from email.mime.text import MIMEText

# Define a custom made event handler that will handle the file system events

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.file_modifications = {}


    def on_modified(self, event):
        # This method will be triggered when a file is modified
        if not event.is_directory:
            file_extension = os.path.splitext(event.src_path)[1]
            if file_extension in ['.docx','.pdf','.txt']:
                self.detect_ransomware(event.src_path)
            print(f"File modified: {event.src_path}")

    def detect_ransomware(self, file_path):
        # Count the number of modification for this file
        if file_path in self.file_modifications:
            self.file_modifications[file_path] +=1
        else:
            self.file_modifications[file_path] = 1

            # Check if too many changes happen in a short period (indicates ransomware)
            if self.file_modifications[file_path] > 5:  # Arbitrary threshold for detection
                print(f"[ALERT] Potential ransomware detected! Rapid changes to {file_path}")


    def on_created(self,event):
        # This method will be triggered when a new file is created
        if not event.is_directory:
            print(f"File created: {event.src_path}")


    def on_deleted(self,event):
        # This method will be triggered when a file is deleted

        if not event.is_directory:
            print(f"File deleted: {event.src_path}")

if __name__ == "__main__":
    # Specify the directory that i want to monitor
    path = "D:\pyhtonpyhtonproject"

    event_handler = MyHandler()
    observer = Observer()

    # now here im scheduling the observer to monitor the specified path
    observer.schedule(event_handler,path, recursive=True)

    observer.start()

    try:
        # keep the script running
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        # Stop the observer when the script is interrupted  (eg, ctrl+c)
        observer.stop()

    observer.join()


# This function is for backup file incase if files are effected

def backup_file(file_path):
    backup_directory = 'D:\pyhtonpyhtonproject\backuppath'
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    try:
        shutil.copy(file_path, backup_directory)
        print(f"[ACtION] Backup created for {file_path} in {backup_directory}")
    except Exception as e:
        print(f"[ERROR] Failed to back up {file_path} {e}")



# This function is for alert email

def sen_email_alert(file_path, recipient=None):
    sender = "ankitsingh11162@gmail.com"
    recipeint = "ankitpal11122@gmail.com"

    subject = "crtical Alert: Ransomware Activity Detected"
    body = f"Supsicious ransomware-like behavior deteced for the file: {file_path}"

    msg = MIMEText(body)
    msg["subject"] = subject
    msg["From"] = sender
    msg["To"] = recipeint

    try:
        with smtplib.SMTP("ankitsingh11162@gmail.com", 587) as server:
            server.starttls()  # Secure connection
            server.login(sender, "your_email_password")
            server.sendmail(sender, [recipient], msg.as_string())
            print(f"[ALERT] Email sent to {recipient} for file: {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")




# dowbelow code represent uer interface using Tkinter

class RansomwareGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ransomware Detection System")

        # Create a text box to display logs
        self.log_box = ScrolledText(root, width=80, height=20)
        self.log_box.pack()

    def log_message(self, message):
        # Insert the log message into the text box
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)  # Scroll to the bottom

# Initialize Tkinter
root = tk.Tk()
gui = RansomwareGUI(root)
root.mainloop()