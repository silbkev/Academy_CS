letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

word_list=[]
player_to_points={}
letter_to_points = dict(zip(letters,points))
letter_to_points.update({' ':0})
print(letter_to_points)

player_to_words = {'BLUE':['EARTH','ERASER','ZAP'],'TENNIS':['EYES','BELLY','COMA'],'EXIT':['MACHINE','HUSKY','PERIOD']}

def score_word(word):
  point_total=0
  for c in word.upper():
    sum = int(letter_to_points.get(c))
    point_total += sum

  return point_total

for name in player_to_words:
  player_points = 0
  word_list=player_to_words.get(name)
  for words in word_list:
    player_points=int(score_word(words))
  player_to_points.update({name:player_points})
print(player_to_points)





#print(score_word("brownie"))