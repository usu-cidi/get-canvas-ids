import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
SOURCE = os.environ.get('SOURCE_FILE')
BASEURL = 'https://usu.instructure.com'
information = ""

f = open(SOURCE, 'r')
aNumbers = f.readlines()


for aNumber in aNumbers:
    if (not aNumber == "") and (aNumber[-1] == "\n"):
        aNumber = aNumber[:-1]
    if (not aNumber == "") and (aNumber[0] == "<feff>"):
        aNumber = aNumber[0:]
    requestURL = BASEURL + "/api/v1/users/sis_login_id:" + aNumber
    shellCommand = f"curl {requestURL} -H 'Authorization: Bearer {TOKEN}'"

    fromShell = os.popen(shellCommand)

    parsedInfo = fromShell.read()
    fromShell.close()
    information += parsedInfo + "\n"

f = open("canvasData9170565.txt", "w")
f.write(information)
f.close()

def getInfo():
    return information