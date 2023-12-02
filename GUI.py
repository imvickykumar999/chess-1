import pygame

class ChessBoard:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                self.board[i][j] = ChessPiece(i, j)

    def draw(self):
        for i in range(8):
            for j in range(8):
                self.board[i][j].draw()

class ChessPiece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("chess_piece.png")

    def draw(self):
        pygame.draw.image(self.image, (self.x, self.y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    board = ChessBoard()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        board.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()