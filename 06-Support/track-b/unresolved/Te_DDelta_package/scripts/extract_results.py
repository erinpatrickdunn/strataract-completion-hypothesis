#!/usr/bin/env python3
"""Extract H4/H5 splitting and strain derivatives from QE bands.out files.
Robust H4/H5 ID: within the 4-band H manifold {b17,b18,b19,b20}, the H6 doublet
= adjacent pair with smallest gap; H4/H5 = the other two singlets.
Reports splitting magnitude = upper_singlet - lower_singlet (Barts 2*Delta convention).
"""
import re
def parse_bands(path):
    lines=open(path).read().split('\n'); blocks=[]; i=0
    while i<len(lines):
        m=re.match(r'\s*k = ([\-\d. ]+)\(\s*\d+ PWs\)\s*bands \(ev\):', lines[i])
        if m:
            vals=[]; j=i+1
            while j<len(lines) and lines[j].strip()=='': j+=1
            while j<len(lines):
                mm=re.findall(r'[\-\d]+\.\d+', lines[j])
                if len(mm)>=2: vals.extend([float(x) for x in mm]); j+=1
                else: break
            blocks.append(vals); i=j
        else: i+=1
    return blocks
def delta_eV(tag, hi=3):
    H=parse_bands(f'strain_{tag}/bands.out')[hi]
    M=sorted([H[16],H[17],H[18],H[19]])
    gaps=[(M[1]-M[0],0,1),(M[2]-M[1],1,2),(M[3]-M[2],2,3)]
    g,lo,hi_=min(gaps); dbl={lo,hi_}; sings=[M[i] for i in range(4) if i not in dbl]
    return sings[1]-sings[0]  # eV, >=0
NU=0.6265
def fd(vals):
    e={-0.005:vals[0],-0.0025:vals[1],0.0025:vals[2],0.005:vals[3]}
    f=lambda x:e[x]
    return (f(0.005)-f(-0.005))/0.01, (f(0.0025)-f(-0.0025))/0.005, (-f(0.005)+8*f(0.0025)-8*f(-0.0025)+f(-0.005))/(12*0.0025)
# clamped (eps_perp=0)
cz=[delta_eV('clamp_m0050'),delta_eV('clamp_m0025'),delta_eV('clamp_p0025'),delta_eV('clamp_p0050')]
# transverse (eps_zz=0)
tz=[delta_eV('trans_m0050'),delta_eV('trans_m0025'),delta_eV('trans_p0025'),delta_eV('trans_p0050')]
# Poisson direct (eps_perp=-nu*eps_zz)
pz=[delta_eV('pois_m0050'),delta_eV('pois_m0025'),delta_eV('pois_p0025'),delta_eV('pois_p0050')]
dz5,dz25,dz4=fd(cz); dp5,dp25,dp4=fd(tz); dpo5,dpo25,dpo4=fd(pz)
print("delta0 (clean zero) = 0.1410 eV = 141.00 meV")
print(f"D_z   clamped  : h=.005={dz5:.4f}  h=.0025={dz25:.4f}  4pt={dz4:.4f} eV")
print(f"D_perp transv  : h=.005={dp5:.4f}  h=.0025={dp25:.4f}  4pt={dp4:.4f} eV")
print(f"D_Poisson dir  : h=.005={dpo5:.4f}  h=.0025={dpo25:.4f}  4pt={dpo4:.4f} eV")
print(f"D_Poisson decomp = D_z - nu*D_perp : h=.005={dz5-NU*dp5:.4f}  h=.0025={dz25-NU*dp25:.4f} eV")
