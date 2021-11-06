from dotenv import load_dotenv
import os 

load_dotenv()

def __getEnvVariable( varName ):    
    #just check if an environment variable exist
    varValue = os.getenv( varName )
    if varValue is None:
        raise Exception(f'{varName} not present in .env file')
    return varValue


SANTA_MAIL =  __getEnvVariable('SANTA_MAIL')
SANTA_PASS =  __getEnvVariable('SANTA_PASSWORD')

