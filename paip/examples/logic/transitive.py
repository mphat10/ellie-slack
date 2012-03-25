import logging
from paip import logic

def main():
    #logging.basicConfig(level=logging.DEBUG)
    db = logic.Database()

    kim = logic.Atom('Kim')
    robin = logic.Atom('Robin')
    sandy = logic.Atom('Sandy')
    lee = logic.Atom('Lee')
    cats = logic.Atom('cats')
    x = logic.Var('x')
    y = logic.Var('y')
    z = logic.Var('z')

    self_likes = logic.Clause(logic.Relation('likes', (x, x)))
    transitive_likes = logic.Clause(logic.Relation('likes', (x, y)),
        (logic.Relation('likes', (x, z)), logic.Relation('likes', (z, y))))

    klr = logic.Clause(logic.Relation('likes', (kim, robin)))
    sll = logic.Clause(logic.Relation('likes', (sandy, lee)))
    slk = logic.Clause(logic.Relation('likes', (sandy, kim)))
    rlc = logic.Clause(logic.Relation('likes', (robin, cats)))
    llr = logic.Clause(logic.Relation('likes', (lee, robin)))

    db.store(klr)
    db.store(sll)
    db.store(slk)
    db.store(rlc)
    db.store(llr)

    db.store(self_likes)
    db.store(transitive_likes)

    print 'Database:'
    print db
    print
    
    query = logic.Relation('likes', (sandy, logic.Var('who')))
    print 'Query:', str(query)
    print

    logic.prolog_prove([query], db)

