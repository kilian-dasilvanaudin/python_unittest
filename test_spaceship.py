import unittest
import time
from spaceship import spaceship
from threading import Thread

class TestVars(unittest.TestCase):
    def test_get_name(self):
        mySpaceship = spaceship("Falcon")
        self.assertEqual(mySpaceship.getName(),"Falcon")

    
    def test_get_initial_position(self):
        mySpaceship = spaceship("Falcon")
        self.assertEqual(mySpaceship.getPosition(),[0,0])
        
    def test_set_speed(self):
        mySpaceship = spaceship("Falcon")
        self.assertEqual(mySpaceship.getSpeed(),1)
        mySpaceship.setSpeed(5)        
        self.assertEqual(mySpaceship.getSpeed(),5)

        
    def test_move_for_duration(self):
        mySpaceship = spaceship("Falcon",[0,0])
        self.assertEqual(mySpaceship.getPosition(),[0,0])
        mySpaceship.flyForX([2,4],5)
        self.assertEqual(mySpaceship.getPosition(),[10,20])

    def test_move_for_duration_at_speed(self):
        mySpaceship = spaceship("Falcon",[0,0])
        mySpaceship.setSpeed(5)
        self.assertEqual(mySpaceship.getPosition(),[0,0])
        mySpaceship.flyForX([2,4],5)
        self.assertEqual(mySpaceship.getPosition(),[50,100])


    def test_is_moving(self):
        mySpaceship = spaceship("Falcon",[0,0])        
        self.assertEqual(mySpaceship.getPosition(),[0,0])
        t1 = Thread(target=mySpaceship.start, args=([2,4]))     
        t2 = Thread(target=mySpaceship.stop)
        t1.start()      
        time.sleep(5)
        t2.start()
        self.assertEqual(mySpaceship.getPosition(),[10,20])


if __name__ == '__main__':
    unittest.main()