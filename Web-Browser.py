import webbrowser
import sys

#This is a python program which takes the url a user has inputted and opens it in a browser.
#The module I am using is "webbrowser" - Here is the link to read the documentation: https://docs.python.org/3.1/library/webbrowser.html

def web_browser():

    print()
    print("=================================================================")
    print()
    print("Welcome to Kyle's Web Browser!")
    print()
    print("You have two options.")
    print()
    print("1. Enter a custom url to visit.")
    print()
    print("2. Pick from the top ten most visited websites(Facebook, Youtube etc).")
    print()
    option = input("Please pick an option(1 or 2): ")
    print()
    print("=================================================================")

    if(option == "1"):
        url = input("Enter in a url you would like to visit: ")
        webbrowser.open(url, new=0, autoraise=True)
        web_browser()

    elif(option == "2"):
        top_ten()

def top_ten():
    print("Welcome to the top ten most viewed websites!")
    print()
    print("1. Google")
    print("2. Youtube")
    print("3. Facebook")
    print("4. Wikipedia")
    print("5. Reddit")
    print("6. Yahoo!")
    print("7. Amazon")
    print("8. Twitter")
    print("9. Instagram")
    print("10. Netflix")
    print()
    print("11. Github - Where I've uploaded this")
    print()
    print("12. Return back to Kyle's Web Browser.")
    print()

    website_choice = input("Please select a number based on the website you would like to vist(1-10): ")

    if(website_choice == "1"):
        webbrowser.open("https://www.google.com/", new=0, autoraise=True)
        top_ten()

    elif(website_choice == "2"):
        webbrowser.open("https://www.youtube.com/", new=0, autoraise=True)
        top_ten()

    elif(website_choice == "3"):
        webbrowser.open("https://www.facebook.com/", new=0, autoraise=True)
        top_ten()

    elif(website_choice == "4"):
        webbrowser.open("https://en.wikipedia.org/wiki/Main_Page", new=0, autoraise=True)
        top_ten()

    elif(website_choice == "5"):
        webbrowser.open("https://www.reddit.com/", new=0, autoraise=True)
        top_ten()

    elif(website_choice == "6"):
        webbrowser.open("https://uk.yahoo.com/", new=0, autoraise=True)
        top_ten()

    elif(website_choice == "7"):
        webbrowser.open("https://www.amazon.co.uk/", new=0, autoraise=True)
        top_ten()

    elif(website_choice == "8"):
        webbrowser.open("https://twitter.com/", new=0, autoraise=True)
        top_ten()

    elif(website_choice == "9"):
        webbrowser.open("https://www.instagram.com/?hl=en", new=0, autoraise=True)
        top_ten()

    elif(website_choice == "10"):
        webbrowser.open("https://www.netflix.com/browse", new=0, autoraise=True)
        top_ten()

    elif(website_choice == "11"):
        webbrowser.open("https://github.com/KyleMcComb16/Web_browser_py", new=0, autoraise=True)

    elif(website_choice == "12"):
        web_browser()

    else:
        print()
        print("ERROR! You have not entered a correct option (1-11 only!)")
        top_ten()
    
web_browser()
#url = input("Please enter a url you would like to visit: ")
#webbrowser.open(url, new=0, autoraise=True)
