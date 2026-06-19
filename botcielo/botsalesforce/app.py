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

from rapidfuzz import fuzz

import os

PASTA_ARTIGOS = os.path.join(
    os.path.dirname(__file__),
    "artigos"
)


def identificar_intencao(texto):

    texto = texto.lower()

    # =========================
    # PROCEDIMENTO DE EQUIPAMENTO
    # =========================

    if (
        "lio" in texto
        or "lio on" in texto
        or "sp930" in texto
        or "máquina" in texto
        or "maquininha" in texto
    ):
        return "cancelamento_maquina"

    # =========================
    # QUEM PODE CANCELAR
    # =========================

    if (
        "quem pode cancelar" in texto
        or "quem solicita cancelamento" in texto
    ):
        return "quem_pode_cancelar"

    # =========================
    # REGRAS / PRAZOS
    # =========================

    if (
        "regras cancelamento" in texto
        or "prazo cancelamento" in texto
    ):
        return "prazos_cancelamento"

    # =========================
    # VENDA MESMO DIA + ANTECIPAÇÃO
    # =========================

    score_antecipacao = max(
        fuzz.partial_ratio(texto, "venda mesmo dia antecipacao"),
        fuzz.partial_ratio(texto, "antecipacao ativa"),
        fuzz.partial_ratio(texto, "venda realizada hoje"),
        fuzz.partial_ratio(texto, "venda hoje antecipacao"),
        fuzz.partial_ratio(texto, "cancelamento mesmo dia")
    )

    if score_antecipacao >= 75:
        return "venda_mesmo_dia_antecipacao"

    # =========================
    # CARTA DE CANCELAMENTO
    # =========================

    score_carta = max(
        fuzz.partial_ratio(texto, "carta de cancelamento"),
        fuzz.partial_ratio(texto, "emitir carta"),
        fuzz.partial_ratio(texto, "comprovante cancelamento"),
        fuzz.partial_ratio(texto, "carta cancelamento"),
        fuzz.partial_ratio(texto, "gerar carta")
    )

    if score_carta >= 70:
        return "carta_cancelamento"

    # =========================
    # BIOMETRIA
    # =========================

    score_biometria = max(
        fuzz.partial_ratio(texto, "biometria"),
        fuzz.partial_ratio(texto, "validacao biometrica"),
        fuzz.partial_ratio(texto, "quem pode validar biometria"),
        fuzz.partial_ratio(texto, "validar biometria"),
        fuzz.partial_ratio(texto, "biometria cancelamento")
    )

    if score_biometria >= 70:
        return "biometria_cancelamento"

    # =========================
    # QUEM PODE CANCELAR
    # =========================

    score_perfil = max(
        fuzz.partial_ratio(texto, "quem pode cancelar"),
        fuzz.partial_ratio(texto, "quem solicita cancelamento"),
        fuzz.partial_ratio(texto, "perfil cancelamento"),
        fuzz.partial_ratio(texto, "quem pode solicitar cancelamento")
    )

    if score_perfil >= 70:
        return "quem_pode_cancelar"

    # =========================
    # PRAZOS
    # =========================

    score_prazo = max(
        fuzz.partial_ratio(texto, "prazo cancelamento"),
        fuzz.partial_ratio(texto, "quantos dias cancelar"),
        fuzz.partial_ratio(texto, "prazo para cancelar venda"),
        fuzz.partial_ratio(texto, "prazo de cancelamento"),
        fuzz.partial_ratio(texto, "quantos dias tenho para cancelar")
    )

    if score_prazo >= 70:
        return "prazos_cancelamento"

    # =========================
    # CANCELAMENTO DE CADASTRO
    # =========================

    score_cadastro = max(
        fuzz.partial_ratio(texto, "cancelar cadastro"),
        fuzz.partial_ratio(texto, "encerrar cadastro"),
        fuzz.partial_ratio(texto, "cancelar conta"),
        fuzz.partial_ratio(texto, "encerrar estabelecimento")
    )

    if score_cadastro >= 75:
        return "cancelamento_cadastro"

    # =========================
    # CANCELAMENTO DE VENDA
    # =========================

    score_venda = max(
        fuzz.partial_ratio(texto, "cancelar venda"),
        fuzz.partial_ratio(texto, "estornar venda"),
        fuzz.partial_ratio(texto, "desfazer venda"),
        fuzz.partial_ratio(texto, "devolver venda"),
        fuzz.partial_ratio(texto, "reverter venda"),
        fuzz.partial_ratio(texto, "cliente quer cancelar venda"),
        fuzz.partial_ratio(texto, "cliente quer estornar venda")
    )

    if score_venda >= 70:
        return "cancelamento_venda"

    return None


def iniciar_bot():

    print("\n=== BOT EINSTEIN ===")

    while True:

        pergunta = input("\nPergunta: ").lower()

        if pergunta == "sair":

            print("\nEncerrando bot...")
            break

        intencao = identificar_intencao(
            pergunta
        )

        print(
            f"\nDEBUG INTENÇÃO = {intencao}"
        )

        if intencao == "cancelamento_maquina":

            maquina = identificar_maquina(
                pergunta
            )

            if maquina:

                print(
                    PROCEDIMENTOS_CANCELAMENTO[
                        maquina
                    ]
                )

            else:

                print("""
Equipamento não identificado.

Informe:

• LIO On
• SP930
""")

            continue

        if intencao == "cancelamento_venda":

            print(
                fluxo_cancelamento_venda()
            )

            continue

        if intencao == "cancelamento_cadastro":

            print(
                fluxo_cancelamento_cadastro()
            )

            continue

        if intencao == "venda_mesmo_dia_antecipacao":

            print(
                fluxo_venda_mesmo_dia_antecipacao()
            )

            continue

        if intencao == "carta_cancelamento":

            print(
                fluxo_carta_cancelamento()
            )

            continue

        if intencao == "biometria_cancelamento":

            print(
                fluxo_biometria_cancelamento()
            )

            continue

        if intencao == "quem_pode_cancelar":

            print(
                fluxo_quem_pode_cancelar()
            )

            continue

        if intencao == "prazos_cancelamento":

            print(
                fluxo_prazos_cancelamento()
            )

            continue

        print(
            "\nDemanda não identificada na base de conhecimento."
        )


if __name__ == "__main__":
    iniciar_bot()