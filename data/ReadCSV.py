import csv
import heapq
import random
from collections import Counter


def get_match_score(preferences, row):
    score = 0
    if row[2] == preferences.operations:
        score += 1
    if row[3] == preferences.leadership:
        score += 1
    if row[4] == preferences.business:
        score += 1
    if row[5] == preferences.research:
        score += 1
    if row[6] == preferences.military:
        score += 1
    else:
        score -= 2
    if row[7] == preferences.wealth_management:
        score += 1
    if row[8] == preferences.banking:
        score += 1
    if row[9] == preferences.consulting:
        score += 1
    if row[10] == preferences.pharma:
        score += 1
    if row[11] == preferences.supply_chain:
        score += 1
    return score, row[1]


def remove_scores_from_bullets(best_scores_bullets):
    bullets_list = []
    for i in best_scores_bullets:
        bullets_list.append(i[0])
    return bullets_list


def get_bullets(preferences):
    num_of_bullets = random.randint(2, 4)
    best_scores_dict = {}
    with open("data/resume_data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #         # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                score, bullet = get_match_score(preferences, row)
                best_scores_dict[bullet] = score
                line_count += 1
        k = Counter(best_scores_dict)
        best_scores_bullets = k.most_common(num_of_bullets)
        best_bullets = remove_scores_from_bullets(best_scores_bullets)
        return best_bullets
