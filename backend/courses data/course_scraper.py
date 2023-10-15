# scrapes the course catalog for 2019 fall-2023 fallcourses
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import time

sleep_time = 1
courses = set()
for year in tqdm([2019, 2020, 2021, 2022, 2023]):
    for sem in ["fall", "spring"]:
        url = f'http://courses.illinois.edu/cisapp/explorer/catalog/{year}/{sem}.xml'
        request = requests.get(url)
        soup = BeautifulSoup(request.content, 'xml')
        subjects = [subject.attrs['id'] for subject in soup.find_all('subject')]
        for subject in tqdm(subjects):
            url = f'http://courses.illinois.edu/cisapp/explorer/catalog/{year}/{sem}/{subject}.xml'
            request = requests.get(url)
            soup = BeautifulSoup(request.content, 'xml')
            courses = courses.union(set([(subject, subject + course.attrs['id'], course.text) for course in soup.find_all('course')]))
            time.sleep(sleep_time)

courses = [[subject, course_num, course_name] for (subject, course_num, course_name) in courses]
fields = ['Subject', 'Course Number', 'Course Name']
with open('./backend/courses data/courses.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(fields)
    csv_writer.writerows(courses)

