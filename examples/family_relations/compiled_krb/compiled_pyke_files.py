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
         ('', '', 'fc_example.krb'):
           [1671490497.30577, 'fc_example_fc.py'],
         ('', '', 'example.krb'):
           [1671490497.3237839, 'example_fc.py', 'example_plans.py', 'example_bc.py'],
         ('', '', 'family.kfb'):
           [1671490497.331497, 'family.fbc'],
         ('', '', 'bc2_example.krb'):
           [1671490497.348387, 'bc2_example_bc.py'],
         ('', '', 'bc_example.krb'):
           [1671490497.361978, 'bc_example_bc.py'],
        },
        compiler_version)

