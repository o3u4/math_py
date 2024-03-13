import sympy as sp

# 定义复变函数
z = sp.symbols('z')
f = z * sp.exp(sp.I * z) / (z ** 2 - 2 * z + 10)
g = z ** 4 / (2 + 3 * z ** 2) ** 4
h = sp.sin(z) / (z - sp.pi / 2) ** 2

# 计算在z=i + 3i处的留数
residue = sp.residue(f, z, 1 + 3*sp.I)
print("在z=1 + 3i处的留数为:", sp.simplify(residue))

residue2 = sp.residue(g, z, sp.sqrt(sp.Rational(2, 3)) * sp.I)  # Rational构造分数
print("在z=sqrt(2/3)i处的留数为:", sp.simplify(residue2))

residue3 = sp.residue(h, z, sp.pi / 2)
print(sp.simplify(residue3))
