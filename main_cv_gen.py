from data import ReadCSV
from pharhparse import Paraphrase
from word.DocWord import DocWord


class Details:
    name = (input('What is your name? '))
    print("=" * 10)


class PreferenceAnswers:
    print("")
    print("Please Select all that Apply 1-yes; 0-no")
    print("=" * 10)
    operations = input('operations ')
    leadership = input('leadership ')
    business = input('business ')
    research = input('research ')
    military = input('military ')
    wealth_management = input('wealth management ')
    banking = input('Banking ')
    consulting = input('consulting ')
    supply_chain = input('supply chain ')
    pharma = input('pharma ')
    print("=" * 10)


if __name__ == '__main__':
    doc = DocWord(Details)
    bullets = ReadCSV.get_bullets(PreferenceAnswers)
    paraphrased = Paraphrase.paraphrase_bullets(bullets)
    doc.add_bullet_to_resume(paraphrased)
    exit()
