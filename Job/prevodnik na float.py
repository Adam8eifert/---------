objem_nadoby = float(input("zadej objem nádoby v litrech: "))

spotreba_v_litrech = float(input("zadej spotřebu kapaliny v litrech: "))
kus = 1.0
vysledek_1 = (objem_nadoby - spotreba_v_litrech)

vysledek_2 = (vysledek_1 / objem_nadoby) 

vysledek_3 = (kus - vysledek_2)

print(vysledek_3)
