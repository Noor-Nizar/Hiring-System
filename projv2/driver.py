# Import Pyke's engine module

from pyke import knowledge_engine, krb_traceback, goal
# Create a Pyke engine

engine = knowledge_engine.engine(__file__)

engine.activate('rules')

my_goal = goal.compile('facts.CSIntern(T)')

any = "T"
# listp = my_goal.prove(engine, any = any)
with my_goal.prove(engine,  T = any) as listp:
    print(list(listp))
    for vars in listp:
        print(vars['T'])
    # for vars in listp:
    #     print("sdfa")
    #     print(vars['T'])

engine.print_stats()