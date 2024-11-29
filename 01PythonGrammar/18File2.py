import pickle

name = '종각'
age = 99
address = '서울시 종로구 관철동'
times = {'JAVA' : 20, 'HTML' : 2, 'Oracle' : 10, 'Python' : 3}

with open('./saveFiles/jong-ro.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(times, file)

with open('./saveFiles/jong-ro.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    times = pickle.load(file)
    
    print("이름", name)
    print("나이", age)
    print("주소", address)
    print("배당시간", times)