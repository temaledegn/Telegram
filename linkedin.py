from bs4 import BeautifulSoup
import time
from pymongo import MongoClient
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://www.linkedin.com')
time.sleep(4)
# locate email form by_class_name
username = driver.find_element_by_xpath('//*[@type="text"]')
# send_keys() to simulate key strokes
username.send_keys('mgentel92@gmail.com')
password = driver.find_element_by_xpath('//*[@type="password"]')
password.send_keys('new123we123')
time.sleep(5)
log_in_button = driver.find_element_by_xpath('//*[@class="sign-in-form__submit-button"]')
log_in_button.click()
time.sleep(6)
link = 'https://www.linkedin.com/in/samuelgirma/'  # Profile link which you want to scrape
driver.get(link)
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight
src = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
time.sleep(8)
soup = BeautifulSoup(src, 'html.parser')
time.sleep(8)
# name
try:
    name = soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'}).get_text().strip()
    print(name)
except IndexError:  # To ignore any kind of error
    name = 'NULL'
    print(name)
except AttributeError:
    name = 'NULL'
    print(name)
# position
try:
    position = soup.find('div', {'class': 'text-body-medium break-words'}).get_text().strip()
    print(position)
except IndexError:  # To ignore any kind of error
    position = 'NULL'
    print(position)
except AttributeError:
    position = 'NULL'
    print(position)

# country
try:
    country = soup.find('span', {'class': 'text-body-small inline t-black--light break-words'}).get_text().strip()
    print(country)
except IndexError:  # To ignore any kind of error
    country = 'NULL'
    print(country)
except AttributeError:
    country = 'NULL'
    print(country)
# connection
try:
    connection = soup.find('li', {'class': 'text-body-small'}).get_text().strip()
    print(connection)
except IndexError:  # To ignore any kind of error
    connection = 'NULL'
    print(connection)
except AttributeError:
    connection = 'NULL'
    print(connection)

# company
try:
    company = soup.find('a', {'class': 'display-flex mb2 link-without-visited-state t-black'}).get_text().strip()
    print(company)
except IndexError:  # To ignore any kind of error
    company = 'NULL'
    print(company)
except AttributeError:
    company = 'NULL'
    print(company)

# university
try:
    university = soup.find('a', {'class': 'display-flex link-without-visited-state t-black'}).get_text().strip()
    print(university)
except IndexError:  # To ignore any kind of error
    university = 'NULL'
    print(university)
except AttributeError:
    university = 'NULL'
    print(university)


# About
try:
    About = soup.find('div', {'class': 'pv-oc ember-view'}).get_text().strip()
    print(About)
except IndexError:
    About = 'NULL'
    print(About)
except AttributeError:
    About = 'NULL'
    print(About)

# Activity
try:
    Activity= soup.find('p', {'class': 't-14 pb2'}).get_text().strip()
    print(Activity)
except IndexError:
    Activity = 'NULL'
    print(Activity)
except AttributeError:
    Activity= 'NULL'
    print(Activity)
time.sleep(8)
# followers
try:
    followers= soup.find('span', {'class': 'align-self-center t-14 t-black--light'}).get_text().strip()
    print(followers)
except IndexError:
    followers = 'NULL'
    print(followers)
except AttributeError:
    followers= 'NULL'
    print(followers)

Experience = soup.find('ul', {'class': 'pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more'})
time.sleep(6)
print(Experience)
Experience=Experience.find_all('li', {'class':'pv-entity__position-group-pager pv-profile-section__list-item ember-view'})
experience=[]
for item in Experience:
    positionE= item.find('h3', {'class': 't-16 t-black t-bold'}).get_text().strip()
    print(positionE)
    Company_Name=item.find('p', {'class': 'pv-entity__secondary-title t-14 t-black t-normal'}).get_text().strip()
    print(Company_Name)
    date_exprince=item.find('h4', {'class': 'pv-entity__date-range t-14 t-black--light t-normal'}).get_text().strip()
    print(date_exprince)
    Employment_Duration=item.find('h4', {'class': 'pv-entity__bullet-item-v2'}).get_text().strip()
    print(Employment_Duration)
    location=item.find('h4', {'class': 'pv-entity__location t-14 t-black--light t-normal block'}).get_text().strip()
    print(location)
    Experiencehold=[]
    Experiencehold={
        "positionE":positionE,
            "Company_Name":Company_Name,
            "date_exprince":date_exprince,
            "Employment_Duration":Employment_Duration,
            "location":location
        }
    experience.append(Experiencehold)

# Edication
try:
    Education= soup.find('section', {'class': 'pv-profile-section education-section ember-view'})
    Education=Education.find_all('li', {'class':'pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view'})
    education=[]
    for item in Education:
        University1= item.find('h3', {'class': 'pv-entity__school-name t-16 t-black t-bold'}).get_text().strip()
        print(university)
        Degree_Name=item.find('span', {'class': 'pv-entity__comma-item'}).get_text().strip()
        print(Degree_Name)
        expected_graduation=item.find('p', {'class': 'pv-entity__dates t-14 t-black--light t-normal'}).get_text().strip()
        print(expected_graduation)
        Edicationhold=[]
        Edicationhold={
            "University":University1,
            "Degree_Name":Degree_Name,
            "Expected_graduation":expected_graduation
        }
        education.append(Edicationhold)
except IndexError:
    Education = 'NULL'
    print(Education)
except AttributeError:
    Education= 'NULL'
    print(Education)
# Licenses & certifications
time.sleep(5)
try:
    certifications= soup.find('section', {'class': 'pv-profile-section pv-profile-section--certifications-section ember-view'})

    certifications=certifications.find_all('li', {'class':'pv-profile-section__sortable-item pv-certification-entity ember-view'})
    Certifications=[]
    for item in certifications:
        certifications_name= item.find('h3', {'class': 't-16 t-bold'}).get_text().strip()
        print(certifications_name)
        training_name=item.find('p', {'class': 't-14'}).get_text().strip()
        print(training_name)
        Certification={
            "Certifications_name":certifications_name,
            "Training_name":training_name
        }
        Certifications.append(Certification)
except IndexError:
    certifications = 'NULL'
    print(certifications)
except AttributeError:
    certifications= 'NULL'
    print(certifications)
    time.sleep(6)
# Interests
try:
    Interests= soup.find('ul', {'class': 'pv-profile-section__section-info section-info display-flex justify-flex-start overflow-hidden'})
    Interests=Interests.find_all('li', {'class':'pv-interest-entity pv-profile-section__card-item ember-view'})
    time.sleep(6)
    Interests_data=[]
    for item in Interests:
        name_interest = item.find('span', {'class': 'pv-entity__summary-title-text'}).get_text().strip()
        print(name_interest)
        work_area=item.find('p', {'class': 'pv-entity__occupation t-12 t-black--light'}).get_text().strip()
        print(work_area)
        nu_follower = item.find('p', {'class': 'class="pv-entity__follower-count text-body-xsmall t-black--light "'}).get_text().strip()
        print(nu_follower)
        Interests=[]
        Interestss={
            "Name_interest":name_interest,
            "Work_area":work_area,
            "Number_follwer":nu_follower

        }
        Interests_data.append(Interestss)

except IndexError:
    Interests = 'NULL'
    print(Interestss)
except AttributeError:
    Interests= 'NULL'
    print(Experience)
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
db = client['socialm']
collection=db['socialm']
post = {"Full_Name": name, "Position": position, "Country": country,"Connection":connection,"company":company,
        "University":university,"About":About,"Activity":Activity,"Followers":followers
        }
collection.profile.insert_one(post)