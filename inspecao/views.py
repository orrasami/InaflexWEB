from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .auxiliar.bd_pedidos import BDPedidos
from .auxiliar.funcoes import FuncoesExtras
from unidecode import unidecode
from azure.storage.blob import BlobServiceClient, BlobClient
from PIL import Image
import io
import uuid
from base64 import b64encode
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

def inspecao_index(request):
    if request.method == 'POST':
        username = request.POST["usuario"]
        password = request.POST["password"]
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT inspecao, senhaUsuario, id FROM usuarios WHERE nomeUsuario = '{username}'")
            resposta = cursor.fetchall()
            conn.close()
            senha_login = resposta[0]['senhaUsuario']
            direito = resposta[0]['inspecao']
            if direito == '1':
                if senha_login == password:
                    request.session['username'] = username.upper()
                    return redirect('inspecao_lote')
                else:
                    messages.error(request, 'Senha errada')
                    return render(request, 'inspecao/index.html')
            else:
                messages.error(request, 'Voce não tem direito para acessar esse módulo')
                return render(request, 'inspecao/index.html')
        except:
            messages.error(request, 'Usuario Não Cadastrado')
            return render(request, 'inspecao/index.html')
    else:
        return render(request, 'inspecao/index.html')


def inspecao_lote(request):
    request.session['context'] = None
    usuario_logado = request.session.get('username', None)
    if usuario_logado != None:
        if request.method == 'POST':
            lote_num = request.POST["lote"]
            conexao = BDPedidos().conectar()
            mensagem, resultados = BDPedidos().verifica_lote(conexao, lote_num)
            BDPedidos().fecha(conexao)
            if mensagem == 1:
                context = {
                    'correto': resultados[0]['correto'],
                    'finalizado': resultados[0]['finalizado'],
                    'pedido': resultados[0]['pedido'],
                    'cliente': resultados[0]['cliente'],
                    'cnpj': resultados[0]['cnpj'],
                    'exigencias': resultados[0]['exigencias'],
                    'lote': resultados[0]['lote'],
                    'h_inicial': resultados[0]['h_inicial'],
                    'h_final': resultados[0]['h_final'],
                    'data': resultados[0]['data'],
                    'empatacao': resultados[0]['empatacao'],
                    'encaixe': resultados[0]['encaixe'],
                    'encaixe_obs': resultados[0]['encaixe_obs'],
                    'solda': resultados[0]['solda'],
                    'solda_obs': resultados[0]['solda_obs'],
                    'cordoalha': resultados[0]['cordoalha'],
                    'cordoalha_obs': resultados[0]['cordoalha_obs'],
                    'tipado': resultados[0]['tipado'],
                    'tipado_obs': resultados[0]['tipado_obs'],
                    'tag': resultados[0]['tag'],
                    'tag_obs': resultados[0]['tag_obs'],
                    'tag_num': resultados[0]['tag_num'],
                    'cola': resultados[0]['cola'],
                    'cola_obs': resultados[0]['cola_obs'],
                    'pead': resultados[0]['pead'],
                    'pead_obs': resultados[0]['pead_obs'],
                    'corda': resultados[0]['corda'],
                    'corda_obs': resultados[0]['corda_obs'],
                    'corda_cor': resultados[0]['corda_cor'],
                    'silicone': resultados[0]['silicone'],
                    'silicone_obs': resultados[0]['silicone_obs'],
                    'cupilha': resultados[0]['cupilha'],
                    'cupilha_obs': resultados[0]['cupilha_obs'],
                    'drenado': resultados[0]['drenado'],
                    'drenado_obs': resultados[0]['drenado_obs'],
                    'plaqueta': resultados[0]['plaqueta'],
                    'plaqueta_obs': resultados[0]['plaqueta_obs'],
                    'plaqueta_info': resultados[0]['plaqueta_info'],
                    'plaqueta_info_obs': resultados[0]['plaqueta_info_obs'],
                    'diametro': resultados[0]['diametro'],
                    'diametro_obs': resultados[0]['diametro_obs'],
                    'etiquetas': resultados[0]['etiquetas'],
                    'etiquetas_obs': resultados[0]['etiquetas_obs'],
                    'modelo': resultados[0]['modelo'],
                    'modelo_obs': resultados[0]['modelo_obs'],
                    'retrabalho': resultados[0]['retrabalho'],
                    'retrabalho_obs': resultados[0]['retrabalho_obs'],
                    'data_armazenamento': resultados[0]['data_armazenamento'],
                    'embalagem': resultados[0]['embalagem'],
                    'embalagem_obs': resultados[0]['embalagem_obs'],
                    'pregos': resultados[0]['pregos'],
                    'pregos_obs': resultados[0]['pregos_obs'],
                    'falha': resultados[0]['falha'],
                    'falha_obs': resultados[0]['falha_obs'],
                    'responsavel': resultados[0]['responsavel'],
                    'responsavel_obs': resultados[0]['responsavel_obs'],
                    'qualidade_obs': resultados[0]['qualidade_obs'],
                    'inspetor': resultados[0]['inspetor'],
                    'data_inspecao': resultados[0]['data_inspecao'],
                    'remetente': resultados[0]['remetente'],
                    'n_pedido': resultados[0]['n_pedido'],
                    'n_embalagem': resultados[0]['n_embalagem'],
                    'pais_origem': resultados[0]['pais_origem'],
                    'pais_destino': resultados[0]['pais_destino'],
                    'liquido': resultados[0]['liquido'],
                    'bruto': resultados[0]['bruto'],
                    'dimensoes': resultados[0]['dimensoes'],
                    'simbolos': resultados[0]['simbolos'],
                    'tipo_embalagem': resultados[0]['tipo_embalagem'],
                    'cintada': resultados[0]['cintada'],
                    'stretch': resultados[0]['stretch'],
                    'foto': resultados[0]['foto'],
                    'foto1': resultados[0]['foto1'],
                    'foto2': resultados[0]['foto2'],
                    'foto3': resultados[0]['foto3'],
                }

                account_name = 'inaflex'
                connection_string = 'FCF8566/TzEdl2hHvp+2owWDZPVxfyX+MYTFX0ToDe1Nkxvg4TO1eHLp2DU1EcBirNrrW4TOxl3v+' \
                                    'AStHXst8w=='
                container_name = 'fotos-inspecao'

                blob_service_client = BlobServiceClient.from_connection_string(
                    f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={connection_string};"
                    f"EndpointSuffix=core.windows.net")
                container_client = blob_service_client.get_container_client(container_name)

                blob_names = [resultados[0]['foto1'], resultados[0]['foto2'], resultados[0]['foto3']]
                image_bytes_list = []

                for image_name in blob_names:
                    if image_name and image_name != '':
                        blob_client = container_client.get_blob_client(image_name)
                        download_stream = blob_client.download_blob()
                        image_bytes = download_stream.readall()
                        image_bytes_list.append(image_bytes)
                    else:
                        image_bytes_list.append('')

                image_str_list = []

                for image_bytes in image_bytes_list:
                    if image_bytes is not '':
                        image_str = b64encode(image_bytes).decode('utf-8')
                        image_str_list.append(image_str)
                    else:
                        image_str_list.append('')

                context['image_str_list'] = image_str_list
                request.session['context'] = context
                request.session['finalizado'] = context['finalizado']
                return redirect('inspecao_editar')
            else:
                messages.error(request, 'Lote não existe')
                return render(request, 'inspecao/lote.html')
        else:
            return render(request, 'inspecao/lote.html')
    else:
        return redirect('inspecao_index')


def apaga_foto_1(request, lote_num):
    context = request.session.get('context', None)
    conexao = BDPedidos().conectar()
    nome_foto = BDPedidos().pega_nome_foto(conexao, lote_num)
    BDPedidos().apaga_nome_foto1(conexao, lote_num)
    BDPedidos().fecha(conexao)

    account_name = 'inaflex'
    connection_string = 'FCF8566/TzEdl2hHvp+2owWDZPVxfyX+MYTFX0ToDe1Nkxvg4TO1eHLp2DU1EcBirNrrW4TOxl3v+' \
                        'AStHXst8w=='
    container_name = 'fotos-inspecao'
    blob_service_client = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={connection_string};" \
                          f"EndpointSuffix=core.windows.net"

    blob_client = BlobClient.from_connection_string(
        conn_str=blob_service_client,
        container_name=container_name,
        blob_name=nome_foto[0]['foto1']
    )
    blob_client.delete_blob()

    context['foto1'] = ""
    context['foto2'] = nome_foto[0]['foto2']
    context['foto3'] = nome_foto[0]['foto3']
    context['image_str_list'][0] = ""
    if context['foto2'] == '':
        context['image_str_list'][1] = ""
    if context['foto3'] == '':
        context['image_str_list'][2] = ""
    return render(request, 'inspecao/editar.html', context)


def apaga_foto_2(request, lote_num):
    context = request.session.get('context', None)
    conexao = BDPedidos().conectar()
    nome_foto = BDPedidos().pega_nome_foto(conexao, lote_num)
    BDPedidos().apaga_nome_foto2(conexao, lote_num)
    BDPedidos().fecha(conexao)

    account_name = 'inaflex'
    connection_string = 'FCF8566/TzEdl2hHvp+2owWDZPVxfyX+MYTFX0ToDe1Nkxvg4TO1eHLp2DU1EcBirNrrW4TOxl3v+' \
                        'AStHXst8w=='
    container_name = 'fotos-inspecao'
    blob_service_client = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={connection_string};" \
                          f"EndpointSuffix=core.windows.net"

    blob_client = BlobClient.from_connection_string(
        conn_str=blob_service_client,
        container_name=container_name,
        blob_name=nome_foto[0]['foto2']
    )
    blob_client.delete_blob()

    context['foto1'] = nome_foto[0]['foto1']
    context['foto2'] = ""
    context['foto3'] = nome_foto[0]['foto3']
    if context['foto1'] == '':
        context['image_str_list'][0] = ""
    context['image_str_list'][1] = ""
    if context['foto3'] == '':
        context['image_str_list'][2] = ""
    return render(request, 'inspecao/editar.html', context)


def apaga_foto_3(request, lote_num):
    context = request.session.get('context', None)
    conexao = BDPedidos().conectar()
    nome_foto = BDPedidos().pega_nome_foto(conexao, lote_num)
    BDPedidos().apaga_nome_foto3(conexao, lote_num)
    BDPedidos().fecha(conexao)

    account_name = 'inaflex'
    connection_string = 'FCF8566/TzEdl2hHvp+2owWDZPVxfyX+MYTFX0ToDe1Nkxvg4TO1eHLp2DU1EcBirNrrW4TOxl3v+' \
                        'AStHXst8w=='
    container_name = 'fotos-inspecao'
    blob_service_client = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={connection_string};" \
                          f"EndpointSuffix=core.windows.net"

    blob_client = BlobClient.from_connection_string(
        conn_str=blob_service_client,
        container_name=container_name,
        blob_name=nome_foto[0]['foto3']
    )
    blob_client.delete_blob()

    context['foto1'] = nome_foto[0]['foto1']
    context['foto2'] = nome_foto[0]['foto2']
    context['foto3'] = ""
    if context['foto1'] == '':
        context['image_str_list'][0] = ""
    if context['foto2'] == '':
        context['image_str_list'][1] = ""
    context['image_str_list'][2] = ""
    return render(request, 'inspecao/editar.html', context)


def inspecao_editar(request):
    context = request.session.get('context', None)
    usuario_logado = request.session.get('username', None)
    if usuario_logado is not None:
        if context is not None:
            return render(request, 'inspecao/editar.html', context)
        else:
            return redirect('inspecao_lote')
    else:
        return redirect('inspecao_index')


def inspecao_finalizar(request):
    context = request.session.get('context')
    if context['correto'] == "SIM":
        if context['finalizado'] == "0":
            conexao = BDPedidos().conectar()
            status = BDPedidos().finaliza_lote(conexao, context)
            BDPedidos().fecha(conexao)
            if status == '1':
                messages.success(request, 'Finalizado com sucesso :)')
                context['finalizado'] = "1"
                return render(request, 'inspecao/editar.html', context)
            else:
                messages.error(request, 'Erro no banco de dados :(')
                return render(request, 'inspecao/editar.html', context)
        else:
            messages.error(request, 'Lote ja esta finalizado')
            return render(request, 'inspecao/editar.html', context)
    else:
        messages.error(request, 'Preencher tudo para poder finalizar')
        return render(request, 'inspecao/editar.html', context)


def inspecao_salvar_lote(request):
    context = request.POST.copy()
    usuario_logado = request.session.get('username', None)
    context['usuario_logado'] = usuario_logado
    finalizado = request.session.get('finalizado', '0')
    context['finalizado'] = finalizado
    if context['lote'] != "":
        if usuario_logado is not None:
            if context is not None:
                # UPLOAD DAS FOTOS ####################################################################################
                uploaded_file1 = request.FILES.get('image1')
                uploaded_file2 = request.FILES.get('image2')
                uploaded_file3 = request.FILES.get('image3')

                if uploaded_file1:
                    filename = f"{context['lote']}-{uuid.uuid4()}.jpg"

                    conexao = BDPedidos().conectar()
                    BDPedidos().insere_nome_foto(conexao, context, filename, 1)
                    BDPedidos().fecha(conexao)

                    # Resize and compress the image
                    image = Image.open(uploaded_file1)
                    output_buffer = io.BytesIO()
                    image.save(output_buffer, format='JPEG', quality=20)  # Adjust quality as needed
                    image_data1 = output_buffer.getvalue()

                    # Upload the compressed image to Azure Blob Storage
                    account_name = 'inaflex'
                    connection_string = 'FCF8566/TzEdl2hHvp+2owWDZPVxfyX+MYTFX0ToDe1Nkxvg4TO1eHLp2DU1EcBirNrrW4TOxl3v+' \
                                        'AStHXst8w=='
                    container_name = 'fotos-inspecao'

                    blob_service_client = BlobServiceClient.from_connection_string(
                        f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={connection_string};"
                        f"EndpointSuffix=core.windows.net")
                    container_client = blob_service_client.get_container_client(container_name)
                    blob_client = container_client.get_blob_client(filename)
                    blob_client.upload_blob(image_data1)

                if uploaded_file2:
                    filename = f"{context['lote']}-{uuid.uuid4()}.jpg"

                    conexao = BDPedidos().conectar()
                    BDPedidos().insere_nome_foto(conexao, context, filename, 2)
                    BDPedidos().fecha(conexao)

                    # Resize and compress the image to a maximum of 500KB
                    image = Image.open(uploaded_file2)
                    output_buffer = io.BytesIO()
                    image.save(output_buffer, format='JPEG', quality=20)  # Adjust quality as needed
                    image_data2 = output_buffer.getvalue()

                    # Upload the compressed image to Azure Blob Storage
                    account_name = 'inaflex'
                    connection_string = 'FCF8566/TzEdl2hHvp+2owWDZPVxfyX+MYTFX0ToDe1Nkxvg4TO1eHLp2DU1EcBirNrrW4TOxl3v+' \
                                        'AStHXst8w=='
                    container_name = 'fotos-inspecao'

                    blob_service_client = BlobServiceClient.from_connection_string(
                        f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={connection_string};"
                        f"EndpointSuffix=core.windows.net")
                    container_client = blob_service_client.get_container_client(container_name)
                    blob_client = container_client.get_blob_client(filename)
                    blob_client.upload_blob(image_data2)

                if uploaded_file3:
                    filename = f"{context['lote']}-{uuid.uuid4()}.jpg"

                    conexao = BDPedidos().conectar()
                    BDPedidos().insere_nome_foto(conexao, context, filename, 3)
                    BDPedidos().fecha(conexao)

                    # Resize and compress the image to a maximum of 500KB
                    image = Image.open(uploaded_file3)
                    output_buffer = io.BytesIO()
                    image.save(output_buffer, format='JPEG', quality=20)  # Adjust quality as needed
                    image_data3 = output_buffer.getvalue()

                    # Upload the compressed image to Azure Blob Storage
                    account_name = 'inaflex'
                    connection_string = 'FCF8566/TzEdl2hHvp+2owWDZPVxfyX+MYTFX0ToDe1Nkxvg4TO1eHLp2DU1EcBirNrrW4TOxl3v+' \
                                        'AStHXst8w=='
                    container_name = 'fotos-inspecao'

                    blob_service_client = BlobServiceClient.from_connection_string(
                        f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={connection_string};"
                        f"EndpointSuffix=core.windows.net")
                    container_client = blob_service_client.get_container_client(container_name)
                    blob_client = container_client.get_blob_client(filename)
                    blob_client.upload_blob(image_data3)

                # #####################################################################################################

                resposta, mensagem = FuncoesExtras().verifica_se_lote_completo(context)
                if resposta:
                    context['correto'] = "SIM"
                else:
                    context['correto'] = "NAO"

                conexao = BDPedidos().conectar()
                status = BDPedidos().salva_lote(conexao, context)
                BDPedidos().fecha(conexao)
                if status != '1':
                    mensagem = "Erro ao salvar"
                messages.success(request, mensagem)
                query_dict = context
                context = {key: str(value) for key, value in query_dict.items()}
                request.session['context'] = context
                return redirect('inspecao_lote')
            else:
                return redirect('inspecao_lote')
        else:
            return redirect('inspecao_index')
    else:
        query_dict = context
        context = {key: str(value) for key, value in query_dict.items()}
        finalizado = request.session.get('finalizado', None)
        context['finalizado'] = finalizado
        messages.error(request, "Lote e obrigatorio")
        return render(request, 'inspecao/editar.html', context)


def inspecao_novo_lote(request):
    context = request.POST
    try:
        pedido = context['pedido']
    except:
        pedido = ""
    if pedido != "":
        query_dict = context
        context = {key: str(value) for key, value in query_dict.items()}
        context['correto'] = 0
        conexao = BDPedidos().conectar()
        status, resultado = BDPedidos().procura_pedido(conexao, pedido)
        BDPedidos().fecha(conexao)
        if status == 1:
            context['cliente'] = unidecode(resultado[0]['cliente'])
            context['cnpj'] = resultado[0]['cnpj']
            if resultado[0]['obs_cliente']:
                context['exigencias'] = resultado[0]['obs_cliente']
            else:
                context['exigencias'] = ""
            context['correto'] = 1
            context['finalizado'] = "0"
            request.session['context'] = context
            messages.warning(request, f"Conferir se o pedido esta correto antes de criar o Lote para inspecao")
            return render(request, 'inspecao/novo.html', context)
        elif status == 2:
            context = {}
            request.session['context'] = context
            messages.error(request, f"Pedido nao esta cadastrado no APP")
            return render(request, 'inspecao/novo.html')
        else:
            context = {}
            request.session['context'] = context
            messages.error(request, f"Erro no banco de dados")
            return render(request, 'inspecao/novo.html')
    else:
        context = {}
        request.session['context'] = context
        return render(request, 'inspecao/novo.html', context)


def inspecao_logout(request):
    request.session['context'] = None
    request.session['username'] = None
    return redirect('inspecao_index')
