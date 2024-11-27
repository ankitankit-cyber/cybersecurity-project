Ransomware Detection System
Project Description
This project is a Ransomware Detection System designed to monitor file system events in real-time, detect potential ransomware activity, and provide mitigation strategies such as backup creation and alert notifications via email. The system combines file monitoring, ransomware-like behavior detection, and a user-friendly graphical interface to provide an effective solution against ransomware threats.

Features
File System Monitoring:

Monitors a specified directory for file creations, modifications, and deletions.
Logs all changes in the monitored directory.

Ransomware Detection:
Detects potential ransomware activity based on rapid file modifications.
Issues alerts for suspicious activities, indicating a possible ransomware threat.

Backup Mechanism:
Automatically creates backups of files when suspicious behavior is detected.
Email Alert System:

Sends email notifications to a designated recipient when ransomware activity is detected.

Graphical User Interface:
A Tkinter-based GUI displays logs in real-time, making the system user-friendly.

How It Works
File Monitoring:
Uses the watchdog library to track changes in the file system.
Detects file creation, modification, and deletion events.

Ransomware Detection:
Analyzes the frequency of file modifications. If a file is modified more than a defined threshold (e.g., 5 times within a short period), it is flagged as suspicious.

Backup and Alerts:
Automatically backs up the flagged files to a secure directory.
Sends an email alert to notify the user of potential ransomware activity.

User Interface:
Logs all file system activities in a scrollable text box.
Allows users to view alerts and logs in a visually accessible format.

Project Structure
MyHandler Class:
Handles file system events (creation, modification, deletion).
Implements ransomware detection logic.

Backup and Alert Functions:
backup_file: Creates backups of suspicious files.
send_email_alert: Sends email alerts for flagged files.

Tkinter GUI:
Displays logs and system activities in real-time.

Prerequisites
Python 3.x
Required libraries:
watchdog
tkinter
smtplib
email
time
os
shutil

Install dependencies using:
bash
Copy code
pip install watchdog
Usage
Setup:
Update the path variable with the directory you want to monitor.
Replace placeholder email details (sender, recipient, email server, password) in the send_email_alert function.

Run the System:
Execute the script:
bash
Copy code
python ransomware_detection.py
The system will monitor the specified directory and log events.

Interface:
Use the Tkinter GUI to view logs in real-time.
Stop the System:

Press Ctrl+C to terminate the script safely.
Future Improvements
Customizable Threshold:

Allow users to adjust the threshold for ransomware detection.

Encryption Support:
Add file encryption/decryption to further secure backups.

Multi-Folder Monitoring:
Extend the system to monitor multiple directories simultaneously.
