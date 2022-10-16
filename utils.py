class Utils:
    @staticmethod
    def dms_to_dd(dms: str) -> float:
        dms = dms.split(':')
        degree, minutes, seconds = float(dms[0]), float(dms[1]), float(dms[2])
        return round(degree + minutes/60 + seconds/3600, 6)

    @staticmethod
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False