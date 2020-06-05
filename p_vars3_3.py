# var int a,b,c;
def p_vars3(p):
    """
    vars3 : vars3_1 ID SEMICOL

    """

    global tipo_var
    global id

    id = [1]
    tipo_var = p[-1]

    if p[-1] == ',':
        tipo_var = 'int'
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)


# var int a,b,c;
def p_vars3_1(p):
    """
    vars3_1 : vars3_1 ID COMMA

    """

    global tipo_var
    global id

    id = [2]
    tipo_var = p[-1]

    if p[-1] == ',':
        tipo_var = 'int'
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)


# var int a,b,c;
def p_vars3_3(p):
    """
    vars3_1 : ID COMMA

    """

    global tipo_var
    global id

    id = [1]
    tipo_var = p[-1]

    if p[-1] == ',':
        tipo_var = 'int'
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)


# var int a,b,c;
def p_vars3_2(p):
    """
    vars3 : ID SEMICOL

    """

    global tipo_var
    global id

    id = [1]
    tipo_var = p[-1]

    if p[-1] == ',':
        tipo_var = 'int'
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)
    else:
        address_id = memory.local_mem(tipo_var)
        v1 = vars(v(id, tipo_var, 'N', scope, address_id))
        vtf.__set__(id, v1)

def p_vars3_empty(p):
    """
    vars3_1 : empty

    """