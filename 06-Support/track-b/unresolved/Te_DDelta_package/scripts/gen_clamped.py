#!/usr/bin/env python3
"""Generate clamped-strain SCF + bands inputs for Te (P3_1 21).
Clamped = uniaxial strain along z with transverse lattice fixed (eps_perp=0),
ionic fractional coordinates fixed (ions clamped). Only c (v3) is scaled by (1+eps_zz).
"""
import os

PSEUDO='/home/user/workspace/qe_runs/pseudo'
ROOT='/home/user/workspace/qe_runs'
a0=4.4572; c0=5.9290; u=0.2636

def cell_params(eps_zz):
    c=c0*(1.0+eps_zz)
    return f"""CELL_PARAMETERS {{angstrom}}
  {a0:.4f}   0.000000   0.000000
 -{a0/2:.4f}   {a0*0.8660254:.6f}   0.000000
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

def scf_in(eps_zz, prefix, outdir):
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
{cell_params(eps_zz)}
{ATOMS}
K_POINTS {{automatic}}
  6 6 6  0 0 0
"""

def bands_in(eps_zz, prefix, outdir):
    return f"""&control
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
{cell_params(eps_zz)}
{ATOMS}
{KLIST}
"""

strains=[-0.005,-0.0025,0.0025,0.005]
for eps in strains:
    tag=f"clamp_p{int(round(eps*10000)):+05d}".replace('+','p').replace('-','m')
    # simpler tag
    sgn='p' if eps>=0 else 'm'; tag=f"clamp_{sgn}{abs(int(round(eps*10000))):04d}"
    d=f"{ROOT}/strain_{tag}"; os.makedirs(d, exist_ok=True)
    od=f"{d}/out"
    open(f"{d}/scf.in","w").write(scf_in(eps,f"te{tag}",od))
    open(f"{d}/bands.in","w").write(bands_in(eps,f"te{tag}",od))
    print("generated",tag,"eps_zz=",eps,"->",d)
print("done")
