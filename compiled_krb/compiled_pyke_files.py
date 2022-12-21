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
         ('', 'examples/family_relations/', 'fc_example.krb'):
           [1671405751.810535, 'fc_example_fc.py'],
         ('', 'examples/family_relations/', 'example.krb'):
           [1671405751.8264709, 'example_fc.py', 'example_plans.py', 'example_bc.py'],
         ('', 'examples/family_relations/', 'family.kfb'):
           [1671405751.8309991, 'family.fbc'],
         ('', 'examples/family_relations/', 'bc2_example.krb'):
           [1671405751.850139, 'bc2_example_bc.py'],
         ('', 'examples/family_relations/', 'bc_example.krb'):
           [1671405751.8627388, 'bc_example_bc.py'],
        },
        compiler_version)

