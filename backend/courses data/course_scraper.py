# scrapes the course catalog for 2019 fall-2023 fallcourses
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import time

# grabs all fall and winter CS courses from 2019-2023
sleep_time = 1
def scrape():
    courses = dict()
    for year in tqdm([2019, 2020, 2021, 2022, 2023]):
        for sem in ["fall", "spring"]:
            url = f'http://courses.illinois.edu/cisapp/explorer/catalog/{year}/{sem}/CS.xml'
            request = requests.get(url)
            soup = BeautifulSoup(request.content, 'xml')
            for course in soup.find_all('course'):
                courses[course.attrs['id']] = course.text
            time.sleep(sleep_time)
    fields = ['Subject', 'Course Number', 'Course Name']
    with open('./backend/courses data/cs_courses.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(fields)
        for course, name in courses.items():
            csv_writer.writerow(['CS', 'CS ' + course, name])

if __name__ == '__main__':
    scrape()
