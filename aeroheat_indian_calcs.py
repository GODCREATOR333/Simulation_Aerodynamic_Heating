alt = int(input("enter altitude:"))


def indian(alt):
    g = 9.78852
    r = 287.05307
    to = 303.15
    po = 100500
    rnot = 1.15491
    alt = alt

    if alt < 16000:
        c = -0.0065
        te = to + (c * (alt - 0))
        sl = -(g / (c * r))
        p = po * ((te / to) ** sl)
        s2 = -((g / (c * r)) + 1)
        den = rnot * ((te / to) ** s2)
    elif alt > 16000 and alt < 46000:
        c = 0.0023
        t1 = 199.0
        te = t1 + (c * (alt - 16000))
        sl = -(g / (c * r))
        p1 = 11045
        p = p1 * ((te / t1) ** sl)
        s2 = -((g / (c * r)) + 1)
        d1 = 0.1933
        den = d1 * ((te / t1) ** s2)
    elif alt > 46000 and alt <= 52000:
        te = 268.0
        p1 = 133.77
        p = p1 * (2.71828 ** (-(g / (r * te)) * (alt - 46000)))
        d1 = 0.0017
        den = d1 * (p / p1)
    elif alt > 52000 and alt < 75000:
        c = -0.003
        t1 = 268
        te = t1 + (c * (alt - 52000))
        s1 = -(g / (c * r))
        p1 = 62.3453
        p = p1 * ((te / t1) ** s1)
        s2 = -((g / (c * r)) + 1)
        d1 = 0.00077
        den = d1 * ((te / t1) ** s2)
    elif alt > 75000 and alt < 80000:
        te = 199.0
        pl = 2.1149
        p = pl * (2.71828 ** (-(g / (r * te)) * (alt - 75000)))
        dl = -0.000035
        den = dl * (p / pl)
    else:
        # Default values if none of the conditions match
        te = 0
        p = 0
        den = 0

    return te, p, den


te, p, den = indian(alt)
print("te=", te)
print("p=", p)
print("den=", den)
