from einfach import termutils, __version__, __license__, clip, floatutils
from time import sleep

print(__version__, __license__)


def test_1():
    def AUIcallback():
        print("")

    AUI = termutils.AsyncUserInput(
        input_callback=AUIcallback,
        name="TestAUI"
    )

    AUI.pause()
    print("AUI paused")
    sleep(1)
    AUI.resume()
    print("AUI resumed")
    sleep(2)
    AUI.pause


def test_2():
    try:
        clip.clip("tet")
    except Exception as e:
        print(e)


def test_3():
    print("##### test_3 #####")
    t_1 = "0.1..1.1.1.1.11."
    t_2 = "Moin"
    t_3 = "0.1"
    t_4 = "9919.3"
    t_5 = 5
    t_6 = ["5", "3", 9, True]
    t_7 = True
    t_8 = None
    t_9 = ".1"

    def t_1test(var, tf):
        print(floatutils.would_be_valid_float(var))
        if floatutils.would_be_valid_float(var) != tf:
            raise Exception
    
    print(" ### would_be_valid_float True: ### ")
    t_1test(t_3, True)
    t_1test(t_4, True)
    t_1test(t_9, True)
    t_1test(t_5, True)
    print(" ### would_be_valid_float False: ### ")
    t_1test(t_1, False)
    t_1test(t_2, False)
    t_1test(t_6, False)
    t_1test(t_7, False)
    t_1test(t_8, False)

    def t_2test(var, tf):
        print(floatutils.is_float_in_range(var, -100, 9918))
        if floatutils.is_float_in_range(var, -100, 9918) != tf:
            raise Exception
        
    print(" ### is_float_in_range True: ### ")
    t_2test(t_3, True)
    t_2test(t_9, True)
    t_2test(t_5, True)
    print(" ### is_float_in_range False: ### ")
    t_2test(t_4, False)
