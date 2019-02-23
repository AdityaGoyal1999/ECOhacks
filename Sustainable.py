import webbrowser
import random


print("Launching...\n")
print("Find something sustainable today!\nEnter a search term, as you normally "
      "would on Google. We'll find you sustainable alternatives.\n")
keyword = input("Search for something.")

google = "https://google.com/"
syntax = "search?q="
path = "ECOhacks/keywords - Sheet1.csv"

sustainable_list = []
with open(path) as file:
    sustainable_list = file.readlines()

sust = sustainable_list[random.randrange(0, len(sustainable_list))]

webbrowser.open_new(google + syntax + sust + '+' + keyword)
