inp = int(input("panjang, lebar, dan tinggi:"))
multi = pow(inp, 3)
L = 6 * pow(inp, 2)

print(f"Volume: {multi}")
print(f"Luas: {L}")

rumus = inp * inp
rumus2 = rumus * 6

p = input("ketahui rumus? (y/n) ")

if p == "y":
    print(f"Volume:\nV = s x s x s\n= {inp} x {inp} x {inp}\n= {rumus} x {inp}\n= {multi}\n")
    print(f"Luas :\nL = 6 (s x s)\n= 6 ({inp} x {inp})\n= 6 ({rumus})\n= {L}")
