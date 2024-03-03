import requests
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/AskReddit/'

response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

posts = soup.find_all('article', class_='w-full m-0')

posts_titles = []

for post in posts:
    post_title = post.find('a').text.strip()
    posts_titles.append(post_title)
    print(post_title)
