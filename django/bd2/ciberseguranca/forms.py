from django import forms
from .models import Role

class RoleForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da role'
            }),

            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descrição da role'
            }),
        }


from .models import Organizacoes

class OrganizacoesForm(forms.ModelForm):

    class Meta:

        model = Organizacoes

        fields = '__all__'


from .models import Utilizadores

class UtilizadoresForm(forms.ModelForm):

    class Meta:

        model = Utilizadores

        fields = '__all__'



from .models import Categorias

class CategoriasForm(forms.ModelForm):

    class Meta:

        model = Categorias

        fields = '__all__'


from .models import Tickets

class TicketsForm(forms.ModelForm):

    class Meta:

        model = Tickets

        fields = [
            'titulo',
            'descricao_suporte',
            'prioridade',
            'estado_resolucao',
            'utilizador',
            'categoria',
            'organizacao'
        ]


from .models import Documentos
from django.utils import timezone

class DocumentosForm(forms.ModelForm):

    data_upload = forms.DateTimeField(
        label='Data de upload',
        initial=timezone.now,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            },
            format='%Y-%m-%dT%H:%M',
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
    )

    class Meta:

        model = Documentos

        fields = [
            'nome_documento',
            'descricao',
            'ficheiro',
            'data_upload',
            'ticket'
        ]


from .models import Chats

class ChatsForm(forms.ModelForm):

    class Meta:

        model = Chats

        fields = [
            'mensagem',
            'utilizador',
            'ticket'
        ]


from .models import Lembretes

class LembretesForm(forms.ModelForm):

    class Meta:

        model = Lembretes

        fields = [
            'titulo',
            'descricao',
            'data_lembrete',
            'concluido',
            'ticket'
        ]


from .models import Registos_Logs

class RegistosLogsForm(forms.ModelForm):

    class Meta:

        model = Registos_Logs

        fields = [
            'acao',
            'descricao',
            'utilizador',
            'ticket'
        ]

  