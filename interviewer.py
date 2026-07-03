questions={
 'What is Python?':['language','programming'],
 'What is AI?':['machine','intelligence'],
 'What is OOP?':['object','class']
}
score=0
for q,keys in questions.items():
 ans=input(q+' ').lower()
 if any(k in ans for k in keys):
  score+=1
print('Score:',score,'/',len(questions))
if score==3:
 print('Excellent')
elif score==2:
 print('Good')
else:
 print('Needs Improvement')
 