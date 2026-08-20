#!/usr/bin/env python3
"""Generate transverse-clamped and Poisson-path strain inputs for Te.
Transverse: eps_perp applied (a,b scaled), eps_zz=0, ions clamped.
Poisson: eps_zz applied, eps_perp = -nu*eps_zz (a,b and c scaled), ions clamped.
"""
import os
PSEUDO='/home/user/workspace/qe_runs/pseudo'; ROOT='/home/user/workspace/qe_runs'
a0=4.4572; c0=5.9290; u=0.2636; NU=0.6265
def cell(eps_perp, eps_zz):
    a=a0*(1.0+eps_perp); c=c0*(1.0+eps_zz)
    return f"""CELL_PARAMETERS {{angstrom}}
  {a:.4f}   0.000000   0.000000
 -{a/2:.4f}   {a*0.8660254:.6f}   0.000000
  0.0000   0.000000   {c:.4f}"""
ATOMS=f"""ATOMIC_POSITIONS {{crystal}}
  Te  {u:.4f}   0.0000   0.3333333
  Te  0.0000   {u:.4f}   0.6666667
  Te -{u:.4f}  -{u:.4f}   0.0000000"""
KLIST="""K_POINTS {crystal}
7
  0.3333333  0.3333333  0.0000000  1.0
  0.3333333  0.3333333  0.2000000  1.0
  0.3333333  0.3333333  0.4000000  1.0
  0.3333333  0.3333333  0.5000000  1.0
  0.3333333  0.3333333  0.6000000  1.0
  0.3333333  0.3333333  0.8000000  1.0
  0.0000000  0.0000000  0.5000000  1.0"""
def scf(ep,ez,prefix,outdir):
    return f"""&control
  calculation  = 'scf'
  prefix       = '{prefix}'
  pseudo_dir   = '{PSEUDO}'
  outdir       = '{outdir}'
  verbosity    = 'high'
  tstress      = .true.
/
&system
  ibrav       = 0
  nat         = 3
  ntyp        = 1
  ecutwfc     = 50.0
  ecutrho     = 300.0
  noncolin     = .true.
  lspinorb     = .true.
  occupations  = 'smearing'
  smearing     = 'gauss'
  degauss      = 0.01
  nspin        = 4
/
&electrons
  conv_thr     = 1.0D-8
  mixing_beta  = 0.4
  diagonalization = 'david'
  diago_thr_init = 1.0D-5
/
ATOMIC_SPECIES
  Te  127.60  Te.rel-pbe-n-rrkjus_psl.1.0.0.UPF
{cell(ep,ez)}
{ATOMS}
K_POINTS {{automatic}}
  6 6 6  0 0 0
"""
def bands(ep,ez,prefix,outdir):
    return scf(ep,ez,prefix,outdir).replace("calculation  = 'scf'","calculation  = 'bands'",1).replace("restart_mode","  restart_mode").replace("  restart_mode =","restart_mode =") if False else f"""&control
  calculation  = 'bands'
  prefix       = '{prefix}'
  pseudo_dir   = '{PSEUDO}'
  outdir       = '{outdir}'
  verbosity    = 'high'
  restart_mode = 'from_scratch'
/
&system
  ibrav       = 0
  nat         = 3
  ntyp        = 1
  ecutwfc     = 50.0
  ecutrho     = 300.0
  noncolin     = .true.
  lspinorb     = .true.
  occupations  = 'smearing'
  smearing     = 'gauss'
  degauss      = 0.01
  nspin        = 4
  nbnd         = 28
/
&electrons
  conv_thr     = 1.0D-8
  diagonalization = 'david'
  diago_thr_init = 1.0D-6
/
ATOMIC_SPECIES
  Te  127.60  Te.rel-pbe-n-rrkjus_psl.1.0.0.UPF
{cell(ep,ez)}
{ATOMS}
{KLIST}
"""
# transverse series: eps_perp = +/-0.005, +/-0.0025, eps_zz=0
for ep in [-0.005,-0.0025,0.0025,0.005]:
    sgn='p' if ep>=0 else 'm'; tag=f"trans_{sgn}{abs(int(round(ep*10000))):04d}"
    d=f"{ROOT}/strain_{tag}"; os.makedirs(d,exist_ok=True); od=f"{d}/out"
    open(f"{d}/scf.in","w").write(scf(ep,0.0,f"te{tag}",od))
    open(f"{d}/bands.in","w").write(bands(ep,0.0,f"te{tag}",od))
    print("gen",tag,"eps_perp=",ep)
# Poisson series: eps_zz=+/-0.005,+/-0.0025, eps_perp=-nu*eps_zz
for ez in [-0.005,-0.0025,0.0025,0.005]:
    ep=-NU*ez; sgn='p' if ez>=0 else 'm'; tag=f"pois_{sgn}{abs(int(round(ez*10000))):04d}"
    d=f"{ROOT}/strain_{tag}"; os.makedirs(d,exist_ok=True); od=f"{d}/out"
    open(f"{d}/scf.in","w").write(scf(ep,ez,f"te{tag}",od))
    open(f"{d}/bands.in","w").write(bands(ep,ez,f"te{tag}",od))
    print("gen",tag,f"eps_zz={ez} eps_perp={ep:.5f}")
print("done")
