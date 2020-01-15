import requests

res=requests.get('https://www.goodreads.com/book/review_counts.json', params={"key": "5NN4kXAIDTjkjjIXWUCBA", "isbns": "9781632168146"})
data=res.json()
d=data['books']
print(d)