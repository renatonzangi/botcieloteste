def fluxo_cancelamento_venda():

    return """
## 💳 Cancelamento de Venda

### Dados obrigatórios

Solicitar ao cliente:

• NSU

• Valor da venda

• Data da venda

• 4 últimos dígitos do cartão

### Atenção

Validar sempre:

• NSU

• 4 últimos dígitos do cartão

Mesmo quando existir apenas uma venda com o valor informado.

Essa validação reduz o risco de cancelamento incorreto.

### Regras de Cancelamento

• Crédito: cancelamento em até 30 dias da venda.

• Débito: cancelamento em até 7 dias da venda.

• Atendimento via Voz, Site, WhatsApp ou E-mail:
  somente após 24 horas da realização da venda.

### Importante

• O cancelamento é válido apenas para bandeiras adquirentes.

• Voucher Ven e bandeira Van devem ser tratados diretamente com a bandeira.

• Para vendas já canceladas, o estorno ao portador depende do banco emissor.

### Perfis permitidos

Podem solicitar cancelamento:

• Proprietário

• Analista cadastrado na Identidade Digital

• Representante Legal

• Contato cadastrado

Perfil Visualizador não pode solicitar cancelamento.

### Biometria

Pode ser validada por:

• Proprietário

• Representante Legal

• Procurador

• Pessoa de Contato

### Prazo de análise

Prazo máximo de análise:

• Até 120 dias corridos.
"""


def fluxo_cancelamento_cadastro():

    return """
## 📄 Cancelamento de Cadastro

### Atenção

A Ilha de Varejo CR não realiza cancelamento de cadastro.

### Ação Obrigatória

• Transferir para a Ilha de Retenção

• Registrar a tratativa

• Orientar o cliente sobre a transferência
"""


def fluxo_venda_mesmo_dia_antecipacao():

    return """
## ⚠️ Venda do Mesmo Dia com Antecipação Ativa

Vendas realizadas no mesmo dia podem não permitir cancelamento imediato quando o cliente possui antecipação ativa.

### Orientar o Cliente

• Aguardar 24 horas

• Retornar pelos canais de atendimento da Cielo

• Solicitar o cancelamento após o prazo
"""


def fluxo_carta_cancelamento():

    return """
## 📑 Carta de Cancelamento

### Disponibilidade

A carta de cancelamento fica disponível através do Site Cielo.

### Prazo

• A maioria dos cancelamentos é concluída em até 24 horas.

• O prazo oficial pode chegar a até 3 dias úteis.

### Status possíveis

• Em análise

• Efetivada

• Negada

### Consulta

Acessar:

Vendas > Minhas Vendas

### Importante

• Vendas realizadas e canceladas no mesmo dia via POS não geram carta de cancelamento.

• Após a solicitação é possível acompanhar o andamento pelo portal.
"""


def fluxo_biometria_cancelamento():

    return """
## 🔐 Biometria para Cancelamento

### Quem pode validar

• Proprietário

• Representante Legal

• Procurador

• Pessoa de Contato

### Importante

O link de validação biométrica é enviado para o responsável cadastrado.

Sem validação biométrica o cancelamento poderá ser impedido conforme as regras de segurança da Cielo.
"""


def fluxo_quem_pode_cancelar():

    return """
## 👤 Quem pode solicitar cancelamento

Perfis autorizados:

• Proprietário

• Analista cadastrado na Identidade Digital

• Representante Legal

• Contato cadastrado

### Atenção

Perfil Visualizador não possui autorização para solicitar cancelamento de vendas.
"""


def fluxo_prazos_cancelamento():

    return """
## ⏱️ Prazos de Cancelamento

### Crédito

• Até 30 dias da data da venda.

### Débito

• Até 7 dias da data da venda.

### Atendimento

• Solicitações pelos canais de atendimento somente após 24 horas da venda.

### Prazo máximo de análise

• Até 120 dias corridos.
"""
def fluxo_quem_pode_cancelar():

    return """
## 👤 Quem pode solicitar cancelamento

Podem solicitar:

• Proprietário

• Analista cadastrado na Identidade Digital

• Representante Legal

• Contato cadastrado

### Observação

Clientes com perfil Visualizador não podem seguir com o cancelamento.

Nesses casos é necessário validar o perfil cadastrado.
"""
def fluxo_regras_cancelamento():

    return """
## 📋 Regras de Cancelamento

### Crédito

Cancelamento em até 30 dias corridos.

### Débito

Cancelamento em até 7 dias corridos.

### Importante

Solicitar obrigatoriamente:

• Código de autorização

• Bandeira

• Valor da venda

• 4 últimos dígitos do cartão

### Biometria

Obrigatória quando aplicável.

### Clientes bloqueados

Clientes fechados por Prevenção e Segurança não podem seguir com cancelamento.
"""