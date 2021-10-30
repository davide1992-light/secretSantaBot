from dotenv import load_dotenv
import os 

load_dotenv()

def __getEnvVariable( varName ):
    varValue = os.getenv( varName )
    if varValue is None:
        raise Exception(f'{varName} not present in .env file')
    return varValue


SANTA_MAIL =  __getEnvVariable('SANTA_MAIL')
SANTA_PASS =  __getEnvVariable('SANTA_PASSWORD')
IMAP_SERVER = __getEnvVariable('IMAP_SERVER')
SMTP_SERVER = __getEnvVariable('SMTP_SERVER')
SMTP_PORT =   __getEnvVariable('SMTP_PORT')


