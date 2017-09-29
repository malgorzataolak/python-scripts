import urllib.request
import re

f=open('insert.txt','a')

MAIN_URL='http://www.napaluchu.waw.pl/czekam_na_ciebie/wszystkie_zwierzeta_do_adopcji'

def get_page_content(pageUrl):

	with urllib.request.urlopen(pageUrl) as r:
		html=r.read()
		strHTML=html.decode('utf-8')
		return strHTML


main_page=get_page_content(MAIN_URL)

regex=re.compile(r'zwierzeta_do_adopcji\/(\d+)')
result=regex.findall(main_page)
print(result)

for i in result:
	animal_url=MAIN_URL+'/'+i
	animal_page=get_page_content(animal_url)
	type_pattern=r'Gatunek:\s(.*?)<'
	type="Pies"
	#imie_pattern=r'<h5>\n\s(.*?)</h5>'#still doesn't work
	breed_pattern=r'Rasa:\s(.*?)</span>'
	gender_pattern=r'Płeć:\s(.*?)</span>'
	age_pattern=r'Wiek:\s(.*?)</span>'
	date_pattern=r'Data przyjęcia:\s(.*?)</span>'
	id_pattern=r'Nr ewidencyjny:\s(.*?)</span>'

	breed_find=re.findall(breed_pattern, animal_page)
	print(breed_find[0])
	if breed_find[0]!=breed:
		print("Poszukujemy tylko psow!")
	else:
		#imie=re.findall(imie_pattern,animal_page)
		#print(imie[0])
		breed=re.findall(breed_pattern, animal_page)
		print(breed[0])
		gender=re.findall(gender_pattern, animal_page)
		print(gender[0])	
		age=re.findall(age_pattern, animal_page)
		print(wiek[0])
		date=re.findall(date_pattern, animal_page)
		print(date[0])
		animal_id=re.findall(id_pattern, animal_page)
		print(animal_id[0])	
		value='INSERT INTO PSY (RASA, PŁEĆ, WIEK, DATA, ID) VALUES ('+breed[0]+', '+gender[0]+', '+age[0]+', '+date[0]+', '+animal_id[0]+');'
		print(value)
		f.write(value+'\n')

f.close()


