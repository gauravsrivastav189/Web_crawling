import re
import urllib.request

word=input("enter word ")
url="https://www.dictionary.com/browse/" + word
data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")

#print(data1)

m=re.search('<meta property="og:description" content=',data1)

#start=m.start()
start=m.end()

end=start + 200

new_string=data1[start:end]
#print(new_string)

m=re.search("See more", new_string)

end=m.start()-2

final=(new_string[0:end])
print(final)
