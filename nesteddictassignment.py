#list
data = ['Amaka disappoint', 'Nedu japan', 'Pretty cynthia', 'Nedu japan', 'Pretty cynthia', 'Pretty cynthia']
print(type(data))

#convert tuple to list
mytuple = ('jon doe', 'john doe', 'john doe', 'jon bellion', 'jon bellion', 'john bellcat', 'jon doe')
designer = list(mytuple)
print(designer)

#convert set to list
myset = {'ada ada', 'pyhon ezege', 'dog catcher', 'bitrus beetroot', 'doja cat', 'beja rat'}
backend = list(myset)
print(backend)

#join list
data = ['Amaka disappoint', 'Nedu japan', 'Pretty cynthia', 'Nedu japan', 'Pretty cynthia', 'Pretty cynthia']
designer = ['jon doe', 'john doe', 'john doe', 'jon bellion', 'jon bellion', 'john bellcat', 'jon doe']
backend = ['pyhon ezege', 'dog catcher', 'bitrus beetroot', 'beja rat', 'doja cat', 'ada ada']
mystudent = list(set(data + designer + backend))
print(mystudent)

#create nested dictionary
tracks = {
'Data': ['Amaka disappoint', 'Nedu japan', 'Pretty cynthia', 'Nedu japan', 'Pretty cynthia', 'Pretty cynthia'],
'Designer': ['jon doe', 'john doe', 'john doe', 'jon bellion', 'jon bellion', 'john bellcat', 'jon doe'],
'Backend': ['ada ada', 'pyhon ezege', 'dog catcher', 'bitrus beetroot', 'doja cat', 'beja rat']}
students = {}
for key, value in tracks.items():
    students[key] = {'names': list(set(value))}
print(students)


#score keys
def test(keys, values):
    return dict(zip(keys, values))
scores = [{'Data': ['Nedu japan', 80, 'Amaka disappoint', 90, 'Pretty cynthia', 75]},
{'Designer': ['jon bellion', 85, 'jon doe', 60, 'john bellcat', 75, 'john doe', 80]},
{'Backend': ['pyhon ezege', 80, 'dog catcher', 70, 'doja cat', 60, 'ada ada', 75, 'beja rat', 80, 'bitrus beetroot', 60]}
          ]
print(scores)

#top student for each track
scores = [{'Data': ['Nedu japan', 80, 'Amaka disappoint', 90, 'Pretty cynthia', 75]},
{'Designer': ['jon bellion', 85, 'jon doe', 60, 'john bellcat', 75, 'john doe', 80]},
{'Backend': ['pyhon ezege', 80, 'dog catcher', 70, 'doja cat', 60, 'ada ada', 75, 'beja rat', 80, 'bitrus beetroot', 60]}]
#print original dictionary
print('scores : ' + str(scores))
#max value in neste dictonary
#using max() + dictionary comprehension
res = {key: max(val.values()) for key, val in scores.items()}
#print result
print('Top student : '+ str(res))
