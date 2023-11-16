def TowerOfHonai(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHonai(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHonai(n-1, aux_rod, to_rod, from_rod)
n = 3
TowerOfHonai(n, "A", "C", "B")
