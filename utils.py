from random import randint



def chose_start(duration):
    a = 120
    b = int(duration - (15 * 60) - 180)
    return randint(a, b)


def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return "{}:{}:{}".format(h, m, s)


def convert(path):
    return '"{}"'.format(path.replace("/mnt/e/Films", "E:\Films")).replace("/", "\\")


REGEX = "/mnt/d/Films" + "/([^/]*)/([^/]*)/([^/]*)/([^/]*) \((\d{4})\)/([^/]*) \((\d{4})\)\." #FixMe change!!!!