class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        pass

        #bubble sort
        # def bubble_sort( arr ):
        #     swaps_occurred = True
        #     while swaps_occurred:
        #         swaps_occurred = False
        #         for i in range(0, len(arr)-1):
        #             if arr[i] > arr[i+1]:
        #                 # swap
        #                 arr[i], arr[i+1] = arr[i+1], arr[i]
        #                 swaps_occurred = True

        #     return arr


        # a go left helper function which will shift the robot all the way to the left again
        # def go_left():
        #     while robot.can_move_left():
        #         robot.move_left()
        #         print(robot._position)
        #     else:
        #         robot.set_light_off()

        # # set light on to return true
        # robot.set_light_on()

        # while robot.light_is_on():

        #     robot.set_light_off

        #     #loop through the list
        #     for i in range(0, len(robot._list)-1):

        #         if robot.compare_item() == None:
        #             robot.swap_item()
        #             robot.move_right()
        #             robot.set_light_on()
                
        #         elif robot.compare_item() == -1:
        #             robot.swap_item()
        #             robot.move_right()
        #             robot.swap_item()
        #             robot.move_left()
        #             robot.swap_item()
        #             robot.set_light_on()
        #             robot.move_right()

        #         elif robot.compare_item() == 1:
        #             robot.move_right()
        #             # robot.set_light_off()
        #         else:
        #             robot.move_right()
        #             # robot.set_light_off()


        #         # if robot.can_move_right() is False:
        #         #     robot.swap_item()
        #         #     go_left()

        while robot.light_is_on() is False:

            #sweep across the list to the right
            while robot.can_move_right():

                robot.swap_item()
                robot.move_right()
                # print(robot._position)
                # print(robot._item)

                # if the item in your pocket is bigger than the 
                if robot.compare_item() == 1:
                    # swap it twice, not once
                    robot.swap_item()
                    robot.move_left()
                    robot.swap_item()
                    robot.move_right()
                    robot.set_light_on()
                    # print(robot._position)
                    # print(robot._item)

            while robot.can_move_left():

                robot.swap_item()
                robot.move_left()

                if robot.compare_item() == -1:
                    robot.set_light_off()
                    robot.move_right()
                    robot.swap_item()
                    robot.move_left()
                    # print(robot._position)
                    # print(robot._item)
             
        print(robot._item)
        return robot._list

        
        """
        #     Swap index[0] for None. Now holding first index value with the rest of the robot._list - 1 all integers
        if robot._item is None:
            robot.swap_item()
            robot._list.remove(None)
            print(robot._list)

        # Loop through the list
        for i in range(len(robot._list)-1):

            # As long as you're not at the end of the list
            while robot.can_move_right():
                
                # Check if the item number of the position you're on is larger than your item.
                # If it's larger then swap the item and move to the right one spot
                if robot.compare_item() == -1:
                    robot.swap_item()
                    robot.move_right()
                    # print(f"swapped a second item: {robot._item}")

                # If it's smaller or equal, just move one spot to the right
                else:
                    robot.move_right()
                    # print(f"didn't swap another item: {robot._item}")

            # insert largest number at the largest index
            else:
                if robot._item:
                    robot._list.append(robot._item)
                    robot._item = None
                    robot._position = 0
                    robot.sort()
                    break
                else:
                    robot.move_left()
                    print(f"did this append?: {robot._list}")
                    print(f"what's in item now?: {robot._item}")
                    break

            return robot._list
            """
                
                





if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)