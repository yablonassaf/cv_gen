import csv


def get_match_score(PreferenceAnswers, row):
    score = 0
    if row[2] == PreferenceAnswers.operations:
        score += 1
    if row[3] == PreferenceAnswers.leadership:
        score += 1
    if row[4] == PreferenceAnswers.business:
        score += 1
    if row[5] == PreferenceAnswers.research:
        score += 1
    if row[6] == PreferenceAnswers.military:
        score += 1
    if row[7] == PreferenceAnswers.wealth_management:
        score += 1
    if row[8] == PreferenceAnswers.banking:
        score += 1
    if row[9] == PreferenceAnswers.consulting:
        score += 1
    if row[10] == PreferenceAnswers.pharma:
        score += 1
    if row[11] == PreferenceAnswers.supply_chain:
        score += 1
    return score, row[1]


def get_bullet(PreferenceAnswers):
    best_score = 0
    best_bullet = "not found"
    with open("data/resume_data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #         # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                phrase = [row[1]]
                score, bullet = get_match_score(PreferenceAnswers, row)
                if score > best_score:
                    best_score = score
                    best_bullet = bullet
                line_count += 1
                # if line_count > 1:
                #     break
        # print(f'Processed {line_count} lines.')
        return best_bullet
