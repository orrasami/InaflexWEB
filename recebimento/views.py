from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .auxiliar.bd_pedidos import BDPedidos
from .auxiliar.funcoes import FuncoesExtras
import pymysql


def get_db_connection():
    conn = pymysql.connect(
        host='mysql.inaflex-app.kinghost.net',
        user='inaflexapp',
        password='zt4cr3',
        db='inaflexapp',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn


def recebimento_index(request):
    if request.method == 'POST':
        username = request.POST["usuario"]
        password = request.POST["password"]
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT recebimento, senhaUsuario, id FROM usuarios WHERE nomeUsuario = '{username}'")
            resposta = cursor.fetchall()
            conn.close()
            senha_login = resposta[0]['senhaUsuario']
            direito = resposta[0]['recebimento']
            if direito == '1':
                if senha_login == password:
                    request.session['username'] = username.upper()
                    return redirect('recebimento_lote')
                else:
                    messages.error(request, 'Senha errada')
                    return render(request, 'recebimento/index.html')
            else:
                messages.error(request, 'Voce não tem direito para acessar esse módulo')
                return render(request, 'recebimento/index.html')
        except:
            messages.error(request, 'Usuario Não Cadastrado')
            return render(request, 'recebimento/index.html')
    else:
        return render(request, 'recebimento/index.html')


def recebimento_lote(request):
    # LOTES - VISUALIZAR / NOVO
    request.session['context'] = None
    usuario_logado = request.session.get('username', None)
    if usuario_logado is not None:
        if request.method == 'POST':
            lote_num = request.POST["lote"]
            conexao = BDPedidos().conectar()
            mensagem, resultados = BDPedidos().verifica_lote(conexao, lote_num)
            BDPedidos().fecha(conexao)
            if mensagem == 1:
                context = {
                    'fornecedor': resultados[0]['fornecedor'],
                    'plcq': resultados[0]['plcq'],
                    'lote': resultados[0]['lote'],
                    'quando': resultados[0]['quando'],
                    'nota': resultados[0]['nota'],
                    'oc': resultados[0]['oc'],
                    'quantidade': resultados[0]['quantidade'],
                    'inspecionado': resultados[0]['inspecionado'],
                    'defeito': resultados[0]['defeito'],
                    'material': resultados[0]['material'],
                    'rnc': resultados[0]['rnc'],
                    'med_forma_1': resultados[0]['med_forma_1'],
                    'med_valor_1': resultados[0]['med_valor_1'],
                    'med_laudo_1': resultados[0]['med_laudo_1'],
                    'med_forma_2': resultados[0]['med_forma_2'],
                    'med_valor_2': resultados[0]['med_valor_2'],
                    'med_laudo_2': resultados[0]['med_laudo_2'],
                    'med_forma_3': resultados[0]['med_forma_3'],
                    'med_valor_3': resultados[0]['med_valor_3'],
                    'med_laudo_3': resultados[0]['med_laudo_3'],
                    'med_forma_4': resultados[0]['med_forma_4'],
                    'med_valor_4': resultados[0]['med_valor_4'],
                    'med_laudo_4': resultados[0]['med_laudo_4'],
                    'med_forma_5': resultados[0]['med_forma_5'],
                    'med_valor_5': resultados[0]['med_valor_5'],
                    'med_laudo_5': resultados[0]['med_laudo_5'],
                    'med_forma_6': resultados[0]['med_forma_6'],
                    'med_valor_6': resultados[0]['med_valor_6'],
                    'med_laudo_6': resultados[0]['med_laudo_6'],
                    'med_forma_7': resultados[0]['med_forma_7'],
                    'med_valor_7': resultados[0]['med_valor_7'],
                    'med_laudo_7': resultados[0]['med_laudo_7'],
                    'med_forma_8': resultados[0]['med_forma_8'],
                    'med_valor_8': resultados[0]['med_valor_8'],
                    'med_laudo_8': resultados[0]['med_laudo_8'],
                    'med_forma_9': resultados[0]['med_forma_9'],
                    'med_valor_9': resultados[0]['med_valor_9'],
                    'med_laudo_9': resultados[0]['med_laudo_9'],
                    'med_forma_10': resultados[0]['med_forma_10'],
                    'med_valor_10': resultados[0]['med_valor_10'],
                    'med_laudo_10': resultados[0]['med_laudo_10'],
                    'med_forma_11': resultados[0]['med_forma_11'],
                    'med_valor_11': resultados[0]['med_valor_11'],
                    'med_laudo_11': resultados[0]['med_laudo_11'],
                    'med_forma_12': resultados[0]['med_forma_12'],
                    'med_valor_12': resultados[0]['med_valor_12'],
                    'med_laudo_12': resultados[0]['med_laudo_12'],
                    'med_forma_13': resultados[0]['med_forma_13'],
                    'med_valor_13': resultados[0]['med_valor_13'],
                    'med_laudo_13': resultados[0]['med_laudo_13'],
                    'med_forma_14': resultados[0]['med_forma_14'],
                    'med_valor_14': resultados[0]['med_valor_14'],
                    'med_laudo_14': resultados[0]['med_laudo_14'],
                    'med_forma_15': resultados[0]['med_forma_15'],
                    'med_valor_15': resultados[0]['med_valor_15'],
                    'med_laudo_15': resultados[0]['med_laudo_15'],
                    'laudo_final': resultados[0]['laudo_final'],
                    'obs_final': resultados[0]['obs_final'],
                    'liberacao_condicional': resultados[0]['liberacao_condicional'],
                    'liberacao': resultados[0]['liberacao'],
                    'novo': '0',
                }
                request.session['context'] = context
                return redirect('recebimento_editar')
            else:
                messages.error(request, 'Lote não existe')
                return render(request, 'recebimento/lote.html')
        else:
            return render(request, 'recebimento/lote.html')
    else:
        return redirect('recebimento_index')


def recebimento_editar(request):
    # VISUALIZAR / NOVO - TELA DE EDIÇÃO
    context = request.session.get('context', None)
    usuario_logado = request.session.get('username', None)
    if usuario_logado is not None:
        if context is not None:
            return render(request, 'recebimento/editar.html', context)
        else:
            return redirect('recebimento_lote')
    else:
        return redirect('recebimento_index')


def recebimento_novo_lote(request):
    # FUNÇÃO DO BOTÃO NOVO - VERIFICA SE LOTE NÃO EXISTE ANTES DE INICAR CRIAÇÃO
    lote_num = request.POST["lote"]
    if len(lote_num) >= 7:
        if lote_num != "":
            conexao = BDPedidos().conectar()
            context = {
                'lote': lote_num,
            }
            mensagem, resultado = BDPedidos().verifica_lote(conexao, lote_num)
            if mensagem == 1:
                messages.error(request, 'Lote já existe')
                return render(request, 'recebimento/lote.html')
            if mensagem == 2:
                request.session['context'] = context
                return redirect('recebimento_editar')
            if mensagem == 3:
                messages.error(request, 'Erro de conexão')
                return render(request, 'recebimento/lote.html')
        else:
            messages.error(request, 'Campo lote não pode estar em branco')
            return render(request, 'recebimento/lote.html')
    else:
        messages.error(request, 'Lote muito pequeno')
        return render(request, 'recebimento/lote.html')


def recebimento_salvar_lote(request):
    converted_context = request.POST.copy()
    context = {}
    context['novo'] = '1'
    for key, value in converted_context.items():
        context[key] = value.upper()
    usuario_logado = request.session.get('username', None)
    context['usuario'] = usuario_logado
    context['liberacao'] = usuario_logado
    if context['lote'] != "":
        if usuario_logado != None:
            if context != None:
                resposta, mensagem = FuncoesExtras().verifica_se_lote_completo(context)
                if resposta == True:
                    conexao = BDPedidos().conectar()
                    status = BDPedidos().salva_lote(conexao, context)
                    BDPedidos().fecha(conexao)
                    if status != '1':
                        mensagem = "Erro ao salvar"
                    context['novo'] = '0'
                messages.error(request, mensagem)
                query_dict = context
                context = {key: str(value) for key, value in query_dict.items()}
                request.session['context'] = context
                return render(request, 'recebimento/editar.html', context)
            else:
                return redirect('recebimento_lote')
        else:
            return redirect('recebimento_index')
    else:
        query_dict = context
        context = {key: str(value) for key, value in query_dict.items()}
        finalizado = request.session.get('finalizado', None)
        context['finalizado'] = finalizado
        messages.error(request, "Lote e obrigatorio")
        return render(request, 'recebimento/editar.html', context)


def recebimento_logout(request):
    # LOGOUT
    request.session['context'] = None
    request.session['username'] = None
    return redirect('recebimento_index')
