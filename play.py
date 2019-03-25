import cv2

from tictactoe import *

def main():
    try:
        ge = GameEngine()
        ge.start()
    except KeyboardInterrupt as e:
        print("\nBye! Thanks for playing!")

if __name__=="__main__":
    main()