import streamlit as st
import json


from app import identificar_intencao

from fluxos import (
    fluxo_cancelamento_venda,
    fluxo_cancelamento_cadastro,
    fluxo_venda_mesmo_dia_antecipacao,
    fluxo_carta_cancelamento,
    fluxo_biometria_cancelamento,
    fluxo_quem_pode_cancelar,
    fluxo_prazos_cancelamento
)

from equipamentos import (
    PROCEDIMENTOS_CANCELAMENTO,
    identificar_maquina
)

st.set_page_config(
    page_title="Cibot",
    page_icon="logobotcielotr.png",
    layout="centered"
)
# ==================================
# ALERTAS OPERACIONAIS
# ==================================

def carregar_alertas():

    try:

        with open(
            "alertas.json",
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)

    except:

        return []


alertas = carregar_alertas()

if alertas:

    with st.expander(
        f"🚨 Alertas Operacionais ({len(alertas)})",
        expanded=True
    ):

        for alerta in alertas:

            if alerta["status"] == "ATIVO":

                st.warning(
                    f"""
**{alerta['titulo']}**

{alerta['orientacao']}
"""
                )

# ==================================
# CSS
# ==================================

st.markdown("""
<style>

.main .block-container{
    max-width:900px;
    padding-top:20px;
}

.chat-wrapper{
    width:750px;
    margin:auto;
    background:white;
    border-radius:25px;
    overflow:hidden;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
}

.chat-header{
    background:#009CDE;
    text-align:center;
    padding:25px;
}

.chat-title{
    color:white;
    font-size:30px;
    font-weight:bold;
}

.chat-subtitle{
    color:white;
    opacity:.9;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# HISTÓRICO
# ==================================

if "mensagens" not in st.session_state:

    st.session_state.mensagens = [
        {
            "tipo": "assistant",
            "texto": """
Olá! Eu sou o Cibot.

Posso ajudar com:

• Cancelamento de venda

• Carta de cancelamento

• Biometria

• Prazos

• Cancelamento de cadastro

• LIO On

• SP930
"""
        }
    ]

# ==================================
# CABEÇALHO
# ==================================

st.markdown("""
<div class="chat-wrapper">
<div class="chat-header">

<div class="chat-title">
Cibot
</div>

<div class="chat-subtitle">
Assistente Interativo
</div>

</div>
""", unsafe_allow_html=True)

st.image(
    "logobotcielo.png",
    width=180
)

# ==================================
# CHAT
# ==================================

for msg in st.session_state.mensagens:

    with st.chat_message(msg["tipo"]):

        st.markdown(
            msg["texto"]
        )

# ==================================
# ENTRADA
# ==================================

pergunta = st.chat_input(
    "Digite sua dúvida..."
)

# ==================================
# PROCESSAMENTO
# ==================================

if pergunta:

    st.session_state.mensagens.append(
        {
            "tipo": "user",
            "texto": pergunta
        }
    )

    intencao = identificar_intencao(
        pergunta
    )

    resposta = ""

    # -------------------------
    # EQUIPAMENTOS
    # -------------------------

    if intencao == "cancelamento_maquina":

        maquina = identificar_maquina(
            pergunta
        )

        if maquina:

            resposta = (
                PROCEDIMENTOS_CANCELAMENTO[
                    maquina
                ]
            )

        else:

            resposta = """
## Equipamento não identificado

Informe:

• LIO On

• SP930
"""

    # -------------------------
    # VENDA
    # -------------------------

    elif intencao == "cancelamento_venda":

        resposta = fluxo_cancelamento_venda()

    # -------------------------
    # CADASTRO
    # -------------------------

    elif intencao == "cancelamento_cadastro":

        resposta = fluxo_cancelamento_cadastro()

    # -------------------------
    # ANTECIPAÇÃO
    # -------------------------

    elif intencao == "venda_mesmo_dia_antecipacao":

        resposta = fluxo_venda_mesmo_dia_antecipacao()

    # -------------------------
    # CARTA
    # -------------------------

    elif intencao == "carta_cancelamento":

        resposta = fluxo_carta_cancelamento()

    # -------------------------
    # BIOMETRIA
    # -------------------------

    elif intencao == "biometria_cancelamento":

        resposta = fluxo_biometria_cancelamento()

    # -------------------------
    # PERFIL
    # -------------------------

    elif intencao == "quem_pode_cancelar":

        resposta = fluxo_quem_pode_cancelar()

    # -------------------------
    # PRAZO
    # -------------------------

    elif intencao == "prazos_cancelamento":

        resposta = fluxo_prazos_cancelamento()

    else:

        resposta = """
## Informação não encontrada

Não encontrei essa orientação na base de conhecimento.

Tente reformular a pergunta.
"""

    st.session_state.mensagens.append(
        {
            "tipo": "assistant",
            "texto": resposta
        }
    )

    st.rerun()
