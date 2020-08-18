# import datetime from datetime
from datetime import datetime

class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
      
    @classmethod
    def from_datetime(cls, datetime):
        year, month, day = map(int, [datetime.year, datetime.month, datetime.day])
        return cls(year, month, day)

# You should be able to run the code below with no errors: 
if __name__ == "__main__":
    today = datetime.today()     
    bd = BetterDate.from_datetime(today)   
    print(bd.year)
    print(bd.month)
    print(bd.day)

    bdstr = BetterDate.from_str('2020-08-18')
    print(bdstr.year)
    print(bdstr.month)
    print(bdstr.day)