import re
import urllib.request

city=input("enter your city name ")
url="https://www.weather-forecast.com/locations/"+city+"/forecasts/latest"

data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")

#print(data1)

m=re.search('span class="phrase"',data1)

#start=m.start()
start=m.end()

end=start + 300

new_string=data1[start:end]

#print(new_string)

m=re.search("</span>",new_string)

end=m.start()-1

final=new_string[0:end]
print(final)
