# Updated code integrating the name generator with the desired structure

import random

# Medieval names
FIRST_NAMES_MEN = [
    "Arthur", "Baldric", "Cedric", "Edgar", "Gareth",
    "Harold", "Lancelot", "Percival", "Roland", "Theodore"
]

FIRST_NAMES_WOMEN = [
    "Adelaide", "Beatrice", "Cecily", "Eleanor", "Felicity",
    "Gwendolyn", "Isolde", "Margery", "Rosalind", "Winifred"
]

LAST_NAMES = [
    "Blackwood", "Dawnbreaker", "Evershade", "Hawthorne", "Ironwood",
    "Kingsley", "Lancaster", "Ravenwood", "Thornfield", "Winterbourne"
]


def generate_name(gender, last_name=None):
    """
    Generate a full name as an array [first_name, last_name].
    - `gender`: 'Male' or 'Female'.
    - `last_name`: Optionally specify a last name. If None, choose randomly.
    """
    if gender == "Male":
        first_name = random.choice(FIRST_NAMES_MEN)
    elif gender == "Female":
        first_name = random.choice(FIRST_NAMES_WOMEN)
    else:
        raise ValueError("Invalid gender. Must be 'Male' or 'Female'.")
    
    if not last_name:
        last_name = random.choice(LAST_NAMES)
    
    return [first_name, last_name]


class GridCell:
    """
    Represents a single cell in the world grid.
    """
    def __init__(self):
        self.npcs = []  # List to hold NPCs in the cell
        self.max_size = 20  # Maximum size the cell can accommodate

    def can_accommodate(self, npc):
        """
        Check if the NPC can be accommodated in the grid cell.
        """
        current_size = sum(npc.size for npc in self.npcs)
        return current_size + npc.size <= self.max_size

    def add_npc(self, npc):
        """
        Add an NPC to the cell if there's space.
        """
        if self.can_accommodate(npc):
            self.npcs.append(npc)
            return True
        return False

    def remove_npc(self, npc):
        """
        Remove an NPC from the cell.
        """
        if npc in self.npcs:
            self.npcs.remove(npc)


class WorldGrid:
    """
    Represents the entire world grid.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[GridCell() for _ in range(width)] for _ in range(height)]

    def is_within_bounds(self, x, y):
        """
        Check if the given coordinates are within the grid bounds.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def move_npc(self, npc, new_x, new_y):
        """
        Move an NPC to a new grid cell if possible.
        """
        if self.is_within_bounds(new_x, new_y):
            current_cell = self.grid[npc.x][npc.y]
            new_cell = self.grid[new_x][new_y]

            if new_cell.can_accommodate(npc):
                current_cell.remove_npc(npc)
                new_cell.add_npc(npc)
                npc.x, npc.y = new_x, new_y
                return True
        return False


class NPC:
    """
    Superclass for all NPCs.
    """
    def __init__(self, name, health, npc_type, x, y):
        self.name = name  # Name is now an array [first_name, last_name]
        self.health = health
        self.type = npc_type
        self.size = 1  # Default size of an NPC
        self.x = x  # Current x position in the grid
        self.y = y  # Current y position in the grid

    def move(self, world, dx, dy):
        """
        Move the NPC by dx, dy in the grid.
        """
        new_x = self.x + dx
        new_y = self.y + dy
        return world.move_npc(self, new_x, new_y)


class Human(NPC):
    """
    Subclass of NPC for Human.
    """
    def __init__(self, x, y, last_name=None):
        gender = random.choice(["Male", "Female"])  # Assign gender
        name = generate_name(gender, last_name)
        health = random.randint(80, 120)  # Base health with some variation
        npc_type = random.choice(["Unassigned", "Farmer"])  # Randomly assign a role
        super().__init__(name, health, npc_type, x, y)
        self.size = 2  # Humans take up size 2 in the grid
        self.gender = gender  # Store gender


class World:
    """
    Represents the entire simulation world, containing the grid and all NPCs.
    """
    def __init__(self, width, height):
        self.grid = WorldGrid(width, height)  # Initialize the grid
        self.npcs = []  # List to hold all NPCs in the world

    def add_npc(self, npc):
        """
        Add an NPC to the world and place them in the grid.
        """
        if self.grid.grid[npc.x][npc.y].add_npc(npc):
            self.npcs.append(npc)
            return True
        return False

    def simulate(self, days):
        """
        Run the simulation for the specified number of days.
        """
        for day in range(1, days + 1):
            print(f"--- Day {day} ---")
            for npc in self.npcs:
                dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])  # Random movement
                if npc.move(self.grid, dx, dy):
                    print(f"{' '.join(npc.name)} moved to ({npc.x}, {npc.y}).")
                else:
                    print(f"{' '.join(npc.name)} could not move from ({npc.x}, {npc.y}).")


# Create the world
world_simulation = World(10, 10)

# Add humans to the world
for i in range(5):
    npc = Human(random.randint(0, 9), random.randint(0, 9))
    if not world_simulation.add_npc(npc):
        print(f"Could not place {' '.join(npc.name)} at ({npc.x}, {npc.y}).")

# Run the simulation for a specified number of days
world_simulation.simulate(days=3)
