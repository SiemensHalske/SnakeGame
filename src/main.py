"""
    Snake game
    -----------
    This program is an implementation of the classic Snake game using Python
    and the PyQt library. The game is built using the QGraphicsView and
    QGraphicsScene classes.

    The game follows the standard Snake game rules - the snake grows in size
    when it eats food, and the game ends if the snake collides with itself
    or the wall.

    The game also features a quadtree data structure for the collision
    detection in the game world. This data structure allows for a more
    efficient detection of potential collisions in the game world.
    The snake direction is controlled by the arrow keys on the keyboard
    or the WASD keys.
"""


from json import JSONDecodeError, dump, load
from os import path
from sys import exit as sys_exit, argv
from time import sleep
from random import random, randint
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGraphicsScene,
                             QGraphicsView, QGraphicsRectItem, QLabel,
                             QVBoxLayout, QMessageBox, QAction,
                             QWidget, QHBoxLayout, QInputDialog, QListWidget,
                             QDialog, QPushButton
                             )
from PyQt5.QtCore import QEvent, QObject


SCOREBOARD_PATH = 'highscores.json'
GAME_SPEED = 100  # initial speed for the game in milliseconds


class Node:
    """
        Node class for the A* algorithm.
        The Node class is used to represent a node in the A* algorithm.
        It is used to store the parent node, the position, and the g, h, and
        f values of the node. The g value represents the cost of the path from
        the start to the current position, the h value represents the
        estimated cost of the path from the current position to the goal, and
        the f value is the sum of the g and h values and is used to determine
        the most promising path to explore next.

        The Node class is used in the implementation of the A* algorithm to
        find the shortest path between two points in the game world. It is
        widely used in many fields, including games, robotics, and geographical
        information systems. The algorithm uses a heuristic function to
        estimate the cost of reaching the goal from the current position and
        makes use of this estimate to find the most promising path to explore.
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(quadtree, start, end):
    """
        A* (A-Star) algorithm implementation to find the shortest path.
        The A* (A-Star) algorithm is an informed search algorithm that is
        used to find the shortest path between two points. It is widely
        used in many fields, including games, robotics, and geographical
        information systems. The algorithm uses a heuristic function to
        estimate the cost of reaching the goal from the current position
        and makes use of this estimate to find the most promising path to
        explore.

        The A* algorithm uses a combination of the g, h, and f values to
        determine the most promising path. The g value represents the
        cost of the path from the start to the current position, and the
        h value represents the estimated cost of the path from the current
        position to the goal. The f value is the sum of the g and h values
        and is used to determine the most promising path to explore next.

        The A* algorithm uses a priority queue to explore the most promising
        path first and gradually explores the other paths based on the f value.

        The implementation of the A* algorithm consists of the following steps:
            1. Create a start node and an end node.
            2. Initialize the open and closed lists.
            3. Add the start node to the open list.
            4. Loop until the end node is found or the open list is empty.
            5. Remove the node with the lowest f value from the open list
               and add it to the closed list.
            6. Generate the child nodes of the current node and calculate
               their f, g, and h values.
            7. Loop through the child nodes and add them to the open list
               if they are not already on the closed list and have a lower
               f value than an existing node in the open list.
            8. Return the path to the end node if found.

        Parameters:
        -----------
            quadtree: Quadtree
                        A Quadtree object representing the quadtree in the
                        game world.

            start: tuple
                        A tuple representing the start position in the
                        game world.

            end: tuple
                        A tuple representing the end position in the
                        game world.

        Returns:
        --------
            path: list
                        A list representing the shortest path between the start
                        and end positions in the game world.
    """

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize the open and closed lists
    open_list = []
    closed_list = []

    open_list.append(start_node)

    # Loop until the end node is found
    while len(open_list) > 0:
        # Get node with the lowest f value
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Remove the current node from the open list and add it to
        # the closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the end node
        if current_node.position == end_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []

        # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1]
            )

            # Make sure the new node is within the bounds of the game world
            if not quadtree.is_open_space(node_position[0], node_position[1]):
                continue

                # Create a new node
                new_node = Node(current_node, node_position)

                # Add it to the list of children
                children.append(new_node)

            # Loop through children
            for child in children:
                # Child is on the closed list
                if child in closed_list:
                    continue

                # Calculate the f, g, and h values
                child.g = current_node.g + 1
                child.h = (
                    (child.position[0] - end_node.position[0]) ** 2) + \
                    ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already on the open list
                for open_node in open_list:
                    conds = [
                        child.position == open_node.position,
                        child.g > open_node.g
                    ]

                    if all(conds):
                        break
                else:
                    # Add the child to the open list
                    open_list.append(child)


class Quadtree:
    """
        Quadtree data structure to represent the game world.
        The Quadtree is used to store the game objects in the game world. It
        uses a hierarchical tree structure to represent the game world, which
        makes collision detection more efficient.

        The Quadtree recursively divides the game world into four quadrants,
        and can store the game objects in each quadrant based on their
        position in the game world.

        What is a Quadtree?
        -------------------
        A quadtree is a tree data structure in which each internal node has
        exactly four children. Quadtrees are the two-dimensional analog of
        octrees and are most often used to partition a two-dimensional
        space by recursively subdividing it into four quadrants or regions. The
        regions may be square or rectangular, or may have arbitrary shapes.

        This data structure is used in many computational geometry algorithms
        and applications, such as the point location problem and image
        processing. The sub regions may be referred to as quads. Each
        node in the tree contains four nodes, which represent the four
        quadrants of the space.

        It should be noted that the term "quadtree" is often used to refer
        to the tree data structure itself, not the quadrants.
    """

    def __init__(self, bounds, level=0):
        """
            Initialize the quadtree with the given bounds and level.
            The bounds parameter is a tuple representing the bounds of the
            quadtree in the game world, and the level parameter represents the
            level of the quadtree.

            Parameters:
            -----------
                bounds: tuple
                    A tuple representing the bounds of the quadtree in the game
                    world.

                level: int
                    An integer representing the level of the quadtree.

            Returns:
            --------
                None
        """
        self.bounds = bounds
        self.level = level
        self.objects = []
        self.nodes = [None, None, None, None]

    def clear(self):
        """
            Clear the quadtree by removing all the objects and nodes from the
            quadtree.

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        self.objects = []
        self.nodes = []

    def split(self):
        """
            Split the quadtree into four quadrants.

            1. top-right quadrant
            2. top-left quadrant
            3. bottom-left quadrant
            4. bottom-right quadrant

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        try:
            subWidth = (self.bounds[2] - self.bounds[0]) / 2
            subHeight = (self.bounds[3] - self.bounds[1]) / 2
            x, y = self.bounds[0], self.bounds[1]

            self.nodes = [
                Quadtree((x + subWidth, y, x + subWidth * 2, y +
                          subHeight), self.level + 1),  # top-right
                Quadtree((x, y, x + subWidth, y + subHeight),
                         self.level + 1),  # top-left
                Quadtree((x, y + subHeight, x + subWidth, y + \
                          subHeight * 2), self.level + 1),  # bottom-left
                Quadtree((x + subWidth, y + subHeight, x + subWidth * 2,
                          y + subHeight * 2), self.level + 1)  # bottom-right
            ]
        except ZeroDivisionError:
            print(
                'Dividing by zero is not allowed. This is due to the fact '
                'that the new object would be at the exact corner of the '
                'scene.'
            )

    def get_index(self, obj):
        """
            Determine the index for the given object.

            The index is used to determine in which quadrant the object should
            be placed based on the object's position.

            0 | 1
            -----
            2 | 3

            0: top-right
            1: top-left
            2: bottom-left
            3: bottom-right

            Parameters:
            -----------
                obj: tuple
                        A tuple representing the position of the object in the
                        game world.

            Returns:
            --------
                index: int
                        An integer representing the index of the quadrant.
        """
        try:
            index = -1
            vertical_midpoint = self.bounds[0] + \
                (self.bounds[2] - self.bounds[0]) / 2
            horizontal_midpoint = self.bounds[1] + \
                (self.bounds[3] - self.bounds[1]) / 2

            top_half = obj[1] < horizontal_midpoint
            bottom_half = obj[1] >= horizontal_midpoint
            left_half = obj[0] < vertical_midpoint
            right_half = obj[0] >= vertical_midpoint

            if top_half:
                if right_half:
                    index = 0
                elif left_half:
                    index = 1
            elif bottom_half:
                if left_half:
                    index = 2
                elif right_half:
                    index = 3

            return index
        except ZeroDivisionError:
            print(
                'Dividing by zero is not allowed. This is due to the fact '
                'that the new object would be at the exact corner of the '
                'scene.'
            )

    def insert(self, obj):
        """
            Insert the given object into the quadtree.
            The insert method is used to insert an object into the quadtree. If
            the quadtree is already at its maximum capacity, the quadtree is
            split into four quadrants.

            Parameters:
            -----------
                obj: tuple
                        A tuple representing the position of the object in the
                        game world.

            Returns:
            --------
                None
        """
        try:
            if self.nodes[0] is not None:
                index = self.get_index(obj)
                if index != -1:
                    self.nodes[index].insert(obj)
                    return

            self.objects.append(obj)

            if len(self.objects) > 4 and self.level < 4:
                if not self.nodes[0]:
                    self.split()

                i = 0
                while i < len(self.objects):
                    index = self.get_index(self.objects[i])
                    if index != -1 and self.nodes[index] is not None:
                        self.nodes[index].insert(self.objects.pop(i))
                    else:
                        i += 1
        except ZeroDivisionError:
            print(
                'Dividing by zero is not allowed. This is due to the fact '
                'that the new object would be at the exact corner of the '
                'scene.'
            )

    def is_open_space(self, x, y):
        """
            Check if the given position is an open space.
            An open space is a space in the game world that is not occupied by
            any object.

            Parameters:
            -----------
                x: int
                        An integer representing the x-coordinate of the
                        position.

                y: int
                        An integer representing the y-coordinate of the
                        position.

            Returns:
            --------
                True, if the position is an open space, False otherwise.
        """
        try:
            field_bound_conds = [
                x < self.bounds[0],
                x >= self.bounds[2],
                y < self.bounds[1],
                y >= self.bounds[3]
            ]

            if any(field_bound_conds):
                return False

            if self.nodes:
                index = self.get_index((x, y))
                # Sicherheitsüberprüfung hinzugefügt
                if index != -1 and self.nodes[index] is not None:
                    return self.nodes[index].is_open_space(x, y)

            for obj in self.objects:
                if obj[0] == x and obj[1] == y:
                    return False

            return True
        except ZeroDivisionError:
            print(
                'Dividing by zero is not allowed. This is due to the fact '
                'that the new object would be at the exact corner of the '
                'scene.'
            )

    def retrieve(self, return_objects, obj):
        """
            Retrieve the objects that could potentially collide with the
            given object.

            The retrieve method is used to retrieve the objects that could
            potentially collide with the given object. It returns the objects
            that could potentially collide with the given object as a list.

            Parameters:
            -----------
                return_objects: list
                            A list of objects that could potentially collide
                            with the given object.

                obj: tuple
                            A tuple representing the position of the object in
                            the game world.
        """
        try:
            index = self.get_index(obj)
            if index != -1 and self.nodes:
                self.nodes[index].retrieve(return_objects, obj)

            return_objects.extend(self.objects)

            return return_objects
        except ZeroDivisionError:
            print(
                'Dividing by zero is not allowed. This is due to the fact '
                'that the new object would be at the exact corner of the '
                'scene.'
            )


class Food:
    """
        Initialize the Food object with the given quadtree, scene width,
        and scene height.

        The quadtree parameter is used to store the food object in the game
        world. The scene width and scene height parameters are used to
        determine the bounds of the quadtree in the game world.

        Parameters:
        -----------
            quadtree: Quadtree
                        A Quadtree object representing the quadtree in the
                        game world.

            scene_width: int
                        An integer representing the width of the game
                        world.

            scene_height: int
                        An integer representing the height of the game
                        world.

        Returns:
        --------
            None
    """

    def __init__(self,
                 quadtree,
                 scene_width=300,
                 scene_height=300,
                 ):
        self.position = (0, 0)
        self.quadtree = quadtree
        self.scene_width = scene_width
        self.scene_height = scene_height
        self.golden_apple_chance = 0.1  # Wahrscheinlichkeit für goldenen Apfel
        self.food_details = self.spawn()

        print(
            f"spawned food at: {self.position}",
            f"food type: {self.food_type}",
            f"value: {self.value}",
            f"food details: {self.food_details}"
        )

    def get_food_details(self):
        """
            Return a string representation of the food object.
            The get_food_details method is used to return a string
            representation of the food object. The string representation
            of the food object includes the position, food type, and
            value of the food object.

            Parameters:
            -----------
                None

            Returns:
            --------
                str
                    A string representation of the food object.
        """
        return self.food_details

    def decide_food_type(self):
        return 'special' if random() < self.golden_apple_chance else 'normal'

    def spawn(self):
        """
            Generate the random position for the food object in the game world.

            The spawn method is used to generate the random position for the
            food object in the game world. It uses the quadtree to check if the
            position is an open space. If the position is not an open space,
            the method will continue generating new positions until an open
            space is found.

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        while True:
            x = randint(0, (self.scene_width // 20) - 1) * 20
            y = randint(0, (self.scene_height // 20) - 1) * 20

            if self.quadtree.is_open_space(x, y):
                self.position = (x, y)
                self.food_type = self.decide_food_type()
                self.assign_value()
                return {"position": self.position,
                        "food_type": self.food_type,
                        "value": self.value
                        }

    def assign_value(self):
        """
            Assign the value for the food object.

            The assign_value method is used to assign the value for the food
            object. The value is used to determine how many times the snake
            will grow when it eats the food.

            There is either a 20% probability of assigning a value of 2 to the
            food object or a 80% probability of assigning a value of 1 to the
            food object.

            The value is assigned using a probability of 20% to 80% by
            generating a random number. If the random number is less than 0.2,
            the value of the food object will be 2. If the random number is
            greater than or equal to 0.2, the value of the food object will be
            1 instead.

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        if self.food_type == 'special':
            self.value = 5  # Spezialnahrung gibt mehr Punkte
        else:
            self.value = 2 if random() < 0.2 else 1


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Settings')
        layout = QVBoxLayout()

        # Füge Einstellungselemente zum Layout hinzu
        layout.addWidget(QLabel('Settings Panel'))
        self.pushButton = QPushButton('Option 1')
        self.pushButton2 = QPushButton('Option 2')
        layout.addWidget(self.pushButton)
        layout.addWidget(self.pushButton2)

        self.setLayout(layout)
        self.connect_signals()

    def connect_signals(self):
        self.pushButton.clicked.connect(self.slot_method)
        self.pushButton2.clicked.connect(self.slot_method_2)

    def slot_method(self):
        print("Option 1")

    def slot_method_2(self):
        print("Option 2")


class SnakeGame(QMainWindow):
    """
        SnakeGame class is responsible for setting up the game and managing
        the game state. The SnakeGame class inherits from the QMainWindow
        class and implements the logic for the snake game using the PyQt
        library. The game is built using the QGraphicsView and QGraphicsScene
        classes.

        The game follows the standard Snake game rules, the snake grows in
        size when it eats food, and the game ends if the snake collides with
        itself or the wall. The snake direction is controlled by the arrow
        keys on the keyboard or the WASD keys.

        The SnakeGame class is responsible for managing the game state and
        updating the game world. It uses the Quadtree data structure for the
        collision detection in the game world, which allows for a more
        efficient detection of potential collisions.

        The SnakeGame class initializes the game world and sets up the
        graphical user interface for the game using the QGraphicsView and
        QGraphicsScene classes. The game world is divided into a grid with a
        size of 300x300 pixels, and the snake and food objects are placed
        within the grid.

        Parameters:
        -----------
            None

        Returns:
        --------
            None
    """

    def __init__(self, screen_width=800, screen_height=800):
        super().__init__()

        self.game_area_width = screen_width
        self.game_area_height = screen_height

        self.keyPressEater = KeyPressEater(self)
        self.installEventFilter(self.keyPressEater)

        self.gameOver_flag = False
        self.autopilot_enabled = False
        self.score = 0
        self.highscores = []
        self.direction = Direction.Right
        self.nextDirection = self.direction
        self.snake_positions = [(100, 100)]
        self.quadtree = Quadtree(
            (0, 0, self.game_area_width, self.game_area_height))
        self.food = None
        self.initUI()
        self.initGame()

    def initUI(self, set_focus: bool = True):
        """
            Set up the graphical user interface for the game.
            The initUI method is responsible for setting up the graphical
            user interface for the game using the PyQt library. It creates the
            main window for the game and adds the necessary widgets and layout
            to the window.

            The main window contains a QLabel for the score, a QLabel for the
            game over text, a QGraphicsView for the game world, and a
            QVBoxLayout to manage the layout of the widgets.

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        self.setWindowTitle("Snake Game")
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QHBoxLayout()
        self.gameLayout = QVBoxLayout()

        # Score and Game Over Labels
        self.scoreLabel = QLabel("Score: 0")
        self.scoreLabel.setFont(QFont("Arial", 16))
        self.gameOverLabel = QLabel("Game Over")
        self.gameOverLabel.setFont(QFont("Arial", 20, QFont.Bold))
        self.gameOverLabel.hide()

        # Layout for labels
        self.labelLayout = QVBoxLayout()
        self.labelLayout.addWidget(self.scoreLabel)
        self.labelLayout.addWidget(self.gameOverLabel)

        # Add label layout to game layout
        self.gameLayout.addLayout(self.labelLayout)

        # GraphicsView for the game world
        self.scene = QGraphicsScene(
            0, 0, self.game_area_width, self.game_area_height)
        self.view = QGraphicsView(self.scene)
        self.view.setFixedSize(int(self.scene.width()) + 2,
                               int(self.scene.height()) + 2)
        self.gameLayout.addWidget(self.view)

        # Scoreboard for the highscores
        self.scoreboard = QListWidget()
        self.scoreboard.setMaximumWidth(200)

        # Add game layout to main layout
        self.mainLayout.addLayout(self.gameLayout)
        self.mainLayout.addWidget(self.scoreboard)

        self.centralWidget.setLayout(self.mainLayout)

        # Setup the menu
        menubar = self.menuBar()

        # Menu "Game"
        fileMenu = menubar.addMenu('Game')
        restartAction = QAction('Restart', self)
        restartAction.triggered.connect(self.restartGame)
        fileMenu.addAction(restartAction)
        closeAction = QAction('Close', self)
        closeAction.triggered.connect(self.close)
        fileMenu.addAction(closeAction)

        # Menu "Preferences"
        prefMenu = menubar.addMenu('Preferences')
        settingsAction = QAction('Settings-Window', self)
        settingsAction.triggered.connect(self.showSettings)
        prefMenu.addAction(settingsAction)

        if set_focus:
            # Setze Fokus
            self.setFocusPolicy(Qt.StrongFocus)
            self.view.setFocusPolicy(Qt.StrongFocus)
            self.view.setFocus()

    def move_settings_window(self):
        # Calculate the position of the settings window
        mainWindowGeometry = self.frameGeometry()
        settingsWidth = self.settingsWindow.frameGeometry().width()
        settingsHeight = self.settingsWindow.frameGeometry().height()

        # Center the settings window next to the main window
        term_1 = int(mainWindowGeometry.left() - settingsWidth)
        sub_term_2 = mainWindowGeometry.top()
        sub_term_3 = (mainWindowGeometry.height() - settingsHeight)
        settings_y = sub_term_2 + sub_term_3 // 2

        self.settingsWindow.move(term_1, settings_y)

    def toggle_autopilot(self):
        self.autopilot_enabled = not self.autopilot_enabled

    def update_direction_based_on_path(self, next_step):
        # If there is no path, continue with the current direction
        if not next_step:
            return

        head_x, head_y = self.snake_positions[0]
        next_x, next_y = next_step

        # Calculate the direction to the next step
        dx = next_x - head_x
        dy = next_y - head_y

        # Check if we need to turn to the left, right, up or down
        if dx == 1 and self.direction != Direction.Left:
            self.nextDirection = Direction.Right
        elif dx == -1 and self.direction != Direction.Right:
            self.nextDirection = Direction.Left
        elif dy == 1 and self.direction != Direction.Up:
            self.nextDirection = Direction.Down
        elif dy == -1 and self.direction != Direction.Down:
            self.nextDirection = Direction.Up

    def showSettings(self):
        if not hasattr(self, 'settingsWindow'):
            self.settingsWindow = SettingsWindow(self)

        self.move_settings_window()
        self.settingsWindow.show()

    def initGame(self):
        """
            Initialize the game state and start the game.
            The initGame method is responsible for initializing the game state
            and starting the game. It creates the snake and food objects in the
            game world and starts the game timer to update the game state.

            The game state is updated using a timer, which calls the updateGame
            method to update the game world and handle the game logic. The game
            speed is determined by the GAME_SPEED constant, which specifies the
            interval between game updates. The speed of the game increases as
            the snake grows in size. (see adjustSpeed method)

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        self.loadScores()
        self.updateScoreboard()
        self.food = Food(self.quadtree)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateGame)
        self.timer.start(GAME_SPEED)
        self.addFood()
        self.updateSnake()

    def updateGame(self):
        """
            Update the game state and handle the game logic when the timer
            triggers the timeout signal. The updateGame method is called by
            the timer when it triggers the timeout signal. It updates the game
            state and handles the game logic by updating the snake position,
            checking for collisions, and handling the game over state.

            If the snake collides with itself or the wall, the game over state
            is triggered, and the game stops updating. If the snake eats the
            food object, the score is updated, and the snake grows in size.

            The method also handles the input from the keyboard, allowing the
            player to change the direction of the snake using the arrow keys
            or the WASD keys.

            The autopilot logic is also handled here. The game will use the
            A* algorithm to find the shortest path to the food, and the snake
            will automatically follow the path. If the path to the food is not
            available, the snake will continue in its current direction and
            the normal controls will be enabled.

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        if self.autopilot_enabled:
            path_to_food = self.calculate_path_to_food()
            if path_to_food:  # Wenn ein Pfad gefunden wurde
                self.update_direction_based_on_path(path_to_food)
            else:
                pass
        else:
            self.direction = self.nextDirection

        new_head_pos = self.calculateNewHeadPosition()

        if self.checkCollisions(new_head_pos):
            self.gameOver()
            return

        self.snake_positions.insert(0, new_head_pos)

        if new_head_pos == self.food.position:
            self.score += self.food.value
            self.scoreLabel.setText(f"Score: {self.score}")
            for _ in range(self.food.value):
                self.snake_positions.append(self.snake_positions[-1])
            self.addFood()
            self.adjustSpeed()
        else:
            self.snake_positions.pop()

        self.updateSnake()

    def calculate_path_to_food(self):
        start = (self.snake_positions[0][0] // 20,
                 self.snake_positions[0][1] // 20)
        end = (self.food.position[0] // 20, self.food.position[1] // 20)

        path = astar(self.quadtree, start, end)
        if path:
            return path[1:]
        else:
            return []

    def calculateNewHeadPosition(self):
        """
            Calculate the new position for the snake head based on the
            current direction. The calculateNewHeadPosition method is used to
            calculate the new position for the snake head based on the current
            direction. It determines the new position based on the current
            direction and the position of the snake head.

            Updates the x or y coordinate based on the direction:
                - 'left': decrements the x-coordinate by 20
                - 'right': increments the x-coordinate by 20
                - 'up': decrements the y-coordinate by 20
                - 'down': increments the y-coordinate by 20

            Parameters:
            -----------
                None

            Returns:
            --------
                tuple
                    A tuple representing the new position for the snake head.
        """
        head_x, head_y = self.snake_positions[0]
        if self.direction == Direction.Left:
            return (head_x - 20, head_y)
        elif self.direction == Direction.Right:
            return (head_x + 20, head_y)
        elif self.direction == Direction.Up:
            return (head_x, head_y - 20)
        elif self.direction == Direction.Down:
            return (head_x, head_y + 20)

    def checkCollisions(self, new_head_pos):
        """
            Check for collisions with the boundaries or the snake's body.
            The checkCollisions method is used to check for collisions with the
            boundaries or the snake's body. It determines if the snake has
            collided with the boundaries of the game world or itself based on
            the new position of the snake's head.

            The boundaries of the game world are the edges of the game window.
            The game world is divided into a grid with a size of
            300x300 pixels, and the boundaries are represented by the edges
            of the grid.

            It checks the following:
                - The new position of the snake's head is within the
                    boundaries of the game world.
                - The new position of the snake's head does not collide with
                    the snake's body.

            Parameters:
            -----------
                new_head_pos: tuple
                                A tuple representing the new position of the
                                snake's head.
        """
        if not (0 <= new_head_pos[0] < 600 and 0 <= new_head_pos[1] < 600):
            return True
        if new_head_pos in self.snake_positions:
            return True
        return False

    def gameOver(self):
        close_on_no = False

        name, ok = QInputDialog.getText(self, "Highscore", "Enter your name:")
        if ok and name:
            # Füge den neuen Score zur Liste hinzu
            self.highscores.append({"name": name, "score": self.score})
            self.saveScores()  # Speichere die aktualisierte Liste
            self.updateScoreboard()

        returnValue = self.show_restart_dialog()
        if returnValue == QMessageBox.Yes:
            self.restartGame()
        else:
            if close_on_no:
                self.close()
            self.timer.stop()

    def show_restart_dialog(self) -> bool:
        """Show the restart dialog."""
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Game Over")
        msgBox.setText("Would you like to restart?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            return True
        return False

    def restartGame(self):
        self.score = 0
        self.direction = Direction.Right
        self.nextDirection = self.direction
        self.snake_positions = [(100, 100)]
        self.food = None
        self.quadtree.clear()
        self.gameOverLabel.hide()
        self.scoreLabel.setText("Score: 0")
        self.initGame()
        self.updateSnake()

    def loadScores(self):
        try:
            if not path.exists(SCOREBOARD_PATH):
                with open(SCOREBOARD_PATH, "w") as file:
                    dump([], file)
                self.highscores = []
            else:
                with open(SCOREBOARD_PATH, "r") as file:
                    self.highscores = load(file)
        except JSONDecodeError:
            self.highscores = []

    def saveScores(self):
        with open("highscores.json", "w") as file:
            dump(self.highscores, file)

    def updateScoreboard(self):
        scores = self.highscores
        self.scoreboard.clear()

        for score in sorted(scores, key=lambda x: x["score"], reverse=True):
            self.scoreboard.addItem(f"{score['name']}: {score['score']}")

    def addFood(self):
        """
            Add the food object to the game world.
            The addFood method is used to add the food object to the game
            world. It generates the random position for the food object
            and updates the food item on the scene.

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        self.food = Food(
            self.quadtree,
            self.scene.width(),
            self.scene.height()
        )
        self.updateFoodOnScene()

    def updateFoodOnScene(self):
        """
            Update the food item on the scene. The updateFoodOnScene method is
            used to update the food item on the scene. It updates the position
            of the food item on the scene based on the position of the food in
            the game world.

            If the food item already exists on the scene, it updates the
            position of the food item. Otherwise, it creates a new
            QGraphicsRectItem for the food item and adds it to the scene.
            It updates the position of the food item on the scene based
            on the position of the food in the game world.

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        if hasattr(self, 'food_item') and self.food_item in self.scene.items():
            self.scene.removeItem(self.food_item)

        color = "red" if self.food.food_type == 'normal' else "gold"
        self.food_item = QGraphicsRectItem(
            self.food.position[0], self.food.position[1], 20, 20)
        self.food_item.setBrush(QColor(color))
        self.scene.addItem(self.food_item)

    def updateSnake(self):
        """
            Update the snake items on the scene.
            The updateSnake method is used to update the snake items on the
            scene. It updates the position of the snake items on the scene
            based on the position of the snake in the game world.

            If the snake items already exist on the scene, it updates the
            position of the snake items. Otherwise, it creates a new
            QGraphicsRectItem for each snake item and adds it to the scene.

            The method also updates the quadtree with the positions of the
            snake items in the game world.

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        self.scene.clear()
        for pos in self.snake_positions:
            self.scene.addRect(pos[0], pos[1], 20, 20, brush=QColor("green"))
        self.updateFoodOnScene()

    def adjustSpeed(self):
        """
            Adjust the game speed based on the length of the snake. The
            adjustSpeed method is used to adjust the game speed based on the
            length of the snake. It increases the speed of the game as the
            snake grows in size.

            The speed of the game is determined by the length of the snake,
            which is used to adjust the interval between game updates. It uses
            the length of the snake to calculate the new interval between game
            updates.

            The speed of the game is calculated using a linear equation to
            determine the interval between game updates. It uses the length of
            the snake to calculate the new interval, and the interval decreases
            as the snake grows in size.

            The base_interval is the initial speed of the game, and the speed
            increases as the snake grows in size. The interval between game
            updates is calculated using the following equation:

            new_interval = max(20, base_interval - L * speed_increase)

                where,
                    L = (length - 1)
                and
                    base_interval = 100
                    speed_increase = 5
                    length = length of the snake

            Parameters:
            -----------
                None

            Returns:
            --------
                None
        """
        snake_length = len(self.snake_positions)
        base_interval = 100
        v_increase = .25

        new_interval = max(
            20, int(base_interval - (snake_length - 1) * v_increase))

        self.timer.setInterval(new_interval)

    def handleDirectionChange(self, key):
        """
            Handle the direction change based on the key press event.
            The handleDirectionChange method is used to handle the direction
            change based on the key press event. It listens for the arrow keys
            on the keyboard and the WASD keys to change the direction of the
            snake.

            It handles the following:
                - Left arrow key or 'A' key: changes the direction of the snake
                                            to the left.
                - Right arrow key or 'D' key: changes the direction of the
                                            snake to the right.
                - Up arrow key or 'W' key: changes the direction of the snake
                                            to up.
                - Down arrow key or 'S' key: changes the direction of the snake
                                            to down.

            Parameters:
            -----------
                key: int
                        An integer representing the key press event.

            Returns:
            --------
                None
        """

        if key == Qt.Key_Left or key == Qt.Key_A or key == Qt.Key_4:
            if self.direction != Direction.Right:
                self.nextDirection = Direction.Left
        elif key == Qt.Key_Right or key == Qt.Key_D or key == Qt.Key_6:
            if self.direction != Direction.Left:
                self.nextDirection = Direction.Right
        elif key == Qt.Key_Up or key == Qt.Key_W or key == Qt.Key_8:
            if self.direction != Direction.Down:
                self.nextDirection = Direction.Up
        elif key == Qt.Key_Down or key == Qt.Key_S or key == Qt.Key_5:
            if self.direction != Direction.Up:
                self.nextDirection = Direction.Down

    def handleSpacePress(self):
        print("Space Pressed: Pause game")
        if self.gameOver_flag:
            print("Game Over! Cannot pause.")
        elif self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start()


class KeyPressEater(QObject):
    application_close_keys = {Qt.Key_Escape}
    game_restart_keys = {Qt.Key_R}
    pause_game_keys = {Qt.Key_Space}
    autopilot_toggle_key = {Qt.Key_Q}
    direction_keys = {
        Qt.Key_Left, Qt.Key_Right,
        Qt.Key_Up, Qt.Key_Down,
        Qt.Key_A, Qt.Key_D,
        Qt.Key_W, Qt.Key_S,
        Qt.Key_4, Qt.Key_8,
        Qt.Key_5, Qt.Key_6
    }

    def __init__(self, game):
        super().__init__()
        self.game = game  # Referenz auf die SnakeGame-Instanz

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()

            if key in self.application_close_keys:
                self.game.close()
                return True
            elif key in self.game_restart_keys:
                self.game.restartGame()
                return True
            elif key in self.pause_game_keys:
                self.game.handleSpacePress()
                return True
            elif key in self.autopilot_toggle_key:
                self.game.toggle_autopilot()
                return True
            elif key in self.direction_keys:
                self.game.handleDirectionChange(key)
                return True

        return super(KeyPressEater, self).eventFilter(obj, event)


class Direction:
    """
        Enumeration for the snake's direction.
        The Direction enumeration is used to represent the possible directions
        of the snake in the game world. It defines the possible directions
        in which the snake can move: left, right, up, and down.
    """
    Left = 0
    Right = 1
    Up = 2
    Down = 3


def main():
    """
        Entry point for the application.
        The main function is the entry point for the application, which
        creates and starts the SnakeGame application using the QApplication
        class.

        It creates a QApplication object, initializes the SnakeGame, and shows
        the game window.

        Parameters:
        -----------
            None

        Returns:
        --------
            ack: bool
                A boolean indicating if the execution was successful.
    """
    ack = False

    try:
        app = QApplication(argv)
        window = SnakeGame(
            screen_width=800,
            screen_height=800
        )
        window.show()
        app.exec_()
        ack = True
    except Exception as e:
        print(f"Exception occurred: {e}")
        ack = False

    return ack


def first_run_check():
    """
        This method is used as a post-installation check.
        The first_run_check method is used as a post-installation
        check to ensure that the game works properly after the installation
        process is completed.

        It looks for the presence of the scores file in the game directory
        and if it doesn't exist it waits for 2 seconds before the program
        is started.

        This should ensure that the post installation process is properly
        completed and everything is in place to ensure the game works
        correctly and smoothly.
    """

    if not path.exists(SCOREBOARD_PATH):
        sleep(2)


if __name__ == "__main__":
    """
        Entry point for the application.
        This is the call to the main function,
        which starts the game.

        If any exception occurs during the game, the application will
        return 1. In normal conditions, it will return 0.
    """
    try:
        sys_exit(0 if main() else 1)
    except Exception as e:
        print(f"Exception occurred: {e}")
        sys_exit(1)
