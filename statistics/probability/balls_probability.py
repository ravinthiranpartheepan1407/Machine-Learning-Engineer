# - p[index] = 100 x count_of_event[index] / sumOf(total_no_of_events)
#     - For ex: A jar containing: 40 Blue balls, 30 Yellow balls, 20 Ornage balls then the probability would be
#     - p[blue] = 100 x 40 / 90 = 44.4%             # 90 - Total balls and 40 - Blue Balls
#     - p[yellow] = 100 x 30 / 90 = 33.3%
#     - p[orange] = 100 x 20 / 90 = 22.2%           # Sum of all the occurance "SANITY CHECK" is (99.9%): 100% -> 44.4 + 33.3 + 22.2
#     - Sanity Check = 44.4 + 33.3 + 22.2 = 99.9%

def balls_probability():
    marbles = {
        "blue":40,
        "yellow": 30,
        "orange": 20,
    }
    total = marbles.get("blue") + marbles.get("yellow") + marbles.get("orange")
    compute_blue = 100 * marbles.get("blue") / total
    compute_yellow = 100 * marbles.get("yellow") / total
    compute_orange = 100 * marbles.get("orange") / total

    print(f'The total probability is: {total}')
    print(f'The probability of blue is: {compute_blue}, The probability of yellow is: {compute_yellow}, The probability of orange is: {compute_orange}')

balls_probability()