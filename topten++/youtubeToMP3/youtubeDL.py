import youtube_dl
from subprocess import call
def main():
	command = " youtube-dl  R7BRWyn4PzY -x --audio-format mp3 -o %(title)s.(ext)s "
	call(command.split(), shell=False)
main()