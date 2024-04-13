import subprocess
import pathlib
import os

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
print(SCRIPT_DIR)

os.chdir(f'{SCRIPT_DIR}/src')
return_code = subprocess.run(f'yes | cp {SCRIPT_DIR}/vendor/Awesome-CV/examples/awesome-cv.cls {SCRIPT_DIR}/src', shell=True)
return_code = subprocess.run([f'xelatex -output-directory={SCRIPT_DIR}/build resume.tex'], shell=True) 

