class Gallows:
    
    def __init__(self):
        self.stages = [
            """
            -----
            |   |
                |
                |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
                |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
            |   |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|   |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
           /    |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
                |
            --------
            """
        ]
        
    def display(self, stage_index):
            if 0 <= stage_index < len(self.stages):
                print(self.stages[stage_index])
            else:
                print("Invalid stage index.")