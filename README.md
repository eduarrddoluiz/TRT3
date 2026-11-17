# Revisão TRT3 Técnico

App de estudo para o concurso do **TRT da 3ª Região (MG), Técnico Judiciário – Área Administrativa**: plano semanal dia a dia, revisões espaçadas (24 h, 7 e 30 dias), registro de questões, banco de horas (meta de 1.000 h), edital com 172 tópicos e simulados.

Tudo roda no navegador, sem servidor. Os dados ficam no `localStorage` do aparelho e do navegador em que você usa o app.

## Importante: seus dados
- Cada navegador/aparelho tem seus próprios dados. Para mudar de aparelho ou fazer cópia de segurança, use **Mais → Backup** (exportar e restaurar). Cada app (estudo e questões) tem o seu backup.
- Limpar os dados do site apaga o progresso. Faça backup de vez em quando.

## Instalar como atalho
Abra o endereço no Chrome ou Edge e use **Instalar app** (ícone na barra de endereço). Ele ganha ícone próprio e abre em janela, inclusive offline. O app de questões (`/questoes/`) é instalado separadamente, com ícone verde.

## Questões (`questoes/`)
App de questões com revisão espaçada, no mesmo site e integrado ao app de estudo (mesmos dados do navegador).

- **Fila do dia:** revisões vencidas (as erradas primeiro) e, depois, questões novas das duas matérias do dia, até a meta (30 por padrão, ajustável).
- **Revisão:** acertou, a questão avança um degrau e volta em 3, 7, 15, 30, 60 e 120 dias; errou, volta amanhã e a escada recomeça. Não há botão de “fácil/difícil”. Assuntos em que você acerta muito ganham intervalos maiores, e os intervalos respeitam a data da prova (definida na aba Horas do app de estudo).
- **Liberação:** só aparecem questões de tópicos que você já iniciou no app de estudo, ou que liberou à mão em Banco → Tópicos liberados. Estudar a Lei 8.112 em Direito Administrativo libera também o espelho dela em Legislação.
- **Nível automático:** básico, intermediário e avançado, por disciplina, conforme seu acerto.
- **Integração:** cada resposta entra no Painel do app de estudo como sessão “Questões” (uma por dia e por tópico). Essas sessões não consomem a cota diária de assuntos.
- **Treino livre:** filtros por disciplina, assunto, nível, situação (não resolvidas, erradas, vencidas, marcadas) e origem.
- **Importar questões:** Banco → Importar questões. Cole no modelo abaixo (ou um JSON) e confira a disciplina e o tópico do edital de cada uma. O app não consulta nenhum site: você copia o que quiser guardar.

```
Disciplina: Noções de Direito Constitucional
Assunto: Direitos individuais e coletivos
Nível: 2
Enunciado: Texto da questão.
A) primeira alternativa
B) segunda alternativa
C) terceira alternativa
D) quarta alternativa
E) quinta alternativa
Gabarito: C
Comentário: explicação opcional
Fonte: opcional
---
Disciplina: Língua Portuguesa
Enunciado: Questão de Certo ou Errado, sem alternativas.
Gabarito: Certo
```

### Banco de questões do app
As questões originais ficam em `questoes/bancos/*.json` (listadas em `questoes/bancos/index.json`). Cada uma tem:
`id`, `t` (id do tópico do edital, como `t042`), `n` (nível 1 a 3), `e` (enunciado), `x` (texto-base, opcional), `a` (5 alternativas), `g` (índice da correta, começando em 0), `c` (comentário, com `{A}` a `{E}` no lugar das letras, porque as alternativas são embaralhadas na tela), `b` (dica de base legal, opcional), `v` (1 = texto legal conferido em cópia do texto da lei, 0 = não conferido), `src` (origem: tema recorrente nas provas anteriores que inspirou a questão, opcional) e `fx` (1 = não embaralhar).

As questões foram escritas especificamente para este estudo e podem conter erros. Use ⚑ para marcar uma suspeita e confira sempre o texto da lei.

#### Lote 1 e lote 2
- **Lote 1** (`lp`, `info`, `cf`, `adm`, `leg`, `dt`, `dpt`): 88 questões escritas a partir do Anexo II do Edital 01/2022.
- **Lote 2** (`lote2.json`): 205 questões originais, escritas depois de ler provas de Técnico Judiciário – Área Administrativa de TRTs (2020 em diante) e de abrir os editais recentes. Cada prova foi tratada como um mapa de temas: as questões **não copiam** enunciados nem alternativas de prova; o campo `src` registra o tema recorrente e as provas em que ele apareceu (por exemplo, "FCC 2022: TRT5, TRT9…"). Quando o tema veio de uma lista de temas sem a questão exata, o `src` diz isso.
- Nas questões jurídicas do lote 2, `v: 1` significa que o artigo foi conferido em 17/11/2026 em cópia do texto da lei (a data e a lei conferida aparecem no fim da base legal, em `b`). O site do Planalto não abriu para a ferramenta que usei, então a conferência foi feita em cópias do texto da lei hospedadas em outros sites (CGU, Senado, órgãos públicos e sites de terceiros que reproduzem o texto do Planalto); para súmulas e temas, no enunciado publicado em sites do STF, do STJ e jurídicos. Não é a conferência no Planalto: na dúvida, abra o texto oficial.
- `v: 0` significa que o artigo e a versão da lei estão indicados em `b`, mas o texto não foi conferido nesta rodada. Confirme no texto da lei antes de decorar.
- CLT: a conferência usou o texto original das Leis 13.467/2017 (reforma trabalhista) e 14.442/2022 (teletrabalho). Os artigos que esses textos não reproduzem (férias, adicionais, rescisão, prescrição de menores, boa parte do processo) continuam com `v: 0`, e eventuais alterações da CLT posteriores a essas leis não foram pesquisadas. Os artigos da Constituição sobre a Justiça do Trabalho (art. 114) também seguem sem conferência.
- Limites: não encontrei o PDF da prova do cargo em todos os 24 TRTs (o levantamento, com as lacunas, está no documento "Provas e editais dos TRTs (2020–2026)"). Quando a lista de temas veio de resumo da prova, e não do PDF lido por inteiro, os temas por prova são aproximados.

## Simulados
Coloque arquivos `.json` em `simulados/` e liste os nomes em `simulados/index.json` (`{"arquivos":["sim01.json"]}`).

## Fonte do edital
Base: Anexo II do Edital 01/2022 (TRT3). Pesos e divisões de tópicos são estimativas minhas e devem ser conferidas quando o edital novo sair.
