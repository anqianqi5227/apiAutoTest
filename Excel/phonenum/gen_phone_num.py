import random
import string


def phone_num():

    num_start = ['130', '131', '132', '134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
           '147', '155', '156', '185', '186', '133', '153', '180', '189', '175', '176']

    start = random.choice(num_start)
    end = ''.join((random.sample(string.digits, 8)))

    phonenum = start + end + '\n'

    return phonenum









