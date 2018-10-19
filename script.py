from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
import string
import time
import requests
import os
from selenium.webdriver.support.ui import WebDriverWait
import random
driver=webdriver.Chrome('S:\\softwares\\chromedriver.exe')
driver.get("http://district.mphc.gov.in/%E0%A4%A8%E0%A4%BF%E0%A4%B0%E0%A5%8D%E0%A4%A3%E0%A4%AF-%E0%A4%86%E0%A4%A6%E0%A5%87%E0%A4%B6")
#jn=driver.find_element_by_partial_link_text("Judge Name")
#jn.click()
district=driver.find_element_by_id("menu_dist1")
path="S:\\iasnlp\\project\\pdfs"
os.chdir(path)
ts=5
#print(district)
print(district.text)
#district=district.find_elements_by_class_name("styled-select")
district=district.find_elements_by_tag_name("option")
print(len(district))
for do in range(len(district))[11:]:
        #element = WebDriverWait(driver, ts).until(find)
        #d.click()
        #d.size
        
        d=district[do]
        x=d.text
        d.click()
        print(x)
        try:
                os.mkdir(path+"\\"+x)
        except:
                print("already exists")
        os.chdir(path+"\\"+x)
        time.sleep(10)
        tehsil=driver.find_element_by_id("menu_teh1")
        tehsil=tehsil.find_elements_by_tag_name("option")
        print(len(tehsil))
        urllist=[]
        for t in tehsil:
                try:
                        y=t.text
                except:
                        continue
                print(">",y)
                t.click()
                '''try:
                        os.mkdir(path+"\\"+x+"\\"+y)
                except:
                        print("already exists")
                os.chdir(path+"\\"+x+"\\"+y)'''
                time.sleep(ts)
                jj=driver.find_element_by_id("seljug_adv")
                optgrp=jj.find_elements_by_tag_name("optgroup")
                try:
                        search=driver.find_element_by_name("btnSearchadv")
                except:
                        continue
                for i in optgrp:
                        opts=i.find_elements_by_tag_name("option")
                        count=0
                        for j in opts:
                                print(">>",j.text)
                                time.sleep(ts)
                                j.click()
                                time.sleep(ts)
                                search.click()
                                time.sleep(ts)
                                tbl=driver.find_element_by_id("dv_result_adv")
                                #print(">>>",tbl.text)
                                for k in tbl.find_elements_by_tag_name("tr"):
                                        bx=k.find_elements_by_tag_name('td')
                                        if(len(bx)>5):
                                                #print(bx[5].text)
                                                bx=bx[5]
                                                try:
                                                        bx=bx.find_element_by_tag_name("a")
                                                        url=bx.get_attribute("href")
                                                        print(url)
                                                        urllist.append(url)
                                                except:
                                                        print(">>>>>>>>>>>>>>>>>>>>>>>>",do,t,i,j,"<<<<<<<<<<<<<<<<<<<<<<<<")
                                                        continue
                                        '''u=bx.text
                                        if(random.randint(0,3)==0):
                                                time.sleep(5)
                                        
                                        if(len(bx)>5):
                                                print(bx)
                                                bx=bx[5]
                                                print(u)
                                                bx=bx.find_element_by_tag_name("a")
                                                
                                                print(">>>",bx.text)
                                                #url=bx.get_attribute("href")
                                                #print(url)
                                                #rep=requests.get(url)
                                                #name=url.split("/")[-1]
                                                #print(name)
                                                        try:
                                                                with(open(name)) as f:
                                                                     print("File already exists")
                                                        except:
                                                                pass
                                                        with open(name,"wb") as f:
                                                                f.write(rep.content)
                                                #print("got it")
                                                count+=1
                                                print(count)
                                                        #urllist.append(url)
                                                #except:
                                                 #       print("no url tag")
                                #if(count==1):
                                        #break'''
                        time.sleep(ts)
                        print("---------------------------------")
        print("******************************************")
        urllist=set(urllist)
        print(len(urllist))
        for u in urllist:
                rep=requests.get(u)
                name=u.split("/")[-1]
                print(name)
                with open(name,"wb") as f:
                        f.write(rep.content)
                if(random.randint(0,7)==0):
                        time.sleep(ts)
                #time.sleep(ts)
        district=driver.find_element_by_id("menu_dist1")
        district=district.find_elements_by_tag_name("option")
        print("******************************************")

'''for i in urllist:
        rep=requests.get(i)
        name=i.split("/")[-1]
        print(name)
        with open(name,"wb") as f:
                f.write(rep.content)
        time.sleep(5)
'''
