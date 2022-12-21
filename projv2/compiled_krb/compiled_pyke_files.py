# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'facts.kfb'):
           [1671651479.976526, 'facts.fbc'],
         ('', '', 'rules.krb'):
           [1671651479.991918, 'rules_fc.py'],
        },
        compiler_version)

