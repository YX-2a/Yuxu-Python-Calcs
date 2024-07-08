def cmin ( val, mode) :
        if mode == "cmtoinch":
            calc = float(val) / 2.54
            return round (calc, 2)
        elif mode == "inchtocm" :
            calc = float(val) * 2.54
            return round (calc, 2)


def mft ( val, mode):
        if mode == "mtoft" :
            calc = float(val) * 3.281
            return round (calc, 2)
        elif mode == "fttom":
            calc = float(val) / 3.281
            return round (calc, 2)

def kmmi ( val, mode):
        if mode == "mitokm":
            calc = float(val) * 1.609
            return round (calc, 2)
        elif mode == "kmtomi":
            calc = float(val) / 1.609
            return round (calc, 2)
