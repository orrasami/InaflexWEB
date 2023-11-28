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


def liberacao_pedidos_index(request):
    if request.method == 'POST':
        username = request.POST["usuario"]
        password = request.POST["password"]
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT liberacao_pedidos, senhaUsuario, id FROM usuarios WHERE nomeUsuario = '{username}'")
            resposta = cursor.fetchall()
            conn.close()
            senha_login = resposta[0]['senhaUsuario']
            direito = resposta[0]['liberacao_pedidos']
            if direito == '1':
                if senha_login == password:
                    request.session['username'] = username.upper()
                    return redirect('liberacao_pedidos_orcamento')
                else:
                    messages.error(request, 'Senha errada')
                    return render(request, 'liberacao_pedidos/index.html')
            else:
                messages.error(request, 'Voce não tem direito para acessar esse módulo')
                return render(request, 'liberacao_pedidos/index.html')
        except:
            messages.error(request, 'Usuario Não Cadastrado')
            return render(request, 'liberacao_pedidos/index.html')
    else:
        return render(request, 'liberacao_pedidos/index.html')


def liberacao_pedidos_orcamento(request):
    # LOTES - VISUALIZAR / NOVO
    request.session['context'] = None
    usuario_logado = request.session.get('username', None)
    if usuario_logado != None:
        if request.method == 'POST':
            orcamento = request.POST["orcamento"]
            conexao = BDPedidos().conectar()
            mensagem, resultados = BDPedidos().verifica_orcamento(conexao, orcamento)
            BDPedidos().fecha(conexao)
            if mensagem == 1:
                context = {
                    'orcamento': resultados[0]['orcamento'],
                    'quando': resultados[0]['quando'],
                    'ckl_01': resultados[0]['ckl_01'],
                    'ckl_02': resultados[0]['ckl_02'],
                    'ckl_03': resultados[0]['ckl_03'],
                    'ckl_04': resultados[0]['ckl_04'],
                    'ckl_05': resultados[0]['ckl_05'],
                    'ckl_06': resultados[0]['ckl_06'],
                    'ckl_07': resultados[0]['ckl_07'],
                    'ckl_08': resultados[0]['ckl_08'],
                    'ckl_09': resultados[0]['ckl_09'],
                    'ckl_10': resultados[0]['ckl_10'],
                    'ckl_11': resultados[0]['ckl_11'],
                    'ckl_12': resultados[0]['ckl_12'],
                    'ckl_13': resultados[0]['ckl_13'],
                    'ckl_14': resultados[0]['ckl_14'],
                    'ckl_15': resultados[0]['ckl_15'],
                    'ckl_16': resultados[0]['ckl_16'],
                    'responsavel': resultados[0]['responsavel'],
                    'obs': resultados[0]['obs'],
                    'novo': '0',
                    'usuario_logado': usuario_logado,
                }
                request.session['context'] = context
                return redirect('liberacao_pedidos_editar')
            else:
                messages.error(request, 'Orçamento não existe')
                return render(request, 'liberacao_pedidos/orcamento.html')
        else:
            return render(request, 'liberacao_pedidos/orcamento.html')
    else:
        return redirect('liberacao_pedidos_index')


def liberacao_pedidos_editar(request):
    # VISUALIZAR / NOVO - TELA DE EDIÇÃO
    context = request.session.get('context', None)
    usuario_logado = request.session.get('username', None)
    if usuario_logado != None:
        if context != None:
            return render(request, 'liberacao_pedidos/editar.html', context)
        else:
            return redirect('liberacao_pedidos_orcamento')
    else:
        return redirect('liberacao_pedidos_index')


def liberacao_pedidos_novo_orcamento(request):
    # FUNÇÃO DO BOTÃO NOVO - VERIFICA SE LOTE NÃO EXISTE ANTES DE INICAR CRIAÇÃO
    usuario_logado = request.session.get('username', None)
    orcamento_num = request.POST["orcamento"]
    if len(orcamento_num) >= 5:
        if orcamento_num != "":
            conexao = BDPedidos().conectar()
            context = {
                'orcamento': orcamento_num,
                'usuario_logado': usuario_logado,
            }
            mensagem, resultado = BDPedidos().verifica_orcamento(conexao, orcamento_num)
            if mensagem == 1:
                messages.error(request, 'Orçamento já existe')
                return render(request, 'liberacao_pedidos/orcamento.html')
            if mensagem == 2:
                request.session['context'] = context
                return redirect('liberacao_pedidos_editar')
            if mensagem == 3:
                messages.error(request, 'Erro de conexão')
                return render(request, 'liberacao_pedidos/orcamento.html')
        else:
            messages.error(request, 'Campo orçamento não pode estar em branco')
            return render(request, 'liberacao_pedidos/orcamento.html')
    else:
        messages.error(request, 'Numero de orçamento muito pequeno')
        return render(request, 'liberacao_pedidos/orcamento.html')


def liberacao_pedidos_salvar_orcamento(request):
    converted_context = request.POST.copy()
    context = {}
    context['novo'] = '1'
    for key, value in converted_context.items():
        context[key] = value.upper()
    usuario_logado = request.session.get('username', None)
    context['usuario_logado'] = usuario_logado
    context['liberacao'] = usuario_logado
    if context['orcamento'] != "":
        if usuario_logado != None:
            if context != None:
                resposta, mensagem = FuncoesExtras().verifica_se_orcamento_completo(context)
                if resposta == True:
                    conexao = BDPedidos().conectar()
                    status = BDPedidos().salva_orcamento(conexao, context)
                    BDPedidos().fecha(conexao)
                    if status != '1':
                        mensagem = "Erro ao salvar"
                    context['novo'] = '0'
                messages.error(request, mensagem)
                query_dict = context
                context = {key: str(value) for key, value in query_dict.items()}
                request.session['context'] = context
                return render(request, 'liberacao_pedidos/editar.html', context)
            else:
                return redirect('liberacao_pedidos_orcamento')
        else:
            return redirect('liberacao_pedidos_index')
    else:
        query_dict = context
        context = {key: str(value) for key, value in query_dict.items()}
        finalizado = request.session.get('finalizado', None)
        context['finalizado'] = finalizado
        messages.error(request, "Lote e obrigatorio")
        return render(request, 'liberacao_pedidos/editar.html', context)


def liberacao_pedidos_logout(request):
    # LOGOUT
    request.session['context'] = None
    request.session['username'] = None
    return redirect('liberacao_pedidos_index')
