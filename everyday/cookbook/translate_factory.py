import string


def translator(frm=" ", to=" ", delete=" ", keep=None):
    if len(to) == 1:
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    # 这里才是关键
    if keep is not None:
        allchars = string.maketrans(' ', ' ')
        delete = allchars.translate(allchars, keep.translate(allchars, delete))

    def translate(s):
        return s.translate(trans, delete)
    return translate


digit_only = translator(keep=string.digits)
print digit_only("zhangjiawei140308chenerbei")


no_digits = translator(delete=string.digits)

print no_digits("zhangjiawei140308chenerbei")

digits_to_hash = translator(frm=string.digits, to="#")
print digits_to_hash("zhangjiawei cell-phone: 13162582627")
