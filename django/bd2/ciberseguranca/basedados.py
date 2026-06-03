import psycopg2


def ligar_bd():

    ligacao = psycopg2.connect(

        host='ep-delicate-lab-aplt581l-pooler.c-7.us-east-1.aws.neon.tech',

        database='neondb',

        user='neondb_owner',

        password='npg_vsaXJuGhx4e6',

        port='5432',

        sslmode='require'
    )

    return ligacao


def inserir_role(nome, descricao):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        INSERT INTO ciberseguranca_role
        (nome, descricao)

        VALUES (%s, %s)
    """

    cursor.execute(sql, (nome, descricao))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def inserir_organizacao(
    nome,
    responsavel,
    contacto,
    classificacao,
    ativo,
    estado
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        INSERT INTO ciberseguranca_organizacoes
        (
            nome,
            responsavel_seguranca,
            contacto_emergencia,
            classificacao_seguranca,
            ativo,
            estado_nis2
        )

        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (
        nome,
        responsavel,
        contacto,
        classificacao,
        ativo,
        estado
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def inserir_utilizador(
    nome,
    email,
    password,
    ativo,
    role_id,
    organizacao_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        INSERT INTO ciberseguranca_utilizadores
        (
            nome,
            email,
            password,
            ativo,
            role_id,
            organizacao_id
        )

        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (
        nome,
        email,
        password,
        ativo,
        role_id,
        organizacao_id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def inserir_categoria(
    nome,
    descricao,
    ativo
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        INSERT INTO ciberseguranca_categorias
        (
            nome,
            descricao,
            ativo
        )

        VALUES (%s, %s, %s)
    """

    cursor.execute((
        sql
    ), (
        nome,
        descricao,
        ativo
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def inserir_ticket(
    titulo,
    descricao,
    prioridade,
    estado,
    utilizador_id,
    categoria_id,
    organizacao_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        INSERT INTO ciberseguranca_tickets
        (
            titulo,
            descricao_suporte,
            prioridade,
            estado_resolucao,
            utilizador_id,
            categoria_id,
            organizacao_id,
            data_abertura
        )

        VALUES
        (%s, %s, %s, %s, %s, %s, %s, NOW())
    """

    cursor.execute(sql, (
        titulo,
        descricao,
        prioridade,
        estado,
        utilizador_id,
        categoria_id,
        organizacao_id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def inserir_documento(
    nome,
    descricao,
    ficheiro,
    ticket_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        INSERT INTO ciberseguranca_documentos
        (
            nome_documento,
            descricao,
            ficheiro,
            ticket_id,
            data_upload
        )

        VALUES (%s, %s, %s, %s, NOW())
    """

    cursor.execute(sql, (
        nome,
        descricao,
        ficheiro,
        ticket_id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def inserir_chat(
    mensagem,
    utilizador_id,
    ticket_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        INSERT INTO ciberseguranca_chats
        (
            mensagem,
            utilizador_id,
            ticket_id,
            data_mensagem
        )

        VALUES (%s, %s, %s, NOW())
    """

    cursor.execute(sql, (
        mensagem,
        utilizador_id,
        ticket_id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def inserir_lembrete(
    titulo,
    descricao,
    data_lembrete,
    concluido,
    ticket_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        INSERT INTO ciberseguranca_lembretes
        (
            titulo,
            descricao,
            data_lembrete,
            concluido,
            ticket_id
        )

        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (
        titulo,
        descricao,
        data_lembrete,
        concluido,
        ticket_id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def inserir_log(
    acao,
    descricao,
    utilizador_id,
    ticket_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        INSERT INTO ciberseguranca_registos_logs
        (
            acao,
            descricao,
            utilizador_id,
            ticket_id,
            data_registo
        )

        VALUES (%s, %s, %s, %s, NOW())
    """

    cursor.execute(sql, (
        acao,
        descricao,
        utilizador_id,
        ticket_id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def listar_roles():

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT *
        FROM ciberseguranca_role
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    cursor.close()

    ligacao.close()

    return dados


def eliminar_role(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        DELETE FROM ciberseguranca_role
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def obter_role(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT *
        FROM ciberseguranca_role
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    dados = cursor.fetchone()

    cursor.close()

    ligacao.close()

    return dados


def atualizar_role(id, nome, descricao):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        UPDATE ciberseguranca_role

        SET
            nome = %s,
            descricao = %s

        WHERE id = %s
    """

    cursor.execute(sql, (
        nome,
        descricao,
        id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def listar_tickets():

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT
            t.id,
            t.titulo,
            t.prioridade,
            t.estado_resolucao,
            u.nome,
            c.nome,
            o.nome

        FROM ciberseguranca_tickets t

        INNER JOIN ciberseguranca_utilizadores u
            ON t.utilizador_id = u.id

        INNER JOIN ciberseguranca_categorias c
            ON t.categoria_id = c.id

        INNER JOIN ciberseguranca_organizacoes o
            ON t.organizacao_id = o.id

        ORDER BY t.id
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    cursor.close()

    ligacao.close()

    return dados


def eliminar_ticket(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        DELETE FROM ciberseguranca_tickets
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def obter_ticket(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT *
        FROM ciberseguranca_tickets
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    dados = cursor.fetchone()

    cursor.close()

    ligacao.close()

    return dados


def atualizar_ticket(
    id,
    titulo,
    descricao,
    prioridade,
    estado,
    utilizador_id,
    categoria_id,
    organizacao_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        UPDATE ciberseguranca_tickets

        SET
            titulo = %s,
            descricao_suporte = %s,
            prioridade = %s,
            estado_resolucao = %s,
            utilizador_id = %s,
            categoria_id = %s,
            organizacao_id = %s

        WHERE id = %s
    """

    cursor.execute(sql, (
        titulo,
        descricao,
        prioridade,
        estado,
        utilizador_id,
        categoria_id,
        organizacao_id,
        id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def listar_utilizadores():

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT
            u.id,
            u.nome,
            u.email,
            u.ativo,
            r.nome,
            o.nome

        FROM ciberseguranca_utilizadores u

        INNER JOIN ciberseguranca_role r
            ON u.role_id = r.id

        INNER JOIN ciberseguranca_organizacoes o
            ON u.organizacao_id = o.id

        ORDER BY u.id
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    cursor.close()

    ligacao.close()

    return dados


def eliminar_utilizador(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        DELETE FROM ciberseguranca_utilizadores
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def atualizar_utilizador(
    id,
    nome,
    email,
    password,
    ativo,
    role_id,
    organizacao_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        UPDATE ciberseguranca_utilizadores

        SET
            nome = %s,
            email = %s,
            password = %s,
            ativo = %s,
            role_id = %s,
            organizacao_id = %s

        WHERE id = %s
    """

    cursor.execute(sql, (
        nome,
        email,
        password,
        ativo,
        role_id,
        organizacao_id,
        id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def listar_organizacoes():

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT
            id,
            nome,
            responsavel_seguranca,
            contacto_emergencia,
            classificacao_seguranca,
            ativo,
            estado_nis2

        FROM ciberseguranca_organizacoes

        ORDER BY id
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    cursor.close()

    ligacao.close()

    return dados


def eliminar_organizacao(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        DELETE FROM ciberseguranca_organizacoes
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def atualizar_organizacao(
    id,
    nome,
    responsavel,
    contacto,
    classificacao,
    ativo,
    estado
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        UPDATE ciberseguranca_organizacoes

        SET
            nome = %s,
            responsavel_seguranca = %s,
            contacto_emergencia = %s,
            classificacao_seguranca = %s,
            ativo = %s,
            estado_nis2 = %s

        WHERE id = %s
    """

    cursor.execute(sql, (
        nome,
        responsavel,
        contacto,
        classificacao,
        ativo,
        estado,
        id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def listar_categorias():

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT
            id,
            nome,
            descricao,
            ativo

        FROM ciberseguranca_categorias

        ORDER BY id
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    cursor.close()

    ligacao.close()

    return dados


def eliminar_categoria(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        DELETE FROM ciberseguranca_categorias
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def atualizar_categoria(
    id,
    nome,
    descricao,
    ativo
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        UPDATE ciberseguranca_categorias

        SET
            nome = %s,
            descricao = %s,
            ativo = %s

        WHERE id = %s
    """

    cursor.execute(sql, (
        nome,
        descricao,
        ativo,
        id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def listar_documentos():

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT
            d.id,
            d.nome_documento,
            d.descricao,
            d.ficheiro,
            t.titulo

        FROM ciberseguranca_documentos d

        INNER JOIN ciberseguranca_tickets t
            ON d.ticket_id = t.id

        ORDER BY d.id
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    cursor.close()

    ligacao.close()

    return dados


def eliminar_documento(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        DELETE FROM ciberseguranca_documentos
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def atualizar_documento(
    id,
    nome,
    descricao,
    ficheiro,
    ticket_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        UPDATE ciberseguranca_documentos

        SET
            nome_documento = %s,
            descricao = %s,
            ficheiro = %s,
            ticket_id = %s

        WHERE id = %s
    """

    cursor.execute(sql, (
        nome,
        descricao,
        ficheiro,
        ticket_id,
        id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def listar_chats():

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT
            c.id,
            c.mensagem,
            c.data_mensagem,
            u.nome,
            t.titulo

        FROM ciberseguranca_chats c

        INNER JOIN ciberseguranca_utilizadores u
            ON c.utilizador_id = u.id

        INNER JOIN ciberseguranca_tickets t
            ON c.ticket_id = t.id

        ORDER BY c.id
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    cursor.close()

    ligacao.close()

    return dados

def eliminar_chat(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        DELETE FROM ciberseguranca_chats
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    ligacao.commit()

    cursor.close()

    ligacao.close()

def atualizar_chat(
    id,
    mensagem,
    utilizador_id,
    ticket_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        UPDATE ciberseguranca_chats

        SET
            mensagem = %s,
            utilizador_id = %s,
            ticket_id = %s

        WHERE id = %s
    """

    cursor.execute(sql, (
        mensagem,
        utilizador_id,
        ticket_id,
        id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def listar_lembretes():

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
    SELECT
        l.id,
        l.titulo,
        l.descricao,
        l.data_lembrete,
        l.concluido,
        t.titulo

    FROM ciberseguranca_lembretes l

    INNER JOIN ciberseguranca_tickets t
        ON l.ticket_id = t.id

    ORDER BY l.id
    """
    cursor.execute(sql)

    dados = cursor.fetchall()

    cursor.close()

    ligacao.close()

    return dados


def eliminar_lembrete(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        DELETE FROM ciberseguranca_lembretes
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def atualizar_lembrete(
    id,
    titulo,
    descricao,
    data_lembrete,
    concluido,
    ticket_id
):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        UPDATE ciberseguranca_lembretes

        SET
            titulo = %s,
            descricao = %s,
            data_lembrete = %s,
            concluido = %s,
            ticket_id = %s

        WHERE id = %s
    """

    cursor.execute(sql, (
        titulo,
        descricao,
        data_lembrete,
        concluido,
        ticket_id,
        id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def listar_logs():

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT
            l.id,
            l.acao,
            l.descricao,
            l.data_registo,
            u.nome

        FROM ciberseguranca_registos_logs l

        INNER JOIN ciberseguranca_utilizadores u
            ON l.utilizador_id = u.id

        ORDER BY l.id
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    cursor.close()

    ligacao.close()

    return dados


def obter_log(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        SELECT *
        FROM ciberseguranca_registos_logs
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    dados = cursor.fetchone()

    cursor.close()

    ligacao.close()

    return dados
    

def eliminar_log(id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        DELETE FROM ciberseguranca_registos_logs
        WHERE id = %s
    """

    cursor.execute(sql, (id,))

    ligacao.commit()

    cursor.close()

    ligacao.close()


def atualizar_log(id, acao, descricao, utilizador_id, ticket_id):

    ligacao = ligar_bd()

    cursor = ligacao.cursor()

    sql = """
        UPDATE ciberseguranca_registos_logs

        SET
            acao = %s,
            descricao = %s,
            utilizador_id = %s,
            ticket_id = %s

        WHERE id = %s
    """

    cursor.execute(sql, (
        acao,
        descricao,
        utilizador_id,
        ticket_id,
        id
    ))

    ligacao.commit()

    cursor.close()

    ligacao.close()