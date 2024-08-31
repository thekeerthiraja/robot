import unittest
import robo
class TestRobotMovement(unittest.TestCase):

    def setUp(self):
        self.terrain = robo.Terrain(5)
        self.terrain.add_robot(1)
        self.terrain.add_robot(2)

    def test_initial_position(self):
        self.assertEqual(self.terrain.get_robot_position(1), (0, 0))
        self.assertEqual(self.terrain.get_robot_position(2), (0, 0))


        self.terrain.move_robot(2, "S3")  # Move Robot 2 to (3, 0)
        self.assertEqual(self.terrain.get_robot_position(2), (3, 0))

    def test_robot_stops_before_occupied_position(self):
        self.terrain.move_robot(1, "E3")  # Robot 1 moves to (0, 3)
        self.terrain.move_robot(2, "E4")  # Robot 2 tries to move to (0, 4) but stops at (0, 2)
        self.assertEqual(self.terrain.get_robot_position(1), (0, 3))
        self.assertEqual(self.terrain.get_robot_position(2), (0, 2))

    def test_robot_stops_if_another_robot_is_already_there(self):
        self.terrain.move_robot(1, "E2")  # Robot 1 moves to (0, 2)
        self.terrain.move_robot(2, "E2")  # Robot 2 moves to (0, 1)
        self.assertEqual(self.terrain.get_robot_position(1), (0, 2))
        self.assertEqual(self.terrain.get_robot_position(2), (0, 1))

        self.terrain.move_robot(1, "E2")  # Robot 1 moves to (0, 4)
        self.terrain.move_robot(2, "E4")  # Robot 2 should stop at (0, 3)
        self.assertEqual(self.terrain.get_robot_position(1), (0, 4))
        self.assertEqual(self.terrain.get_robot_position(2), (0, 3))

    


if __name__ == '__main__':
   unittest.main()
