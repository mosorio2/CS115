class Track(object):
    def __init__(self, title, artist, minutes, seconds):
        '''Initializes PRIVATE fields with the same name as those
           passed in as arguments.
           title and artist will be passed in as strings.
           minutes and seconds will be passed in as integers.
           seconds will be between 0 and 59.
           '''
        self.__title="title"
        self.__artist="artist"
        self.__minutes= int(minutes)
        self.__seconds=int(seconds)
        

    def length_as_str(self):
        '''Returns the length of the track as a string.
           Example:
              A track of 4 minutes and 22 seconds should be "4:22"
              A track of 3 minutes and 9 seconds should be "3:09"
              (note the leading 0 for the seconds portion)
        '''
        if self._seconds > 9:
            return str(self.__minutes) + ': ' + str(self.__seconds)
        else:
            return str(self.__minutes) + ':0' + str(self.__seconds)
        

    def length_in_seconds(self):
        '''Returns the length of the track in seconds.'''
        return str(self.__minutes * 60) + str(self.__seconds)

    def __str__(self):
        '''Returns a string representation of the track.'''
        return self.__title + ': ' + self.__artist + ' (' + \
               self.length_as_str() + ')'
