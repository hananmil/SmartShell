from dotenv import load_dotenv
import os
import subprocess

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

load_dotenv('.env')

word_completer = WordCompleter(['command1', 'command2', 'command3'])
session = PromptSession()
cwd = os.getcwd()
cp = subprocess.Popen(['/bin/sh'],cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

def execute(command):
    try:
        # output = subprocess.run([command,'pwd'],cwd=cwd,capture_output=True,shell=True)
        output = cp.stdin.write(command.encode('utf-8'))
        cp.stfin.flush()
        output = cp.communicate()
        if (len(output.stdout) > 0):
            print(output.stdout.decode('utf-8'))
        if (len(output.stderr) > 0):
            print(output.stdout.decode('utf-8'))
        
        print(output.stderr.decode('utf-8'))
    except Exception as e:
        print(e)


while True:
    try:
        user_input = session.prompt('{}>'.format(cwd), completer=word_completer)
        execute(user_input)
    except KeyboardInterrupt:
        cp.kill()
        break
