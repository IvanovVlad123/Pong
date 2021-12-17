from game import ball,player
import unittest
import pygame
import unittest.mock
from pygame.math import Vector2

class Test(unittest.TestCase):
    def test_1(self):
        bal = ball(Vector2(1280//2,800//2))
        self.assertEqual(bal.b, Vector2(1280//2,800//2))
    def test_2(self):
        p1=player(1280-5,800//2)
        p2=player(5,800//2)
        bal = ball(Vector2(10,799))
        bal.s=Vector2(0,1)
        bal.update(1,p1,p2,1280,800)
        bal.update(7,p1,p2,1280,800)
        self.assertEqual(bal.b, Vector2(10, 793))
    def test_3(self):
        p1=player(1280-5,800//2)
        p2=player(5,800//2)
        bal = ball(Vector2(6,400))
        bal.s=Vector2(-1,0)
        bal.update(1,p1,p2,1280,800)
        bal.update(2,p1,p2,1280,800)
        self.assertEqual(bal.b, Vector2(7, 400))
    def test_4(self):
        p1=player(5,400)
        p1.s = -1
        p1.update(1280,800,1)
        self.assertEqual(p1.rect.top, 399)
    def test_5(self):
        p1=player(5,600)
        p1.s = 10
        p1.update(1280,800,1)
        self.assertEqual(p1.rect.top, 600)
if __name__ == '__main__':
    unittest.main()
