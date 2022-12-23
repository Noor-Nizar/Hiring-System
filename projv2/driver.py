import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal
from pyke import ask_tty
engine = knowledge_engine.engine(__file__)
# Create a Pyke engine
def test():
    engine.reset()
    engine.activate('rules')
    print ("doing proof")
    try :
        with engine.prove_goal('facts.QualifiedForJob($job)') as gen :
            for vars,plan in gen:
                print ("-------------------")
                print (vars['job'])
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    print ()
    print ("done")
    # engine.print_stats()
    
test()