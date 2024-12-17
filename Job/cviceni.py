objem_nadoby = float(input("zadej objem nádoby v litrech: "))
spotreba_v_litrech = float(input("zadej spotřebu kapaliny v litrech: "))
kus = 1.0
vysledek = (objem_nadoby - spotreba_v_litrech) / objem_nadoby - kus

print(vysledek)
