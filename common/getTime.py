import os
import time
from datetime import date

class GetTime:
    @staticmethod
    def get_current_day():
        try:
            current_day = date.today()
        except Exception as e:
            raise e
        else:
            return str(current_day)

    @staticmethod
    def get_current_time():
        try:
            current_time = time.strftime('%H-%M-%S')
        except Exception as e:
            raise e
        else:
            return str(current_time)


# day = GetTime.get_current_day()
# print (day)
#
# current_time = GetTime.get_current_time()
# print(current_time)


