import requests, time, urllib3, json, argparse

parser = argparse.ArgumentParser(description="Spam Moodle Quizzes")
parser.add_argument("-a", required=True, dest="attempts")
parser.add_argument("-d", required=True, dest="data_file", help="Quiz data json file")
args = parser.parse_args()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def _end(s, id, sesskey):
	url = "https://ipe1.moodle.school/mod/lesson/view.php"
	p = {"id": id, "pageid": "-9", "sesskey": sesskey}
	s.post(url, data=p, verify=False)

def _continue(s, id, pid, sesskey, is_tf, ansid):
	if is_tf:
		p = {"id": id, "pageid": pid, "sesskey": sesskey, 
		"_qf__lesson_display_answer_form_truefalse": "1", "answerid": ansid,
		"submitbutton": "Submit"}
	else:
		p = {"id": id, "pageid": pid, "sesskey": sesskey, 
		"_qf__lesson_display_answer_form_multichoice_singleanswer": "1", "answerid": ansid,
		"submitbutton": "Submit"}
	url = "https://ipe1.moodle.school/mod/lesson/continue.php"
	r = s.post(url, data=p, verify=False)
	if "That's right" in r.text:
		print("Correct")

s = requests.Session()
s.cookies.set("MoodleSessionipe1", "d341af4751c62446c9fc07b93ebfe1a8")
s.headers.update({"Content-Type": "application/x-www-form-urlencoded",
	"Upgrade-Insecure-Requests": "1",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-User": "?1",
	"Sec-Fetch-Dest": "document"})

#s.proxies.update({"https": "http://127.0.0.1:8080"})

attempts = int(args.attempts)

f = open(args.data_file)
data = json.load(f)
id = str(data["id"])
pid = str(data["pid"])
sesskey = str(data["sesskey"])
answers = []
for ans in data["answers"]:
	answers.append([str(ans["answer"]), ans["tf_question"]])

for i in range(attempts):
	tmp = pid
	print(f"Attempts: {i+1}")
	for ans in answers:
		_continue(s, id, pid, sesskey, ans[1], ans[0])
		pid = str(int(pid) + 1)
	_end(s, id, sesskey)
	pid = tmp
	time.sleep(1)