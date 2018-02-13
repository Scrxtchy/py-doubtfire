import requests

class Doubtfire:
	def __init__(self, username, password):
		api(username, password)
		self.courses = self.getCourses()
		self.request = api.tt

	def getCourses(self):
		ret = []
		for course in api.tt.get('https://doubtfire.ict.swin.edu.au/api/projects').json():
			ret.append(Course(course))
		return ret


class Course:
	def __init__(self, data):
		self.unit_id = data['unit_id']
		self.project_id = data['project_id']
		self.tutor_name = data['tutor_name']
		self.unit_name = data['unit_name']
		self.target_grade = data['target_grade']
		self.has_portfolio = data['has_portfolio']
		self.unit_code = data['unit_code']
		self.start_date = data['start_date']
		self.tasks = self.getTasks()

	def getTasks(self):
		ret = []
		for task in api.tt.get('https://doubtfire.ict.swin.edu.au/api/units/' + str(self.unit_id)).json()['task_definitions']:
			ret.append(Task(task))
		return ret

class Task:
	def __init__(self, data):
		self.id = data['id']
		self.abbreviation = data['abbreviation']
		self.name = data['name']
		self.description = data['description']
		self.weight = data['weight']
		self.target_grade = data['target_grade']
		self.target_date = data['target_date']
		self.upload_requirements = data['upload_requirements']
		self.plagiarism_checks = data['plagiarism_checks']
		self.plagiarism_report_url = data['plagiarism_report_url']
		self.plagiarism_warn_pct = data['plagiarism_warn_pct']
		self.restrict_status_updates = data['restrict_status_updates']
		self.group_set_id = data['group_set_id']
		self.has_task_pdf = data['has_task_pdf']
		self.has_task_resources = data['has_task_resources']
		self.due_date = data['due_date']
		self.start_date = data['start_date']
		self.is_graded = data['is_graded']
		self.max_quality_pts = data['max_quality_pts']



class api:
	tt = requests.session()
	def __init__(self, username, password):
		login = api.tt.post('https://doubtfire.ict.swin.edu.au/api/auth', params={'username': username, 'password': password, 'remember': True}).json()
		try:
			api.tt.params.update({'auth_token': login['auth_token']})
		except KeyError:
			print("Login Failed, probably a bad password. Any key to quit")
			from msvcrt import getch
			getch()
			from sys import exit
			exit(0)