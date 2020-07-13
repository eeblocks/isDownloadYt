import pytube
from colorama import init
init()
from colorama import Fore

print(Fore.YELLOW+'Welcome to isDownloadYt!')
print(Fore.WHITE+'------------------------')
url = input('Please Enter the URL from the YouTube video: ')
path = input('Then Enter the path where you want to download the video: ')

video = pytube.YouTube(url)
youtube = video.streams.first()

if (youtube.download(path)):
	print(Fore.GREEN+'Your video has been successfully downloaded :)')
else:
	print(Fore.RED+'Your video cannot be downloaded by a BUG. (Check the problems.txt file)')