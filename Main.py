from model.User import User
from service import UserService

def convertTupleListToUsersList(tupleList):
    returnValue = []
    for tuple in tupleList:
        returnValue.append(User(tuple[0],tuple[1],tuple[2],tuple[3]))
    return returnValue

# Create table if it doesn't exist one
UserService.createTable()

# Save new user
user = User(0,'Luan','luangenro98@gmail.com','123')
UserService.save(user)

# Load created user
loadedTupleList = UserService.findById(14)
users = convertTupleListToUsersList(loadedTupleList)
loadedUser = users[0]
print(f"Loaded user's name: {loadedUser.name}")

# Update loaded user
loadedUser.name = 'Lucas'
UserService.update(loadedUser)
loadedUsersToupleList1 = UserService.findByName('Lucas')
print(f"Loaded user's name: {loadedUsersToupleList1[0][1]}")

# Delete user
UserService.delete(loadedUser.id)

# Find all users
loadedTupleList1 = UserService.findAll()