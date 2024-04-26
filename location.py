import phonenumbers
#pip install phonenumbers
import opencage
#pip install opencage
import folium
#pip install folium

#insert phone number here ..and include country code
#you can also have the phone number in another python file and import it
number = ''

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))


from opencage.geocoder import OpenCageGeocode
#go to opencage.com .. sign up to  get a new account and paste your api here
#paste your API HERE!!
key = ''


geocoder = OpenCageGeocode(key)
query  = str(location)
results =  geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)


myMap = folium.Map(location = [lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup = location).add_to(myMap)

#html file ..open with live server or any other browser
myMap.save("mylocation.html")