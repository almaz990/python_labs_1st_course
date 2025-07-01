d = {"matan": 4, "culture": 5, "C++": 5, "history": 5}


def middle_result(d, stip, arg=1):
    sm = sum(d[i] for i in d)
    avrg = sm / len(d)
    if 3.5 <= avrg and avrg <= 4.5:
        print(stip * arg)
    elif 4.5 <= avrg and avrg <= 5:
        print(stip * 1.5 * arg)
    else:
        print("стипендия не выплачивается")


middle_result(d, 2500.0, 2)
