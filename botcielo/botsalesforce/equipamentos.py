PROCEDIMENTOS_CANCELAMENTO = {

    "lio on": """
### Procedimento de Cancelamento - LIO On

1. Acessar a tela de realização de venda.

2. Clicar nos três pontos no canto superior direito.

3. Selecionar "Cancelar Venda".

4. Seguir as orientações apresentadas pela própria máquina.
""",

    "sp930": """
### Procedimento de Cancelamento - SP930

1. Pressionar a tecla "Cancelar".

2. Digitar a Senha de Supervisor.

3. Confirmar em "Sim".

4. Inserir ou aproximar o cartão do cliente.

5. Aguardar a emissão do comprovante de estorno.
"""
}


def identificar_maquina(texto):

    texto = texto.lower()

    # LIO On

    if (
        "lio on" in texto
        or "lioon" in texto
    ):
        return "lio on"

    # SP930

    if "sp930" in texto:
        return "sp930"

    return None


def nome_maquina(maquina):

    nomes = {
        "lio on": "LIO On",
        "sp930": "SP930"
    }

    return nomes.get(
        maquina,
        maquina
    )