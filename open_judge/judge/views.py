from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from django.views.decorators.csrf import csrf_exempt
import json
import random
import subprocess

path = Path(__file__).resolve().parent.parent
SUBMISSION_DIR = path/'submissions'
QUESTIONS_DIR = '../questions/1/statement'
wrap_map = None

#An endpoint to display the code editor to user
def workspace(request):
    return render(request, "judge/workspace.html", context={'d_path': QUESTIONS_DIR})

#It is used to generate the command need to run the code
def new_attempt(answer, language):
    f_name = SUBMISSION_DIR/f'{random.randint(1,100_00_00)}.py'
    with open(f_name, 'w') as code_file:
        code_file.write(answer)
    with open(path/'wrapper.json' , "r") as w:
        wrapper = json.load(w)
        cmd = wrapper[language].format(code_file=f_name)
        process = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        print(stderr, stdout)
        return (stderr, stdout)

@csrf_exempt
def handler(request):
    answer = request.POST['code']
    language = request.POST['language']
    output = new_attempt(answer, language)
    return HttpResponse(output)
