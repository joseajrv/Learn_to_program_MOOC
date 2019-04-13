# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col, num_sprouts_eaten = 0):
        """
         (Rat, str, int, int) -> NoneType
         
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num_sprouts_eaten


    def set_location(self,row,col):
        """
        (Rat,int,int) -> NoneType
        
        
        Set the rat's row and col instance variables to the given row and column.
        Add one to the rat's instance variable num_sprouts_eaten.
        
        """
        self.row = row
        self.col = col

    def eat_sprout(self, row, col):
        """
        (Rat) -> NoneType        
        
        """
        self.num_sprouts_eaten += 1
        
    def __str__(self):
        """
        (Rat) -> str
        
        Return a string representation of the rat, in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts.
        
        ’J at (4,3) ate 2 sprouts.’
        """
        
        return ("{0} at ({1}, {2}) ate {3} sprouts.").format(self.symbol, self.row, self.col, self.num_sprouts_eaten)
        
   
class Maze:
    """ A 2D maze. """
    
    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2, num_sprouts_left = 0):
        """
         (Maze, list of list of str, Rat, Rat) -> NoneType
         
         
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        sprouts = 0
        for rows in maze:
            for col in rows:
                if col == SPROUT:
                    sprouts = sprouts + 1
        self.num_sprouts_left = sprouts
    
    def is_wall(self, row, col):
        """
        (Maze, int, int) -> bool
        
        Return True iff there is a wall at the given row and column of the maze.
        
        """
        return self.maze[row][col] == WALL
    
    def get_character(self, row, col):
        """
        (Maze, int, int) -> str
        
        Return the character in the maze at the given row and column. 
        If there is a rat at that location, then its character should be returned rather than HALL.
        
        """
        if(row == self.rat_1.row and col == self.rat_1.col):
            return RAT_1_CHAR
        elif (row == self.rat_2.row and col == self.rat_2.col):
            return RAT_2_CHAR
        else:
            return self.maze[row][col]
    
    def move(self, movingrat, vertical, horizontal):
        #Return a bool
        if(vertical == UP or vertical == DOWN or horizontal == LEFT or horizontal == RIGHT or vertical == NO_CHANGE or horizontal == NO_CHANGE):
            ##Check if wall
            if(self.is_wall(movingrat.row + vertical, movingrat.col + horizontal)):
                return False 
            else:
                #set old location stuff
                self.maze[movingrat.row][movingrat.col] = HALL

                #if sprout
                if(self.maze[movingrat.row + vertical][movingrat.col + horizontal] == SPROUT):  
                    movingrat.eat_sprout()
                    self.num_sprouts_left = self.num_sprouts_left -1
                    
                #move rat
                self.maze[movingrat.row + vertical][movingrat.col + horizontal] = movingrat.symbol
                movingrat.set_location(movingrat.row + vertical, movingrat.col + horizontal)
                return True
    
    
    def __str__(self):
        finalMazeString = ""
        for rows in self.maze:
            finalMazeString = finalMazeString + str(rows) + '\n'
        return (finalMazeString + str(self.rat_1) + '\n' + str(self.rat_2) )
    