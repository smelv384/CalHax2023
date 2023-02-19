reviews = dict()
score = dict()

pickedRoom = ""

# allows user to choose a room to rate and review
def chooseRoomToRateAndReview(room):
    pickedRoom = room

# rate the picked room out of 5
def rate():
    userScore = input("Please rate the quality of your rest in the room out of 5!: ")
    if userScore > 5 or userScore < 1:
        print("Please enter a valid number.")
    else:
        score[pickedRoom] = list()
        score[pickedRoom].append(userScore)

# write a review for the room
def writeReview():
    reviews[pickedRoom] = input("How was the room? Let us know!: ")

# gets the average score of a room
def getAverageRoomScore(room):
    averageScore = sum(score[room]) / len(score[room])
    return averageScore

# gets a list of reviews of a room
def getRoomReview(room):
    return reviews[room]