def p_expression(p):
    """
    expression : var_gt
               | var_lt
               | var_equal
               | var_neq
               | var_geq
               | var_leq
               | expr
               | TRUE
               | FALSE
               | ID

    """
    p[0] = p[1]


def p_LT(p):
    """
    var_lt : expr LT expr
    """
    global address_id
    global tipo_var
    global address_op_izq
    global address_op_der

    temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo1 = 'int'
    elif isinstance(p[1], float) is True:
        tipo1 = 'float'
    else:
        tipo1 = 'char'

    if isinstance(p[3], int) is True:
        tipo2 = 'int'
    elif isinstance(p[3], float) is True:
        tipo2 = 'float'
    else:
        tipo2 = 'char'

    res = semCube.checkResult('<', tipo1, tipo2)
    # print("RES ", res)


    if res == 'int':
        tipo_var = 'int'
    elif res == 'float':
        tipo_var = 'float'
    elif res == 'Bool':
        tipo_var = 'bool'


    if tc.__contains__(p[1]) is True:
        address_op_izq = list(tc.__getitem__(p[1]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[1]).values())[0]):
        address_op_izq = list(vtf.__getitem__(p[1]).values())[4]

    if tc.__contains__(p[1]) is True:
        address_op_der = list(tc.__getitem__(p[3]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[3]).values())[0]):
        address_op_der = list(vtf.__getitem__(p[3]).values())[4]


    address_id = memory.temp_mem(tipo_var)
    adidt.__set__(address_id, adid(address_id, temp))
    v1 = vars(v(temp, tipo_var, 'N', 'local', address_id))
    vtf.__set__(temp, v1)

    quad = ('<', address_op_izq, address_op_der, address_id)
    quadList.append(quad)
    p[0] = address_id

    ## FALTA : no ta agregando el 5 del if(2<5)

    # quad = ('<', p[1], p[3], temp)
    # if p[1] < p[3]:
    #     p[0] = True
    #
    # else:
    #     # p[0] = False


def p_GT(p):
    """
    var_gt : expr GT expr
    """

    global address_id
    global tipo_var
    global address_op_izq
    global address_op_der

    temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo1 = 'int'
    elif isinstance(p[1], float) is True:
        tipo1 = 'float'
    else:
        tipo1 = 'char'

    if isinstance(p[3], int) is True:
        tipo2 = 'int'
    elif isinstance(p[3], float) is True:
        tipo2 = 'float'
    else:
        tipo2 = 'char'

    res = semCube.checkResult('>', tipo1, tipo2)
    # print("RES ", res)

    if res == 'int':
        tipo_var = 'int'
    elif res == 'float':
        tipo_var = 'float'
    elif res == 'Bool':
        tipo_var = 'bool'

    if tc.__contains__(p[1]) is True:
        address_op_izq = list(tc.__getitem__(p[1]).values())[2]


    elif vtf.__contains__(list(vtf.__getitem__(p[1]).values())[0]):
        address_op_izq = list(vtf.__getitem__(p[1]).values())[4]

    if tc.__contains__(p[3]) is True:
        address_op_der = list(tc.__getitem__(p[3]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[3]).values())[0]):
        address_op_der = list(vtf.__getitem__(p[3]).values())[4]

    # print("id_op_izq >>> ", vtf.__getitem__('b'))


    # adidt.__set__(address_id, adid(address_id, id))

    address_id = memory.temp_mem(tipo_var)
    adidt.__set__(address_id, adid(address_id, temp))
    v1 = vars(v(temp, tipo_var, 'N', 'local', address_id))
    vtf.__set__(temp, v1)

    ##### print("id con adidt >> ", list(vars(adidt.__getitem__(address_id)).values())[1]) #######

    print(vars(vtf))
    print(address_id)

    quad = ('>', address_op_izq, address_op_der, address_id)
    # quad = ('>', p[1], p[3], temp)
    # quad = ('>', p[1], p[3], memory.temp_mem(tip))
    quadList.append(quad)
    p[0] = address_id



    # if p[1] > p[3]:
    #     p[0] = True
    # else:
    #     p[0] = False

def p_LEQ(p):
    """
    var_leq : expr LEQ expr
    """
    global address_id
    global tipo_var
    global address_op_izq
    global address_op_der

    temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo1 = 'int'
    elif isinstance(p[1], float) is True:
        tipo1 = 'float'
    else:
        tipo1 = 'char'

    if isinstance(p[3], int) is True:
        tipo2 = 'int'
    elif isinstance(p[3], float) is True:
        tipo2 = 'float'
    else:
        tipo2 = 'char'

    res = semCube.checkResult('<=', tipo1, tipo2)
    # print("RES ", res)

    if res == 'int':
        tipo_var = 'int'
    elif res == 'float':
        tipo_var = 'float'
    elif res == 'Bool':
        tipo_var = 'bool'

    if tc.__contains__(p[1]) is True:
        address_op_izq = list(tc.__getitem__(p[1]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[1]).values())[0]):
        address_op_izq = list(vtf.__getitem__(p[1]).values())[4]

    if tc.__contains__(p[1]) is True:
        address_op_der = list(tc.__getitem__(p[3]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[3]).values())[0]):
        address_op_der = list(vtf.__getitem__(p[3]).values())[4]


    address_id = memory.temp_mem(tipo_var)
    adidt.__set__(address_id, adid(address_id, temp))
    v1 = vars(v(temp, tipo_var, 'N', 'local', address_id))
    vtf.__set__(temp, v1)

    quad = ('<=', address_op_izq, address_op_der, address_id)
    quadList.append(quad)
    p[0] = address_id


def p_GEQ(p):
    """
    var_geq : expr GEQ expr
    """
    global address_id
    global tipo_var
    global address_op_izq
    global address_op_der

    temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo1 = 'int'
    elif isinstance(p[1], float) is True:
        tipo1 = 'float'
    else:
        tipo1 = 'char'

    if isinstance(p[3], int) is True:
        tipo2 = 'int'
    elif isinstance(p[3], float) is True:
        tipo2 = 'float'
    else:
        tipo2 = 'char'

    res = semCube.checkResult('>=', tipo1, tipo2)
    # print("RES ", res)

    if res == 'int':
        tipo_var = 'int'
    elif res == 'float':
        tipo_var = 'float'
    elif res == 'Bool':
        tipo_var = 'bool'

    if tc.__contains__(p[1]) is True:
        address_op_izq = list(tc.__getitem__(p[1]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[1]).values())[0]):
        address_op_izq = list(vtf.__getitem__(p[1]).values())[4]

    if tc.__contains__(p[1]) is True:
        address_op_der = list(tc.__getitem__(p[3]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[3]).values())[0]):
        address_op_der = list(vtf.__getitem__(p[3]).values())[4]


    address_id = memory.temp_mem(tipo_var)
    adidt.__set__(address_id, adid(address_id, temp))
    v1 = vars(v(temp, tipo_var, 'N', 'local', address_id))
    vtf.__set__(temp, v1)

    quad = ('>=', address_op_izq, address_op_der, address_id)
    quadList.append(quad)
    p[0] = address_id


def p_EQUAL(p):
    """
    var_equal : expr EQUAL expr
    """
    global address_id
    global tipo_var
    global address_op_izq
    global address_op_der

    temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo1 = 'int'
    elif isinstance(p[1], float) is True:
        tipo1 = 'float'
    else:
        tipo1 = 'char'

    if isinstance(p[3], int) is True:
        tipo2 = 'int'
    elif isinstance(p[3], float) is True:
        tipo2 = 'float'
    else:
        tipo2 = 'char'

    res = semCube.checkResult('==', tipo1, tipo2)
    # print("RES ", res)

    if res == 'int':
        tipo_var = 'int'
    elif res == 'float':
        tipo_var = 'float'
    elif res == 'Bool':
        tipo_var = 'bool'

    if tc.__contains__(p[1]) is True:
        address_op_izq = list(tc.__getitem__(p[1]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[1]).values())[0]):
        address_op_izq = list(vtf.__getitem__(p[1]).values())[4]

    if tc.__contains__(p[1]) is True:
        address_op_der = list(tc.__getitem__(p[3]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[3]).values())[0]):
        address_op_der = list(vtf.__getitem__(p[3]).values())[4]


    address_id = memory.temp_mem(tipo_var)
    adidt.__set__(address_id, adid(address_id, temp))
    v1 = vars(v(temp, tipo_var, 'N', 'local', address_id))
    vtf.__set__(temp, v1)

    quad = ('==', address_op_izq, address_op_der, address_id)
    quadList.append(quad)
    p[0] = address_id


def p_NEQ(p):
    """
    var_neq : expr NEQ expr
    """
    global address_id
    global tipo_var
    global address_op_izq
    global address_op_der

    temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo1 = 'int'
    elif isinstance(p[1], float) is True:
        tipo1 = 'float'
    else:
        tipo1 = 'char'

    if isinstance(p[3], int) is True:
        tipo2 = 'int'
    elif isinstance(p[3], float) is True:
        tipo2 = 'float'
    else:
        tipo2 = 'char'

    res = semCube.checkResult('!=', tipo1, tipo2)
    # print("RES ", res)

    if res == 'int':
        tipo_var = 'int'
    elif res == 'float':
        tipo_var = 'float'
    elif res == 'Bool':
        tipo_var = 'bool'

    if tc.__contains__(p[1]) is True:
        address_op_izq = list(tc.__getitem__(p[1]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[1]).values())[0]):
        address_op_izq = list(vtf.__getitem__(p[1]).values())[4]

    if tc.__contains__(p[1]) is True:
        address_op_der = list(tc.__getitem__(p[3]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[3]).values())[0]):
        address_op_der = list(vtf.__getitem__(p[3]).values())[4]


    address_id = memory.temp_mem(tipo_var)
    adidt.__set__(address_id, adid(address_id, temp))
    v1 = vars(v(temp, tipo_var, 'N', 'local', address_id))
    vtf.__set__(temp, v1)

    quad = ('!=', address_op_izq, address_op_der, address_id)
    quadList.append(quad)
    p[0] = address_id




def p_expr(p):
    """
    expr : expr MUL expr
         | expr DIV expr
         | expr PLUS expr
         | expr MINUS expr
    """
    global address_id
    global tipo_var
    global address_op_izq
    global address_op_der
    global op_izq
    global op_der
    global id_op_izq
    global id_op_der

    op_izq = p[1]
    op_der = p[3]


    if p[2] == '+':
        print(list(tc.__getitem__(op_izq).values())[1])

        op_izq = list(vars(adidt.__getitem__(op_izq)).values())[1]
        op_der = list(vars(adidt.__getitem__(op_der)).values())[1]
        print("1 ", op_izq)

        if isinstance(op_izq, int):
            tipo1 = 'int'
            print("SSSSS")
        elif isinstance(op_izq, float):
            tipo1 = 'float'
        else:
            tipo1 = 'char'

        if isinstance(op_der, int):
            tipo2 = 'int'
            print("DDDDD")
        elif isinstance(op_der, float):
            tipo2 = 'float'
        else:
            tipo2 = 'char'


        res = semCube.checkResult('+', tipo1, tipo2)
        ## FALTA : que cuando tipo2 sea char, usar el valor de esa variable

        if res == 'int':
            tipo_var = 'int'
        elif res == 'float':
            tipo_var = 'float'
        elif res == 'Bool':
            tipo_var = 'bool'
        else:
            print("Type mismatch! ", tipo1, '+', tipo2)
            # sys.exit(0)

        # print(list(tc.__getitem__(op_izq).values())[2])
        if tc.__contains__(op_izq) is True:
            print("2 ", list(tc.__getitem__(op_izq).values())[2])
            address_op_izq = list(tc.__getitem__(op_izq).values())[2]


        if tc.__contains__(op_der) is True:
            print("3 ", list(tc.__getitem__(op_der).values())[2])
            address_op_der = list(tc.__getitem__(op_der).values())[2]



        temp = avail.next()
        address_id = memory.temp_mem(tipo_var)
        # adidt.__set__(address_id, adid(address_id, temp))

        # print(op_izq)
        # print(op_der)

        quad = ('+', address_op_izq, address_op_der, address_id)
        quadList.append(quad)
        p[0] = p[1] + p[3]



    elif p[2] == '-':

        if isinstance(p[1], int) is True:
            tipo1 = 'int'
        elif isinstance(p[1], float) is True:
            tipo1 = 'float'
        else:
            tipo1 = 'char'

        if isinstance(p[3], int) is True:
            tipo2 = 'int'
        elif isinstance(p[3], float) is True:
            tipo2 = 'float'
        else:
            tipo2 = 'char'

        res = semCube.checkResult('-', tipo1, tipo2)

        if res == 'int':
            tip = 'int'
        elif res == 'float':
            tip = 'float'
        elif res == 'Bool':
            tip = 'bool'
        else:
            print("Type mismatch! ", tipo1, '-', tipo2)
            # sys.exit(0)

        if tc.__contains__(op_izq) is True:
            address_op_izq = list(tc.__getitem__(op_izq).values())[2]

        if tc.__contains__(op_der) is True:
            address_op_der = list(tc.__getitem__(op_der).values())[2]

        temp = avail.next()
        address_id = memory.temp_mem(tipo_var)
        quad = ('-', address_op_izq, address_op_der, address_id)
        quadList.append(quad)
        p[0] = address_id

        # # p[0] = p[1] - p[3]
        # temp = avail.next()
        # quad = ('-', p[1], p[3], temp)
        # p[0] = temp
        # # quad_type = semCube.checkResult(p[1],p[3],'+')
        # quadList.append(quad)
        # # print(quadList)

    elif p[2] == '*':

        if isinstance(p[1], int) is True:
            tipo1 = 'int'
        elif isinstance(p[1], float) is True:
            tipo1 = 'float'
        else:
            tipo1 = 'char'

        if isinstance(p[3], int) is True:
            tipo2 = 'int'
        elif isinstance(p[3], float) is True:
            tipo2 = 'float'
        else:
            tipo2 = 'char'

        res = semCube.checkResult('*', tipo1, tipo2)

        if res == 'int':
            tip = 'int'
        elif res == 'float':
            tip = 'float'
        elif res == 'Bool':
            tip = 'bool'
        else:
            print("Type mismatch! ", tipo1, '*', tipo2)
            # sys.exit(0)


        if tc.__contains__(op_izq) is True:
            address_op_izq = list(tc.__getitem__(op_izq).values())[2]

        if tc.__contains__(op_der) is True:
            address_op_der = list(tc.__getitem__(op_der).values())[2]


        temp = avail.next()
        address_id = memory.temp_mem(tipo_var)
        quad = ('*', address_op_izq, address_op_der, address_id)
        quadList.append(quad)
        p[0] = address_id

        # # p[0] = p[1] * p[3]
        # temp = avail.next()
        # quad = ('*', p[1], p[3], temp)
        # p[0] = temp
        # # quad_type = semCube.checkResult(p[1],p[3],'+')
        # quadList.append(quad)
        # # print(quadList)

    elif p[2] == '/':

        if isinstance(p[1], int) is True:
            tipo1 = 'int'
        elif isinstance(p[1], float) is True:
            tipo1 = 'float'
        else:
            tipo1 = 'char'

        if isinstance(p[3], int) is True:
            tipo2 = 'int'
        elif isinstance(p[3], float) is True:
            tipo2 = 'float'
        else:
            tipo2 = 'char'

        res = semCube.checkResult('/', tipo1, tipo2)

        if res == 'int':
            tip = 'int'
        elif res == 'float':
            tip = 'float'
        elif res == 'Bool':
            tip = 'bool'
        else:
            print("Type mismatch! ", tipo1, '/', tipo2)
            # sys.exit(0)


        if tc.__contains__(op_izq) is True:
            address_op_izq = list(tc.__getitem__(op_izq).values())[2]

        if tc.__contains__(op_der) is True:
            address_op_der = list(tc.__getitem__(op_der).values())[2]


        temp = avail.next()
        address_id = memory.temp_mem(tipo_var)
        quad = ('/', address_op_izq, address_op_der, address_id)
        quadList.append(quad)
        p[0] = address_id

        # # p[0] = p[1] / p[3]
        # temp = avail.next()
        # quad = ('/', p[1], p[3], temp)
        # p[0] = temp
        # # quad_type = semCube.checkResult(p[1],p[3],'+')
        # quadList.append(quad)
        # # print(quadList)


def p_expression_int_float(p):
    """
    expr : CTE_I
         | CTE_F
         | ID
    """
    print("EXPR")
    global address_id


    if tc.__contains__(p[1]) is False:
        if isinstance(p[1], int):

            address_id = memory.cte_mem('int')
            c1 = vars(c('int', p[1], address_id))
            tc.__set__(p[1], c1)
            v1 = adid(address_id, p[1])
            adidt.__set__(address_id, adid(address_id, p[1]))
            print(vars(adidt))
            print(vars(tc))
            print(vars(vtf))

        elif isinstance(p[1], float):
            address_id = memory.cte_mem('float')
            c1 = vars(c('float', p[1], address_id))
            tc.__set__(p[1], c1)
            adidt.__set__(address_id, adid(address_id, p[1]))

    elif tc.__contains__(list(vars(adidt.__getitem__(p[1])).values())[1]) is True:
        if isinstance(p[1], int):
            print(vars(tc))
            address_id = memory.cte_mem('int')
            c1 = vars(c('int', p[1], address_id))
            tc.__set__(p[1], c1)
            adidt.__set__(address_id, adid(address_id, p[1]))

        elif isinstance(p[1], float):
            address_id = memory.cte_mem('float')
            c1 = vars(c('float', p[1], address_id))
            tc.__set__(p[1], c1)
            adidt.__set__(address_id, adid(address_id, p[1]))

    p[0] = address_id



def p_GT(p):
    """
    var_gt : expr GT expr
    """

    global address_id
    global tipo_var
    global address_op_izq
    global address_op_der

    temp = avail.next()

    if isinstance(p[1], int) is True:
        tipo1 = 'int'
    elif isinstance(p[1], float) is True:
        tipo1 = 'float'
    else:
        tipo1 = 'char'

    if isinstance(p[3], int) is True:
        tipo2 = 'int'
    elif isinstance(p[3], float) is True:
        tipo2 = 'float'
    else:
        tipo2 = 'char'

    res = semCube.checkResult('>', tipo1, tipo2)
    # print("RES ", res)

    if res == 'int':
        tipo_var = 'int'
    elif res == 'float':
        tipo_var = 'float'
    elif res == 'Bool':
        tipo_var = 'bool'

    if tc.__contains__(p[1]) is True:
        address_op_izq = list(tc.__getitem__(p[1]).values())[2]


    elif vtf.__contains__(list(vtf.__getitem__(p[1]).values())[0]):
        address_op_izq = list(vtf.__getitem__(p[1]).values())[4]

    if tc.__contains__(p[3]) is True:
        address_op_der = list(tc.__getitem__(p[3]).values())[2]

    elif vtf.__contains__(list(vtf.__getitem__(p[3]).values())[0]):
        address_op_der = list(vtf.__getitem__(p[3]).values())[4]

    # print("id_op_izq >>> ", vtf.__getitem__('b'))


    # adidt.__set__(address_id, adid(address_id, id))

    address_id = memory.temp_mem(tipo_var)
    adidt.__set__(address_id, adid(address_id, temp))
    v1 = vars(v(temp, tipo_var, 'N', 'local', address_id))
    vtf.__set__(temp, v1)

    ##### print("id con adidt >> ", list(vars(adidt.__getitem__(address_id)).values())[1]) #######

    print(vars(vtf))
    print(address_id)

    quad = ('>', address_op_izq, address_op_der, address_id)
    # quad = ('>', p[1], p[3], temp)
    # quad = ('>', p[1], p[3], memory.temp_mem(tip))
    quadList.append(quad)
    p[0] = address_id



    # if p[1] > p[3]:
    #     p[0] = True
    # else:
    #     p[0] = False