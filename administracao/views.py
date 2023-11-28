from django.shortcuts import render, redirect
from django.contrib import messages
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


def administracao_login(request):
    if request.method == 'POST':
        username = request.POST["usuario"]
        password = request.POST["password"]
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT administracao, senhaUsuario, id FROM usuarios WHERE nomeUsuario = '{username}'")
            resposta = cursor.fetchall()
            conn.close()
            senha_login = resposta[0]['senhaUsuario']
            direito = resposta[0]['administracao']
            if direito == '1':
                if senha_login == password:
                    request.session['username'] = username.upper()
                    return redirect('table_list')
                else:
                    messages.error(request, 'Senha errada')
                    return render(request, 'administracao/login.html')
            else:
                messages.error(request, 'Voce não tem direito para acessar esse módulo')
                return render(request, 'administracao/login.html')
        except:
            messages.error(request, 'Usuario Não Cadastrado')
            return render(request, 'administracao/login.html')
    else:
        return render(request, 'administracao/login.html')


def table_list(request):
    if request.session['username'] is not None:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table['Tables_in_inaflexapp'] for table in cursor.fetchall()]
        conn.close()
        return render(request, 'administracao/table_list.html', {'tables': tables})
    else:
        return render(request, 'administracao/login.html')


def table_detail(request, table_name):
    try:
        filtro = int(request.POST["filtro"])
    except:
        filtro = None
    if request.session['username'] != None:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        column_types = {column['Field']: column['Type'] for column in cursor.fetchall()}
        cursor.execute(f"SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1")
        try:
            last_id = cursor.fetchone()['id']
        except:
            last_id = 0
        if last_id == 0:
            qtd = 0
        else:
            qtd = int((last_id/500)//1 + 1)
        conta = qtd - 1
        qtd = range(qtd)
        if filtro == None:
            inicio = conta * 500
            final = last_id
        else:
            inicio = filtro
            final = filtro + 500
        cursor.execute(f"SELECT * FROM {table_name} WHERE (id >= {inicio}) AND (id <= {final})")
        rows = cursor.fetchall()
        conn.close()
        return render(request, 'administracao/table_detail.html', {'table_name': table_name, 'rows': rows, 'column_types': column_types, 'qtd': qtd, 'last_id': last_id})
    else:
        return render(request, 'administracao/login.html')


def table_edit(request, table_name, pk):
    if request.session['username'] != None:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        column_types = {column['Field']: column['Type'] for column in cursor.fetchall()}
        columns = list(column_types.keys())  # CRIA UMA LISTA COM AS KEYS DO DICT
        if request.method == 'POST':
            for index in range(len(columns)):
                try:
                    if request.POST[columns[index]] == 'on':
                        valor = 1
                        consulta = f"UPDATE {table_name} SET {columns[index]}={valor} WHERE id={pk}"
                    else:
                        valor = request.POST[columns[index]]
                        consulta = f"UPDATE {table_name} SET {columns[index]}='{valor}' WHERE id={pk}"
                except:
                    valor = 0
                    consulta = f"UPDATE {table_name} SET {columns[index]}={valor} WHERE id={pk}"
                cursor.execute(consulta)
                conn.commit()
            cursor.execute(f"SELECT * FROM {table_name} WHERE id={pk}")
            row = cursor.fetchone()
            conn.close()
            return render(request, 'administracao/table_edit.html', {'table_name': table_name, 'row': row, 'pk': pk, 'column_types': column_types})
        else:
            cursor.execute(f"SELECT * FROM {table_name} WHERE id={pk}")
            row = cursor.fetchone()
            conn.close()
            return render(request, 'administracao/table_edit.html', {'table_name': table_name, 'row': row, 'pk': pk, 'column_types': column_types})
    else:
        return render(request, 'administracao/login.html')


def table_new(request, table_name):
    if request.session['username'] != None:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        column_types = {column['Field']: column['Type'] for column in cursor.fetchall()}
        columns = list(column_types.keys())  # CRIA UMA LISTA COM AS KEYS DO DICT
        columns_insert = list(column_types.keys())
        columns_insert.pop(0)
        if request.method == 'POST':
            values = []
            for index in range(len(columns_insert)):
                try:
                    if request.POST[columns_insert[index]] == 'on':
                        valor = 1
                    else:
                        my_value = request.POST.get(columns_insert[index], '').strip()  # get the value of the field and remove leading/trailing whitespace
                        if not my_value:  # check if the value is empty
                            valor = '0'  # set the value to '0' if it is empty
                        else:
                            valor = request.POST[columns_insert[index]]
                    values.append(f"'{str(valor)}'")
                except:
                    values.append("0")
            values_str = ','.join(values)
            consulta = f"INSERT INTO {table_name} ({','.join(columns_insert)}) VALUES ({values_str})"
            cursor.execute(consulta)
            conn.commit()
            cursor.execute(f"SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1")
            pk = cursor.fetchone()
            conn.close()
            return redirect('table_edit', table_name=table_name, pk=pk['id'])
        else:
            conn.close()
            return render(request, 'administracao/table_edit.html', {'table_name': table_name, 'columns': columns, 'column_types': column_types})
    else:
        return render(request, 'administracao/login.html')


def administracao_logout(request):
    request.session['context'] = None
    request.session['username'] = None
    return redirect('administracao_login')
