# secondconverter.py
# translate seconds into more readable hours, mins, secs

def second_converter():
    print 'hi and welcome to the second converter.' +
    ' if you give me a big amount of seconds, i can' +
    ' convert your amount into hours, minutes, and seconds.'

    given_sec = int(input('how many seconds would you like to convert?'))

    minutes = given_sec // 60
    leftover_sec = given_sec % 60
    hours = minutes // 60
    leftover_min = minutes % 60

    print('you gave me ', hours, 'hours,', leftover_min, 'min, and', leftover_sec, 'seconds.')

second_converter()