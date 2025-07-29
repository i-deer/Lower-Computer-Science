#Importing the Random Integer Function#
import random

#Importing the time function (shows current hour and day as well as the timer function for the rounds)#
import datetime
import timeit

#Adding space for clarity#
def space():
  print("                                                     ")
  print("#########################################################")
  print("                                                     ")

#Users can add recommendations if they want#
def recommendations():
  recommendationSong = input("Enter a song you would like to add: ")
  recommendationSong = recommendationSong.upper()
  recommendationArtist = input("Enter the artist: ")
  recommendationArtist = recommendationArtist.upper()
  recommendationsFile = open("recommendations.txt", "a")
  recommendation = str(recommendationSong) + " , " + str(recommendationArtist)
  recommendationsFile.writelines(str(recommendation) + "\n")
  recommendationsFile.close()

  #Saves all the current songs and artists in an array#
  songs = [""]
  songFile = open("songs.txt","r")
  for line in songFile:
    x = len(line)
    songs.append(line[0:x-1])
  songs.remove(songs[0])
  songFile.close()

  artists = [""]
  artistFile = open("artists.txt","r")
  for line in artistFile:
    x = len(line)
    artists.append(line[0:x-1])
  artists.remove(artists[0])
  artistFile.close()

  #Checks to see if recommendation is in list#
  comparisons = []
  
  for index in range(len(songs)):
    comparison = str(songs[index]) + " , " + str(artists[index])
    comparisons.append(comparison)

  #Adds recommendation to the respective files#
  if recommendation not in comparisons:
    print("Thank you this song has been added")
    songFile = open("songs.txt","a")
    songFile.writelines(str(recommendationSong) + "\n")
    songFile.close()
    artistFile = open("artists.txt","a")
    artistFile.writelines(str(recommendationArtist) + "\n")
    artistFile.close()
      
  else:
    print("Someone else has already added this song.")
      
#The game itself#
def game():
  #Introduction#
  print("                                                     ")
  print("Welcome player to Noel's music quiz.")
  print("I'm I.T.U.N.E. and I'll quickly explain the rules.")
  space()
  print("Firstly this game is about testing your knowledge of different artists and their songs.")
  print("The game will not finish until you incorrectly guess twice; this means if you fail to guess a song (which you will have two guesses for) the game will end.")
  print("On the screen you'll be shown the intials of the song along with the song artist's name in full.")
  space()
  print("You get 3 points if you guess correctly the first time.")
  print("You get 1 point if you guess correctly the second time.")
  print("If you don't get it, you get 0 points.")
  print("There will also be bonus points depending how fast you guess it.")
  print("                                                     ")
  print("You will be able to see the time and your score for each round.")
  space()
  print("Let's begin and good luck!")
  space()

  #Stores the songs and artists in local variables#
  songs = [""]
  songFile = open("songs.txt","r")
  for line in songFile:
    x = len(line)
    songs.append(line[0:x-1])
  songs.remove(songs[0])
  songFile.close()

  artists = [""]
  artistFile = open("artists.txt","r")
  for line in artistFile:
    x = len(line)
    artists.append(line[0:x-1])
  artists.remove(artists[0])
  artistFile.close()

  #Defining variables needed for the game#
  numOfSongs = len(songs)
  rounds = 0
  points = 0
  guesses = 2
  answer = ""

  #Rounds for each game#
  while guesses != 0:
    from datetime import datetime
    print(datetime.now())
    space()
    rounds = rounds + 1
    print("Round: " + str(rounds))
    randomiser = random.randint(0, numOfSongs-1)
    selected = songs[randomiser]
    #Gets the first letter of each word in the song title#
    initials = ""
    initials = initials + selected[0]
    totalLetters = len(selected)
    for num in range(totalLetters):
        if selected[num] == " ":
          initials = initials + selected[num+1]
          
    #Outputs the artist and song to the user#
    print("This is the artist: " + str(artists[randomiser]))
    print("These are the intials of the song: " + str(initials))
    space()
    
    from timeit import default_timer
    start = default_timer()

    #User enters their first guess and points allocated accordingly#
    answer = input("Enter your first guess: ")
    answer = answer.upper()
    if answer == selected:
      duration = default_timer() - start
      print("                                                     ")
      print("How long it took you: " + str(duration))
      print("Well done!")
      points = points + 3
      guesses = 2
      #Points according to duration#
      if duration <= 10:
        points = points + 5
      elif duration <= 20:
        points = points + 3
      elif duration <= 30:
        points = points + 1
      print("Your score for this round: " + str(points))
      space()
    else:
      guesses = guesses - 1
      print("                                                     ")
      print("Oh no you have one guess left!")
      #User enters their second guess and points allocated accordingly#
      answer = input("Enter your second guess: ")
      answer = answer.upper()
      if answer != selected:
        guesses = guesses - 1
        print("That's incorrect, you have no guesses left.")
      else:
        duration = default_timer() - start
        print("                                                     ")
        print("How long it took you: " + str(duration))
        print("Well done! ")
        points = points + 1
        guesses = 2
        #Points according to duration#
        if duration <= 10:
          points = points + 5
        elif duration <= 20:
          points = points + 3
        elif duration <= 30:
          points = points + 1
        print("Your score for this round: " + str(points))
        space()
  #Message when game has ended#        
  print("You have finished the game, well done for all your efforts!")
  print("Your final score is " + str(points))
  username = input("Please enter your username: ")
  scoreFile = open("scores.txt","a")
  scoreFile.writelines(str(username) + ", " + str(points) + "\n")
  scoreFile.close()

  #Ranking the top 5 players#
  scores = []
  scoreFile = open("scores.txt","r")
  for line in scoreFile:
    score = ""
    for char in line:
      if char.isdigit():
        score = score + char
    scores.append(int(score))
    
  #Reverses list into descending order#
  scores.sort(reverse=True)
  space()

  #Outputs ranking to user
  print("The Top 5 Players:")
  space()
  for num in range (5):
    scoreFile = open("scores.txt","r")
    searchedscore = scores[num]
    for line in scoreFile:
        if str(searchedscore) in line:
          print(line)
    scoreFile.close() 

  #Offers them the choice to add a suggestion
  choice = input("Would you like to add a song to the game? Enter 'Y' for Yes or 'N' for No: ")
  choice = choice.upper()
  if choice == "Y":
    recommendations()

# Where user can sign up to the program # 
def signup():
  print("                                           ")
  username = input("Enter the username you want: ")
  userDetails = open("userDetails.txt", "r")
  for line in userDetails:
    if username in line:
      print("Sorry this username is taken, please choose another one.")
      signup()
  
  email = input("Enter the email address you are going to use: ")
  #Gives them a code#
  code = random.randint(0, 1000000)
  print("                                           ")
  print("This is your unique code: " + str(code) + " , you will only be able to see this once so keep it safe.")
  print("                                           ")
  #Adds new login to file#
  userDetails = open("userDetails.txt", "a")
  userDetails.writelines(str(username) + ", " + str(email) + ", " + str(code) + "\n")
  userDetails.close()
  login()

# Where user can log into the program #
def login():
  validDomains =["@gmail.com","@yahoo.com","@yahoo.co.uk","@gmail.co.uk", "@outlook.com","@outlook.co.uk"]
  print("Hello and welcome to Noel's Music Quiz")
  print("                                           ")
  login = input("If you have an account, enter 'Y' else enter 'N: ")
  login = login.upper()
  # Ensures they are a validated user
  if login == "Y":
    print("                                           ")
    email = input("Please enter your email address: ")
    username = input("Please enter you name: ")
    code = input("Please enter your digit code: ")
    print("                                           ")
    
    # Checks whether they are banned
    banned = open("bannedList.txt","r")
    for line in banned:
      if line == email:
        print("Sorry, you are banned from this game.")
        exit()
    banned.close()
        
    # Checks whether they are using a valid domain name
    passCheck = ""
    for num in range(6):
      if validDomains[num] in email:
        passCheck = "TRUE"
        StopIteration()
  
    if passCheck != "TRUE":
      print("Warning unauthorised email domain!")
      exit()

    # Checks whether they are an existing player
    userDetails = open("userDetails.txt", "r")
    for line in userDetails:
      if username in line and email in line and code in line:
        passCheck = "TRUE"
    userDetails.close()

    if passCheck == "TRUE":
      print("Ok, you are able to play the game!")
      game()
    
  # Takes them to the sign up page
  elif login == "N":
    signup()
  else:
    print("I apologise, this is an illogical input. Please try again.")
    login()


login()
