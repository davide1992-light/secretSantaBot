import pathlib 

def checkMessage(text, addressFlag): 
#check that the message skeleton has a {sender} and a {receiver} string inside of it, so it can be used with format later on
    if not '{sender}' in text:
        raise Exception('Error! Missing {sender} in message file')
    if not '{receiver}' in text:
        raise Exception('Error! Missing {receiver} in message file')
    if addressFlag and (not '{address}' in text):
        raise Exception('Error! When using --address a {address} flag must be present in message file.')
    
    

def getMessage( messagefile, addressFlag=False):
#given a message file, check that it is a good message, and returns the text.
    path = pathlib.Path(messagefile)
    if not path.is_file():  #check if file actually exists
        raise Exception('Error! {} is not a valid file!'.format(messagefile))
    text = path.open('r').read()
    checkMessage(text, addressFlag)
    return text 
    
