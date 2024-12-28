""" Day 25: Code Chronicle

Calculates which key and lock schematics fit together
by comparing if letters in the same spots are different.
"""
schematics = open("input").read().split('\n\n')

for i in range(len(schematics)):
    for j in range(len(schematics)):
        if j == i:
            continue
        fit = True
        a = schematics[i].split('\n')
        b = schematics[j].split('\n')
        for k in range(len(a)):
            for l in range(5):
                if a[k][l] is b[k][l]:
                    print(a[k][l] + b[k][l] + a[k] + b[k])
                    fit = False
                    break
            if fit is False:
                break
        if fit is True:
            print("fit true: " + str(i + 1) + ' & ' + str(j + 1))
            break
