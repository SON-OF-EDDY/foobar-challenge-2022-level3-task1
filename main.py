def solution(brick_count):

    import math

    brick_count = brick_count

    level_array = []

    max_num_steps_found = False

    max_number_steps = 0

    step_counter = 2

    while not max_num_steps_found:

        total = 0

        for i in range(step_counter):
            total += (step_counter - i)

        min_bricks = total

        if brick_count >= min_bricks:
            pass
        else:
            max_number_steps = step_counter
            max_number_steps -= 1
            break
        step_counter += 1

    num_sub_arrays = max_number_steps

    for x in range(num_sub_arrays-1):
        level_array.append([])

    num_entries = brick_count - 2 + 3



    for sub_array in level_array:
        for i in range(num_entries):
            sub_array.append(0)



    for n in range(3,brick_count+1):

        max_num_steps_found = False

        step_counter = 2

        while not max_num_steps_found:

            total = 0

            for i in range(step_counter):
                total += (step_counter - i)

            min_bricks = total

            if n >= min_bricks:
                pass
            else:
                max_number_steps = step_counter
                max_number_steps -= 1
                break
            step_counter += 1

        level_array[0][n]= 1 + math.floor((n-3)/2)

        for i in range(1,len(level_array)):

            determining_factor = i + 2

            if max_number_steps >= determining_factor:

                blocks_left = n - determining_factor

                final_result = 0
                for x in range(i,i-2,-1):

                    final_result += level_array[x][blocks_left]

                level_array[i][n] = final_result

    from operator import add

    final = [0 for _ in range(num_entries)]

    for element in level_array:
        final = list(map(add, element, final))


    ultimate_victory = final[-1]

    print(ultimate_victory)

solution(200)