import webbrowser
print("Follow Ifeanyi on GitHub?")
choice=input("(yes(1)/no(2)): ")
if choice == '1':
    webbrowser.open("https://github.com/CoderIfeanyi")
else:
    activity=input("\nWhat would you like to open:\nGoogle(1):\nYoutube(2):\nGitHub(3):\nCalculator(4):\nMusic(5):\nSpeech Recognition(6):\n ")
if activity == '1':
               webbrowser.open("https://google.com")
if activity == '2':
    webbrowser.open("https://www.youtube.com/")

if activity == '3':
    webbrowser.open("https://github.com/")

if activity == '4':
    webbrowser.open("https://www.online-calculator.com/full-screen-calculator/")

if activity == '5':
    webbrowser.open("https://open.spotify.com/")

