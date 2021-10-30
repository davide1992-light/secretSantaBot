import json
import pathlib


def validateJSON(jsonFile):
    #check if the input file is a valid JSON file 
    try:
        json.load(jsonFile)
    except ValueError as err:
        return False
    return True   
    

def getJSONdata(jsonFilepath):
    #given the path to a file, returns the json data
    
    Filepath = pathlib.Path(jsonFilepath)
    if not Filepath.is_file():  #if the path do not correspond to existing file, raise error
        raise Exception('Error! File {} does not exist'.format(jsonFilepath))

    if not validateJSON( Filepath.open('r') ):
        raise Exception('Error! File {} is not a valid JSON file!'.format(jsonFilepath) )
    data = json.load( Filepath.open('r') )
    
    Users = set(data.keys()) 
    if not all( 'mail' in data[user] for user in Users):        #all the people present in the JSON must have a "mail" attribute
        raise Exception('Some people do not have a corresponding email')
    for user in Users:
        if not 'previousSanta' in data[user]:           #if a previous santa is not define for a user, it is set to the default value ''
            data[user]['previousSanta'] = ''
    
    previousSantas = set( data[user]['previousSanta'] for user in Users if data[user]['previousSanta'] != '' )
    if not previousSantas.issubset(Users):                  #check that the previous santas correspond to actual users of the secret santa
        raise Exception('There are unknown previous-santas in the json file')
    
    return data
    
    
    
