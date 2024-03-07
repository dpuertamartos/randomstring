import time
import string
import random


def generate_random_string(string_length):
    """
    Generates a random string of string_length size
    :param string_length:
    :return random_string:
    """
    all_alphanum_chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    len_alphanum_chars = len(all_alphanum_chars)

    return "".join([all_alphanum_chars[random.randint(0, len_alphanum_chars - 1)] for _ in range(string_length)])


if __name__ == '__main__':
    random_str = generate_random_string(10)
    while True:
        print(random_str)
        time.sleep(5)

