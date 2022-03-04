from karma import Karma
from exeptions import KillError
from exeptions import DrunkError
from exeptions import CarCrashError
from exeptions import GluttonyError
from exeptions import DepressionError


def write_log(error):
    with open("karma.log", 'a', encoding='utf-8') as file:
        file.write(error + '\n')


karma = Karma()
while True:
    if karma.get_karma() > 500:
        break
    else:
        try:
            karma.one_day()
        except KillError:
            write_log('KillError')
        except DrunkError:
            write_log('DrunkError')
        except CarCrashError:
            write_log('CarCrashError')
        except GluttonyError:
            write_log('GluttonyError')
        except DepressionError:
            write_log('DepressionError')
