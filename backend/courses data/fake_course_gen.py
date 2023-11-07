# generates 8 fake CS courses for each student
# uses the 6k generated CS students from fake_cs_students.csv

import csv
import pandas as pd
from tqdm import tqdm
from random import sample

students = pd.read_csv('./backend/majors data/fake_cs_students.csv')
with open('./backend/courses data/cs_courses.csv', 'r') as file:
    file.readline()
    courses = [line.split(',')[0] for line in file.readlines()]

df = pd.DataFrame(columns=['Email', 'Course'])
for index, row in tqdm(students.iterrows()):
    transcript = sample(courses, 8)
    for course in transcript:
        df.loc[len(df)] = [row['Email'], course]

df.to_csv('./backend/courses data/fake_enrolls.csv', index=False)

