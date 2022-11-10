# Copyright (C) 2022  Emma Lynn
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, version 3 of the License.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

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