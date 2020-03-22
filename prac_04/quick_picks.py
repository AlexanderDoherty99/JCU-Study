import random

HIGHEST_NUMBER = 45
LOWEST_NUMBER = 1

desired_number_of_picks = int(input("How many quick picks? "))
quick_picks = []
for quick_pick in range(desired_number_of_picks):
    current_pick_line = []
    # current_pick_line = [random.randint(1, 10) for number in range(6) if number not in current_pick_line]
    # for number in range(6):
    #     random_number = random.randint(1,10)
    #     if random_number not in current_pick_line:
    #         current_pick_line.append(random_number)
    #         break
    i = 0
    while i < 6:
        random_number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
        if random_number not in current_pick_line:
            current_pick_line.append(random_number)
            i += 1
    # print(str(current_pick_line).strip('[]').replace(',', ''))
    print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(*current_pick_line))