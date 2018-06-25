import urllib.request
import json
import re
from flask import Flask
from flask import url_for, render_template, request, redirect
req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=17283336&count=100&v=5.74&access_token=8423c2448423c2448423c244d08441f2a1884238423c244dee1644d9e90529494134bf8') 
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
data = json.loads(result)
polls = []
number = 0
numbers = []
for i in data['response']['items']:
    text = json.dumps(i)
    if 'poll' in text:
        text = json.loads(text)
        polls.append(text)
        number = number+1
        numbers.append(number)
#polls = json.dumps(polls)
#polls = json.loads(polls)
#print(polls)
#print(numbers)
polls_list = dict(zip(numbers, polls))

app = Flask(__name__)

@app.route('/poll')
def poll_template():
    polltext = polls_list [pollnumber]['text']
    innerpolltext = ['attachment']['poll']['question']
    answers = [pollnumber]['attachment']['poll']['answers']
    picture = [pollnumber]['attechment']['photo']
    return render_template ('poll_template.html',  text = polltext, innertext = innerpolltext, pollpicture = picture, answer = answers)

@app.route('/error')
def error:
    return '<html><body><p> Такого опроса нет </p></body></html>'

@app.route('/')
def poll_selection():
    if 1 < pollnumber < 29:
        return redirect(url_for('poll_template'))
    else:
        return redirect (url_for('error')
if __name__ == '__main__':
    app.run()

