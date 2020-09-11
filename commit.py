import subprocess as cmd
import time
from datetime import datetime



def updateGithub():
    while True:
        
        cmd.run("git add data", check=True, shell=True)
        cmd.run(f"git commit -m 'data'", check=True, shell=True)
        cmd.run("git push origin master", check=True, shell=True)
        now = datetime.now()
        print('completed commit: ', now)
        time.sleep(600)


updateGithub()
