import pandas as pd
import matplotlib.pyplot as plt
import json


df = pd.read_csv("full_victims.csv")


#creating the txt file
num = df[df['age']<23]['age'].count()
names=df['name'].tolist()
job=df['job'].tolist()
l1= zip(names,job)
l1= set(l1)

with open('results.txt','w') as f:
    f.write(f'{num} that died were under 25\n\n\n')

    f.write(f'victims \n')
    for i in l1:
        f.write(f'{i[0]} : {i[1]}\n\n')


    




ages= df['age'].value_counts().sort_index()
jobs=df['job'].value_counts().sort_index()
ages_dict = ages.to_dict()
jobs_dict = jobs.to_dict()




#creating the json file
with open('people.json','w') as f:
    json.dump({'ages':ages_dict, 'jobs':jobs_dict},f,indent=4)
    




#creating the images
ages = ages.sort_values(ascending=False)
ages.plot(kind='bar')
plt.xlabel('number of people')
plt.ylabel('age')
plt.title('Number of People per age')
plt.savefig('age-people.png')
plt.show()


jobs.sort_values( ascending=False)
jobs.plot(kind='bar')
plt.xlabel('job')
plt.ylabel('number of workers')
plt.title('Number of People per job')
plt.savefig('jobs-people.png')
plt.show()

