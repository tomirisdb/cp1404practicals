import wikipedia

title = 'Donald Trump'

page = wikipedia.page(title, auto_suggest=False)

print(page.title)
print(page.summary)
print(page.url)
