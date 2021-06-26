# MoodleSpammer
A python script that spams moodle quizzes to give you higher grades🚀

## Data file format
```json
{
	"id": 2619,
	"pid": 8291,
	"sesskey": "PYTS6vu8QP",
	"moodlesessionid": "fb330d1c8642f7ec50c3bbabc0fb379c",
	"answers": [
		{
			"answer": 18979,
			"tf_question": false
		},
		{
			"answer": 18983,
			"tf_question": false
		},
		{
			"answer": 18987,
			"tf_question": true
		},
		{
			"answer": 18978,
			"tf_question": false
		}
	]
}
```
`id`: lesson id  
`pid`: page id of the first question of the quiz  
`moodlesessionid`: moodle session id cookie
`sesskey`: moodle session key  
`answers.answer`: correct answer id  
`answers.tf_question`: is the question a t/f question  

## How to find data required
![image](https://user-images.githubusercontent.com/69721002/123500197-49234f80-d60a-11eb-8064-4f2bacede12e.png)
* Answer the first question of the quiz while opening network tab on inspect  
* Find `continue.php`, go down to form data, and you will find lesson id, pageid, sesskey, and answerid  
* Keep answering the questions and record the correct answer ids and if it is a t/f question  
* Go to application tab and find the moodle session id cookie  
__The moodle session cookie name may vary across different moodle courses, in my case it is MoodleSessionipe1__
