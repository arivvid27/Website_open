import webbrowser
from time import sleep

while True: # This keeps the program going until you press 'q'
	user = input('''
~~~~~~WEBSITES~~~~~~
[G]oogle
[Gi]thub
[F]lat.io
[O]ffice 365
[C]anvas
[S]kyward
[T]eams
[Q]uit
>>> ''')	# This is what the user gets prompted. This is in charge of what website will open
	''' This will open websites according to the input '''
	if user == 'g':
		webbrowser.open('https://www.google.com/', new=0, autoraise=True)
	elif user == 'gi':
		webbrowser.open('https://github.com/', new=0, autoraise=True)
	elif user == 'f':
		webbrowser.open('https://flat.io/my-library', new=0, autoraise=True)
	elif user == 'o':
		webbrowser.open('https://www.office.com/?auth=2', new=0, autoraise=True)
	elif user == 'c':
		webbrowser.open('https://issaquah.instructure.com/', new=0, autoraise=True)
	elif user == 's':
		webbrowser.open('https://www01.nwrdc.wa-k12.net/scripts/cgiip.exe/WService=wissaqus71/fwemnu01.w', new=0, autoraise=True)
	elif user == 't':
		webbrowser.open('https://teams.microsoft.com/_?culture=en-us&country=US&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school/conversations/General?threadId=19:9e74feca54a646ff89094952c7af701e@thread.tacv2&ctx=channel', new=0, autoraise=True)
	elif user == 'q':
		break
	else:
		print('Please enter valid command')
		sleep(0.6)
