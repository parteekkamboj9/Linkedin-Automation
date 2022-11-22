from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
user_name=input("Enter your mail to login:-")
pass_word=input("Enter your correct Password:-")
look_for=input("What do you looking for:-")
filter_name=input("select type: jobs, people, groups, posts, courses, schools, events, companies, services:-")
url="https://www.linkedin.com/login/"
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()
driver.get(url)

action=ActionChains(driver)
description_of_job=[]
try:
	sleep(3)
	driver.find_element_by_id("username").send_keys(user_name)
	driver.find_element_by_id("password").send_keys(pass_word)
	driver.find_element_by_xpath("//button[@type='submit']").click()
	sleep(5)
	driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys(look_for)
	action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
	sleep(5)
except:
	print("Your mail or password is incorrect. please run agian and try again")
	driver.quit()
	
try:
	job_filter_9=driver.find_elements_by_xpath("//div[@id='search-reusables__filters-bar']/ul/li/button")
	for job_filter in job_filter_9:
	    job_filter_txt=job_filter.text
	    if job_filter_txt.lower()==filter_name:
		job_filter.click()
		sleep(3)
		break
	sleep(3)
	all_filter=driver.find_element_by_xpath('//button[@aria-label="Show all filters. Clicking this button displays all available filter options."]').click()
	sleep(2)
	filters_only=driver.find_elements_by_xpath("//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li")
except:
	print("There is a error to find your information. please try again")
	driver.quit()



def for_add_only(count):
    filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
    heading_sort_by=filter_only.find_element_by_xpath(".//h3")
    print(heading_sort_by.text)
    print('add your choice',":-",end='')
    try:
        input_box=str(input(" "))
    except:
        input_box=""
    filter_only.find_element_by_xpath(".//li/button").click()
    sleep(1)
    if filter_only.find_element_by_xpath(".//li/div//input"):
        location=filter_only.find_element_by_xpath(".//li/div//input")
        location.click()
        sleep(1)
        location.send_keys(input_box)
        sleep(2)
        location.send_keys(Keys.ARROW_DOWN)
        sleep(1)
        location.send_keys(Keys.ENTER)
    else:
        print("no such input")
def for_options_only(count):
    filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
    heading_sort_by=filter_only.find_element_by_xpath(".//h3")
    inside_filters=filter_only.find_elements_by_xpath(".//li/label")
    label_names=filter_only.find_elements_by_xpath(".//li/label//span[1]")
    label_list=[]
    for l_name in label_names:
        label_list.append(l_name.text)
    print(heading_sort_by.text,count,label_list,end="")
    print('select upto',len(inside_filters),":-",end='')
    try:
        sort_by=int(input(" "))
    except:
        sort_by=0
    if sort_by<=len(inside_filters) and sort_by>0:
        f_sort_by=filter_only.find_element_by_xpath(f".//li[{sort_by}]/label")
        f_sort_by.click()
    else:
        print("invalid selection")
def for_on_off_only(count):
    filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
    heading_sort_by=filter_only.find_element_by_xpath(".//h3")
    print(heading_sort_by.text,count,'select upto:-',end='')
    try:
        Radio_button=int(input("there is a button type 1 for ON:-"))
    except:
        Radio_button=0
    f_sort_by=filter_only.find_element_by_xpath(".//div/div")
    if Radio_button==1:
        f_sort_by.click()
    else:
        print("invalid input")


if job_filter_txt.lower()=='jobs':
    count=1
    for x in filters_only:
        if ((count>=1 and count<=3) or (count>=5 and count<=7) or (count>=11 and count<=12) or count==9) and count<len(filters_only):
            for_options_only(count)
            count+=1
        if (count==8 or count==13 or count==14) and count<len(filters_only)+1:
            for_on_off_only(count)
            count+=1
        if (count==4 or count==10) and count<len(filters_only)+1:
            for_add_only(count)
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//div[@class="justify-flex-end display-flex mv3 mh2"]//button[@aria-live="polite"]').click()
    sleep(3)


if job_filter_txt.lower()=='people':
    count=1
    for x in filters_only:
        
        if (count==11 or (count>=2 and count<=8)) and count<len(filters_only)+1:
            for_add_only(count)
            count+=1
        if (count==1 or count==9 or count==10) and count<len(filters_only)+1:
            for_options_only(count)
            count+=1
        if (count==0) and count<len(filters_only)+1:
            for_on_off_only(count)
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//div[@class="justify-flex-end display-flex mv3 mh2"]//button[@aria-live="polite"]').click()
    sleep(3)


if job_filter_txt.lower()=='posts':
    count=1
    for x in filters_only:
        
        if (count>=4 and count<=9) and count<len(filters_only)+1:
            for_add_only(count)
            count+=1
        if (count>=1 and count<=3) and count<len(filters_only)+1:
            for_options_only(count)
            count+=1
        if (count==0) and count<len(filters_only)+1:
            for_on_off_only(count)
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//div[@class="justify-flex-end display-flex mv3 mh2"]//button[@aria-live="polite"]').click()
    sleep(3)


if job_filter_txt.lower()=='courses':
    count=1
    for x in filters_only:
        
        if count==0 and count<len(filters_only)+1:
            for_add_only(count)
            count+=1
        if (count>=1 and count<=4) and count<len(filters_only)+1:
            for_options_only(count)
            count+=1
        if (count==0) and count<len(filters_only)+1:
            for_on_off_only(count)
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//div[@class="justify-flex-end display-flex mv3 mh2"]//button[@aria-live="polite"]').click()
    sleep(3)

if job_filter_txt.lower()=='companies':
    count=1
    for x in filters_only:
        
        if (count==1 or count==2) and count<len(filters_only)+1:
            for_add_only(count)
            count+=1
        if (count>=3 and count<=5) and count<len(filters_only)+1:
            for_options_only(count)
            count+=1
        if (count==0) and count<len(filters_only)+1:
            for_on_off_only(count)
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//div[@class="justify-flex-end display-flex mv3 mh2"]//button[@aria-live="polite"]').click()
    sleep(3)

    
if job_filter_txt.lower()=='services':
    count=1
    for x in filters_only:
        
        if (count==1 or count==2) and count<len(filters_only)+1:
            for_add_only(count)
            count+=1
        if (count>=3 and count<=4) and count<len(filters_only)+1:
            for_options_only(count)
            count+=1
        if (count==0) and count<len(filters_only)+1:
            for_on_off_only(count)
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//div[@class="justify-flex-end display-flex mv3 mh2"]//button[@aria-live="polite"]').click()
    sleep(3)

if job_filter_txt.lower()=='schools':
    print("school has no filter")
    sleep(2)
    driver.find_element_by_xpath('//div[@class="justify-flex-end display-flex mv3 mh2"]//button[@aria-live="polite"]').click()
    sleep(3)
if job_filter_txt.lower()=='events':
    print("events has no filter")
    sleep(2)
    driver.find_element_by_xpath('//div[@class="justify-flex-end display-flex mv3 mh2"]//button[@aria-live="polite"]').click()
    sleep(3)
if job_filter_txt.lower()=='groups':
    print("group has no filter")
    sleep(2)
    driver.find_element_by_xpath('//div[@class="justify-flex-end display-flex mv3 mh2"]//button[@aria-live="polite"]').click()
    sleep(3)
    
else:
    print("invalid filter input ")



all_post_details=[]
for x in range(8):
    item_111=driver.find_element_by_xpath('//ul[@class="scaffold-layout__list-container"]/li//div[@class="full-width artdeco-entity-lockup__title ember-view"]/a')
    sleep(1)
    item_111.send_keys(Keys.PAGE_DOWN)
    sleep(3)

all_item=driver.find_elements_by_xpath('//ul[@class="scaffold-layout__list-container"]/li//div[@class="full-width artdeco-entity-lockup__title ember-view"]/a')
sleep(5)
print(len(all_item))
for one_item in all_item:
    one_item.click()
    sleep(5)
    delail_section=driver.find_element_by_xpath('//div[@class="job-view-layout jobs-details"]/div[1]')
    total_detail=[]
    overall=[]
    requirments=[]
    company=[]
    section_divs=delail_section.find_elements_by_xpath('.//div[@class="jobs-unified-top-card__content--two-pane"]//span')
    for spans in section_divs:
        overall.append(spans.text)
    total_detail.append(overall)
    section_req=delail_section.find_element_by_xpath('.//div[@id="job-details"]/span')
    section_req_txt=section_req.text
    requirments.append(section_req_txt)
    total_detail.append(requirments)
    # section_req.send_keys(Keys.PAGE_DOWN)
    # section_req.send_keys(Keys.PAGE_DOWN)
    # comapany_detail=delail_section.find_element_by_xpath('.//div[@class="jobs-company__box"]').text
    # company.append(comapany_detail)
    # total_detail.append(company)

    print(total_detail)
    all_post_details.append(total_detail)


print(len(all_post_details))

sleep(1)
driver.maximize_window()

# driver.quit()

