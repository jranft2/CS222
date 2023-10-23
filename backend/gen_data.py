import pandas as pd
import random
from tqdm import tqdm # progress bar

with open('./backend/majors data/undergrad_cs.txt') as file:
    ug_cs = [line.rstrip() for line in file]

with open('backend/majors data/undergrad_majors.txt') as file:
    ug_majors = [line.rstrip() for line in file]

with open('backend/majors data/grad_cs.txt') as file:
    g_cs = [line.rstrip() for line in file]

with open('backend/majors data/grad_majors.txt') as file:
    g_majors = [line.rstrip() for line in file]

"""
generates 55K fake students (35K undergrads, 20K grads), each with their own:
    -name ('Johnny Test{i}' for i in [1, 44K])
    -email ('jt{i}@illinois.edu for i in [1, 44k])
    -major
roughly reflecting UIUC's student demographic:
4K undergrad CS or related majors
2K graduate CS or related majors

output: a CSV file containing student info
"""
def gen_data() -> pd.DataFrame:
    df = gen_cs_data()

    # generates 31K undergrad non-CS majors
    for i in tqdm(range(6000, 37000)):
        student = {
            'Name': f'Johnny Test{i}',
            'Email': f'jt{i}@illinois.edu',
            'Major': random.choice(ug_majors)
        }
        df.loc[len(df)] = student
    
    # generates 18K graduate non-CS majors
    for i in tqdm(range(37000, 55000)):
        student = {
            'Name': f'Johnny Test{i}',
            'Email': f'jt{i}@illinois.edu',
            'Major': random.choice(g_majors)
        }
        df.loc[len(df)] = student
    
    return df

"""
generates 6K fake CS students (4K undergrads, 2K grads), each with their own:
    -name ('Johnny Test{i}' for i in [1, 44K])
    -email ('jt{i}@illinois.edu for i in [1, 44k])
    -major
roughly reflecting UIUC's CS students demographic

output: a CSV file containing CS student info
"""
def gen_cs_data() -> pd.DataFrame:
    df = pd.DataFrame(columns=['Name', 'Email', 'Major'])

    # generates 4K undergrad CS majors
    for i in tqdm(range(4000)):
        student = {
            'Name': f'Johnny Test{i}',
            'Email': f'jt{i}@illinois.edu',
            'Major': random.choice(ug_cs)
        }
        df.loc[len(df)] = student
    
    #generates 2K grad CS majors
    for i in tqdm(range(4000, 6000)):
        student = {
            'Name': f'Johnny Test{i}',
            'Email': f'jt{i}@illinois.edu',
            'Major': random.choice(g_cs)
            
        }
        df.loc[len(df)] = student

    return df

# adds a default bio and profile picture link
# gets rid of majors column (should be in relational table instead)
def clean() -> pd.DataFrame:
    students = pd.read_csv('./backend/majors data/fake_cs_students.csv')
    students = students.drop('Major', axis='columns')
    students['Bio'] = 'Hello, world!'
    students['PFP'] = 'https://studentengagement.illinois.edu/about/staff/images/BlockI.png'
    return students

# generates fake relational data (email & major, degree type)
def gen_majors() -> pd.DataFrame:
    students = pd.read_csv('./backend/majors data/fake_cs_students.csv')
    students = students.drop('Name', axis='columns').drop('Bio', axis='columns').drop('PFP', axis='columns')
    for i in tqdm(range(4000)):
        major, degree = random.choice(ug_cs).split(',')
        students.loc[i, 'Major Name'] = major
        students.loc[i, 'Degree Type'] = degree
    for i in tqdm(range(4000, 6000)):
        major, degree = random.choice(ug_cs).split(',')
        students.loc[i, 'Major Name'] = major
        students.loc[i, 'Degree Type'] = degree
    return students

def main():
    df = gen_majors()
    df.to_csv('./backend/majors data/fake_studies.csv', index=False)
    

if __name__ == '__main__':
    main()