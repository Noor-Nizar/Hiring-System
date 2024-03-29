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
           [1671973653.653653, 'facts.fbc'],
         ('', '', 'fr.kfb'):
           [1671973653.654996, 'fr.fbc'],
         ('', '', 'rules.krb'):
           [1671973653.6750028, 'rules_fc.py'],
        },
        compiler_version)

