import pathlib 

def checkMessage(text):
    if not '{sender}' in text:
        raise Exception('Error! Missing {sender} in message file')
    if not '{receiver}' in text:
        raise Exception('Error! Missing {receiver} in message file')
    

def getMessage( messagefile):
    path = pathlib.Path(messagefile)
    if not path.is_file( messagefile ): 
        raise Exception('Error! {} is not a valid file!'.format(messagefile))
    text = path.open('r').read()
    checkMessage(text)
    return text 
    
