# rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def no_degree(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'tech_degree', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'non_tech_degree', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'no_degree',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_For_Tech_SLfacts(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'no_degree', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
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
                if context.lookup_data('years') > 2:
                  mark4 = context.mark(True)
                  if rule.pattern(0).match_data(context, context,
                          years-2):
                    context.end_save_all_undo()
                    engine.assert_('facts', 'QualifiedForTech',
                                   (rule.pattern(1).as_data(context),
                                    rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
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

def is_Qualified_for_SEIntern(rule, context = None, index = None):
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
              engine.assert_('facts', 'SEIntern',
                             (rule.pattern(0).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_For_SEJunior(rule, context = None, index = None):
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
                    engine.assert_('facts', 'SEJunior',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_SESenior(rule, context = None, index = None):
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
              engine.assert_('facts', 'SESenior',
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
              engine.assert_('facts', 'DSIntern',
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
                    engine.assert_('facts', 'DSJunior',
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
              engine.assert_('facts', 'DSSenior',
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
              engine.assert_('facts', 'ITIntern',
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
                    engine.assert_('facts', 'ITJunior',
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
              engine.assert_('facts', 'ITSenior',
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
              engine.assert_('facts', 'CSIntern',
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
                    engine.assert_('facts', 'CSJunior',
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
              engine.assert_('facts', 'CSSenior',
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
        engine.assert_('facts', 'QualifiedForsecurity',
                       ()),
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
        engine.assert_('facts', 'QualifiedForservice',
                       ()),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_Qualified_for_receptionest(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'non_tech_cert', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'QualifiedForreceptionest',
                       ()),
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
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'no_degree', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
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
        engine.assert_('facts', 'SalesPerson',
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
        engine.assert_('facts', 'Accountant',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  fc_rule.fc_rule('no_degree', This_rule_base, no_degree,
    (('facts', 'tech_degree',
      (contexts.anonymous('_any'),),
      False),
     ('facts', 'non_tech_degree',
      (contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_For_Tech_SLfacts', This_rule_base, is_Qualified_For_Tech_SLfacts,
    (('facts', 'no_degree',
      (),
      False),
     ('facts', 'tech_cert',
      (contexts.anonymous('_any'),
       contexts.anonymous('_any'),),
      False),
     ('facts', 'tech_experience',
      (contexts.variable('field'),
       contexts.variable('years'),),
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
  
  fc_rule.fc_rule('is_Qualified_for_SEIntern', This_rule_base, is_Qualified_for_SEIntern,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('SE'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('SE'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_For_SEJunior', This_rule_base, is_Qualified_For_SEJunior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('SE'),
       contexts.variable('y'),),
      False),
     ('facts', 'QualifiedForTech',
      (pattern.pattern_literal('SE'),
       contexts.variable('ys'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('SE'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_for_SESenior', This_rule_base, is_Qualified_for_SESenior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('SE'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('SE'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_for_DSIntern', This_rule_base, is_Qualified_for_DSIntern,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('DS'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('DS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
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
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_for_DSSenior', This_rule_base, is_Qualified_for_DSSenior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('DS'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('DS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_for_ITIntern', This_rule_base, is_Qualified_for_ITIntern,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('IT'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('IT'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
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
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_for_ITSenior', This_rule_base, is_Qualified_for_ITSenior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('IT'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('IT'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_for_CSIntern', This_rule_base, is_Qualified_for_CSIntern,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('CS'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('CS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_for_CSJunior', This_rule_base, is_Qualified_for_CSJunior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('CS'),
       contexts.variable('y'),),
      False),
     ('facts', 'QualifiedForTech',
      (contexts.variable('ys'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('CS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_for_CSSenior', This_rule_base, is_Qualified_for_CSSenior,
    (('facts', 'QualifiedForTech',
      (pattern.pattern_literal('CS'),
       contexts.variable('y'),),
      False),
     ('facts', 'tech_cert',
      (pattern.pattern_literal('CS'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_for_Security', This_rule_base, is_Qualified_for_Security,
    (('facts', 'gender',
      (pattern.pattern_literal('male'),),
      False),),
    ())
  
  fc_rule.fc_rule('is_Qualified_for_Service', This_rule_base, is_Qualified_for_Service,
    (('facts', 'gender',
      (pattern.pattern_literal('female'),),
      False),),
    ())
  
  fc_rule.fc_rule('is_Qualified_for_receptionest', This_rule_base, is_Qualified_for_receptionest,
    (('facts', 'non_tech_cert',
      (pattern.pattern_literal('Languages'),
       contexts.anonymous('_any'),),
      False),),
    ())
  
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
    (('facts', 'no_degree',
      (),
      False),
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
    (pattern.pattern_literal('T'),))
  
  fc_rule.fc_rule('is_Qualified_For_Accounting', This_rule_base, is_Qualified_For_Accounting,
    (('facts', 'QualifiedForBuisness',
      (pattern.pattern_literal('Accounting'),
       contexts.anonymous('_any'),),
      False),),
    (pattern.pattern_literal('T'),))


Krb_filename = '../rules.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 21), (4, 4)),
    ((22, 23), (6, 6)),
    ((32, 36), (10, 10)),
    ((37, 41), (11, 11)),
    ((42, 46), (12, 12)),
    ((47, 47), (13, 13)),
    ((50, 50), (14, 14)),
    ((52, 54), (16, 16)),
    ((65, 69), (21, 21)),
    ((70, 74), (22, 22)),
    ((75, 77), (24, 24)),
    ((86, 90), (29, 29)),
    ((91, 91), (30, 30)),
    ((92, 96), (31, 31)),
    ((97, 98), (33, 33)),
    ((107, 111), (37, 37)),
    ((112, 112), (38, 38)),
    ((113, 117), (39, 39)),
    ((118, 118), (40, 40)),
    ((119, 123), (41, 41)),
    ((124, 125), (43, 43)),
    ((134, 138), (48, 48)),
    ((139, 139), (49, 49)),
    ((140, 144), (50, 50)),
    ((145, 146), (52, 52)),
    ((155, 159), (57, 57)),
    ((160, 160), (58, 58)),
    ((161, 165), (59, 59)),
    ((166, 167), (61, 61)),
    ((176, 180), (66, 66)),
    ((181, 181), (67, 67)),
    ((182, 186), (68, 68)),
    ((187, 187), (69, 69)),
    ((188, 192), (70, 70)),
    ((193, 194), (72, 72)),
    ((203, 207), (77, 77)),
    ((208, 208), (78, 78)),
    ((209, 213), (79, 79)),
    ((214, 215), (81, 81)),
    ((224, 228), (85, 85)),
    ((229, 229), (86, 86)),
    ((230, 234), (87, 87)),
    ((235, 236), (89, 89)),
    ((245, 249), (94, 94)),
    ((250, 250), (95, 95)),
    ((251, 255), (96, 96)),
    ((256, 256), (97, 97)),
    ((257, 261), (98, 98)),
    ((262, 263), (100, 100)),
    ((272, 276), (105, 105)),
    ((277, 277), (106, 106)),
    ((278, 282), (107, 107)),
    ((283, 284), (109, 109)),
    ((293, 297), (114, 114)),
    ((298, 298), (115, 115)),
    ((299, 303), (116, 116)),
    ((304, 305), (118, 118)),
    ((314, 318), (123, 123)),
    ((319, 319), (124, 124)),
    ((320, 324), (125, 125)),
    ((325, 325), (126, 126)),
    ((326, 330), (127, 127)),
    ((331, 332), (129, 129)),
    ((341, 345), (134, 134)),
    ((346, 346), (135, 135)),
    ((347, 351), (136, 136)),
    ((352, 353), (138, 138)),
    ((362, 366), (143, 143)),
    ((367, 368), (145, 145)),
    ((377, 381), (150, 150)),
    ((382, 383), (152, 152)),
    ((392, 396), (157, 157)),
    ((397, 398), (159, 159)),
    ((407, 411), (165, 165)),
    ((412, 416), (166, 166)),
    ((417, 419), (168, 168)),
    ((428, 432), (172, 172)),
    ((433, 437), (173, 173)),
    ((438, 442), (174, 174)),
    ((443, 443), (175, 175)),
    ((446, 446), (176, 176)),
    ((448, 450), (178, 178)),
    ((461, 465), (183, 183)),
    ((466, 467), (185, 185)),
    ((476, 480), (190, 190)),
    ((481, 482), (192, 192)),
)
