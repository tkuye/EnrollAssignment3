from enrollStudent import EnrollTable
table = EnrollTable(35)
finder = 20
i = 999999
c = 0
while i > 100000 and c < 10:
    if table.cmputIndex(str(i)) == 20:
        print(i)
        c += 1
    i-= 1