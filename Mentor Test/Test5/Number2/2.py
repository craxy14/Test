# დავალება 2:
# ● როდესაც ვმუშაობთ 4 ელემენტიან მასივზე (no duplicates) და გვაქვს თანაბარი
# განაწილება მაქსიმალური მნიშვნელობის თითოეული წილის მიხედვით: P(a1 =
# max) = P(a2 = max) = P(a3 = max) = P(a4 = max), საშუალოდ რამდენი
# მინიჭება გვექნება?

a = [1,3,2,4]

arr_max = a[0]

for i in a:
    if i > arr_max:
        arr_max = i

#თუ P(a1 = max), მოხდება 1 მინიჭება
#თუ P(a2 = max), მოხდება 2 მინიჭება
#თუ P(a3 = max), best case მოხდება 2 მინიჭება, worst case მოხდება 3 მინიჭება
#თუ P(a4 = max), best case მოხდება 2 მინიჭება, worst case მოხდება 4 მინიჭება