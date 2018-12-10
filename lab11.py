#Lab 11
#Team 10 - M. Mariscal, C. Piwarski, W. Robleh

# One object of Class Room represents a room in the game map
class Room:

    # Constructor method for class Room
    def __init__(self, name='', desc='', north=None, south=None, \
        west=None, east=None, item = ''):
        self.name = name
        self.desc = desc
        self.beenVisited = False
        self.item = item

        # set exits
        self.north = north
        self.south = south
        self.west = west
        self.east = east

    # This method returns the name of the room
    def getName(self):
        return self.name

    # This method returns the items contained in the room
    def getItem(self):
      return self.item

    # This method sets the item for the room
    def setItem(self, item):
        self.item = item

    # This method removes an item from the room
    def removeItem(self, item):
        self.item = ''

    # This method returns the description of the room
    def getDesc(self):
        return self.desc
      
    def printExits(self):
      return_string = ''
      if self.north is not None:
        return_string += 'There is an exit to the north.\n'
      if self.south is not None:
        return_string += 'There is an exit to the south.\n'
      if self.east is not None:
        return_string += 'There is an exit to the east.\n'
      if self.west is not None:
        return_string += 'There is an exit to the west.\n'
      return return_string

    # This method returns the exit to the room based on the given direction
    def getExit(self, direction):
        if direction == 'n':
            return self.north
        elif direction == 's':
            return self.south
        elif direction == 'e':
            return self.east
        elif direction == 'w':
            return self.west
        else:
            return None

    # String method for class Room
    def __string__(self):
        return name + ' ' + desc + ' ' + exits

    # This method sets the name of the room
    def setName(self, name):
        self.name = name

    # This method sets the description of the room
    def setDesc(self, desc):
        self.desc = desc

    # This method sets the north exit for the room
    def setNorth(self, room):
        self.north = room

    # This method sets the south exit for the room
    def setSouth(self, room):
        self.south = room

    # This method sets the east exit for the room
    def setEast(self, room):
        self.east = room

    # This method sets the west exit for the room
    def setWest(self, room):
        self.west = room
        
    
    

# Class Player represents the player character
class Player:

    # Constructor method for Class Player
    def __init__(self, inventory=''):
        self.inventory = inventory
        self.location = None

    # This method returns the contents of the player's inventory
    def getInventory(self):
        return self.inventory

    # This method sets the location of the player
    def setLocation(self, location):
        self.location = location

    # This method sets the player inventory
    def setInventory(self, inventory):
        self.inventory = inventory

    # This method returns the room that the player is currently in
    def getLocation(self):
        return self.location
      
    # This method adds an item to your inventory
    def addInventory(self, itemToAdd):
      self.inventory += itemToAdd + ' '

    # This method prints out your inventory
    def printInventory(self):
        if self.inventory != '':
            printNow('You have: ' + self.inventory)
        else:
            printNow('You do not have anything.')
        if 'key' in self.inventory:
            printNow('This looks like a gate key for the prison')
        if 'lockpick' in self.inventory:
            printNow('A flimsy lockpick that criminals use. Better off\
 finding the key...')
        if 'cat' in self.inventory:
            printNow('Its a cat. Why did you take it???')

# Main function for the game
def Main():

    # Create Map 
    descCell = 'A cold, lonely prison cell, your home for the last 15 years for a crime you did not do!'
    descHall = 'The hallway of a prison. All your prisonmates are sound asleep. If you are loud, they will wake up and your cover will be blown. the'
    descKitchen = 'The kitchen for the prison. Where the food is disgusting.'
    descCloset = 'Closet in the Kitchen. It smells like something died in here. You are in the wrong location!'
    twoHall = 'Another hallway, the prison cat is sound asleep.'
    
    threeHall = 'Entering a third hallway. This place seemingly goes on forever.'
    twoCell = 'Entering another Cell. Your old prisonmate who assaulted you is reading a book. He waves as you walk through the cell.'
    
    guardRoom = 'You enter and see about three guards. What should you do now?'
    endDescription = 'This is the exit. You\'re happy to make it out Alive!'
    
    room1 = Room('Your cell', descCell)
    room2 = Room('Hall', descHall)
    room3 = Room('Kitchen', descKitchen)
    room4 = Room('Closet', descCloset)
    room5 = Room('2nd Hall', twoHall)
    room6 = Room('2nd Cell', twoCell)
    room7 = Room('3rd Hall', threeHall)
    room8 = Room('Guard Room', guardRoom )
    room9 = Room('Exit', endDescription)
    
    
    # Connect Rooms
    room1.setNorth(room2)
    room2.setSouth(room1)
    room2.setEast(room3)
    room3.setWest(room2)
    room3.setNorth(room4)
    room4.setSouth(room3)
    
    room3.setEast(room5)
    room5.setWest(room3)
    room5.setSouth(room6)#entering second cell
    room6.setNorth(room5) #would like this to be a gameOver later on - Wais
    room5.setEast(room7)#entering third hallway
    room7.setWest(room5)
    
    room7.setNorth(room8)
    room7.setEast(room9)
    
    room4.setItem('key')

    # Create Player
    player1 = Player()
    player1.setLocation(room1)

    # Define Extra Variables
    commands = ['examine', 'n', 's', 'e', 'w', 'get', 'exit', 'help']
    directions = ['n', 's', 'e', 'w']
    gameWon = False
    welcomeMessage = 'Welcome to Jailbreak\n You are a prisoner who is looking to escape from one of the most dangerous prisons in the world.\n'
    helpMessage = 'Type exit to quit your game.\n''To move your player type n,s,e,and w.\n''Type get to pick up objects\n''Type in examine to look at your surroundings.\n' 
    
    # print welcome message
    printNow(welcomeMessage)
    printNow(helpMessage)
    
    # Main game loop
    while gameWon != True:
        printNow(player1.getLocation().getName())
        printNow(player1.getLocation().getDesc())
        printNow(player1.getLocation().printExits())
        
        if player1.getLocation().getItem() != '':
            item = player1.getLocation().getItem()
            printNow('You see a: ' + item)

        # input loop. Keep asking for input until a valid command is received
        inputValidation = False
        while inputValidation == False:
            input = requestString('What would you like to do?')
            if input in commands:
              inputValidation = True
            else:
              printNow('Invalid Command. Try Again')

        # handle a request to exit
        if input == 'exit':
          printNow('Quitting game. Have a nice day.')
          break
        
        # handle a request for help
        if input == 'help':
            printNow(helpMessage) 
          
        # handle an examine request
        if input == 'examine':
            printNow(player1.getLocation().getDesc())
        
        # handle movement requests
        if input in directions:
          nextRoom = player1.getLocation().getExit(input)
          if nextRoom is not None:
            player1.setLocation(player1.getLocation().getExit(input))
          else:
            printNow('There is no exit in that direction')

        # handle a get request
        if input == 'get':
            getWhat = requestString('Get what?')
            roomItem = player1.getLocation().getItem()
            if roomItem == getWhat:
                player1.addInventory(roomItem)
                player1.getLocation().removeItem(roomItem)
                printNow('Took item: ' + roomItem)
            else:
                printNow('Invalid command. Try again.')
        
        
        #######If there is a better way of doing this let me know ######
        # game over conditions
        if player1.getLocation() == room9:
          gameWon = True
          print 'Congratulations, you escaped!'
        
       ##want to check if player is in guard room and tries to leave he will be caught and game ends.
        if player1.getLocation() == room8:
          gameWon = True
          print 'You entered the Guard\'s Room. You got caught!!!'
          

          
  
  
  
  
  