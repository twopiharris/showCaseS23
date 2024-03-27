## based on
# https://pypi.org/project/getch/
def Getcha():
    result = ''
    try:
        import getch
        result = getch.getch()
    except ImportError:
        import msvcrt
        result = msvcrt.getwch()
    return result
        
