# Michael Osorio
DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    def tomorrow(self):
        if self.month == 12 and self.day == DIM[self.month]:
            self.month = 1
            self.day = 1
            self.year = self.year+1

        if  self.month==2 and self.day== 28 and d.isLeapYear() == True:
            self.month = 2
            self.day = 29
            self.year = self.year
        if self.month==2 and self.day== 29:
            self.month = self.month+1
            self.day = 1
            self.year = self.year
        
        elif self.day == DIM[self.month]:
            self.month = self.month+1
            self.day = 1
            self.year = self.year
        else:
            self.month = self.month
            self.day = self.day+1
            self.year = self.year

    def addNDays(self,n):
        n = n
        print self
        while n > 0:
            self.tomorrow()
            n-=1
            print self


        

    def yesterday(self):
        
        if self.month == 1 and self.day == 1:
            self.month = 12
            self.day = 31
            self.year = self.year-1

        if  self.month==3 and self.day== 01 and d.isLeapYear() == True:
            self.month = 2
            self.day = 29
            self.year = self.year
        if self.month==2 and self.day== 29:
            self.month = self.month
            self.day = self.day-1
            self.year = self.year
        
        elif self.day == 1:
            self.month = self.month-1
            self.day = DIM[self.month-1]
            self.year = self.year
        else:
            self.month = self.month
            self.day = self.day-1
            self.year = self.year
        

    def subNDays(self,n):
        n = n
        print self
        while n > 0:
            self.yesterday()
            n-=1
            print self

    def isBefore(self,d2):
        if self.year < d2.year:
            return True
        if self.month < d2.month and self.year == d2.year:
            return True
        if self.day < d2.day and self.month == d2.month and self.year == d2.year:
            return True
        return False
    def isAfter(self,d2):
        if self.year > d2.year:
            return True
        if self.month > d2.month and self.year == d2.year:
            return True
        if self.day > d2.day and self.month == d2.month and self.year == d2.year:
            return True
        return False

    def diff(self,d2):
        newSelf = self.copy()
        newD = d2.copy()
        if newSelf.equals(newD):
            return 0
        elif newSelf.isBefore(newD):
            count=0
            while(newSelf.isBefore(newD)):
                count += 1
                newD.yesterday()
            return -1 * count
        else:
            count=0
            while(newSelf.isAfter(newD)):
                count += 1
                newD.tomorrow()
            return count

    def dow(self):
        d = Date(11,9,2011)
        x = self.diff(d)%7
        if x % 7 == 0:
            return 'Sunday'
        if x % 7 == 6:
            return 'Saturday'
        if x % 7 == 5:
            return "Friday"
        if x % 7 == 4:
            return 'Thursday'
        if x % 7 == 3:
            return 'Wednesday'
        if x % 7 == 2:
            return 'Tuesday'
        if x % 7 == 1:
            return 'Monday'

    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False
