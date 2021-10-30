import pathlib 



def checkMessage(text): 
#check that the message skeleton has a {sender} and a {receiver} string inside of it, so it can be used with format later on
    if not '{sender}' in text:
        raise Exception('Error! Missing {sender} in message file')
    if not '{receiver}' in text:
        raise Exception('Error! Missing {receiver} in message file')
    

def getMessage( messagefile):
#given a message file, check that it is a good message, and returns the text.
    path = pathlib.Path(messagefile)
    if not path.is_file():  #check if file actually exists
        raise Exception('Error! {} is not a valid file!'.format(messagefile))
    text = path.open('r').read()
    checkMessage(text)
    return text 
    
