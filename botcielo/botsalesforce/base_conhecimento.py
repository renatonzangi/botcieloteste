BASE_CONHECIMENTO = {

    "cancelamento_venda": {
        "titulo": "Cancelamento de Venda",
        "conteudo": """
Solicitar ao cliente:

• NSU
• Valor da venda
• Data da venda
• 4 últimos dígitos do cartão

Validar sempre NSU e cartão para evitar cancelamento incorreto.
"""
    },

    "cancelamento_cadastro": {
        "titulo": "Cancelamento de Cadastro",
        "conteudo": """
A Ilha de Varejo CR não realiza cancelamento de cadastro.

Ação obrigatória:

• Transferir para Retenção
• Registrar tratativa
• Orientar cliente
"""
    },

    "lio_on_cancelamento": {
        "titulo": "Procedimento LIO On",
        "conteudo": """
1. Acessar a tela de venda.

2. Clicar nos três pontos.

3. Selecionar Cancelar Venda.

4. Seguir orientações da máquina.
"""
    },

    "sp930_cancelamento": {
        "titulo": "Procedimento SP930",
        "conteudo": """
1. Pressionar Cancelar.

2. Digitar Senha Supervisor.

3. Confirmar em Sim.

4. Inserir ou aproximar cartão.

5. Aguardar comprovante.
"""
    }
}


def buscar_artigo(chave):

    return BASE_CONHECIMENTO.get(
        chave,
        {
            "titulo": "Não encontrado",
            "conteudo": "Artigo não encontrado."
        }
    )