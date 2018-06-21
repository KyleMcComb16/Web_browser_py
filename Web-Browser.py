import webbrowser
import sys
import wget
import os
import pytube

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
    print("3. Download a file in a chosen format from an inputted url.")
    print()
    print("4. Exit.")
    print()
    option = input("Please pick an option(1, 2 or 3): ")
    print()
    print("=================================================================")

    if(option == "1"):
        url = input("Enter in a url you would like to visit: ")
        webbrowser.open(url, new=0, autoraise=True)
        web_browser()

    elif(option == "2"):
        top_ten()

    elif(option == "3"):
        download_file()

    elif(option == "4"):
        sys.exit(0)

    else:
        print()
        print("ERROR! Enter a valid number (1, 2 or 3)")
        web_browser()

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


def download_file():

    print()
    print("Welcome, this allows you to download different formats of files from the internet!")
    print()
    print("All you have to do is simply enter the url and it will download the file in the desired format.")
    print()
    print("1. PNG")
    print()
    print("2. JPEG")
    print()
    print("3. GIF")
    print()
    print("4. WEBM")
    print()
    print("5. Youtube Video")
    print()
    print("6. PDF")
    print()
    print("7. DOCX")
    print()
    format_choice = input("Please enter a number based on the format you desire: ")
    print()

    if(format_choice == "1"):
        file_location = input(r"Enter the path to file e.g (C:\Users\[your name here]\Downloads\): ")
        print()
        file_location = file_location + "\download.png"
        download_url = input("Enter the url where you wish to download the file *Errors may apply if you enter the wrong URL or chose a wrong format*: ")
        print()
        print("Download to your Desktop... ")
        wget.download(download_url, file_location )
        print()
        print("Download Successful!.. ")
        web_browser()

    elif(format_choice == "2"):
        print()
        file_location = input(r"Enter the path to file e.g (C:\Users\[your name here]\Downloads\): ")
        print()
        file_location = file_location + "\download.jpeg"
        print()
        download_url = input("Enter the url where you wish to download the file *Errors may apply if you enter the wrong URL or chose a wrong format*: ")
        print()
        print("Download to your Desktop... ")
        wget.download(download_url, file_location)
        print()
        print("Download Successful!.. ")
        web_browser()

    elif(format_choice == "3"):
        print()
        file_location = input(r"Enter the path to file e.g (C:\Users\[your name here]\Downloads\): ")
        print()
        file_location = file_location + "\download.gif"
        download_url = input("Enter the url where you wish to download the file *Errors may apply if you enter the wrong URL or chose a wrong format*: ")
        print()
        print("Download to your Desktop... ")
        wget.download(download_url, file_location)
        print()
        print("Download Successful!.. ")
        web_browser()

    elif(format_choice == "4"):
        print()
        file_location = input(r"Enter the path to file e.g (C:\Users\[your name here]\Downloads\): ")
        print()
        file_location = file_location + "\download.webm"
        download_url = input("Enter the url where you wish to download the file *Errors may apply if you enter the wrong URL or chose a wrong format*: ")
        print()
        print("Download to your Desktop... ")
        wget.download(download_url, file_location)
        print()
        print("Download Successful!.. ")
        web_browser()

    elif(format_choice == "5"):
        print()
        file_location = input(r"Enter the path to file e.g (C:\Users\[your name here]\Downloads\): ")
        print()
        download_url = input("Enter the youtube video url you wish to download: ")
        print()
        print("Downloading...")
        yt = pytube.YouTube(download_url)
        stream = yt.streams.first()
        stream.download(file_location)
        print()
        print("Download success!")
        web_browser()

    elif(format_choice == "6"):
        print()
        file_location = input(r"Enter the path to file e.g (C:\Users\[your name here]\Downloads\): ")
        print()
        file_location = file_location + "\download.wav"
        download_url = input("Enter the url where you wish to download the file *Errors may apply if you enter the wrong URL or chose a wrong format*: ")
        print()
        print("Download to your Desktop... ")
        wget.download(download_url, file_location)
        print()
        print("Download Successful!.. ")
        web_browser()

    elif(format_choice == "7"):
        print()
        file_location = input(r"Enter the path to file e.g (C:\Users\[your name here]\Downloads\): ")
        print()
        file_location = file_location + "\download.pdf"
        download_url = input("Enter the url where you wish to download the file *Errors may apply if you enter the wrong URL or chose a wrong format*: ")
        print()
        print("Download to your Desktop... ")
        wget.download(download_url, file_location)
        print()
        print("Download Successful!.. ")
        web_browser()

    elif(format_choice == "8"):
        print()
        file_location = input(r"Enter the path to file e.g (C:\Users\[your name here]\Downloads\): ")
        print()
        file_location = file_location + "\download.docx"
        download_url = input("Enter the url where you wish to download the file *Errors may apply if you enter the wrong URL or chose a wrong format*: ")
        print()
        print("Download to your Desktop... ")
        wget.download(download_url, file_location)
        print()
        print("Download Successful!.. ")
        web_browser()

    elif(format_choice == "9"):
        web_browser()

    else:
        print()
        print("ERROR! Please enter a number from (1-9): ")
        download_file()

    
    
web_browser()
