import subprocess
import databaseConnection
import constants


def executeCommand(command):
    try:
        output = subprocess.Popen(command,stdout=subprocess.PIPE)
        return output
    except:
        return {}


def synthesize_command(command,options,input):
    fulltext=""
    for option in options:
        fulltext += " -"
        fulltext += option

    for variable in input:
        fulltext += variable

    return fulltext     

