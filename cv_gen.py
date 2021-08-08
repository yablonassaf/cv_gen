from data import ReadCSV
from pharhparse import Paraphrase
from word.DocWord import DocWord


class PreferenceAnswers:
    print("")
    print("Please Select all that Apply 1-yes; 0-no")
    print("="*10)
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
    print("="*10)


if __name__ == '__main__':
    # phrases = ["Here, we’ll be using a for loop to iterate through all the sentences in the phrases variable"]
    # pharhparse_text(phrases)
    # read_bullet()
    #word()

    industry = (input('What industry are you making this resume for? ')).lower()
    if industry == "tech" or industry == "technology":
        print("technology chosen")

    ops = PreferenceAnswers.operations
    doc = DocWord()
    bullet = ReadCSV.get_bullet(PreferenceAnswers)
    print("bullet bef = ", bullet)
    paraphrased = Paraphrase.paraphrase_bullet(bullet)
    print("bullet aft = ", paraphrased[0][0])
    doc.add_bullet_to_CV(bullet)
    print("bullet added to word doc")
    #doc = DocWord()

    #doc.add_bullet(text="aaaaaaaxxxxxxxxbbbb")
    exit()
