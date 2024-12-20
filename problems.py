import requests
from conts import Consts
from Environment import Environment


def get_calendar_data(env:Environment, year=2020, day=1):
    data = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={'session': env.SESSIONID}, headers={'User-Agent': env.USER_AGENT})

    return data.text.splitlines()
env = Environment()
calendar_data = get_calendar_data(env)
def two_sum(calender_data:list[str]=[1721,979,366,299,675,1456], target_sum=2020):
    # https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/
    dict_values = {}
    for data in calender_data:
        complement = target_sum - int(data)
        dict_values[complement] = int(data)
        if str(complement) in calender_data:
            return complement  * dict_values[complement], dict_values
    return False, dict_values

def three_sum(calender_data, target_sum=2020):
    # https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
    calendar_data_int = list(map(int, calender_data))
    number_of_items = len(calender_data)

    # Sort the elements
    calendar_data_int.sort()
    for i in range( number_of_items - 2):
        left_pointer = i + 1
        right_pointer = number_of_items - 1
        while i < right_pointer:
            current_sum =  calendar_data_int[i] + calendar_data_int[left_pointer] + calendar_data_int[right_pointer]
            if current_sum == target_sum:
                print(f"Triplet is {calendar_data_int[i]}, {calendar_data_int[left_pointer]}, {calendar_data_int[right_pointer]}")
                return  calendar_data_int[i] * calendar_data_int[left_pointer] * calendar_data_int[right_pointer]
            elif current_sum < target_sum:
                left_pointer = left_pointer + 1
            else:
                right_pointer = right_pointer - 1





#print(two_sum(calendar_data))
#print(three_sum(calendar_data))
class PasswordPolicy:
    def __init__(self, pair:str, symbol, text):
        result = pair.split("-") 
        self.min, self.max = int(result[0]), int(result[1])
        self.symbol = symbol[0]
        self.text = text
    def __str__(self):
        return f"{self.min} {self.max} {self.symbol} {self.text} "
    def __repr__(self):
        return f"{self.min} {self.max} {self.symbol} {self.text} "
def day_2():
    result = []
    calendar_data = get_calendar_data(env, day=2)
    for data in calendar_data:
        check = data.split()

        result.append(PasswordPolicy(check[0], check[1], check[2]))
    print(result)

        


def day3():
    grid = get_calendar_data(env, day=3)
#     Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.


    # grid = [
    #     "..##.......",
    #     "#...#...#..",
    #     ".#....#..#.",
    #     "..#.#...#.#",
    #     ".#...##..#.",
    #     "..#.##.....",
    #     ".#.#.#....#",
    #     ".#........#",
    #     "#.##...#...",
    #     "#...##....#",
    #     ".#..#...#.#",
    # ]  # Replace with get_calendar_data if available

    total = check_trees(grid, 1,1) * check_trees(grid, 3,1) * check_trees(grid, 5,1) * check_trees(grid, 7,1) * check_trees(grid, 1,2)

    return total

def check_trees(grid, right, down):
    consts = Consts(grid)
    x, y = 0,0
    tree_count = 0

    while y < consts.height:
        if grid[y][x % consts.width] ==  consts.TREE_SYMBOL:
            tree_count += 1
        
        y += down
        x += right

    return tree_count

