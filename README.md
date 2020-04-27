# Judicial-Cases-Dataset

## Introduction
A Database of all the judgements passed from all high courts of all the districts from the state of Madhya Pradesh. The dataset contains all the cases downloaded in form PDF. 

Site from which all these were downloaded is https://district.mphc.gov.in/%E0%A4%A8%E0%A4%BF%E0%A4%B0%E0%A5%8D%E0%A4%A3%E0%A4%AF-%E0%A4%86%E0%A4%A6%E0%A5%87%E0%A4%B6

The Crawler Bot was developed in Selenium, to automate the task fo filling the form about the District and the Judge name and various other information. All the Judgement Cases which appeared were then downloaded.

Also, it was taken care to make the queries look like real so that the IP doesn't get blocked because of fo repetitive calls.

## Tech Stack
- Selenium
- Python

## Challenges Faced
- The forms on the website were dynamic. By dynamic, I mean the value in the next field depends on the value which we selected earlier. For eg:- If we select a district then corresponding to the Judge's name was shown. And to get the information, I had to wait for some time so that the information is loaded.
- I wasn't able to crawl the complete website because the complete information because the crawler was running on my laptop only and it used to stop as soon as the wifi connection was lost.
- Keeping sufficient delay, to prevent the IP from getting blocked, as a consequence, the IP of complete college would get blocked.
- Extracting information from PDF which was written in Hindi to a format which can be processed. I tried a lot of OCR's but none of them gave proper results because of languages.

## Mistakes Done 
- Not making a counter which could keep a record of the point to which the crawling has been made and resume from there
- Not using ScrapingHub to run my project

## What did I enjoy?
It was a pretty challenging work with a time which I had to do in a small-time constraint without even knowing the technology stack. So, this was a great learning experience. Also, I enjoyed how I can automate the complete process of filling the form to extract the information.

## How it can be improved?
Currently, I can improve the project in a ton of ways
- We can use proxy servers, in python and crawl parallelly also protecting the IP from getting blocked.
- For extracting information I can apply a bit complex algorithm(using multiple API's), which might give us some better results.
- Making a counter, which would keep a record from where it left, and then when it restarts, it can start from that very point.
-  Instead of using Selenium, I could have used Scrapy + Splash or would have seen the function which is being called, which might help in increasing the crawling process and simplify it a lot using Scrappy.
- To crawl the complete website I can use ScrapingHub to run the crawler, which would do this task easily.

## What can be done differently now?
- Use Scrapy instead of Selenium 
- Deploy on ScrapingHub
- Using proxy servers to make requests

