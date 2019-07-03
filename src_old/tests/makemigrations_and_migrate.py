import os

def makemigrations_and_migrate(project_root, this_dir, commands):
	print(project_root)

	os.chdir(project_root)


	for command in commands:
		ret = os.system(command)
		if ret:
			print('Failed - (' + command + ')')

	print('I am in ', os.getcwd())
	os.chdir(this_dir)
	print('Now, I\'m in', os.getcwd())
