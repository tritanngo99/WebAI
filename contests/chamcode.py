from subprocess import *
import subprocess

def runPy(file):
	s = check_output("python3 "+file,shell=True)
	return str(s.decode("UTF-8"))
def runC(file):
	s = check_output("gcc "+file+" -o "+"out1" + ";./out1",shell=True)
	return str(s.decode("UTF-8"))
def runCpp(file):
	s = check_output("g++ "+file+" -o "+"out1" + ";./out1",shell=True)
	return str(s.decode("UTF-8"))
def runJava(file):
	s = check_output("javac "+file + ";java "+file,shell = True)
	return str(s.decode("UTF-8"))

def solve(file_name):
	result_answer = ""
	if(file_name.endswith("py")):
		result_answer = runPy(file_name)
	elif(file_name.endswith("c")):
		result_answer = runC(file_name)
	elif(file_name.endswith("cpp")):
		result_answer = runCpp(file_name)
	elif(file_name.endswith("java")):
		result_answer = runJava(file_name)
	return result_answer