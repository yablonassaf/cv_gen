# https://towardsdatascience.com/how-to-paraphrase-text-using-python-73b40a8b7e66
import random

from parrot import Parrot
import torch
import warnings

warnings.filterwarnings("ignore")


def random_state(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


random_state(1234)

parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=True)


def paraphrase_bullets(phrases):
    bullets_list = []
    for phrase in phrases:
        para_phrases = parrot.augment(input_phrase=phrase)
        bullet = random.choice(para_phrases)
        bullets_list.append(bullet)
    return bullets_list


def paraphrase_bullet(bullet):
    paraphrased = parrot.augment(input_phrase=bullet)
    return paraphrased

# if __name__ == '__main__':
#     text = ["A list is like an array of items created using square brackets. They are different from arrays as they can contain items of different types. Lists are different from tuples as they are mutable.", "In Python 3.7 and above the Data Class can be used to return a class with automatically added unique methods", "This article is contributed by Shubham Agrawal. If you like GeeksforGeeks and would like to contribute, you can also write an article and mail your article to contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks."]
#     ans = paraphrase_bullets(text)
#     print(ans)