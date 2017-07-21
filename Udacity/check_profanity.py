import urllib.request as ur

def read_text():
   quotes= open("G:\Python\movie_quotes.txt")
   content=quotes.read()
   print(content)
   quotes.close()
   check_prof(content)

def check_prof(text_to_check):

    try:
        connection = ur.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
        output = connection.read()
        print(output)
        connection.close()
        if "true" in output:
            print("Alert!! cursed words found in your document")
        elif "false" in output:
            print("There are no cursed word in your document")

            

    except:
        print("an error occured ")
        return

read_text()