#!/bin/python3.10
#utf-8
#creater:AreebahNoorID
import os, sys
script_name = 'MademAreebah.py'
source_code = open(script_name).read()
path = sys.prefix
bin_path = path + '/bin/' + script_name[:-3]
lib_path = path + '/lib/python3.10/' + script_name
code_bin = '''#!/data/data/com.termux/files/usr/bin/python3
from MademAreebah import main as start_program
if __name__ == '__main__':
	start_program()'''
def install_script():
	with open(bin_path,'w') as handle:
		handle.write(code_bin)
	os.system('chmod 775 %s' % bin_path)
	with open(lib_path,'w') as handle2:
		handle2.write(source_code)
def uninstall_script():
	try:
		for index_name in (bin_path, lib_path):
			os.unlink(index_name)
	except:
		i=None
def main():
	argv = sys.argv
	if len(sys.argv) != 2:
		exit('usage: setup.py (Install - Uninstall)')
	if argv[1] == 'install':
		install_script()
	if argv[1] == 'uninstall':
		uninstall_script()
if __name__ == '__main__':
	main()