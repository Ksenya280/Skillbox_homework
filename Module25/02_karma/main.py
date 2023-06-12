import random

class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

def one_day():
    karma = random.randint(1, 7)
    if random.randint(1, 10) == 1:
        error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
        raise error
    return karma

karma = 0
while karma < 500:
    try:
        karma += one_day()
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
        with open('karma.log', 'a') as f:
            f.write(str(e) + '\n')

print('Просветление достигнуто!')