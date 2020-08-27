
import requests 
#Get parameters from the user

#Get their sign (List of all signs - aries, taurus, gemini, cancer,
#leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius and pisces.)

sign = input("Please enter your zodiac sign: ")

#Get the horoscope day (today, tomorrow, or yesterday)

day = input("Please enter the horoscope day (today, tomorrow, or yesterday): ")


#parameters for the HTTP request

params = (

	('sign', sign),
	('day', day)

	)

#make the request

response = requests.post('https://aztro.sameerkumar.website/', params=params)

json = response.json()


print("\nHoroscope for",json.get('current_date'),"\n")
print(json.get('description'),'\n')
print('Compatibility:',json.get('compatibility'))
print('Mood:', json.get('mood'))
print('Color:', json.get('color'))
print('Lucky Number:', json.get('lucky_number'))
print('Lucky Time:', json.get('lucky_time'),"\n")









