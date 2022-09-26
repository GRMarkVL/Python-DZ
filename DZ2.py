 # Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат


list_x = [0, 1]
list_y = [0, 1]
list_z = [0, 1]

for x in list_x:
    for y in list_y:
        for z in list_z:
            if(not(x or y or z)) == (not x and not y and not z):
                print(f"Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - Истинно, при X ={x} , Y={y}, Z={z}")