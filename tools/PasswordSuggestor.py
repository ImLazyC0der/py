def passwordGenerator():
    import random
    import string

    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(4)))
    sample_str += ''.join((random.choice(string.digits) for i in range(1)))
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

print("Welcome to Password Suggestor\nHere's a strong Password:\n")
passwordGenerator()
