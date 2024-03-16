from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
import os

output_dir = 'D:/Project1244/'

new_list_naukri = ['Data Analyst Internship','Backend Developer Internship','App Developer Internship','Data Science Internship']
new_list = ['Data Analyst Internship','Frontend Developer Internship','Backend Developer Internship','App Developer Internship','Data Science Internship']
#Inputs a job title into the input box
dfs = {}
#df = pd.DataFrame({'Job Title':[''], 'Company':[''], 'Location':[''],'Link':['']})

for i in new_list:
    driver = webdriver.Chrome()
    driver.get('https://in.indeed.com/?from=gnav-util-homepage')


    time.sleep(2)
    input_box = driver.find_element('xpath','//*[@id="text-input-what"]')
    input_box.send_keys(i)
    #input_box.send_keys(Keys.ENTER)

    location_box = driver.find_element('xpath','//*[@id="text-input-where"]')
    location_box.send_keys('India')
    location_box.send_keys(Keys.ENTER)

    time.sleep(2)
    press_dateposted = driver.find_element('xpath','//*[@id="filter-dateposted"]')
    press_dateposted.click()
    lastWEEK = driver.find_element('xpath','//*[@id="filter-dateposted-menu"]/li[3]')
    lastWEEK.click()
    time.sleep(1)
    
    df = pd.DataFrame({'Job Title':[''], 'Company':[''], 'Location':[''],'Link':['']})

    #This loop goes through every page and grabs all the details of each posting
    #Loop will only end when there are no more pages to go through
    while True:  
        #Imports the HTML of the current page into python
        soup = BeautifulSoup(driver.page_source, 'lxml')
        
        #Grabs the HTML of each posting
        postings = soup.find_all('li', class_ = 'css-5lfssm eu4oa1w0')
        
        #grabs all the details for each posting and adds it as a row to the dataframe
        for post in postings:
            try:
                link = post.find('a', class_ = 'jcs-JobTitle css-jspxzf eu4oa1w0').get('href')
                link_full = 'https://in.indeed.com'+link
            except:
                link_full = 'N/A'
            
            try:
                name = post.find('h2', class_ = 'jobTitle css-14z7akl eu4oa1w0').text.strip()
            except:
                name = 'N/A'
            
            try:
                company = post.find('span', class_ = 'css-92r8pb eu4oa1w0').text.strip()
            except:
                company = "N/A"
            try:
                location = post.find('div', class_ = 'css-1p0sjhy eu4oa1w0').text.strip()
            except:
                location = 'N/A'
            #date = post.find('span', class_ = 'date').text.strip()
            #try:
                #stipend = post.find('div', class_ = 'css-1ihavw2 eu4oa1w0').text.strip()
            #except:
                #salary = 'N/A'
            df = df.append({'Job Title':name, 'Company':company, 'Location':location, 'Link':link_full },
                           ignore_index = True)
        
        #checks if there is a button to go to the next page, and if not will stop the loop
        try:
            button = soup.find('a', attrs = {'aria-label': 'Next Page'}).get('href')
            driver.get('https://in.indeed.com'+button)
        except:
            break
        
    dfs[i] = df
    #with pd.ExcelWriter('D:/BeautifulSoup/i.xlsx') as writer:
    #for key, value in dfs.items():
    #    value.to_excel(writer, sheet_name=key, index=False)
    for i, df in dfs.items():
    # Construct the file path for the CSV file
        file_path = os.path.join(output_dir, f'{i} indeed.csv')
    
    # Write the DataFrame to a CSV file
        df.to_csv(file_path, index=False)
        
    time.sleep(3)
    driver.close()
    
for j in new_list:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.glassdoor.co.in/index.htm')
    time.sleep(3)
    
    email_box = driver.find_element('xpath','//*[@id="inlineUserEmail"]')
    email_box.send_keys('jobsearchautomated@gmail.com')
    email_box.send_keys(Keys.ENTER)
    time.sleep(2)

    password_box = driver.find_element('xpath','//*[@id="inlineUserPassword"]')
    password_box.send_keys('iamproject1244')
    password_box.send_keys(Keys.ENTER)
    time.sleep(3)

    pressJob = driver.find_element('xpath','//*[@id="ContentNav"]/li[2]')
    pressJob.click()
#search_line = driver.find_element('xpath','//*[@id="UtilityNav"]/div[1]/button')
#search_line.click()
#time.sleep(1)
#search_box = driver.find_element('xpath','/html/body/header/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/input')
#search_box.send_keys('Data analyst job')
#search_box.send_keys(Keys.ENTER)


#location_box = driver.find_element('xpath','//*[@id="text-input-where"]')
#location_box.send_keys('Tamil Nadu')
#location_box.send_keys(Keys.ENTER)

    time.sleep(2)
    input_box = driver.find_element('xpath','//*[@id="searchBar-jobTitle"]')
    input_box.send_keys(j)
    time.sleep(1)
    loc_box = driver.find_element('xpath','//*[@id="searchBar-location"]')
    loc_box.send_keys('India')
    loc_box.send_keys(Keys.ENTER)
    #press_dateposted = driver.find_element('xpath','//*[@id="filter-dateposted"]')
    #press_dateposted.click()
    #press_dateposted.send_keys(Keys.ARROW_DOWN*3)
    #time.sleep(1)
    #pastWeek = driver.find_element('xpath','//*[@id="filter-dateposted-menu"]/li[3]')
    #pastWeek.click()

    time.sleep(2)

    try:
        anotherButt = driver.find_element('xpath','//*[@id="JAModal"]/div/div[2]/span')
        anotherButt.click()
    except:
        pass    
       

    datePostedButton = driver.find_element('xpath','//*[@id="app-navigation"]/div[4]/div[1]/div[3]/div/button[2]')
    datePostedButton.click()
    time.sleep(2)
    lastWeekButton = driver.find_element('xpath','//*[@id="app-navigation"]/div[4]/div[1]/div[3]/div[2]/ul/li[4]/button')
    lastWeekButton.click()
    time.sleep(4)
    
    df = pd.DataFrame({'Job Title':[''], 'Company':[''], 'Location':[''],'Link':['']})

    while True:  
    #Imports the HTML of the current page into python
        soup = BeautifulSoup(driver.page_source, 'lxml')
    
    #Grabs the HTML of each posting
        postings = soup.find_all('li', class_ = 'JobsList_jobListItem__wjTHv')
    

    #grabs all the details for each posting and adds it as a row to the dataframe
        for post in postings:
            try:
                link = post.find('a', class_ = 'JobCard_jobTitle___7I6y').get('href')
                link_full = link
            except:
                break
        

            try:
                name = post.find('a', class_ = 'JobCard_jobTitle___7I6y').text.strip()
            except:
                break
            try:
                company = post.find('span', class_ = 'EmployerProfile_compactEmployerName__LE242').text.strip()
            except:
                break
        

            location = post.find('div', class_ = 'JobCard_location__rCz3x').text.strip()
        
        
        #date = post.find('span', class_ = 'date').text.strip()
        #try:
            #stipend = post.find('div', class_ = 'css-1ihavw2 eu4oa1w0').text.strip()
        #except:
            #salary = 'N/A'
            df = df.append({'Job Title':name, 'Company':company, 'Location':location, 'Link':link_full },
                       ignore_index = True)
        
        try:
            finalButt = driver.find_element('xpath','//*[@id="left-column"]/div[2]/div/button')
            finalButt.click()
        except:
            break   
    dfs[j] = df
    #with pd.ExcelWriter('D:/BeautifulSoup/i.xlsx') as writer:
    #for key, value in dfs.items():
    #    value.to_excel(writer, sheet_name=key, index=False)
    for j, df in dfs.items():
    # Construct the file path for the CSV file
        file_path = os.path.join(output_dir, f'{j} glassdoor.csv')
    
    # Write the DataFrame to a CSV file
        df.to_csv(file_path, index=False)      
    time.sleep(2)    
    driver.close()        


for k in new_list_naukri:
    driver = webdriver.Chrome()
    driver.get('https://www.naukri.com/')


    time.sleep(2)
    input_box = driver.find_element('xpath','//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input')
    input_box.send_keys(k)
    #input_box.send_keys(Keys.ENTER)
    time.sleep(1)
    experience = driver.find_element('xpath','//*[@id="expereinceDD"]')
    experience.click()
    time.sleep(1)
    fresher = driver.find_element('xpath','//*[@id="sa-dd-scrollexpereinceDD"]/div[1]/ul/li[1]')
    fresher.click()
    time.sleep(1)    
    location_box = driver.find_element('xpath','//*[@id="root"]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
    location_box.send_keys('India')
    location_box.send_keys(Keys.ENTER)

    time.sleep(2)
    
    freshness = driver.find_element('xpath','//*[@id="filter-freshness"]')
    freshness.click()
    time.sleep(1)
    
    #press_dateposted = driver.find_element('xpath','//*[@id="filter-dateposted"]')
    #press_dateposted.click()
    lastWEEK = driver.find_element('xpath','//*[@id="search-result-container"]/div[1]/div[1]/div/div/div[2]/div[11]/div[2]/div/div/ul/li[3]')
    #//*[@id="search-result-container"]/div[1]/div[1]/div/div/div[2]/div[10]/div[2]/div/div/ul/li[3]

    lastWEEK.click()
    time.sleep(1)
    
    df = pd.DataFrame({'Job Title':[''], 'Company':[''], 'Location':[''],'Link':['']})

    #This loop goes through every page and grabs all the details of each posting
    #Loop will only end when there are no more pages to go through
    while True:  
        #Imports the HTML of the current page into python
        soup = BeautifulSoup(driver.page_source, 'lxml')
        
        #Grabs the HTML of each posting
        postings = soup.find_all('div', class_ = 'cust-job-tuple layout-wrapper lay-2 sjw__tuple internship-tuple')
        
        #grabs all the details for each posting and adds it as a row to the dataframe
        for post in postings:
            try:
                link = post.find('a', class_ = 'title').get('href')
                link_full = link
            except:
                link_full = 'N/A'
            
            try:
                name = post.find('div', class_ = 'row1').text.strip()
            except:
                name = 'N/A'
            
            try:
                company = post.find('a', class_ = 'comp-name').text.strip()
            except:
                company = "N/A"
            try:
                location = post.find('span', class_ = 'ni-job-tuple-icon ni-job-tuple-icon-srp-location loc').text.strip()
            except:
                location = 'N/A'
            #date = post.find('span', class_ = 'date').text.strip()
            #try:
                #stipend = post.find('div', class_ = 'css-1ihavw2 eu4oa1w0').text.strip()
            #except:
                #salary = 'N/A'
            df = df.append({'Job Title':name, 'Company':company, 'Location':location, 'Link':link_full },
                           ignore_index = True)
        
        #checks if there is a button to go to the next page, and if not will stop the loop
        try:
            button = soup.find('a', class_='styles_btn-secondary__2AsIP').get('href')
            driver.get('https://www.naukri.com/'+button)
        except:
            break
        
    dfs[k] = df
    #with pd.ExcelWriter('D:/BeautifulSoup/i.xlsx') as writer:
    #for key, value in dfs.items():
    #    value.to_excel(writer, sheet_name=key, index=False)
    for k, df in dfs.items():
    # Construct the file path for the CSV file
        file_path = os.path.join(output_dir, f'{k} naukri.csv')
    
    # Write the DataFrame to a CSV file
        df.to_csv(file_path, index=False)
        
    time.sleep(3)
    driver.close()
    

driver = webdriver.Chrome()
driver.get('https://www.naukri.com/')


time.sleep(2)
input_box = driver.find_element('xpath','//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input')
input_box.send_keys('Frontend Developer Internship')
#input_box.send_keys(Keys.ENTER)
time.sleep(1)
experience = driver.find_element('xpath','//*[@id="expereinceDD"]')
experience.click()
time.sleep(1)
fresher = driver.find_element('xpath','//*[@id="sa-dd-scrollexpereinceDD"]/div[1]/ul/li[1]')
fresher.click()
time.sleep(1)    
location_box = driver.find_element('xpath','//*[@id="root"]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
location_box.send_keys('India')
location_box.send_keys(Keys.ENTER)

time.sleep(2)

freshness = driver.find_element('xpath','//*[@id="filter-freshness"]')
freshness.click()
time.sleep(1)

#press_dateposted = driver.find_element('xpath','//*[@id="filter-dateposted"]')
#press_dateposted.click()
lastWEEK = driver.find_element('xpath','//*[@id="search-result-container"]/div[1]/div[1]/div/div/div[2]/div[10]/div[2]/div/div/ul/li[3]')
#//*[@id="search-result-container"]/div[1]/div[1]/div/div/div[2]/div[10]/div[2]/div/div/ul/li[3]
lastWEEK.click()
time.sleep(1)

df = pd.DataFrame({'Job Title':[''], 'Company':[''], 'Location':[''],'Link':['']})

#This loop goes through every page and grabs all the details of each posting
#Loop will only end when there are no more pages to go through
while True:  
    #Imports the HTML of the current page into python
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    #Grabs the HTML of each posting
    postings = soup.find_all('div', class_ = 'cust-job-tuple layout-wrapper lay-2 sjw__tuple internship-tuple')
    
    #grabs all the details for each posting and adds it as a row to the dataframe
    for post in postings:
        try:
            link = post.find('a', class_ = 'title').get('href')
            link_full = link
        except:
            link_full = 'N/A'
        
        try:
            name = post.find('a', class_ = 'title').text.strip()
        except:
            name = 'N/A'
        
        try:
            company = post.find('span', class_ = 'comp-dtls-wrap').text.strip()
        except:
            company = "N/A"
        try:
            location = post.find('span', class_ = 'ni-job-tuple-icon ni-job-tuple-icon-srp-location loc').text.strip()
        except:
            location = 'N/A'
        #date = post.find('span', class_ = 'date').text.strip()
        #try:
            #stipend = post.find('div', class_ = 'css-1ihavw2 eu4oa1w0').text.strip()
        #except:
            #salary = 'N/A'
        df = df.append({'Job Title':name, 'Company':company, 'Location':location, 'Link':link_full },
                       ignore_index = True)
    
    #checks if there is a button to go to the next page, and if not will stop the loop
    try:
        button = soup.find('a', class_='styles_btn-secondary__2AsIP').get('href')
        driver.get('https://www.naukri.com/'+button)
    except:
        break
    
dfs['Frontend Developer Internship'] = df
#with pd.ExcelWriter('D:/BeautifulSoup/i.xlsx') as writer:
#for key, value in dfs.items():
#    value.to_excel(writer, sheet_name=key, index=False)

# Construct the file path for the CSV file
file_path = os.path.join(output_dir, 'Frontend Developer Internship naukri.csv')

# Write the DataFrame to a CSV file
df.to_csv(file_path, index=False)
    
time.sleep(3)
driver.close()


# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/App Developer Internship glassdoor.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/App Developer Internship glassdoor.csv', index=False)


# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Frontend Developer Internship glassdoor.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Frontend Developer Internship glassdoor.csv', index=False)


# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Backend Developer Internship glassdoor.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Backend Developer Internship glassdoor.csv', index=False)


# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/App Developer Internship indeed.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/App Developer Internship indeed.csv', index=False)


# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Backend Developer Internship indeed.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Backend Developer Internship indeed.csv', index=False)


# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Frontend Developer Internship indeed.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Frontend Developer Internship indeed.csv', index=False)


# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Data Analyst Internship glassdoor.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Data Analyst Internship glassdoor.csv', index=False)


# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Data Analyst Internship indeed.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Data Analyst Internship indeed.csv', index=False)


# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Data Science Internship glassdoor.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Data Science Internship glassdoor.csv', index=False)



# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Data Science Internship indeed.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Data Science Internship indeed.csv', index=False)

# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Backend Developer Internship naukri.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Backend Developer Internship naukri.csv', index=False)

# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Frontend Developer Internship naukri.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Frontend Developer Internship naukri.csv', index=False)

# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/App Developer Internship naukri.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/App Developer Internship naukri.csv', index=False)

# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Data Analyst Internship naukri.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Data Analyst Internship naukri.csv', index=False)

# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Project1244/Data Science Internship naukri.csv")
# Remove duplicates based on all columns
df = df.drop_duplicates()
# Write the updated DataFrame back to a new CSV file
df.to_csv('D:/Project1244/Data Science Internship naukri.csv', index=False)

# Read the two CSV files into separate DataFrames
df1 = pd.read_csv('D:/Project1244/Data Science Internship indeed.csv')
df2 = pd.read_csv('D:/Project1244/Data Science Internship glassdoor.csv')
df3 = pd.read_csv('D:/Project1244/Data Science Internship naukri.csv')
# Concatenate the two DataFrames
merged_df = pd.concat([df1, df2, df3], ignore_index=True)
# Write the merged DataFrame to a new CSV file
merged_df.to_csv('D:/Project1244/Data Science Internship.csv', index=False)


# Read the two CSV files into separate DataFrames
df1 = pd.read_csv('D:/Project1244/Data Analyst Internship indeed.csv')
df2 = pd.read_csv('D:/Project1244/Data Analyst Internship glassdoor.csv')
df3 = pd.read_csv('D:/Project1244/Data Analyst Internship naukri.csv')
# Concatenate the two DataFrames
merged_df = pd.concat([df1, df2, df3], ignore_index=True)
# Write the merged DataFrame to a new CSV file
merged_df.to_csv('D:/Project1244/Data Analyst Internship.csv', index=False)



# Read the two CSV files into separate DataFrames
df1 = pd.read_csv('D:/Project1244/App Developer Internship indeed.csv')
df2 = pd.read_csv('D:/Project1244/App Developer Internship glassdoor.csv')
df3 = pd.read_csv('D:/Project1244/App Developer Internship naukri.csv')
# Concatenate the two DataFrames
merged_df = pd.concat([df1, df2, df3], ignore_index=True)
# Write the merged DataFrame to a new CSV file
merged_df.to_csv('D:/Project1244/App Developer Internship.csv', index=False)


# Read the two CSV files into separate DataFrames
df1 = pd.read_csv('D:/Project1244/Backend Developer Internship indeed.csv')
df2 = pd.read_csv('D:/Project1244/Backend Developer Internship glassdoor.csv')
df3 = pd.read_csv('D:/Project1244/Backend Developer Internship naukri.csv')
# Concatenate the two DataFrames
merged_df = pd.concat([df1, df2, df3], ignore_index=True)
# Write the merged DataFrame to a new CSV file
merged_df.to_csv('D:/Project1244/Backend Developer Internship.csv', index=False)


# Read the two CSV files into separate DataFrames
df1 = pd.read_csv('D:/Project1244/Frontend Developer Internship indeed.csv')
df2 = pd.read_csv('D:/Project1244/Frontend Developer Internship glassdoor.csv')
df3 = pd.read_csv('D:/Project1244/Frontend Developer Internship naukri.csv')
# Concatenate the two DataFrames
merged_df = pd.concat([df1, df2, df3], ignore_index=True)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('D:/Project1244/Frontend Developer Internship.csv', index=False)


file_path0 = "D:/Project1244/App Developer Internship glassdoor.csv"
file_path1 = "D:/Project1244/App Developer Internship indeed.csv"
file_path2 = "D:/Project1244/Data Analyst Internship indeed.csv"
file_path3 = "D:/Project1244/Data Analyst Internship glassdoor.csv"
file_path4 = "D:/Project1244/Frontend Developer Internship indeed.csv"
file_path5 = "D:/Project1244/Frontend Developer Internship glassdoor.csv"
file_path6 = 'D:/Project1244/Backend Developer Internship glassdoor.csv'
file_path7 = 'D:/Project1244/Backend Developer Internship indeed.csv'
file_path8 = 'D:/Project1244/Data Science Internship glassdoor.csv'
file_path9 = 'D:/Project1244/Data Science Internship indeed.csv'
file_path10 = "D:/Project1244/Data Analyst Internship naukri.csv"
file_path11 = "D:/Project1244/Data Science Internship naukri.csv"
file_path12 = "D:/Project1244/Frontend Developer Internship naukri.csv"
file_path13 = "D:/Project1244/Backend Developer Internship naukri.csv"
file_path14 = "D:/Project1244/App Developer Internship naukri.csv"

if os.path.exists(file_path0):
    # Delete the file
    os.remove(file_path0)
else:
    pass

if os.path.exists(file_path1):
    # Delete the file
    os.remove(file_path1)
else:
    pass
if os.path.exists(file_path2):
    # Delete the file
    os.remove(file_path2)
else:
    pass
if os.path.exists(file_path3):
    # Delete the file
    os.remove(file_path3)
else:
    pass
if os.path.exists(file_path4):
    # Delete the file
    os.remove(file_path4)
else:
    pass
if os.path.exists(file_path5):
    # Delete the file
    os.remove(file_path5)
else:
    pass
if os.path.exists(file_path6):
    # Delete the file
    os.remove(file_path6)
else:
    pass
if os.path.exists(file_path7):
    # Delete the file
    os.remove(file_path7)
else:
    pass
if os.path.exists(file_path8):
    # Delete the file
    os.remove(file_path8)
else:
    pass
if os.path.exists(file_path9):
    # Delete the file
    os.remove(file_path9)
else:
    pass
if os.path.exists(file_path14):
    # Delete the file
    os.remove(file_path14)
else:
    pass
if os.path.exists(file_path10):
    # Delete the file
    os.remove(file_path10)
else:
    pass
if os.path.exists(file_path11):
    # Delete the file
    os.remove(file_path11)
else:
    pass
if os.path.exists(file_path12):
    # Delete the file
    os.remove(file_path12)
else:
    pass
if os.path.exists(file_path13):
    # Delete the file
    os.remove(file_path13)
else:
    pass
