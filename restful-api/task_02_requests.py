import request
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    print(f"Status Code: {response.status_code}")

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    r = reguests.get('https://jsonplaceholder.typicode.com/todos/1')

    if response.status_code == 200:
        posts = r.json()
 
        posts_data = [{"id": post["id"], "title": post['title'], "body": post['body']} for post in posts]
        
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
             writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
             writer.writeheader()
             writer.writerows(posts_data)
             
        print("Posts have been saved to posts.csv.")
