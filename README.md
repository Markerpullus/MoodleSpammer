# MoodleSpammer
A python script that spams moodle quizzes to give you higher grades🚀

## Data file format
```json
{
	"id": 2619,
	"pid": 8291,
	"sesskey": "PYTS6vu8QP",
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
			"tf_question": true
		}
	]
}
```
`id`: lesson id  
`pid`: page id of the first question of the quiz  
`sesskey`: moodle session key  
`answers.answer`: correct answer id  
`answers.tf_question`: is the question a t/f question  
