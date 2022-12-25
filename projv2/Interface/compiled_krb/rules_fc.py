# rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def has_Degree_equivelent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    notany3_worked = True
    with engine.lookup('facts', 'tech_degree', context, \
                       rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany3_worked = False
        if not notany3_worked: break
    if notany3_worked:
      with knowledge_base.Gen_once if index == 1 \
               else engine.lookup('facts', 'tech_cert', context,
                                  rule.foreach_patterns(1)) \
        as gen_1:
        for dummy in gen_1:
          with knowledge_base.Gen_once if index == 2 \
                   else engine.lookup('facts', 'tech_experience', context,
                                      rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              with knowledge_base.Gen_once if index == 3 \
                       else engine.lookup('fr', 'equivDegree', context,
                                          rule.foreach_patterns(3)) \
                as gen_3:
                for dummy in gen_3:
                  if context.lookup_data('years') > context.lookup_data('nyears'):
                    mark5 = context.mark(True)
                    if rule.pattern(0).match_data(context, context,
                            context.lookup_data('years')-context.lookup_data('nyears')):
                      context.end_save_all_undo()
                      engine.assert_('facts', 'QualifiedForTech',
                                     (rule.pattern(1).as_data(context),
                                      rule.pattern(0).as_data(context),)),
                      rule.rule_base.num_fc_rules_triggered += 1
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark5)
  finally:
    context.done()

def is_Qualified_For_Tech(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'tech_degree', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'tech_experience', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'QualifiedForTech',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_SE(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForTech', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('fr', 'SErole', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('y') >= context.lookup_data('yr'):
              with knowledge_base.Gen_once if index == 2 \
                       else engine.lookup('facts', 'tech_cert', context,
                                          rule.foreach_patterns(2)) \
                as gen_2:
                for dummy in gen_2:
                  notany28_worked = True
                  with engine.lookup('facts', 'QualifiedForJob', context, \
                                     rule.foreach_patterns(3)) \
                    as gen_3:
                    for dummy in gen_3:
                      notany28_worked = False
                      if not notany28_worked: break
                  if notany28_worked:
                    engine.assert_('facts', 'QualifiedForJob',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_DSIntern(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForTech', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('y') < 2:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('facts', 'tech_cert', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              engine.assert_('facts', 'QualifiedForJob',
                             (rule.pattern(0).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_DSJunior(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForTech', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('y') >= 2:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('facts', 'QualifiedForTech', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              if context.lookup_data('ys') < 5:
                with knowledge_base.Gen_once if index == 2 \
                         else engine.lookup('facts', 'tech_cert', context,
                                            rule.foreach_patterns(2)) \
                  as gen_2:
                  for dummy in gen_2:
                    engine.assert_('facts', 'QualifiedForJob',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_DSSenior(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForTech', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('y') >= 5:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('facts', 'tech_cert', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              engine.assert_('facts', 'QualifiedForJob',
                             (rule.pattern(0).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_ITIntern(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForTech', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('y') < 2:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('facts', 'tech_cert', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              engine.assert_('facts', 'QualifiedForJob',
                             (rule.pattern(0).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_ITJunior(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForTech', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('y') >= 2:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('facts', 'QualifiedForTech', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              if context.lookup_data('ys') < 5:
                with knowledge_base.Gen_once if index == 2 \
                         else engine.lookup('facts', 'tech_cert', context,
                                            rule.foreach_patterns(2)) \
                  as gen_2:
                  for dummy in gen_2:
                    engine.assert_('facts', 'QualifiedForJob',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_ITSenior(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForTech', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('y') >= 5:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('facts', 'tech_cert', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              engine.assert_('facts', 'QualifiedForJob',
                             (rule.pattern(0).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_CSIntern(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForTech', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('y') <2 :
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('facts', 'tech_cert', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              engine.assert_('facts', 'QualifiedForJob',
                             (rule.pattern(0).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_CSJunior(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForTech', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('y') >=2 :
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('facts', 'QualifiedForTech', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              if context.lookup_data('ys') < 5:
                with knowledge_base.Gen_once if index == 2 \
                         else engine.lookup('facts', 'tech_cert', context,
                                            rule.foreach_patterns(2)) \
                  as gen_2:
                  for dummy in gen_2:
                    engine.assert_('facts', 'QualifiedForJob',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_CSSenior(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForTech', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('y') >= 5:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('facts', 'tech_cert', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              engine.assert_('facts', 'QualifiedForJob',
                             (rule.pattern(0).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_Security(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'gender', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'QualifiedForJob',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_Service(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'gender', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'QualifiedForJob',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_receptionist(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'non_tech_cert', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'QualifiedForJob',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_For_Business(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'business_degree', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'business_experience', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'QualifiedForBuisness',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_For_Business_SL(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    notany150_worked = True
    with engine.lookup('facts', 'non_tech_degree', context, \
                       rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany150_worked = False
        if not notany150_worked: break
    if notany150_worked:
      with knowledge_base.Gen_once if index == 1 \
               else engine.lookup('facts', 'business_cert', context,
                                  rule.foreach_patterns(1)) \
        as gen_1:
        for dummy in gen_1:
          with knowledge_base.Gen_once if index == 2 \
                   else engine.lookup('facts', 'business_experience', context,
                                      rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              if context.lookup_data('years') > 2:
                mark4 = context.mark(True)
                if rule.pattern(0).match_data(context, context,
                        context.lookup_data('years') -2 ):
                  context.end_save_all_undo()
                  engine.assert_('facts', 'QualifiedForBuisness',
                                 (rule.pattern(1).as_data(context),
                                  rule.pattern(0).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
                else: context.end_save_all_undo()
                context.undo_to_mark(mark4)
  finally:
    context.done()

def is_Qualified_for_Sales(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForBuisness', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'QualifiedForJob',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_For_Accounting(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'QualifiedForBuisness', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'QualifiedForJob',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  fc_rule.fc_rule('has_Degree_equivelent', This_rule_base, has_Degree_equivelent,
    (('facts', 'tech_degree',
      (contexts.anonymous('_any'),),
      True),
     ('facts', 'tech_cert',
      (contexts.variable('field'),
       contexts.anonymous('_any'),),
      False),
     ('facts', 'tech_experience',
      (contexts.variable('field'),
       contexts.variable('years'),),
      False),
     ('fr', 'equivDegree',
      (contexts.variable('field'),
       contexts.variable('nyears'),),
      False),),
    (contexts.variable('eyears'),
     contexts.variable('field'),))
  
  fc_rule.fc_rule('is_Qualified_For_Tech', This_rule_base, is_Qualified_For_Tech,
    (('facts', 'tech_degree',
      (contexts.anonymous('_any'),),
      False),
     ('facts', 'tech_experience',
      (contexts.variable('field'),
       contexts.variable('years'),),
      False),),
    (contexts.variable('field'),
     contexts.variable('years'),))
  
  fc_rule.fc_rule('is_Qualified_for_SE', This_rule_base, is_Qualified_for_SE,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('SE'),
       contexts.variable('y'),),
      False),
     ('fr', 'SErole',
      (contexts.variable('role'),
       contexts.variable('yr'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('SE'),
       contexts.anonymous('_any'),),
      False),
     ('facts', 'QualifiedForJob',
      (contexts.anonymous('_any'),),
      True),),
    (contexts.variable('role'),))
  
  fc_rule.fc_rule('is_Qualified_for_DSIntern', This_rule_base, is_Qualified_for_DSIntern,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('DS'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('DS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Data Science Intern'),))
  
  fc_rule.fc_rule('is_Qualified_for_DSJunior', This_rule_base, is_Qualified_for_DSJunior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('DS'),
       contexts.variable('y'),),
      False),
     ('facts', 'QualifiedForTech',
      (pattern.pattern_literal('DS'),
       contexts.variable('ys'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('DS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Data Science Junior'),))
  
  fc_rule.fc_rule('is_Qualified_for_DSSenior', This_rule_base, is_Qualified_for_DSSenior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('DS'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('DS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Data Science Senior'),))
  
  fc_rule.fc_rule('is_Qualified_for_ITIntern', This_rule_base, is_Qualified_for_ITIntern,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('IT'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('IT'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Information Technology Intern'),))
  
  fc_rule.fc_rule('is_Qualified_for_ITJunior', This_rule_base, is_Qualified_for_ITJunior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('IT'),
       contexts.variable('y'),),
      False),
     ('facts', 'QualifiedForTech',
      (pattern.pattern_literal('IT'),
       contexts.variable('ys'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('IT'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Information Technology Junior'),))
  
  fc_rule.fc_rule('is_Qualified_for_ITSenior', This_rule_base, is_Qualified_for_ITSenior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('IT'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('IT'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Information Technology Senior'),))
  
  fc_rule.fc_rule('is_Qualified_for_CSIntern', This_rule_base, is_Qualified_for_CSIntern,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('CS'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('CS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Cyber Security Intern'),))
  
  fc_rule.fc_rule('is_Qualified_for_CSJunior', This_rule_base, is_Qualified_for_CSJunior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('CS'),
       contexts.variable('y'),),
      False),
     ('facts', 'QualifiedForTech',
      (pattern.pattern_literal('CS'),
       contexts.variable('ys'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('CS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Cyber Security Junior'),))
  
  fc_rule.fc_rule('is_Qualified_for_CSSenior', This_rule_base, is_Qualified_for_CSSenior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('CS'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('CS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Cyber Security Senior'),))
  
  fc_rule.fc_rule('is_Qualified_for_Security', This_rule_base, is_Qualified_for_Security,
    (('facts', 'gender',
      (pattern.pattern_literal('male'),),
      False),),
    (pattern.pattern_literal('Security'),))
  
  fc_rule.fc_rule('is_Qualified_for_Service', This_rule_base, is_Qualified_for_Service,
    (('facts', 'gender',
      (pattern.pattern_literal('female'),),
      False),),
    (pattern.pattern_literal('Service'),))
  
  fc_rule.fc_rule('is_Qualified_for_receptionist', This_rule_base, is_Qualified_for_receptionist,
    (('facts', 'non_tech_cert',
      (pattern.pattern_literal('Languages'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Receptionist'),))
  
  fc_rule.fc_rule('is_Qualified_For_Business', This_rule_base, is_Qualified_For_Business,
    (('facts', 'business_degree',
      (contexts.anonymous('_any'),),
      False),
     ('facts', 'business_experience',
      (contexts.variable('field'),
       contexts.variable('years'),),
      False),),
    (contexts.variable('field'),
     contexts.variable('years'),))
  
  fc_rule.fc_rule('is_Qualified_For_Business_SL', This_rule_base, is_Qualified_For_Business_SL,
    (('facts', 'non_tech_degree',
      (contexts.anonymous('_any'),),
      True),
     ('facts', 'business_cert',
      (contexts.anonymous('_any'),
       contexts.anonymous('_any'),),
      False),
     ('facts', 'business_experience',
      (contexts.variable('field'),
       contexts.variable('years'),),
      False),),
    (contexts.variable('eyears'),
     contexts.variable('field'),))
  
  fc_rule.fc_rule('is_Qualified_for_Sales', This_rule_base, is_Qualified_for_Sales,
    (('facts', 'QualifiedForBuisness',
      (pattern.pattern_literal('Sales'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Sales'),))
  
  fc_rule.fc_rule('is_Qualified_For_Accounting', This_rule_base, is_Qualified_For_Accounting,
    (('facts', 'QualifiedForBuisness',
      (pattern.pattern_literal('Accounting'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('Accountant'),))


Krb_filename = '../rules.krb'
Krb_lineno_map = (
    ((13, 16), (4, 4)),
    ((20, 24), (5, 5)),
    ((25, 29), (6, 6)),
    ((30, 34), (7, 7)),
    ((35, 35), (8, 8)),
    ((38, 38), (9, 9)),
    ((40, 42), (11, 11)),
    ((53, 57), (16, 16)),
    ((58, 62), (17, 17)),
    ((63, 65), (19, 19)),
    ((74, 78), (24, 24)),
    ((79, 83), (25, 25)),
    ((84, 84), (26, 26)),
    ((85, 89), (27, 27)),
    ((91, 94), (29, 29)),
    ((98, 99), (31, 31)),
    ((108, 112), (35, 35)),
    ((113, 113), (36, 36)),
    ((114, 118), (37, 37)),
    ((119, 120), (39, 39)),
    ((129, 133), (44, 44)),
    ((134, 134), (45, 45)),
    ((135, 139), (46, 46)),
    ((140, 140), (47, 47)),
    ((141, 145), (48, 48)),
    ((146, 147), (50, 50)),
    ((156, 160), (55, 55)),
    ((161, 161), (56, 56)),
    ((162, 166), (57, 57)),
    ((167, 168), (59, 59)),
    ((177, 181), (63, 63)),
    ((182, 182), (64, 64)),
    ((183, 187), (65, 65)),
    ((188, 189), (67, 67)),
    ((198, 202), (72, 72)),
    ((203, 203), (73, 73)),
    ((204, 208), (74, 74)),
    ((209, 209), (75, 75)),
    ((210, 214), (76, 76)),
    ((215, 216), (78, 78)),
    ((225, 229), (83, 83)),
    ((230, 230), (84, 84)),
    ((231, 235), (85, 85)),
    ((236, 237), (87, 87)),
    ((246, 250), (92, 92)),
    ((251, 251), (93, 93)),
    ((252, 256), (94, 94)),
    ((257, 258), (96, 96)),
    ((267, 271), (101, 101)),
    ((272, 272), (102, 102)),
    ((273, 277), (103, 103)),
    ((278, 278), (104, 104)),
    ((279, 283), (105, 105)),
    ((284, 285), (107, 107)),
    ((294, 298), (112, 112)),
    ((299, 299), (113, 113)),
    ((300, 304), (114, 114)),
    ((305, 306), (116, 116)),
    ((315, 319), (121, 121)),
    ((320, 321), (123, 123)),
    ((330, 334), (128, 128)),
    ((335, 336), (130, 130)),
    ((345, 349), (135, 135)),
    ((350, 351), (137, 137)),
    ((360, 364), (143, 143)),
    ((365, 369), (144, 144)),
    ((370, 372), (146, 146)),
    ((382, 385), (151, 151)),
    ((389, 393), (152, 152)),
    ((394, 398), (153, 153)),
    ((399, 399), (154, 154)),
    ((402, 402), (155, 155)),
    ((404, 406), (157, 157)),
    ((417, 421), (162, 162)),
    ((422, 423), (164, 164)),
    ((432, 436), (169, 169)),
    ((437, 438), (171, 171)),
)
