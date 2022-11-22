from os import PRIO_PGRP
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



if job_filter_txt.lower()=='jobs':
    count=1
    print(len(filters_only))
    for x in filters_only:
        if (count!=8 or count!=13) and count<len(filters_only):
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            inside_filters=filter_only.find_elements_by_xpath(".//li/label")
            label_names=filter_only.find_elements_by_xpath(".//li/label//span[1]")
            label_list=[]
            for l_name in label_names:
                label_list.append(l_name.text)
            print(heading_sort_by.text,count,label_list,end='')
            print('select upto',len(inside_filters),":-",end='')
            sort_by=int(input(" "))
            if sort_by<=len(inside_filters) and sort_by>0:
                f_sort_by=filter_only.find_element_by_xpath(f".//li[{sort_by}]/label")
                f_sort_by.click()
            else:
                print("invalid selection")
            count+=1
        if (count==8 or count==13 or count==14) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            print(heading_sort_by.text,count,'select upto:-',end='')
            Radio_button=int(input("there is a button type 1 for ON:-"))
            f_sort_by=filter_only.find_element_by_xpath(".//div/div")
            if Radio_button==1:
                f_sort_by.click()
            else:
                print("invalid input")
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//button[@aria-label="Apply current filters to show results"]').click()
    sleep(3)

elif job_filter_txt.lower()=='people':
    count=1
    print(len(filters_only))
    for x in filters_only:
        filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
        heading_sort_by=filter_only.find_element_by_xpath(".//h3")
        
        if (count==11 or (count>=2 and count<=8)) and count<len(filters_only)+1:
            print(heading_sort_by.text)
            print('add your choice',":-",end='')
            input_box=str(input(" "))
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
            count+=1
    
        if (count==1 or count==9 or count==10) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            inside_filters=filter_only.find_elements_by_xpath(".//li/label")
            label_names=filter_only.find_elements_by_xpath(".//li/label//span[1]")
            label_list=[]
            for l_name in label_names:
                label_list.append(l_name.text)
            print(heading_sort_by.text,count,label_list,end="")
            print('select upto',len(inside_filters),":-",end='')
            sort_by=int(input(" "))
            if sort_by<=len(inside_filters) and sort_by>0:
                f_sort_by=filter_only.find_element_by_xpath(f".//li[{sort_by}]/label")
                f_sort_by.click()
            else:
                print("invalid selection")
            count+=1
    
        if (count==0) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            print(heading_sort_by.text,count,'select upto:-',end='')
            Radio_button=int(input("there is a button type 1 for ON:-"))
            f_sort_by=filter_only.find_element_by_xpath(".//div/div")
            if Radio_button==1:
                f_sort_by.click()
            else:
                print("invalid input")
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//button[@aria-label="Apply current filters to show results"]').click()
    sleep(3)

elif job_filter_txt.lower()=='posts':
    count=1
    print(len(filters_only))
    for x in filters_only:
        filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
        heading_sort_by=filter_only.find_element_by_xpath(".//h3")
        
        if (count>=4 and count<=9) and count<len(filters_only)+1:
            print(heading_sort_by.text)
            print('add your choice',":-",end='')
            input_box=str(input(" "))
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
            count+=1
    
        if (count>=1 and count<=3) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            inside_filters=filter_only.find_elements_by_xpath(".//li/label")
            label_names=filter_only.find_elements_by_xpath(".//li/label//span[1]")
            label_list=[]
            for l_name in label_names:
                label_list.append(l_name.text)
            print(heading_sort_by.text,count,label_list,end="")
            print('select upto',len(inside_filters),":-",end='')
            sort_by=int(input(" "))
            if sort_by<=len(inside_filters) and sort_by>0:
                f_sort_by=filter_only.find_element_by_xpath(f".//li[{sort_by}]/label")
                f_sort_by.click()
            else:
                print("invalid selection")
            count+=1
    
        if (count==0) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            print(heading_sort_by.text,count,'select upto:-',end='')
            Radio_button=int(input("there is a button type 1 for ON:-"))
            f_sort_by=filter_only.find_element_by_xpath(".//div/div")
            if Radio_button==1:
                f_sort_by.click()
            else:
                print("invalid input")
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//button[@aria-label="Apply current filters to show results"]').click()
    sleep(3)

elif job_filter_txt.lower()=='courses':
    count=1
    print(len(filters_only))
    for x in filters_only:
        filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
        heading_sort_by=filter_only.find_element_by_xpath(".//h3")
        
        if count==0 and count<len(filters_only)+1:
            print(heading_sort_by.text)
            print('add your choice',":-",end='')
            input_box=str(input(" "))
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
            count+=1
    
        if (count>=1 and count<=4) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            inside_filters=filter_only.find_elements_by_xpath(".//li/label")
            label_names=filter_only.find_elements_by_xpath(".//li/label//span[1]")
            label_list=[]
            for l_name in label_names:
                label_list.append(l_name.text)
            print(heading_sort_by.text,count,label_list,end="")
            print('select upto',len(inside_filters),":-",end='')
            sort_by=int(input(" "))
            if sort_by<=len(inside_filters) and sort_by>0:
                f_sort_by=filter_only.find_element_by_xpath(f".//li[{sort_by}]/label")
                f_sort_by.click()
            else:
                print("invalid selection")
            count+=1
    
        if (count==0) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            print(heading_sort_by.text,count,'select upto:-',end='')
            Radio_button=int(input("there is a button type 1 for ON:-"))
            f_sort_by=filter_only.find_element_by_xpath(".//div/div")
            if Radio_button==1:
                f_sort_by.click()
            else:
                print("invalid input")
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//button[@aria-label="Apply current filters to show results"]').click()
    sleep(3)

elif job_filter_txt.lower()=='schools':
    print("school has no filter")
elif job_filter_txt.lower()=='events':
    print("events has no filter")
elif job_filter_txt.lower()=='companies':
    count=1
    print(len(filters_only))
    for x in filters_only:
        filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
        heading_sort_by=filter_only.find_element_by_xpath(".//h3")
        
        if (count==1 or count==2) and count<len(filters_only)+1:
            print(heading_sort_by.text)
            print('add your choice',":-",end='')
            input_box=str(input(" "))
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
            count+=1
    
        if (count>=3 and count<=5) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            inside_filters=filter_only.find_elements_by_xpath(".//li/label")
            label_names=filter_only.find_elements_by_xpath(".//li/label//span[1]")
            label_list=[]
            for l_name in label_names:
                label_list.append(l_name.text)
            print(heading_sort_by.text,count,label_list,end="")
            print('select upto',len(inside_filters),":-",end='')
            sort_by=int(input(" "))
            if sort_by<=len(inside_filters) and sort_by>0:
                f_sort_by=filter_only.find_element_by_xpath(f".//li[{sort_by}]/label")
                f_sort_by.click()
            else:
                print("invalid selection")
            count+=1
    
        if (count==0) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            print(heading_sort_by.text,count,'select upto:-',end='')
            Radio_button=int(input("there is a button type 1 for ON:-"))
            f_sort_by=filter_only.find_element_by_xpath(".//div/div")
            if Radio_button==1:
                f_sort_by.click()
            else:
                print("invalid input")
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//button[@aria-label="Apply current filters to show results"]').click()
    sleep(3)

elif job_filter_txt.lower()=='services':
    count=1
    print(len(filters_only))
    for x in filters_only:
        filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
        heading_sort_by=filter_only.find_element_by_xpath(".//h3")
        
        if (count==1 or count==2) and count<len(filters_only)+1:
            print(heading_sort_by.text)
            print('add your choice',":-",end='')
            input_box=str(input(" "))
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
            count+=1
    
        if (count>=3 and count<=4) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            inside_filters=filter_only.find_elements_by_xpath(".//li/label")
            label_names=filter_only.find_elements_by_xpath(".//li/label//span[1]")
            label_list=[]
            for l_name in label_names:
                label_list.append(l_name.text)
            print(heading_sort_by.text,count,label_list,end="")
            print('select upto',len(inside_filters),":-",end='')
            sort_by=int(input(" "))
            if sort_by<=len(inside_filters) and sort_by>0:
                f_sort_by=filter_only.find_element_by_xpath(f".//li[{sort_by}]/label")
                f_sort_by.click()
            else:
                print("invalid selection")
            count+=1
    
        if (count==0) and count<len(filters_only)+1:
            filter_only=driver.find_element_by_xpath(f"//div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]/ul/li[{count}]")
            heading_sort_by=filter_only.find_element_by_xpath(".//h3")
            print(heading_sort_by.text,count,'select upto:-',end='')
            Radio_button=int(input("there is a button type 1 for ON:-"))
            f_sort_by=filter_only.find_element_by_xpath(".//div/div")
            if Radio_button==1:
                f_sort_by.click()
            else:
                print("invalid input")
            count+=1
    sleep(2)
    driver.find_element_by_xpath('//button[@aria-label="Apply current filters to show results"]').click()
    sleep(3)

else:
    print("invalid filter input ")



driver.maximize_window()

# driver.quit()

#  //div[@class='artdeco-modal artdeco-modal--layer-default justify-space-between search-reusables__side-panel search-reusables__side-panel--open']/div[2]//li[1]  filter
#   //button[@class='artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view']
#    //main[@id="main"]//ul[@class='reusable-search__entity-result-list list-style-none']/li  allpeople
# print(description_of_job)
