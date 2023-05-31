import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) #Авто резет нужен что бы параметры текста не передались на следующую строку

print(Fore.GREEN + 'Green text')
print(Back.BLACK + 'Black background')
print(Style.BRIGHT + 'Slightly brighter text')
print(Fore.GREEN + Back.BLACK + Style.BRIGHT + 'Mixed text')
print('Normal text')