import json
import pathlib


def validateJSON(jsonFile):
    try:
        json.load(jsonFile)
    except ValueError as err:
        return False
    return True   
    

def getJSONdata(jsonFilepath):
    Filepath = pathlib.Path(jsonFilepath)
    if not Filepath.is_file():
        raise Exception('Error! File {} does not exist'.format(jsonFilepath))

    if not validateJSON( Filepath.open('r') ):
        raise Exception('Error! File {} is not a valid JSON file!'.format(jsonFilepath) )
    data = json.load( Filepath.open('r') )
    
    Users = set(data.keys()) 
    if not all( 'mail' in data[user] for user in Users):
        raise Exception('Some people do not have a corresponding email')
    for user in Users:
        if not 'previousSanta' in data[user]:
            data[user]['previousSanta'] = ''
    
    previousSantas = set( data[user]['previousSanta'] for user in Users if data[user]['previousSanta'] != '' )
    if not previousSantas.issubset(Users):
        raise Exception('There are unknown previous-santas in the json file')
    
    return data
    
    
    
