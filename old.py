import webbrowser
# by abdullah for nostalgia 

# 



firstdate = input("which year you want to begin with :")
lastdate = input("which year you want to end with :")
whichvid = input("which videos you want to watch :")

linkk = "https://www.google.com/search?q=site%3Ayoutube.com+"+whichvid+"&biw=1920&bih=979&tbs=cdr%3A1%2Ccd_min%3A1%2F2%2F"+firstdate+"%2Ccd_max%3A12%2F31%2F"+lastdate+"&tbm=vid&sxsrf=AOaemvL7rf7n5ZyhcegntmcsQ9MT_0UulQ%3A1642950219253&ei=S27tYemPD5OcUrCHldAK&ved=0ahUKEwip4c7Bksj1AhUTjhQKHbBDBaoQ4dUDCA0&uact=5&oq=site%3Ayoutube.com"
webbrowser.open(linkk)





question = input("does it work? use Y or N, like a linux chad:   ")
if question == ("Y"):
    print("ok goodbye")
elif question == ("N"):
    print(linkk)
else: 
    print("peasent lmao")

