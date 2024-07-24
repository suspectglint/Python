#Dictionaries
#key-value pair

pupil = {'name':'Sravan','age':21,'Phone':'+91-9666754863'}
print(pupil)
print(pupil['name'])
print(pupil.get('Phone'))
pupil.update({'Roll No':'U16CO071'})
print(pupil)
print(len(pupil))
for key in pupil:
  print(key)
for key, value in pupil.items():
  print(key,value)
del pupil['Roll No']
print(pupil) 
#print(dir(dict))
