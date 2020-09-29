destinations = [
    'Paris, France',
    'Shanghai, China',
    'Los Angeles, USA',
    'São Paulo, Brazil',
    'Cairo, Egypt'
]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[], [], [], [], []]


def get_destination_index(destination):
  for i in destinations:
      if i == destination:
        destination_index = destinations.index(i)
        return destination_index
        break

def get_traveler_location(traveler):
  traveler_destination =  traveler[1]
  traveler_destination_index=get_destination_index(traveler_destination)
  return traveler_destination, traveler_destination_index

def add_attraction(destination,attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
    return attractions
  except:
    print("Input Missing!")
    return

def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  attraction_tags = []
  possible_attraction = []
  for i in attractions_in_city:
    possible_attraction = i
    attraction_tags = i[1]
    for e in interests:
      if e in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

def get_attractions_for_traveler(traveler):
  traveler_destination=traveler[1]
  traveler_interests=traveler[2]
  traveler_attractions=find_attractions(traveler_destination,traveler_interests)
  interests_string = '"Hi ' + str(traveler[0]) + ", we think you'll like these places around " + str(traveler[1]) + ': '


  for e in traveler_attractions:
    interests_string = interests_string + e + '"'
    return interests_string 

try:
  get_destination_index("Los Angeles, USA")
  get_destination_index("Paris, France")
  get_traveler_location(test_traveler)
  add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
  add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
  add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
  add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
  add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
  add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
  add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
  add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
  add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
  add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
  add_attraction('Los Angeles, USA',['Venice Beach', ['beach']])
  la_arts = find_attractions('Los Angeles, USA',['art'])
  #print(la_arts)
  #get_destination_index()
  smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
  print(smills_france)
  #get_destination_index()

except:
  print("Function get_destination_index() expects one parameter!")