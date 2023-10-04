alt = int(input("enter altitude:"))


def stdatm(alt):
    g = 9.81
    r = 287
    to = 288.16
    po = 1.01e5
    rnot = 1.23
    alt = alt

    if alt < 11000:
        c = -0.0065
        te = to + (c * (alt - 0))
        sl = -(g / (c * r))
        s1 = -(g / (to * r))
        p = po * ((te / to) ** s1)
        s2 = -((g / (c * r)) + 1)
        den = rnot * ((te / to) ** s2)

    elif alt > 11000 and alt <= 25000:
        te = 216.66
        p1 = 22540
        p = p1 * (2.71828 ** (-(g / (r * te)) * (alt - 11000)))
        d1 = 0.367
        den = d1 * (p / p1)

    elif alt > 25000 and alt < 47000:
        t1 = 216.66
        p1 = 2.481e3
        c = 0.003
        te = t1 + c * (alt - 25000)
        p = p1 * ((te / t1) ** (-(g / (c * r))))
        d1 = 0.041
        den = d1 * ((te / t1) ** (-(g / (c * r) + 1)))

    elif alt > 47000 and alt <= 53000:
        te = 282.66
        p1 = 1.1973e2
        p = p1 * (2.71828 ** (-(g / (r * te)) * (alt - 47000)))
        d1 = 0.0014757
        den = d1 * (p / p1)

    elif alt > 53000 and alt < 74000:
        t1 = 282.66
        p1 = 61.493
        c = -0.0045
        te = t1 + c * (alt - 53000)
        p = p1 * ((te / t1) ** (-(g / (c * r))))
        d1 = 0.00075791
        den = d1 * ((te / t1) ** (-(g / (c * r) + 1)))

    elif alt > 79000 and alt < 90000:
        te = 165.66
        p1 = 1.06668
        p = p1 * (2.71828 ** (-g / r * te) * (alt - 79000))
        d1 = 0.000013147
        den = d1 * (p / p1)
    else:
        te = 0
        p = 0
        den = 0

    return te, p, den


te, p, den = stdatm(alt)
print("te=", te)
print("p=", p)
print("den=", den)
