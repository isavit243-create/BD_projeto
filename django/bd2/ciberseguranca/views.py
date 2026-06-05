from .basedados import *
from .models import Tickets
from .models import Utilizadores
from .models import Organizacoes
from .models import Categorias
from .models import Documentos
from .models import Chats
from .models import Lembretes
from .models import Registos_Logs
from django.shortcuts import render, redirect


from .forms import RoleForm

def criar_role(request):

    if request.method == 'POST':

        form = RoleForm(request.POST)

        if form.is_valid():

            nome = form.cleaned_data['nome']

            descricao = form.cleaned_data['descricao']

            inserir_role(nome, descricao)

            return redirect('listar_roles')

    else:

        form = RoleForm()

    return render(request, 'role_form.html', {
        'form': form
    })


from .forms import OrganizacoesForm

def criar_organizacao(request):

    if request.method == 'POST':

        form = OrganizacoesForm(request.POST)

        if form.is_valid():

            nome = form.cleaned_data['nome']

            responsavel = form.cleaned_data['responsavel_seguranca']

            contacto = form.cleaned_data['contacto_emergencia']

            classificacao = form.cleaned_data['classificacao_seguranca']

            ativo = form.cleaned_data['ativo']

            estado = form.cleaned_data['estado_nis2']

            inserir_organizacao(
                nome,
                responsavel,
                contacto,
                classificacao,
                ativo,
                estado
            )

            return redirect('listar_organizacoes')

    else:

        form = OrganizacoesForm()

    return render(
        request,
        'organizacoes_form.html',
        {'form': form}
    )


from .forms import UtilizadoresForm

def criar_utilizador(request):

    if request.method == 'POST':

        form = UtilizadoresForm(request.POST)

        if form.is_valid():

            nome = form.cleaned_data['nome']

            email = form.cleaned_data['email']

            password = form.cleaned_data['password']

            ativo = form.cleaned_data['ativo']

            role = form.cleaned_data['role']

            organizacao = form.cleaned_data['organizacao']

            inserir_utilizador(
                nome,
                email,
                password,
                ativo,
                role.id,
                organizacao.id
            )

            return redirect('listar_utilizadores')

    else:

        form = UtilizadoresForm()

    return render(
        request,
        'utilizadores_form.html',
        {'form': form}
    )


from .forms import CategoriasForm

def criar_categoria(request):

    if request.method == 'POST':

        form = CategoriasForm(request.POST)

        if form.is_valid():

            nome = form.cleaned_data['nome']

            descricao = form.cleaned_data['descricao']

            ativo = form.cleaned_data['ativo']

            inserir_categoria(
                nome,
                descricao,
                ativo
            )

            return redirect('listar_categorias')

    else:

        form = CategoriasForm()

    return render(
        request,
        'categorias_form.html',
        {'form': form}
    )


from .forms import TicketsForm


def criar_ticket(request):

    if request.method == 'POST':

        form = TicketsForm(request.POST)

        if form.is_valid():

            titulo = form.cleaned_data['titulo']

            descricao = form.cleaned_data['descricao_suporte']

            prioridade = form.cleaned_data['prioridade']

            estado = form.cleaned_data['estado_resolucao']

            utilizador = form.cleaned_data['utilizador']

            categoria = form.cleaned_data['categoria']

            organizacao = form.cleaned_data['organizacao']

            inserir_ticket(
                titulo,
                descricao,
                prioridade,
                estado,
                utilizador.id,
                categoria.id,
                organizacao.id
            )

            return redirect('listar_tickets')

    else:

        form = TicketsForm()

    return render(
        request,
        'tickets_form.html',
        {'form': form}
    )


from .forms import DocumentosForm

def criar_documento(request):

    if request.method == 'POST':

        form = DocumentosForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            nome = form.cleaned_data['nome_documento']

            descricao = form.cleaned_data['descricao']

            ficheiro = form.cleaned_data['ficheiro']

            ticket = form.cleaned_data['ticket']

            data_upload = form.cleaned_data['data_upload']

            inserir_documento(
                nome,
                descricao,
                str(ficheiro),
                ticket.id,
                data_upload
            )

            return redirect('listar_documentos')

    else:

        form = DocumentosForm()

    return render(
        request,
        'documentos_form.html',
        {'form': form}
    )


from .forms import ChatsForm

def criar_chat(request):

    if request.method == 'POST':

        form = ChatsForm(request.POST)

        if form.is_valid():

            mensagem = form.cleaned_data['mensagem']

            utilizador = form.cleaned_data['utilizador']

            ticket = form.cleaned_data['ticket']

            inserir_chat(
                mensagem,
                utilizador.id,
                ticket.id
            )

            return redirect('listar_chats')

    else:

        form = ChatsForm()

    return render(
        request,
        'chats_form.html',
        {'form': form}
    )


from .forms import LembretesForm

def criar_lembrete(request):

    if request.method == 'POST':

        form = LembretesForm(request.POST)

        if form.is_valid():

            titulo = form.cleaned_data['titulo']

            descricao = form.cleaned_data['descricao']

            data_lembrete = form.cleaned_data['data_lembrete']

            concluido = form.cleaned_data['concluido']

            ticket = form.cleaned_data['ticket']

            inserir_lembrete(
                titulo,
                descricao,
                data_lembrete,
                concluido,
                ticket.id
            )

            return redirect('listar_lembretes')

    else:

        form = LembretesForm()

    return render(
        request,
        'lembretes_form.html',
        {'form': form}
    )


from .forms import RegistosLogsForm

def criar_log(request):

    if request.method == 'POST':

        form = RegistosLogsForm(request.POST)

        if form.is_valid():

            acao = form.cleaned_data['acao']

            descricao = form.cleaned_data['descricao']

            utilizador = form.cleaned_data['utilizador']

            ticket = form.cleaned_data['ticket']

            inserir_log(
                acao,
                descricao,
                utilizador.id,
                ticket.id
            )

            return redirect('listar_logs')

    else:

        form = RegistosLogsForm()

    return render(
        request,
        'logs_form.html',
        {'form': form}
    )


def listar_roles_view(request):

    roles = listar_roles()

    return render(
        request,
        'listar_roles.html',
        {'roles': roles}
    )


def eliminar_role_view(request, id):

    try:

        eliminar_role(id)

    except Exception:

        return render(
            request,
            'erro.html',
            {
                'mensagem': 'Não é possível eliminar esta role porque existem utilizadores associados a ela.',
                'voltar_url': '/roles/',
                'voltar_label': 'Voltar às Roles'
            }
        )

    return redirect('listar_roles')


def editar_role_view(request, id):

    role = obter_role(id)

    if request.method == 'POST':

        nome = request.POST['nome']

        descricao = request.POST['descricao']

        atualizar_role(
            id,
            nome,
            descricao
        )

        return redirect('listar_roles')

    return render(
        request,
        'editar_role.html',
        {
            'role': role
        }
    )


def listar_tickets_view(request):

    tickets = listar_tickets()

    return render(
        request,
        'listar_tickets.html',
        {
            'tickets': tickets
        }
    )


def eliminar_ticket_view(request, id):

    try:

        eliminar_ticket(id)

    except Exception:

        return render(
            request,
            'erro.html',
            {
                'mensagem': 'Não é possível eliminar este ticket porque existem documentos, chats, lembretes ou logs associados a ele. Elimine-os primeiro.',
                'voltar_url': '/tickets-lista/',
                'voltar_label': 'Voltar aos Tickets'
            }
        )

    return redirect('listar_tickets')


def editar_ticket_view(request, id):

    ticket = Tickets.objects.get(id=id)

    if request.method == 'POST':

        form = TicketsForm(request.POST, instance=ticket)

        if form.is_valid():

            titulo = form.cleaned_data['titulo']

            descricao = form.cleaned_data['descricao_suporte']

            prioridade = form.cleaned_data['prioridade']

            estado = form.cleaned_data['estado_resolucao']

            utilizador = form.cleaned_data['utilizador']

            categoria = form.cleaned_data['categoria']

            organizacao = form.cleaned_data['organizacao']

            from django.utils import timezone

            # Preenche data_fecho automaticamente quando o ticket é resolvido ou fechado
            if estado in ('Resolvido', 'Fechado') and not ticket.data_fecho:
                data_fecho = timezone.now()
            elif estado not in ('Resolvido', 'Fechado'):
                data_fecho = None
            else:
                data_fecho = ticket.data_fecho

            atualizar_ticket(
                id,
                titulo,
                descricao,
                prioridade,
                estado,
                utilizador.id,
                categoria.id,
                organizacao.id,
                data_fecho
            )

            return redirect('listar_tickets')

    else:

        form = TicketsForm(instance=ticket)

    return render(
        request,
        'editar_ticket.html',
        {
            'form': form
        }
    )


def home(request):

    nis2 = dashboard_nis2()
    nis2_labels  = [row[0] for row in nis2]
    nis2_valores = [row[1] for row in nis2]

    top5 = dashboard_top5_incidentes()
    top5_labels  = [row[0] for row in top5]
    top5_valores = [row[1] for row in top5]

    # Pivota os dados de documentos: meses no eixo X, uma série por cliente
    docs_raw = dashboard_documentos_por_mes()

    docs_meses = sorted(set(row[1] for row in docs_raw))
    docs_clientes = sorted(set(row[0] for row in docs_raw))

    # lookup: {(cliente, mes): total}
    docs_lookup = {(row[0], row[1]): row[2] for row in docs_raw}

    # Uma lista de valores por cliente, alinhada com docs_meses
    docs_series = [
        {
            'label': cliente,
            'data': [docs_lookup.get((cliente, mes), 0) for mes in docs_meses]
        }
        for cliente in docs_clientes
    ]

    roles = dashboard_utilizadores_por_role()
    roles_labels  = [row[0] for row in roles]
    roles_valores = [row[1] for row in roles]

    estados = dashboard_estado_tickets()
    estados_labels  = [row[0] for row in estados]
    estados_valores = [row[1] for row in estados]

    tempo_medio = dashboard_tempo_medio_resolucao()

    return render(
        request,
        'home.html',
        {
            'nis2_labels':      nis2_labels,
            'nis2_valores':     nis2_valores,
            'top5_labels':      top5_labels,
            'top5_valores':     top5_valores,
            'docs_meses':       docs_meses,
            'docs_series':      docs_series,
            'roles_labels':     roles_labels,
            'roles_valores':    roles_valores,
            'estados_labels':   estados_labels,
            'estados_valores':  estados_valores,
            'tempo_medio':      tempo_medio,
        }
    )


def listar_utilizadores_view(request):

    utilizadores = listar_utilizadores()

    return render(
        request,
        'listar_utilizadores.html',
        {
            'utilizadores': utilizadores
        }
    )


def eliminar_utilizador_view(request, id):

    try:

        eliminar_utilizador(id)

    except Exception:

        return render(
            request,
            'erro.html',
            {
                'mensagem': 'Não é possível eliminar este utilizador porque existem tickets, chats ou logs associados a ele.',
                'voltar_url': '/utilizadores-lista/',
                'voltar_label': 'Voltar aos Utilizadores'
            }
        )

    return redirect('listar_utilizadores')


def editar_utilizador_view(request, id):

    utilizador = Utilizadores.objects.get(id=id)

    if request.method == 'POST':

        form = UtilizadoresForm(request.POST, instance=utilizador)

        if form.is_valid():

            nome = form.cleaned_data['nome']

            email = form.cleaned_data['email']

            password = form.cleaned_data['password']

            ativo = form.cleaned_data['ativo']

            role = form.cleaned_data['role']

            organizacao = form.cleaned_data['organizacao']

            atualizar_utilizador(
                id,
                nome,
                email,
                password,
                ativo,
                role.id,
                organizacao.id
            )

            return redirect('listar_utilizadores')

    else:

        form = UtilizadoresForm(instance=utilizador)

    return render(
        request,
        'editar_utilizador.html',
        {
            'form': form
        }
    )


def listar_organizacoes_view(request):

    organizacoes = listar_organizacoes()

    return render(
        request,
        'listar_organizacoes.html',
        {
            'organizacoes': organizacoes
        }
    )


def eliminar_organizacao_view(request, id):

    try:

        eliminar_organizacao(id)

    except Exception:

        return render(
            request,
            'erro.html',
            {
                'mensagem': 'Não é possível eliminar esta organização porque existem utilizadores ou tickets associados a ela.',
                'voltar_url': '/organizacoes-lista/',
                'voltar_label': 'Voltar às Organizações'
            }
        )

    return redirect('listar_organizacoes')

def editar_organizacao_view(request, id):

    organizacao = Organizacoes.objects.get(id=id)

    if request.method == 'POST':

        form = OrganizacoesForm(request.POST, instance=organizacao)

        if form.is_valid():

            nome = form.cleaned_data['nome']

            responsavel = form.cleaned_data['responsavel_seguranca']

            contacto = form.cleaned_data['contacto_emergencia']

            classificacao = form.cleaned_data['classificacao_seguranca']

            ativo = form.cleaned_data['ativo']

            estado = form.cleaned_data['estado_nis2']

            atualizar_organizacao(
                id,
                nome,
                responsavel,
                contacto,
                classificacao,
                ativo,
                estado
            )

            return redirect('listar_organizacoes')

    else:

        form = OrganizacoesForm(instance=organizacao)

    return render(
        request,
        'editar_organizacao.html',
        {
            'form': form
        }
    )


def listar_categorias_view(request):

    categorias = listar_categorias()

    return render(
        request,
        'listar_categorias.html',
        {
            'categorias': categorias
        }
    )


def eliminar_categoria_view(request, id):

    try:

        eliminar_categoria(id)

    except Exception:

        return render(
            request,
            'erro.html',
            {
                'mensagem': 'Não é possível eliminar esta categoria porque existem tickets associados a ela.',
                'voltar_url': '/categorias-lista/',
                'voltar_label': 'Voltar às Categorias'
            }
        )

    return redirect('listar_categorias')


def editar_categoria_view(request, id):

    categoria = Categorias.objects.get(id=id)

    if request.method == 'POST':

        form = CategoriasForm(request.POST, instance=categoria)

        if form.is_valid():

            nome = form.cleaned_data['nome']

            descricao = form.cleaned_data['descricao']

            ativo = form.cleaned_data['ativo']

            atualizar_categoria(
                id,
                nome,
                descricao,
                ativo
            )

            return redirect('listar_categorias')

    else:

        form = CategoriasForm(instance=categoria)

    return render(
        request,
        'editar_categoria.html',
        {
            'form': form
        }
    )


def listar_documentos_view(request):

    documentos = listar_documentos()

    return render(
        request,
        'listar_documentos.html',
        {
            'documentos': documentos
        }
    )


def eliminar_documento_view(request, id):

    try:

        eliminar_documento(id)

    except Exception:

        return render(
            request,
            'erro.html',
            {
                'mensagem': 'Não foi possível eliminar este documento.',
                'voltar_url': '/documentos-lista/',
                'voltar_label': 'Voltar aos Documentos'
            }
        )

    return redirect('listar_documentos')



def editar_documento_view(request, id):

    documento = Documentos.objects.get(id=id)

    if request.method == 'POST':

        form = DocumentosForm(
            request.POST,
            request.FILES,
            instance=documento
        )

        if form.is_valid():

            nome = form.cleaned_data['nome_documento']

            descricao = form.cleaned_data['descricao']

            ficheiro = form.cleaned_data['ficheiro']

            ticket = form.cleaned_data['ticket']

            atualizar_documento(
                id,
                nome,
                descricao,
                str(ficheiro),
                ticket.id
            )

            return redirect('listar_documentos')

    else:

        form = DocumentosForm(instance=documento)

    return render(
        request,
        'editar_documento.html',
        {
            'form': form
        }
    )


def listar_chats_view(request):

    chats = listar_chats()

    return render(
        request,
        'listar_chats.html',
        {
            'chats': chats
        }
    )


def eliminar_chat_view(request, id):

    try:

        eliminar_chat(id)

    except Exception:

        return render(
            request,
            'erro.html',
            {
                'mensagem': 'Não foi possível eliminar esta mensagem.',
                'voltar_url': '/chats-lista/',
                'voltar_label': 'Voltar aos Chats'
            }
        )

    return redirect('listar_chats')


def editar_chat_view(request, id):

    chat = Chats.objects.get(id=id)

    if request.method == 'POST':

        form = ChatsForm(request.POST, instance=chat)

        if form.is_valid():

            mensagem = form.cleaned_data['mensagem']

            utilizador = form.cleaned_data['utilizador']

            ticket = form.cleaned_data['ticket']

            atualizar_chat(
                id,
                mensagem,
                utilizador.id,
                ticket.id
            )

            return redirect('listar_chats')

    else:

        form = ChatsForm(instance=chat)

    return render(
        request,
        'editar_chat.html',
        {
            'form': form
        }
    )


def listar_lembretes_view(request):

    lembretes = listar_lembretes()

    return render(
        request,
        'listar_lembretes.html',
        {
            'lembretes': lembretes
        }
    )


def eliminar_lembrete_view(request, id):

    try:

        eliminar_lembrete(id)

    except Exception:

        return render(
            request,
            'erro.html',
            {
                'mensagem': 'Não foi possível eliminar este lembrete.',
                'voltar_url': '/lembretes-lista/',
                'voltar_label': 'Voltar aos Lembretes'
            }
        )

    return redirect('listar_lembretes')


def editar_lembrete_view(request, id):

    lembrete = Lembretes.objects.get(id=id)

    if request.method == 'POST':

        form = LembretesForm(request.POST, instance=lembrete)

        if form.is_valid():

            titulo = form.cleaned_data['titulo']

            descricao = form.cleaned_data['descricao']

            data_lembrete = form.cleaned_data['data_lembrete']

            concluido = form.cleaned_data['concluido']

            ticket = form.cleaned_data['ticket']

            atualizar_lembrete(
                id,
                titulo,
                descricao,
                data_lembrete,
                concluido,
                ticket.id
            )

            return redirect('listar_lembretes')

    else:

        form = LembretesForm(instance=lembrete)

    return render(
        request,
        'editar_lembrete.html',
        {
            'form': form
        }
    )


def listar_logs_view(request):

    logs = listar_logs()

    return render(
        request,
        'listar_logs.html',
        {
            'logs': logs
        }
    )


def eliminar_log_view(request, id):

    try:

        eliminar_log(id)

    except Exception:

        return render(
            request,
            'erro.html',
            {
                'mensagem': 'Não foi possível eliminar este registo de log.',
                'voltar_url': '/logs-lista/',
                'voltar_label': 'Voltar aos Logs'
            }
        )

    return redirect('listar_logs')


def editar_log_view(request, id):

    log = obter_log(id)

    if request.method == 'POST':

        form = RegistosLogsForm(request.POST)

        if form.is_valid():

            acao = form.cleaned_data['acao']

            descricao = form.cleaned_data['descricao']

            utilizador = form.cleaned_data['utilizador']

            ticket = form.cleaned_data['ticket']

            atualizar_log(
                id,
                acao,
                descricao,
                utilizador.id,
                ticket.id
            )

            return redirect('listar_logs')

    else:

        from .models import Utilizadores, Tickets

        form = RegistosLogsForm(initial={

            'acao': log[1],
            'descricao': log[2],
            'utilizador': Utilizadores.objects.get(id=log[4]),
            'ticket': Tickets.objects.get(id=log[5])

        })

    return render(
        request,
        'editar_log.html',
        {'form': form}
    )


def modelo_logico_view(request):

    return render(request, 'modelo_logico.html')