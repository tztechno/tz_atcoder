####################################################

d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
print(d.get('key1'))
# val1
print(d.get('key4'))
# None

####################################################

class_names = ['paper', 'rock', 'scissors']
N = list(range(len(class_names)))
normal_mapping = dict(zip(class_names, N)) 
reverse_mapping = dict(zip(N, class_names))    

####################################################

FACT = {2: 3, 3: 1, 5: 2}
i = 3
count = FACT.get(i, 0)
print(count)
#iある時値を取り出す、iない時0を返す

####################################################
