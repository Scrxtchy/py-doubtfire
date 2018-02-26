import doubtfire
from os import getcwd, path, makedirs
from getpass import getpass



df = doubtfire.Doubtfire(input('Username: '), getpass('Password: '))

print('\nPick a unit to download:')
for course in df.courses:
	print("{0} - {1} [{2}]".format(course.unit_id, course.unit_name, course.tutor_name))


downloadCourse = int(input('\n# Select: '))
print

def DownloadFile(url, filename):
	file = df.request.get(url, stream=True)
	file.raise_for_status()
	downloaded = 0
	
	with open(getcwd() + filename, 'wb') as handle:
		for block in file.iter_content(1024):
			downloaded = downloaded + len(block)
			handle.write(block)
	print('downloaded file: ' + filename)

for course in df.courses:
	if course.unit_id == downloadCourse:
		if not path.exists(getcwd() + '\\' +str(course.unit_code)):
			makedirs(getcwd() + '\\' + str(course.unit_code))
		for task in course.tasks:
			if task.has_task_pdf is True:
				DownloadFile('https://doubtfire.ict.swin.edu.au/api/units/{0}/task_definitions/{1}/task_pdf.json'.format(course.unit_id, task.id), '\\{0}\\{1}.pdf'.format(course.unit_code, task.abbreviation))
			if task.has_task_resources is True:
				DownloadFile('https://doubtfire.ict.swin.edu.au/api/units/{0}/task_definitions/{1}/task_resources.json'.format(course.unit_id, task.id), '\\{0}\\{1}resources.zip'.format(course.unit_code, task.abbreviation))
