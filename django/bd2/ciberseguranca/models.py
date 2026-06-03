from django.db import models


class Role(models.Model):

    nome = models.CharField(max_length=100)

    descricao = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome


class Organizacoes(models.Model):

    ESTADOS = [
        ('Conforme', 'Conforme'),
        ('Em avaliação', 'Em avaliação'),
        ('Com pendências', 'Com pendências'),
    ]

    nome = models.CharField(max_length=100)

    responsavel_seguranca = models.CharField(max_length=100)

    contacto_emergencia = models.CharField(max_length=20)

    classificacao_seguranca = models.IntegerField()

    ativo = models.BooleanField(default=True)

    estado_nis2 = models.CharField(
        max_length=30,
        choices=ESTADOS
    )

    def __str__(self):
        return self.nome


class Utilizadores(models.Model):

    nome = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=100)

    ativo = models.BooleanField(default=True)

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE
    )

    organizacao = models.ForeignKey(
        Organizacoes,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome


class Categorias(models.Model):

    nome = models.CharField(max_length=100)

    descricao = models.TextField()

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Tickets(models.Model):

    PRIORIDADES = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
        ('Crítica', 'Crítica'),
    ]

    ESTADOS = [
        ('Aberto', 'Aberto'),
        ('Em análise', 'Em análise'),
        ('Resolvido', 'Resolvido'),
        ('Fechado', 'Fechado'),
    ]

    titulo = models.CharField(max_length=150)

    descricao_suporte = models.TextField()

    data_abertura = models.DateTimeField(auto_now_add=True)

    prioridade = models.CharField(
        max_length=20,
        choices=PRIORIDADES
    )

    estado_resolucao = models.CharField(
        max_length=30,
        choices=ESTADOS
    )

    utilizador = models.ForeignKey(
        Utilizadores,
        on_delete=models.CASCADE
    )

    categoria = models.ForeignKey(
        Categorias,
        on_delete=models.CASCADE
    )

    organizacao = models.ForeignKey(
        Organizacoes,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo


class Documentos(models.Model):

    nome_documento = models.CharField(max_length=150)

    descricao = models.TextField()

    ficheiro = models.FileField(
        upload_to='documentos/'
    )

    data_upload = models.DateTimeField(
        auto_now_add=True
    )

    ticket = models.ForeignKey(
        Tickets,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome_documento


class Chats(models.Model):

    mensagem = models.TextField()

    data_mensagem = models.DateTimeField(
        auto_now_add=True
    )

    utilizador = models.ForeignKey(
        Utilizadores,
        on_delete=models.CASCADE
    )

    ticket = models.ForeignKey(
        Tickets,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return f"{self.utilizador} - {self.ticket}"


class Lembretes(models.Model):

    titulo = models.CharField(max_length=150)

    descricao = models.TextField()

    data_lembrete = models.DateTimeField()

    concluido = models.BooleanField(default=False)

    ticket = models.ForeignKey(
        Tickets,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return self.titulo


class Registos_Logs(models.Model):

    acao = models.CharField(max_length=200)

    descricao = models.TextField()

    data_registo = models.DateTimeField(
        auto_now_add=True
    )

    utilizador = models.ForeignKey(
        Utilizadores,
        on_delete=models.CASCADE
    )

    ticket = models.ForeignKey(
        Tickets,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return self.acao