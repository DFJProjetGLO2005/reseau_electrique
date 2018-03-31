import random, os, platform

def create_location(boundaries):
    lat = round(random.uniform(0, boundaries[1]), 3)
    lon = round(random.uniform(0, boundaries[0]), 3)
    if lat == int(lat): lat += 0.001
    if lon == int(lon): lon += 0.001
    return '"POINT({} {})"'.format(lat, lon)


def display_loading(text, loading_ratio):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    bar_length = 40
    loaded = int(loading_ratio * bar_length)
    bar = '|' * loaded  + '-' * (bar_length - loaded) 
    print("{0}   {1}    {2:3.2f}%".format(text, bar, loading_ratio*100))



def get_divisors(n):
    original_n = n
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    max_factor = max(factors)
    return max_factor, original_n // max_factor

