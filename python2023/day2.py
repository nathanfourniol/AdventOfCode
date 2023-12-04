
import time


RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

BLUE = "blue"
RED = "red"
GREEN = "green"


def validTry(tirageTuple):
    reds = tirageTuple[0]
    greens = tirageTuple[1]
    blues = tirageTuple[2]
    if reds <= RED_CUBES and greens <= GREEN_CUBES and blues <= BLUE_CUBES:
        return True
    else:
        return False


def findMaxColorByGame(list_of_tries):
    blue = [0]
    green = [0]
    red = [0]
    for trie in list_of_tries:
        red.append(trie[0])
        green.append(trie[1])
        blue.append(trie[2])
    max_red = max(red)
    max_green = max(green)
    max_blue = max(blue)
    return max_red, max_green, max_blue


def decodeTry(trie):
    # print(trie)
    result = [0, 0, 0]  # red, green, blue
    for k in trie:
        nb_cubes, color = k.split()
        if color.strip() == RED:
            result[0] = int(nb_cubes.strip())
        if color.strip() == GREEN:
            result[1] = int(nb_cubes.strip())
        if color.strip() == BLUE:
            result[2] = int(nb_cubes.strip())
    return result


def decodeLine(line):
    """ obj : [GAME_ID, try 1, try 2 ...]
    with try1 = [Red, Blue, Green]
    """
    lineStplited = line.split(":")
    # print(lineStplited)
    game_id = int(lineStplited[0].split()[1])
    tries = lineStplited[1].split(";")
    # print(tries)
    list_of_try = []
    for trie in tries:
        trieSplited = trie.split(",")
        # print(game_id, trieSplited)
        results = decodeTry(trieSplited)  # [red, green, blue]
        # print(results)
        list_of_try.append(results)
    return game_id, list_of_try


def main_2():
    # with open("../assets/input_example_day_2.txt", "r") as f:
    with open("../assets/input_day_2.txt", "r") as f:
        data = f.readlines()
    t0 = time.time()
    power_sum = 0
    for line in data:
        game_id, list_of_tries = decodeLine(line)
        print(f"Processing game {game_id}")
        max_red, max_green, max_blue = findMaxColorByGame(list_of_tries)
        print(max_red, max_green, max_blue)
        power_sum += max_red * max_green * max_blue
    compute_time = time.time()-t0
    print("SUM : ", power_sum)
    print(f"TIME {compute_time}")


def main_1():
    # with open("../assets/input_example_day_2.txt", "r") as f:
    with open("../assets/input_day_2.txt", "r") as f:
        data = f.readlines()
    t0 = time.time()
    game_id_sum = 0
    for line in data:
        game_id, list_of_tries = decodeLine(line)
        print(f"Processing game {game_id}")
        nb_tries = len(list_of_tries)
        valid_tries = 0
        for aTry in list_of_tries:
            if validTry(aTry):
                valid_tries += 1
            else:
                print(f"Game {game_id} invalid")
                break
        if valid_tries == nb_tries:
            print(f"Game {game_id} valid")
            game_id_sum += game_id
    compute_time = time.time()-t0
    print("SUM : ", game_id_sum)
    print(f"TIME {compute_time}")

if __name__ == "__main__":
    main_2()
