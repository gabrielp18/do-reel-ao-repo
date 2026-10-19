import numpy as np, pandas as pd
X = pd.read_excel("base_ibov.xlsx", header=[0, 1], index_col=0)
T = ["^BVSP", "ITUB4.SA", "PETR4.SA", "MGLU3.SA"]   # 3 ações
S = X["Close"][T].resample("W-FRI").last()[:"2026-08-21"]  # sexta
R = S.pct_change()["2024-08-30":] * 100             # 104 semanas
m, a = R["^BVSP"], R["ITUB4.SA"]
print(np.polyfit(m, a, 1))                          # (2) a reta: β, α
dm, da = m - m.mean(), a - a.mean()
print(((dm * da) > 0).sum(), ((dm * da) < 0).sum()) # 92 e 12
cov = (dm * da).sum() / (len(m) - 1)                # 5,83 %²
var = (dm**2).sum() / (len(m) - 1)                  # 4,70 %²
print(cov / var)                                    # (3) 1,24
beta = lambda t: R[t].cov(m) / m.var()
print(beta("PETR4.SA"), beta("MGLU3.SA"))           # 0,55 e 1,96
rho = R.corr()["^BVSP"]; s = R.std() / m.std()
print(rho * s)                                      # (5) β = ρ × σa/σm
print(rho**2)                                       # (6) R²: 74, 10, 30 %
ep = lambda t: np.sqrt((1 - rho[t]**2) / (len(m) - 2)) * s[t]  # (8)
print(beta("PETR4.SA") + np.array([-1, 1]) * 1.98 * ep("PETR4.SA"))
H = S.pct_change().dropna()                         # desde 2020
h = H["^BVSP"].rolling(52)                          # janela de 1 ano
bm = H["PETR4.SA"].rolling(52).cov(H["^BVSP"]) / h.var()
print(bm.min(), bm.max())                           # 0,34 e 1,62
w = {"ITUB4.SA": .5, "PETR4.SA": .3, "MGLU3.SA": .2}
bp = sum(q * beta(t) for t, q in w.items())         # (9) 1,18
ib = X["Close"]["^BVSP"].iloc[-1]                   # 174.586 pontos
print(bp * 500_000 / (ib * 0.20))                   # (10) 17 minis
p = R[list(w)] @ pd.Series(w)                       # a carteira
v = lambda r: r.std() * 52**.5                      # vol anual, %
print(v(p), v(p - bp * m))                          # 21,8 e 11,6
