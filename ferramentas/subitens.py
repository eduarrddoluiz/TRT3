# Subitens do Anexo II (Edital 01/2022, TRT3) — divisão de cada tópico em institutos/aspectos.
# A divisão é minha, feita a partir dos institutos que o Anexo II lista em cada item (resumo do Anexo II
# lido em 24/11/2026 no repositório do TRT3) e da aba "Edital verticalizado" da planilha EDITAL TRT.
# Cada subitem: (rótulo, regex sobre o texto normalizado da questão: minúsculas, sem acento).
import re, unicodedata

def norm(s):
    s = unicodedata.normalize('NFD', s or '')
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.lower()

S = {}
def T(t, *subs):
    S[t] = [(lab, re.compile(rx)) for lab, rx in subs]

# ---------------- Língua Portuguesa ----------------
T('t001', ('Localização de informação explícita', r'informa|afirma|segundo o texto|de acordo com o texto|literal|explicit|texto (diz|menciona|declara)'),
          ('Paráfrase e reescrita fiel ao sentido', r'parafras|reescrit|mantem o sentido|sem alterar o sentido|equivale'),
          ('Ideia central e tema do texto', r'tema|ideia central|ideia principal|assunto principal|objetivo do texto|finalidade'))
T('t002', ('Inferência autorizada pelo texto', r'infer|conclui|depreende|pressup|subentend|implicit|permite concluir'),
          ('Pressupostos e subentendidos', r'pressup|subentend|implicit'),
          ('Inferência indevida (extrapolação)', r'extrapol|nao se pode concluir|nao autoriza|indevid|nao e possivel inferir|incorret'))
T('t003', ('Retomada por pronome (anáfora)', r'pronome|retoma|anafor|refere-se|referente'),
          ('Retomada por sinônimo, hiperônimo ou expressão nominal', r'sinonim|hiperonim|expressao nominal|substitui|retoma'),
          ('Catáfora e elipse', r'catafor|elipse|antecip|omiss'))
T('t004', ('Conectivos de causa, consequência e conclusão', r'caus|consequen|conclus|portanto|logo|pois|porque|visto que'),
          ('Conectivos de oposição e concessão', r'oposi|concess|adversat|embora|porem|contudo|entretanto|todavia|mas\b|no entanto'),
          ('Conectivos de condição, finalidade, tempo e adição', r'condic|finalidade|temporal|tempo|adic|alem disso|caso|a fim de|para que|quando'),
          ('Operadores sequenciais e organização do texto', r'sequenc|ordena|enumer|em primeiro lugar|por fim|organiza'))
T('t005', ('Coesão referencial e sequencial', r'coes|retom|referenc|conect'),
          ('Coerência (lógica e não contradição)', r'coeren|contradi|incoeren|logic|sentido'))
T('t006', ('Sentido de palavra ou expressão no contexto', r'sentido|significa|sinonim|contexto|substitu|equivale'),
          ('Linguagem figurada e conotação', r'figurad|conota|metafor|ironi|denota'))
T('t007', ('Crase obrigatória', r'crase|acento grave|\ba\b.*(obrigat|exige)'),
          ('Crase proibida', r'crase|acento grave|proib|nao ocorre|indevid'),
          ('Crase facultativa', r'facultat|opcional|pronome possessivo|ate a'))
T('t008', ('Modo indicativo (tempos)', r'indicativ|preterito|presente|futuro do presente|mais-que-perfeito|imperfeito'),
          ('Modo subjuntivo', r'subjuntiv|conjuntiv'),
          ('Futuro do pretérito e correlação verbal', r'futuro do preterito|correla|hipotet|condicional'),
          ('Imperativo, formas nominais e locuções', r'imperativ|infinitiv|gerund|particip|locucao verbal|formas nominais'))
T('t009', ('Colocação pronominal (próclise, ênclise, mesóclise)', r'proclise|enclise|mesoclise|coloca(cao)? (do )?pronom|atrativ'),
          ('Pronomes relativos', r'relativ|\bcujo|\bonde\b|o qual|a qual'),
          ('Pronomes pessoais, oblíquos e de tratamento', r'pessoa|obliquo|\blhe\b|\bo\b.*complemento|tratamento|vossa'),
          ('Pronomes demonstrativos e indefinidos', r'demonstrativ|\beste\b|\besse\b|\baquele|indefinid'))
T('t010', ('Regência verbal', r'regencia verbal|verbo .*(exige|rege|pede)|transitiv|preposi|regencia'),
          ('Regência nominal', r'regencia nominal|nome .*preposi|substantivo|adjetivo .*preposi'),
          ('Pronome relativo regido por preposição', r'(de|a|em|com|por) que\b|(ao|do|no|pelo) qual|cujo|preposicao antes do relativo|relativ'))
T('t011', ('Concordância verbal', r'concordancia verbal|verbo .*concord|sujeito|plural|singular|concord'),
          ('Concordância nominal', r'concordancia nominal|adjetivo|anexo|meio|bastante|obrigad|nominal'),
          ('Casos especiais (haver, fazer, se, coletivos)', r'\bhaver\b|\bhavia|\bfaz\b|impessoal|\bse\b.*(apassiv|indetermin)|coletiv|porcentag|um dos que'))
T('t012', ('Vírgula', r'virgula'),
          ('Ponto, ponto e vírgula, dois-pontos', r'ponto e virgula|dois-pontos|dois pontos|\bponto\b'),
          ('Travessão, parênteses, aspas', r'travess|parentes|aspas|reticenc'))
T('t013', ('Variação regional, social e situacional', r'varia|regional|social|diatop|diastrat|diafas|registro|formal|informal|coloquial'),
          ('Preconceito linguístico e adequação', r'preconceito|adequa|inadequa|situacao comunicativ'))
T('t014', ('Norma-padrão x norma culta x uso', r'norma|padrao|culta|gramatic'),
          ('Adequação ao registro formal', r'formal|registro|oficial|redacao'))

# ---------------- Informática ----------------
T('t015', ('LibreOffice: arquivos e pastas (abrir, salvar, formatos)', r'salvar|abrir|formato|odt|ods|odp|extens|exportar|pdf|arquivo|pasta'),
          ('LibreOffice: configurações (Ferramentas > Opções)', r'ferramentas|opcoes|configura|idioma|autocorre|personaliz'))
T('t016', ('Explorador de Arquivos: copiar, mover, renomear', r'explorador|copiar|mover|recortar|colar|renomear|arrast'),
          ('Lixeira e exclusão', r'lixeira|excluir|exclus|shift\s*\+\s*delete|apagar|delete'),
          ('Atalhos de teclado do Windows', r'atalho|tecla|ctrl|windows\s*\+|alt\s*\+'),
          ('Extensões, caminhos e propriedades de arquivos', r'extens|caminho|propriedades|oculto|somente leitura|tamanho'))
T('t017', ('Configurações e Painel de Controle', r'configura|painel de controle|personaliza|atualiza|windows update|sistema'),
          ('Contas de usuário e permissões', r'permiss|conta|administrador|usuario|ntfs|controle de conta|uac|compartilh'),
          ('Segurança do Windows (Defender, firewall, BitLocker)', r'defender|firewall|bitlocker|seguranca do windows'))
T('t018', ('Criar, abrir e salvar documentos; formatos', r'salvar|abrir|novo documento|\.docx|\.dotx|formato|pdf'),
          ('Modelos de documento', r'modelo|template|dotx'),
          ('Estrutura da janela (faixa de opções, guias)', r'faixa de opcoes|guia|aba|barra de status|modos de exibicao|layout de impressao'))
T('t019', ('Formatação de fonte', r'fonte|negrito|italico|sublinhad|tamanho da fonte|realce'),
          ('Formatação de parágrafo (recuo, espaçamento, alinhamento)', r'paragrafo|recuo|espacamento|alinhament|justific'),
          ('Estilos e Pincel de Formatação', r'estilo|pincel'),
          ('Cabeçalho e rodapé', r'cabecalho|rodape'),
          ('Colunas', r'coluna'))
T('t020', ('Marcadores e numeração de listas', r'marcador|numeracao|lista'),
          ('Tabelas', r'tabela|celula|mesclar|linha'),
          ('Texto em colunas', r'coluna'))
T('t021', ('Configuração de página (margens, orientação, tamanho)', r'margem|orientacao|retrato|paisagem|tamanho do papel|configurar pagina|layout'),
          ('Impressão', r'imprim|impressao|ctrl\s*\+\s*p'),
          ('Ortografia e gramática; revisão', r'ortograf|gramatic|revisao|controlar alteracoes|f7'))
T('t022', ('Quebras de página e de seção', r'quebra'),
          ('Numeração de páginas', r'numero de pagina|numeracao de pagina|numerar'),
          ('Legendas e índices (sumário)', r'legenda|indice|sumario'))
T('t023', ('Inserir objetos e imagens', r'objeto|imagem|figura|inserir'),
          ('Campos predefinidos', r'campo'),
          ('Caixas de texto e caracteres especiais', r'caixa de texto|simbolo|caractere especial'))
T('t024', ('Desenhos, formas e cliparts', r'desenh|forma|clip|smartart|icone'),
          ('Régua, janelas e modos de exibição', r'regua|janela|exibi|zoom'),
          ('Atalhos e menus do Word', r'atalho|ctrl|menu|tecla'))
T('t025', ('Mala direta', r'mala direta|correspondencia|destinatari'),
          ('Proteção de documentos (senha, restringir edição)', r'protege|protecao|senha|restringir|somente leitura|criptograf'))
T('t026', ('Células, linhas, colunas e referências', r'celula|linha|coluna|referencia|endereco'),
          ('Pastas de trabalho e planilhas', r'pasta de trabalho|planilha|guia|aba|xlsx'),
          ('Formatação de células e tipos de dados', r'formatar celulas|formato|numero|data|moeda|porcentag|mesclar'))
T('t027', ('Gráficos', r'grafico'),
          ('Tabelas e tabela dinâmica', r'tabela dinamica|tabela|filtro'))
T('t028', ('Fórmulas e operadores', r'formula|operador|\=|referencia (absoluta|relativa|mista)|\$'),
          ('Funções (SOMA, MÉDIA, SE, PROCV, CONT.SE...)', r'soma|media|\bse\(|\bse\b|procv|cont\.se|maximo|minimo|concat|funcao|hoje'),
          ('Macros', r'macro|vba'),
          ('Erros de fórmula (#DIV/0!, #REF!...)', r'#div|#ref|#nome|#valor|#n/d|erro'))
T('t029', ('Impressão de planilhas (área, títulos)', r'imprim|impressao|area de impressao|ajustar'),
          ('Inserção de objetos e campos', r'objeto|imagem|inserir|campo'),
          ('Controle de quebras de página', r'quebra'))
T('t030', ('Numeração de páginas na planilha', r'numer|cabecalho|rodape|pagina'),
          ('Obtenção de dados externos', r'dados externos|importar|obter dados|power query|csv|texto|conex'))
T('t031', ('Classificação e filtro de dados', r'classific|ordenar|ordem|filtro|crescente|decrescente'),
          ('Atalhos e menus do Excel', r'atalho|ctrl|menu|tecla|f2|f4'))
T('t032', ('Criação e estrutura de apresentações; modelos', r'apresentacao|modelo|tema|slide mestre|layout|novo slide'),
          ('Edição e formatação de slides', r'format|editar|texto|fonte|plano de fundo'))
T('t033', ('Animações', r'animac'),
          ('Transições', r'transic'),
          ('Objetos, multimídia, desenho e clipart', r'objeto|imagem|video|audio|som|multimidia|desenh|forma|clip|grafico'))
T('t034', ('Apresentar (modo de apresentação, F5)', r'f5|apresentac|modo apresentador|exibicao de slides|iniciar'),
          ('Impressão de apresentações (folhetos, anotações)', r'imprim|folheto|anotac'),
          ('Atalhos e menus do PowerPoint', r'atalho|ctrl|menu|tecla'))
T('t035', ('Envio de e-mail (Para, Cc, Cco, anexos)', r'\bcc\b|cco|copia oculta|para:|anexo|destinat|enviar|encaminhar|responder'),
          ('Pastas, regras e organização', r'pasta|caixa de entrada|caixa de saida|itens enviados|regra|arquivar|lixo'),
          ('Calendário, reuniões, contatos e tarefas', r'calendario|reuniao|compromisso|contato|tarefa'))
T('t036', ('Abas, janelas e navegação anônima', r'aba|guia|janela|anonim'),
          ('Histórico, downloads, favoritos', r'historico|download|favorit|marcador'),
          ('Atalhos do Chrome', r'atalho|ctrl|tecla'),
          ('Segurança e privacidade no navegador (cookies, cadeado, https)', r'cookie|cadeado|https|privacidade|senha|certificado|cache'))
T('t037', ('Vírus', r'virus'),
          ('Cavalo de Troia (trojan)', r'troia|trojan'),
          ('Worm', r'worm'),
          ('Outros malwares (backdoor, bot, rootkit) e proteção', r'backdoor|bot\b|botnet|rootkit|antivirus|malware'))
T('t038', ('Spyware (keylogger, adware)', r'spyware|keylogger|screenlogger|adware'),
          ('Phishing', r'phishing'),
          ('Pharming', r'pharming|dns'),
          ('Ransomware', r'ransomware|resgate|sequestr'),
          ('Spam', r'spam'))

# ---------------- Direito Constitucional ----------------
T('t039', ('Conceitos e sentidos de Constituição', r'sentido|conceito|sociolog|politic|juridic|lassalle|schmitt|kelsen|material|formal'),
          ('Classificações das Constituições', r'classific|rigid|flexivel|semirrigid|promulgad|outorgad|escrit|analitic|sintetic|dogmatic'))
T('t040', ('Eficácia plena, contida e limitada', r'eficacia|plena|contida|limitada|programatic|aplicabilidade'),
          ('Interpretação constitucional (métodos e princípios)', r'interpret|unidade|concordancia pratica|efeito integrador|forca normativa|conforme a constituicao'))
T('t041', ('Fundamentos (art. 1º)', r'fundament|soberania|cidadania|dignidade|valores sociais|pluralismo|art\. 1'),
          ('Separação dos Poderes (art. 2º)', r'poderes|independentes e harmonicos|art\. 2'),
          ('Objetivos fundamentais (art. 3º)', r'objetivo|erradicar|sociedade livre|desenvolvimento nacional|art\. 3'),
          ('Princípios das relações internacionais (art. 4º)', r'relacoes internacionais|autodetermina|nao intervencao|asilo|art\. 4|integracao .*america latina'))
T('t042', ('Igualdade, legalidade e liberdades (art. 5º)', r'igualdade|legalidade|liberdade|manifestacao do pensamento|crenca|locomocao|associa|reuniao'),
          ('Inviolabilidades (domicílio, sigilo, intimidade)', r'domicilio|sigilo|intimidade|correspondencia|comunicac|casa'),
          ('Propriedade e desapropriação', r'propriedade|desapropria|requisi'),
          ('Garantias penais e processuais (prisão, júri, devido processo)', r'prisao|flagrante|juri|devido processo|contraditorio|ampla defesa|crime|pena|retroag|extradi'),
          ('Remédios constitucionais (HC, MS, MI, HD, ação popular)', r'habeas|mandado de seguranca|mandado de injuncao|acao popular|remedio'),
          ('Direito adquirido, ato jurídico perfeito, coisa julgada; tratados', r'direito adquirido|ato juridico perfeito|coisa julgada|tratad|emenda constitucional .*equivalent'))
T('t043', ('Direitos sociais (art. 6º)', r'art\. 6|direitos sociais|educacao|saude|moradia|transporte|lazer'),
          ('Direitos dos trabalhadores (art. 7º)', r'art\. 7|trabalhador|salario|ferias|jornada|aviso'),
          ('Liberdade sindical e greve (arts. 8º e 9º)', r'sindic|art\. 8|art\. 9|greve|contribuicao'),
          ('Participação e representação (arts. 10 e 11)', r'art\. 10|art\. 11|colegiad|representante|mais de duzentos'))
T('t044', ('Brasileiros natos', r'nato|natos|nascid'),
          ('Naturalização', r'naturaliz'),
          ('Cargos privativos e distinções', r'privativ|cargos|distinc'),
          ('Perda da nacionalidade', r'perda|perde|cancelad'))
T('t045', ('Sufrágio, voto e alistamento', r'voto|sufragio|alistamento|facultativ|obrigatori'),
          ('Condições de elegibilidade e idades mínimas', r'elegibil|idade minima|domicilio eleitoral|filiacao'),
          ('Inelegibilidades', r'inelegiv|inelegibil|parentes|conjuge|reeleic'),
          ('Perda e suspensão dos direitos políticos; partidos', r'perda|suspensao|cassac|partid|anterioridade eleitoral'))
T('t046', ('Federação, entes autônomos e capital', r'federa|autonom|brasilia|capital|indissoluvel'),
          ('Vedações aos entes (art. 19) e criação de Estados/Municípios', r'art\. 19|vedad|criacao|incorporacao|fusao|desmembramento|plebiscit|cultos'))
T('t047', ('Bens e competências da União', r'bens da uniao|competencia (privativa|exclusiva|comum|concorrente)|uniao'),
          ('Estados federados', r'estados|governador|assembleia legislativa'),
          ('Municípios', r'municip|camara municipal|prefeito|vereador'),
          ('Distrito Federal e Territórios', r'distrito federal|territorio'),
          ('Intervenção federal e estadual', r'interven'))
T('t048', ('Princípios do art. 37, caput', r'legalidade|impessoalidade|moralidade|publicidade|eficiencia|limpe|caput'),
          ('Acesso a cargos, concurso e validade', r'concurso|acesso|validade|prorrog|estrangeiro'),
          ('Cargos em comissão, funções de confiança e contratação temporária', r'comissao|confianca|temporari|excepcional interesse'),
          ('Teto, remuneração e acumulação', r'teto|subsidio|remunerac|acumula|irredutib'),
          ('Responsabilidade civil do Estado (art. 37, § 6º) e improbidade (art. 37, § 4º)', r'responsabilidade|§ 6|improbidade|§ 4|dolo ou culpa'))
T('t049', ('Estabilidade e estágio probatório (art. 41)', r'estabilidade|estavel|estagio|art\. 41|tres anos|avaliacao'),
          ('Aposentadoria do servidor (art. 40)', r'aposent|art\. 40|previdenc'),
          ('Disponibilidade, reintegração, recondução e aproveitamento', r'disponibilidade|reintegr|recondu|aproveitamento'),
          ('Servidor em mandato eletivo (art. 38) e direitos (art. 39)', r'mandato eletivo|art\. 38|art\. 39|regime juridico unico|direitos'))
T('t050', ('Separação dos Poderes e funções típicas/atípicas', r'tipica|atipica|separacao|funcoes|independentes e harmonicos|pesos e contrapesos'),
          ('Cláusulas pétreas e organização geral', r'clausula petrea|art\. 60|forma federativa|voto direto'))
T('t051', ('Composição e funcionamento do Congresso (sessões, legislatura)', r'legislatura|sessao|sessoes|reuni|composi|recesso|convoca'),
          ('Atribuições do Congresso (arts. 48 e 49)', r'art\. 48|art\. 49|exclusiva do congresso|compete ao congresso|sancao'),
          ('Imunidades e vedações dos parlamentares', r'imunidade|inviolav|vedac|perda do mandato|foro'),
          ('Comissões parlamentares e CPIs', r'comiss|cpi|inquerito'))
T('t052', ('Câmara dos Deputados (composição e competências privativas)', r'camara dos deputados|deputad|art\. 51|proporcional'),
          ('Senado Federal (composição e competências privativas)', r'senado|senador|art\. 52|majoritari|processar e julgar'))
T('t053', ('Emendas constitucionais', r'emenda|art\. 60|proposta de emenda'),
          ('Leis complementares e ordinárias (iniciativa, quórum)', r'lei complementar|lei ordinaria|iniciativa|quorum|maioria absoluta|maioria simples'),
          ('Sanção, veto e promulgação', r'sancao|veto|promulga'),
          ('Medidas provisórias', r'medida provisoria|art\. 62'),
          ('Leis delegadas, decretos legislativos e resoluções', r'delegad|decreto legislativo|resoluc'))
T('t054', ('Eleição, posse e mandato', r'eleic|posse|mandato|reeleic|vacancia|substitu'),
          ('Atribuições do Presidente (art. 84)', r'art\. 84|privativamente ao presidente|atribuic|delegar'),
          ('Crimes de responsabilidade e responsabilidade do Presidente', r'crime de responsabilidade|crimes comuns|impeachment|art\. 85|art\. 86|suspens'),
          ('Ministros de Estado e Conselhos', r'ministros de estado|conselho da republica|conselho de defesa'))
T('t055', ('Garantias e vedações da magistratura', r'vitalic|inamovib|irredutib|garantias|vedad|magistrad'),
          ('Estatuto da Magistratura e ingresso na carreira (art. 93)', r'art\. 93|ingresso|concurso|promoc|tres anos de atividade juridica'),
          ('Quinto constitucional e autonomia do Judiciário', r'quinto|autonomia|orcament|art\. 94|art\. 99'),
          ('Órgãos do Judiciário (art. 92) e precatórios', r'art\. 92|orgaos do poder judiciario|precatori'))
T('t056', ('Composição do STF', r'composi|onze ministros|notavel saber|nomead|sabatin'),
          ('Competência originária do STF', r'originari|processar e julgar|acao direta|adi|adc|adpf'),
          ('Recurso extraordinário e repercussão geral', r'recurso extraordinario|repercussao geral|recurso ordinario'),
          ('Súmula vinculante', r'sumula vinculante|art\. 103-a|reclamac'))
T('t057', ('Composição do CNJ', r'composi|quinze membros|presidid|corregedor'),
          ('Competências do CNJ', r'compete ao cnj|controle da atuacao|competenc|disciplinar|ouvidoria|avocar'))
T('t058', ('Composição do STJ', r'composi|trinta e tres|33|nomead'),
          ('Competências do STJ (recurso especial)', r'recurso especial|competenc|processar e julgar|homologa'),
          ('Órgãos junto ao STJ (CJF, ENFAM)', r'conselho da justica federal|enfam|escola nacional'))
T('t059', ('TST: composição e competência', r'tribunal superior do trabalho|tst|vinte e sete|27 ministros|art\. 111-a'),
          ('TRTs: composição', r'tribunais regionais|trt|sete juizes|art\. 115|itinerant|camaras regionais'),
          ('Competência da Justiça do Trabalho (art. 114)', r'art\. 114|compete a justica do trabalho|competenc'),
          ('Juízes do Trabalho e Varas', r'juiz do trabalho|juizes do trabalho|varas|art\. 112|art\. 116|juiz de direito'))
T('t060', ('Composição e funcionamento do CSJT', r'conselho superior da justica do trabalho|csjt|funciona junto'),
          ('Competência do CSJT (supervisão administrativa, orçamentária, financeira, patrimonial)', r'supervis|administrativ|orcamentari|financeir|patrimonial|vinculante'))

# ---------------- Direito Administrativo ----------------
T('t061', ('Princípios expressos (LIMPE)', r'legalidade|impessoalidade|moralidade|publicidade|eficiencia'),
          ('Supremacia e indisponibilidade do interesse público', r'supremacia|indisponibilidade|interesse publico'),
          ('Autotutela, segurança jurídica e motivação', r'autotutela|seguranca juridica|motiva|confianca legitima'),
          ('Razoabilidade, proporcionalidade, continuidade e especialidade', r'razoabil|proporcional|continuidade|especialidade|tutela'))
T('t062', ('Administração direta (órgãos, desconcentração)', r'direta|orgao|desconcentra|ministerio|secretaria'),
          ('Administração indireta (entidades)', r'indireta|entidade|autarquia|fundacao|empresa publica|sociedade de economia mista'),
          ('Controle/tutela e vinculação ministerial', r'tutela|supervisao ministerial|vincula|controle finalistico'))
T('t063', ('Centralização x descentralização', r'centraliza|descentraliza'),
          ('Descentralização por outorga e por delegação', r'outorga|delegac|servicos|concess|permiss'),
          ('Desconcentração', r'desconcentra'))
T('t064', ('Autarquias', r'autarquia'),
          ('Fundações públicas', r'fundac'),
          ('Empresas públicas', r'empresa publica'),
          ('Sociedades de economia mista', r'economia mista'))
T('t065', ('Poder hierárquico (delegação, avocação, revisão)', r'hierarq|delega|avoca|subordin|revis'),
          ('Poder disciplinar', r'disciplinar|sanc|punic|penalidade|servidor'))
T('t066', ('Poder regulamentar (decretos, regulamentos)', r'regulament|decreto|art\. 84'),
          ('Poder de polícia (conceito, atributos, ciclo)', r'policia|coercib|autoexecutor|discricion|ciclo|fiscaliza|condicionar'))
T('t067', ('Excesso de poder', r'excesso'),
          ('Desvio de poder (finalidade)', r'desvio|finalidade'),
          ('Omissão e uso regular do poder', r'omiss|uso do poder|uso regular|abuso'))
T('t068', ('Cargo público', r'cargo'),
          ('Emprego público', r'emprego'),
          ('Função pública (de confiança, temporária)', r'funcao|confianca|temporari'))
T('t069', ('Conceito de ato administrativo e ato x fato', r'conceito|fato administrativo|ato da administracao|declaracao|manifestacao'),
          ('Classificações dos atos', r'classific|simples|complexo|composto|vinculad|discricion|geral|individual|espec'))
T('t070', ('Competência', r'competen'),
          ('Finalidade', r'finalidade'),
          ('Forma', r'forma\b|forma escrita|formal'),
          ('Motivo e motivação', r'motivo|motiva|teoria dos motivos determinantes'),
          ('Objeto', r'objeto|conteudo'))
T('t071', ('Presunção de legitimidade e veracidade', r'presun|legitimidade|veracidade'),
          ('Imperatividade', r'imperativ'),
          ('Autoexecutoriedade', r'autoexecut|executoriedade'),
          ('Tipicidade', r'tipicidade'))
T('t072', ('Anulação (ilegalidade; prazo de 5 anos)', r'anula|ilegal|cinco anos|decai|sumula 473'),
          ('Revogação (conveniência e oportunidade)', r'revoga|conveniencia|oportunidade'),
          ('Convalidação', r'convalida|sanavel|vicio sanavel'))
T('t073', ('Ato vinculado', r'vinculad'),
          ('Ato discricionário e mérito administrativo', r'discricion|merito|conveniencia|oportunidade'),
          ('Controle judicial da discricionariedade', r'controle judicial|poder judiciario|razoabil|proporcional'))
# Lei 8.112 (t074–t079 em Adm.; t084–t091 em Legislação): mesmos subitens nos tópicos gêmeos
L8112 = {
 'b1': [('Âmbito, conceito de servidor e de cargo (arts. 1º a 4º)', r'servidor e a pessoa|cargo publico e o conjunto|art\. [1-4]\b|regime juridico|prestacao de servicos gratuitos|conceito')],
 'b2': [('Provimento: requisitos, nomeação, concurso, posse e exercício', r'provimento|nomeac|concurso|posse|exercicio|requisitos basicos'),
        ('Estágio probatório e estabilidade', r'estagio|estabilidade|probatorio'),
        ('Readaptação, reversão, aproveitamento, reintegração e recondução', r'readapta|revers|aproveitament|reintegr|recondu'),
        ('Vacância', r'vacancia|exoneracao|demissao|falecimento|posse em outro cargo'),
        ('Remoção e redistribuição', r'remoc|redistribu'),
        ('Substituição', r'substitui')],
 'b3': [('Vencimento e remuneração', r'vencimento|remuneracao|desconto|consignac|irredutiv'),
        ('Indenizações (ajuda de custo, diárias, transporte, auxílio-moradia)', r'ajuda de custo|diaria|transporte|auxilio-moradia|indeniz'),
        ('Gratificações e adicionais', r'gratifica|adicional|natalina|insalubr|noturno|servico extraordinario|ferias')],
 'b4': [('Férias', r'ferias'),
        ('Licenças', r'licenc'),
        ('Afastamentos e concessões', r'afastament|concess|doar sangue|alistamento|casamento|falecimento|horario especial|estudo no exterior|mandato'),
        ('Tempo de serviço', r'tempo de servico|contad'),
        ('Direito de petição', r'peticao|requerer|recurso|pedido de reconsideracao|prescreve')],
 'b5': [('Deveres', r'dever|art\. 116|zelo|lealdade|assiduidade|sigilo'),
        ('Proibições', r'proib|art\. 117|vedad|gerencia|participar'),
        ('Acumulação', r'acumula')],
 'b6': [('Responsabilidades civil, penal e administrativa', r'responsabil|civil|penal|administrativ'),
        ('Penalidades e prescrição', r'penalidade|advertencia|suspensao|demissao|cassacao|destituic|prescri'),
        ('Sindicância e afastamento preventivo', r'sindicancia|afastamento preventivo|sessenta dias'),
        ('PAD: comissão, fases e julgamento', r'processo disciplinar|pad|comissao|inquerito|julgamento|defesa|indiciac|revisao')],
 'b7': [('Benefícios do plano de seguridade do servidor', r'seguridade|aposentadori|pensao|auxilio|salario-familia|licenca para tratamento|assistencia a saude|beneficio')],
}
for t, b in [('t074','b1'),('t084','b1'),('t075','b2'),('t085','b2'),('t076','b3'),('t086','b3'),('t077','b4'),('t087','b4'),('t078','b5'),('t088','b5'),('t079','b6'),('t089','b6'),('t090','b7')]:
    T(t, *L8112[b])
T('t091', ('Sindicância e afastamento preventivo', r'sindicancia|afastamento preventivo|sessenta dias'),
          ('Comissão de inquérito e fases do PAD', r'comissao|inquerito|instaurac|instrucao|indiciac|fases|portaria'),
          ('Defesa, relatório e julgamento', r'defesa|relatorio|julgamento|defensor dativo|revel|prazo'),
          ('Revisão do processo', r'revisao'))
T('t080', ('Princípios, objetivos e agentes da contratação', r'principio|objetivo|agente de contratacao|comissao de contratacao|pregoeiro|segregacao'),
          ('Fases do processo licitatório', r'fase|preparatoria|divulgacao|habilitacao|julgamento|homologa|recursal|edital'),
          ('Modalidades (pregão, concorrência, concurso, leilão, diálogo competitivo)', r'pregao|concorrencia|concurso|leilao|dialogo competitivo|modalidade'),
          ('Critérios de julgamento', r'menor preco|maior desconto|melhor tecnica|tecnica e preco|maior lance|maior retorno|criterio'),
          ('Contratação direta (dispensa e inexigibilidade)', r'dispensa|inexigib|contratacao direta'),
          ('Contratos administrativos (duração, alteração, extinção, sanções)', r'contrato|clausula|garantia|alteracao|extinc|reequilibrio|sanc|multa|impedimento|inidoneidade'),
          ('Procedimentos auxiliares (registro de preços, credenciamento)', r'registro de precos|credenciamento|pre-qualificacao|manifestacao de interesse|registro cadastral'))
T('t081', ('Responsabilidade objetiva e teoria do risco administrativo', r'objetiv|risco administrativo|art\. 37, § 6|nexo'),
          ('Excludentes e atenuantes (culpa da vítima, força maior)', r'exclud|culpa exclusiva|forca maior|caso fortuito|culpa concorrente|atenua'),
          ('Omissão estatal e responsabilidade subjetiva', r'omiss|subjetiv|culpa do servico|faute'),
          ('Ação regressiva e prescrição', r'regress|direito de regresso|prescri|dolo ou culpa'))
T('t082', ('Princípios e critérios do processo (art. 2º)', r'art\. 2|principio|criterio|oficialidade|gratuidade'),
          ('Direitos e deveres do administrado', r'direitos do administrado|deveres do administrado|administrado'),
          ('Início, legitimados, competência, impedimento e suspeição', r'inicio|legitimad|competencia|delegac|avocac|impediment|suspeic'),
          ('Forma, tempo, lugar, comunicação e prazos', r'forma|lugar|intimac|prazo|dias uteis|contagem'),
          ('Instrução, decisão e motivação', r'instrucao|prova|decisao|motiva|parecer|decidir'),
          ('Anulação, revogação, convalidação e decadência', r'anula|revoga|convalida|decai|cinco anos'),
          ('Recurso administrativo e revisão', r'recurso|revisao|reformatio|tres instancias|reconsider'))
T('t083', ('Atos que importam enriquecimento ilícito (art. 9º)', r'art\. 9|enriquecimento ilicito'),
          ('Atos que causam lesão ao erário (art. 10)', r'art\. 10|lesao ao erario|prejuizo ao erario'),
          ('Atos contra os princípios (art. 11)', r'art\. 11|principios da administracao'),
          ('Sanções (art. 12) e dolo', r'sanc|art\. 12|dolo|perda da funcao|suspensao dos direitos politicos|multa'),
          ('Processo, prescrição, acordo e sujeitos', r'prescri|acordo de nao persecucao|legitim|sujeito|agente publico|terceiro|indisponibilidade|afastamento'))
T('t092', ('Princípios e critérios do processo (art. 2º)', r'art\. 2|principio|criterio|oficialidade|gratuidade'),
          ('Direitos e deveres do administrado', r'direitos do administrado|deveres do administrado|administrado'),
          ('Início, legitimados, competência, impedimento e suspeição', r'inicio|legitimad|competencia|delegac|avocac|impediment|suspeic'),
          ('Forma, tempo, lugar, comunicação e prazos', r'forma|lugar|intimac|prazo|dias uteis|contagem'),
          ('Instrução, decisão e motivação', r'instrucao|prova|decisao|motiva|parecer|decidir'),
          ('Anulação, revogação, convalidação e decadência', r'anula|revoga|convalida|decai|cinco anos'),
          ('Recurso administrativo e revisão', r'recurso|revisao|reformatio|tres instancias|reconsider'))
T('t093', ('Atos que importam enriquecimento ilícito (art. 9º)', r'art\. 9|enriquecimento ilicito'),
          ('Atos que causam lesão ao erário (art. 10)', r'art\. 10|lesao ao erario|prejuizo ao erario'),
          ('Atos contra os princípios (art. 11)', r'art\. 11|principios da administracao'),
          ('Sanções (art. 12) e dolo', r'sanc|art\. 12|dolo|perda da funcao|suspensao dos direitos politicos|multa'),
          ('Processo, prescrição, acordo e sujeitos', r'prescri|acordo de nao persecucao|legitim|sujeito|agente publico|terceiro|indisponibilidade|afastamento'))
T('t094', ('Conceitos (dado pessoal, sensível, anonimizado, titular)', r'dado pessoal|sensivel|anonimiz|titular|tratamento|conceito|art\. 5'),
          ('Princípios (art. 6º)', r'principio|finalidade|adequacao|necessidade|transparencia|art\. 6'),
          ('Bases legais do tratamento (arts. 7º e 11)', r'consentimento|base legal|hipotese|art\. 7|art\. 11|legitimo interesse|obrigacao legal'),
          ('Direitos do titular (art. 18)', r'direitos do titular|art\. 18|portabilidade|eliminacao|acesso|correcao'),
          ('Agentes de tratamento e encarregado', r'controlador|operador|encarregado|agentes de tratamento'),
          ('Crianças e adolescentes; poder público', r'crianca|adolescent|poder publico|art\. 14|art\. 23'),
          ('ANPD, sanções e incidentes de segurança', r'anpd|autoridade nacional|sanc|multa|incidente|seguranca'))
T('t095', ('Conceito de pessoa com deficiência e avaliação', r'conceito|considera-se pessoa com deficiencia|avaliacao|biopsicossocial|impedimento de longo prazo'),
          ('Igualdade, não discriminação e capacidade civil', r'discrimina|igualdade|capacidade|curatela|tomada de decisao apoiada'),
          ('Acessibilidade, barreiras e tecnologia assistiva', r'acessibil|barreira|tecnologia assistiva|desenho universal|adaptacao razoavel'),
          ('Direito ao trabalho e outros direitos fundamentais', r'trabalho|emprego|habilitacao|reabilitacao|educacao|saude|moradia'),
          ('Crimes e infrações', r'crime|reclusao|infrac|pena'))
T('t096', ('Regimento Interno: composição e órgãos do TRT3', r'regimento|pleno|orgao especial|turma|presidente|corregedor|desembargador|composi'),
          ('Regimento Interno: competências e funcionamento', r'regimento|compete|competencia|sessao|eleic'),
          ('Código de Ética: princípios e deveres', r'codigo de etica|principio|dever|conduta'),
          ('Código de Ética: vedações e Comissão de Ética', r'vedad|proib|comissao de etica|apuracao|censura'))

# ---------------- Direito do Trabalho ----------------
T('t097', ('Princípios do Direito do Trabalho', r'principio|protec|in dubio|norma mais favoravel|condicao mais benefica|primazia|continuidade|irrenunciab|inalterab'),
          ('Fontes do Direito do Trabalho e hierarquia', r'fonte|hierarquia|art\. 8|costume|jurisprudencia|analogia|regulamento de empresa|autonom|heteronom'))
T('t098', ('Proteção contra despedida, seguro-desemprego e FGTS (art. 7º, I a III)', r'despedida|seguro-desemprego|fgts|inciso i\b|inciso ii\b|inciso iii\b'),
          ('Salário (mínimo, piso, irredutibilidade, 13º) (art. 7º, IV a X)', r'salario minimo|piso|irredutib|decimo terceiro|13|noturno|retencao'),
          ('Jornada, turnos, DSR, férias e horas extras (art. 7º, XIII a XVII)', r'jornada|oito horas|quarenta e quatro|turnos ininterruptos|repouso|ferias|extraordinari|cinquenta por cento'),
          ('Licenças, proteção da mulher e aviso-prévio (art. 7º, XVIII a XXI)', r'licenca|gestante|paternidade|mulher|aviso'),
          ('Saúde, segurança, adicionais e acidente (art. 7º, XXII a XXVIII)', r'reducao dos riscos|insalubr|periculos|penosa|acidente|seguro'),
          ('Prescrição, igualdade e proibições (art. 7º, XXIX a XXXIV); domésticos', r'prescri|cinco anos|dois anos|discrimina|menor|dezesseis|avulso|domestic'))
T('t099', ('Requisitos da relação de emprego (pessoalidade, onerosidade, não eventualidade, subordinação)', r'pessoalidade|onerosidade|eventual|subordina|requisito|pessoa fisica'),
          ('Relação de trabalho x emprego: autônomo, eventual, avulso, estagiário, voluntário', r'autonom|eventual|avulso|estagi|voluntari|cooperad|relacao de trabalho'))
T('t100', ('Conceito e requisitos do contrato intermitente', r'intermitente|alternancia|art\. 452-a|art\. 443'),
          ('Convocação, recusa e pagamento', r'convoca|recusa|tres dias|um dia util|pagamento|remuneracao|ferias'))
T('t101', ('Conceito de empregado (art. 3º) e espécies', r'art\. 3|empregado|domestico|rural|hipersuficiente|altos empregados'),
          ('Conceito de empregador (art. 2º) e empregador por equiparação', r'art\. 2|empregador|equipara|riscos da atividade|alteridade'))
T('t102', ('Poder diretivo e regulamentar', r'diretivo|organiza|regulament|comando'),
          ('Poder fiscalizatório (revista, monitoramento)', r'fiscaliz|revista|controle|monitora'),
          ('Poder disciplinar (advertência, suspensão)', r'disciplinar|advertencia|suspensao|punic|trinta dias'))
T('t103', ('Grupo econômico (art. 2º, §§ 2º e 3º)', r'grupo economico|§ 2|§ 3|interesse integrado|efetiva comunhao'),
          ('Sucessão de empregadores (arts. 10, 448 e 448-A)', r'sucess|art\. 10|art\. 448|mudanca na propriedade|sucedid|sucessor'))
T('t104', ('Responsabilidade solidária', r'solidari'),
          ('Responsabilidade subsidiária (terceirização, Súmula 331)', r'subsidiari|terceiriz|tomador|sumula 331|6\.019|dono da obra'))
T('t105', ('Conceito e características do contrato de trabalho', r'conceito|caracterist|consensual|sinalagmatic|oneroso|sucessivo|intuitu personae|art\. 442'),
          ('Classificação: prazo determinado e indeterminado; experiência', r'prazo determinado|indeterminad|experiencia|noventa dias|dois anos|prorroga'),
          ('Forma do contrato e anotação na CTPS', r'tacito|expresso|verbal|escrito|ctps|carteira de trabalho|anotac'))
T('t106', ('Requisitos da alteração lícita (art. 468)', r'art\. 468|mutuo consentimento|prejuizo|nulidade|alteracao'),
          ('Jus variandi e reversão ao cargo efetivo', r'jus variandi|revers|funcao de confianca|gratificacao'),
          ('Transferência do empregado (art. 469)', r'transfer|art\. 469|domicilio|adicional de transferencia|vinte e cinco'))
T('t107', ('Interrupção (hipóteses e efeitos)', r'interrup|art\. 473|ferias|doacao de sangue|faltas'),
          ('Suspensão (hipóteses e efeitos)', r'suspens|auxilio|aposentadoria por invalidez|incapacidade|greve|art\. 476'),
          ('Distinção e casos especiais (militar, acidente)', r'servico militar|acidente|deposito do fgts|contagem'))
T('t108', ('Justas causas do empregado (art. 482)', r'art\. 482|improbidade|incontinencia|desidia|embriaguez|abandono|insubordina|indisciplina'),
          ('Requisitos da justa causa (imediatidade, proporcionalidade, non bis in idem)', r'imediat|proporcional|bis in idem|gradac|perdao tacito'))
T('t109', ('Despedida (rescisão) indireta (art. 483)', r'indireta|art\. 483'),
          ('Dispensa arbitrária ou sem justa causa; multa do FGTS', r'arbitraria|sem justa causa|quarenta por cento|40%|multa'),
          ('Despedida coletiva (art. 477-A)', r'coletiva|477-a|plurima'),
          ('Extinção por acordo (art. 484-A) e pedido de demissão', r'484-a|acordo|comum acordo|pedido de demissao'))
T('t110', ('Culpa recíproca e indenização (art. 484; Súmula 14)', r'culpa reciproca|art\. 484|sumula 14|metade|vinte por cento'))
T('t111', ('Prazo e proporcionalidade (Lei 12.506/2011)', r'proporcional|12\.506|trinta dias|tres dias por ano|noventa'),
          ('Redução de jornada e dispensa do cumprimento (art. 488)', r'art\. 488|duas horas|sete dias|reducao'),
          ('Aviso-prévio indenizado, reconsideração e justa causa no curso', r'indenizad|reconsidera|art\. 489|art\. 490|art\. 491|projec|integra'))
T('t112', ('Dirigente sindical e membro da CIPA', r'dirigente sindical|cipa|cipeiro|representante'),
          ('Gestante', r'gestante|gravidez'),
          ('Acidentado (art. 118 da Lei 8.213)', r'acident|art\. 118|doze meses|auxilio-doenca acidentario'),
          ('Outras garantias e estabilidade decenal', r'decenal|cooperativa|comissao de conciliacao|garantia provisoria|reintegrac'))
T('t113', ('Jornada normal e controle de ponto (art. 58, art. 74)', r'jornada|art\. 58|ponto|registro|oito horas|cinco minutos|variac'),
          ('Horas in itinere (art. 58, § 2º, após a Reforma)', r'in itinere|deslocamento|transporte|percurso'),
          ('Empregados sem controle de jornada (art. 62)', r'art\. 62|gerente|externa|teletrabalh'))
T('t114', ('Intervalo intrajornada (art. 71)', r'intrajornada|art\. 71|uma hora|quinze minutos|refeicao'),
          ('Intervalo interjornada (art. 66) e outros intervalos', r'interjornada|onze horas|art\. 66|art\. 72|mecanograf|frigorific'))
T('t115', ('Descanso semanal remunerado (Lei 605/1949; art. 67)', r'descanso semanal|repouso semanal|dsr|domingo|605|art\. 67'),
          ('Feriados e trabalho em domingo', r'feriado|domingo|em dobro|escala'))
T('t116', ('Trabalho noturno (art. 73)', r'noturno|art\. 73|vinte e duas|22h|cinco horas|hora reduzida|52 minutos'),
          ('Horas extraordinárias (art. 59)', r'extraordinari|horas extras|art\. 59|duas horas|adicional'),
          ('Compensação e banco de horas', r'compensac|banco de horas|doze por trinta|12x36|seis meses'))
T('t117', ('Conceito e garantia do salário mínimo (art. 76)', r'salario minimo|art\. 76|garant|necessidades vitais|piso'),
          ('Irredutibilidade e salário mínimo proporcional', r'irredutib|proporcional|jornada reduzida|reduc'))
T('t118', ('Período aquisitivo e duração (art. 130)', r'aquisitivo|art\. 130|trinta dias|faltas|duracao'),
          ('Concessão, época e fracionamento (arts. 134 a 136)', r'concess|fracion|tres periodos|quatorze|cinco dias|epoca|art\. 134|art\. 136'),
          ('Férias coletivas (arts. 139 a 141)', r'coletiva'),
          ('Perda do direito e férias em dobro', r'perde|perda|art\. 133|dobro|art\. 137'))
T('t119', ('Remuneração das férias e terço constitucional', r'terco|um terco|remuneracao das ferias|art\. 142|pagamento .*dois dias'),
          ('Abono pecuniário (art. 143)', r'abono|art\. 143|um terco do periodo|converter'))
T('t120', ('Salário x remuneração (art. 457) e gorjetas', r'remuneracao|gorjeta|art\. 457|salario'),
          ('Parcelas não salariais (diárias, ajuda de custo, prêmios, abonos)', r'nao integra|nao incorpora|ajuda de custo|diaria|premio|abono|natureza'))
T('t121', ('Salário in natura (utilidade) e limites', r'in natura|utilidade|art\. 458|habitacao|alimentacao|vestuario'),
          ('Modalidades: por tempo, por produção, por tarefa; comissões', r'por tempo|producao|tarefa|comiss|percentag'),
          ('Forma, prazo e meios de pagamento (arts. 459 a 465)', r'quinto dia util|art\. 459|art\. 463|moeda|recibo|deposito|cheque|prazo'),
          ('Proteção do salário (descontos, intangibilidade)', r'desconto|art\. 462|intangib|truck system|impenhorab'))
T('t122', ('13º salário (Leis 4.090 e 4.749)', r'decimo terceiro|13|gratificacao natalina|4\.090|4\.749|vinte de dezembro|adiantamento'),
          ('Equiparação salarial (art. 461)', r'equipara|art\. 461|paradigma|identica funcao|quatro anos|dois anos|quadro de carreira'))
T('t123', ('Depósitos e alíquota (8%)', r'oito por cento|8%|deposit|mensal|aliquota|dois por cento'),
          ('Hipóteses de saque', r'saque|movimenta|levantamento|art\. 20'),
          ('Multa rescisória e prescrição do FGTS', r'quarenta por cento|40%|multa|prescri|sumula 362|tema 608'))
T('t124', ('Prescrição bienal e quinquenal (art. 7º, XXIX; art. 11 da CLT)', r'bienal|quinquenal|dois anos|cinco anos|art\. 11|xxix'),
          ('Prescrição total x parcial; menores; interrupção', r'total|parcial|menor|interrup|suspens|sumula 294|sumula 268|sumula 275'),
          ('Decadência', r'decaden|decai|inquerito'))
T('t125', ('Insalubridade (art. 189 e ss.)', r'insalubr|art\. 189|art\. 192|grau|minimo|medio|maximo|epi'),
          ('Periculosidade (art. 193)', r'periculos|art\. 193|trinta por cento|inflamav|explosiv|energia eletrica|motocicl|vigilan'),
          ('Normas gerais de segurança (CIPA, EPI, NR)', r'cipa|epi|equipamento de protecao|norma regulamentadora|nr\b|embargo|interdic'))
T('t126', ('Bancários e telefonistas (arts. 224 a 231)', r'bancari|art\. 224|telefon|art\. 227'),
          ('Professores (arts. 317 a 324)', r'professor|art\. 31[7-9]|art\. 32'),
          ('Minas, motoristas e outras categorias', r'mina|subsolo|art\. 29|motorista|ferroviari|jornalista|musico|operador cinematografic|art\. 2[3-9]\d'))
T('t127', ('Estabilidade da gestante (art. 10, II, b, do ADCT)', r'adct|confirmacao da gravidez|cinco meses apos o parto|estabilidade|garantia'),
          ('Licença-maternidade (120 dias, Empresa Cidadã, adoção)', r'licenca-maternidade|cento e vinte|120|empresa cidada|adoc|salario-maternidade|prorroga'),
          ('Proteção ao trabalho da mulher (amamentação, consultas, atividade insalubre)', r'amament|consulta|art\. 39[2-6]|insalubr|art\. 373|discrimina'))
T('t128', ('Convenção x acordo coletivo (art. 611)', r'convencao|acordo coletivo|art\. 611|sindicato|categoria'),
          ('Prevalência do negociado (arts. 611-A e 611-B)', r'611-a|611-b|prevalec|negociado|objeto ilicito|tema 1046'),
          ('Vigência, ultratividade e prevalência do acordo (arts. 614 e 620)', r'vigencia|dois anos|ultratividade|art\. 614|art\. 620'))
T('t129', ('Conceito e requisitos da greve (Lei 7.783)', r'7\.783|requisit|assembleia|aviso previo|quarenta e oito|setenta e duas|negocia'),
          ('Serviços essenciais e abuso do direito de greve', r'essenci|abus|art\. 1[01]|atividades essenciais|ordem judicial'),
          ('Efeitos sobre o contrato e lockout', r'suspens|lockout|salarios|contratacao de substitutos|piquete'))
T('t130', ('Teletrabalho: conceito e forma (arts. 75-A a 75-F)', r'teletrabalh|75-[a-f]|remoto|tecnologias da informacao|aditivo'),
          ('Outras mudanças da Reforma Trabalhista (Lei 13.467/2017)', r'13\.467|reforma|hipersuficiente|arbitragem|quitacao anual|termo de quitacao'))
T('t131', ('Dano extrapatrimonial: bens tutelados e titulares (arts. 223-A a 223-E)', r'223-[a-e]|extrapatrimonial|dano moral|honra|imagem|intimidade|pessoa juridica'),
          ('Fixação da indenização (art. 223-G)', r'223-g|grau|leve|media|grave|gravissima|indeniza|parametro'),
          ('Assédio moral e dano existencial', r'assedio|existencial|humilha'))
T('t132', ('Súmulas do TST de Direito do Trabalho', r'sumula'),
          ('Orientações Jurisprudenciais do TST', r'orientacao jurisprudencial|\boj\b|sdi'))
T('t133', ('Súmulas vinculantes do STF em Direito do Trabalho', r'sumula vinculante|\bsv\b'))
T('t134', ('Instruções normativas e atos do TST (Direito do Trabalho)', r'instrucao normativa|\bin\b|ato|resoluc|precedente normativo'))
T('t135', ('Conceito de acidente do trabalho e equiparações (Lei 8.213, arts. 19 a 21)', r'art\. (19|20|21)\b|acidente do trabalho|doenca ocupacional|doenca profissional|equipara|trajeto|nexo'),
          ('CAT, benefícios e garantia no emprego', r'cat\b|comunicacao de acidente|auxilio|beneficio|art\. 118|estabilidade|21-a'))
T('t136', ('Responsabilidade subjetiva e objetiva do empregador', r'subjetiv|objetiv|risco|culpa|dolo|art\. 927|tema 932'),
          ('Dano material, lucros cessantes e pensionamento', r'dano material|lucros cessantes|pensao|pension|emergente|art\. 950|art\. 945'))

# ---------------- Direito Processual do Trabalho ----------------
T('t137', ('Organização da Justiça do Trabalho (órgãos)', r'orgaos|organiza|art\. 111|tribunal superior|tribunais regionais|juizes do trabalho'),
          ('Competência material (art. 114 da CF)', r'art\. 114|competencia material|relacao de trabalho|greve|sindic|penalidades administrativas|contribuicoes'),
          ('Competência territorial (art. 651 da CLT)', r'art\. 651|territorial|local da prestacao|foro|agente ou viajante'))
T('t138', ('Varas do Trabalho (jurisdição e competência)', r'vara|art\. 65[0-9]|juiz do trabalho|juiz de direito'),
          ('TRTs (composição, competência)', r'tribunal regional|trt|art\. 67[0-9]|art\. 68[0-9]|turma'),
          ('TST (composição, órgãos e competência)', r'tribunal superior do trabalho|tst|sdi|sdc|orgao especial'))
T('t139', ('Secretarias das Varas e diretor de secretaria (arts. 710 a 712)', r'secretaria|diretor|art\. 71[0-2]|chefe de secretaria'),
          ('Distribuidores (arts. 713 a 715)', r'distribuidor|art\. 71[3-5]|distribuic'),
          ('Oficiais de justiça e avaliadores (art. 721)', r'oficial de justica|oficiais|avaliador|art\. 721|nove dias|mandado'))
T('t140', ('Nomeação, perito único e assistentes técnicos', r'nomea|perito|assistente tecnico|art\. 3\b|5\.584'),
          ('Honorários periciais (art. 790-B) e prova pericial', r'honorarios periciais|790-b|sucumbente|pericia|adiantamento'))
T('t141', ('Organização do MPT (LC 75/1993)', r'lc 75|lei complementar 75|procurador-geral do trabalho|organiza|ramo|ministerio publico da uniao|colegio|camara de coordenacao'),
          ('Atribuições do MPT (art. 83 da LC 75; ação civil pública; inquérito civil)', r'art\. 83|acao civil publica|inquerito civil|custos legis|recorrer|parecer|atribui|compete'))
T('t142', ('Princípios do processo do trabalho (oralidade, conciliação, celeridade, irrecorribilidade)', r'principio|oralidade|concilia|celeridade|irrecorrib|informalidade|concentrac|protec|impulso oficial'),
          ('Aplicação subsidiária do CPC (art. 769 da CLT e art. 15 do CPC; IN 39)', r'subsidiari|supletiv|art\. 769|art\. 15|in 39|instrucao normativa 39|omissao|compatib'))
T('t143', ('Prescrição (bienal, quinquenal) e decadência no processo', r'prescri|bienal|quinquenal|decaden|arguic|instancia ordinaria|sumula 153'),
          ('Prescrição intercorrente (art. 11-A)', r'intercorrente|11-a|dois anos .*execu'))
T('t144', ('Atos processuais: publicidade, horário, forma', r'publico|publicidade|seis as vinte|horario|forma|assinatura|art\. 770|art\. 771'),
          ('Termos processuais', r'termo|art\. 773|art\. 772'),
          ('Prazos: contagem em dias úteis, suspensão e prorrogação (arts. 774 a 775-A)', r'prazo|dias uteis|775|recesso|vinte de dezembro|prorroga|contagem|774'))
T('t145', ('Distribuição', r'distribui|art\. 783|art\. 784|art\. 785|art\. 786|art\. 787|art\. 788'),
          ('Valor da causa e alçada (Lei 5.584)', r'valor da causa|alcada|5\.584|dois salarios|art\. 2\b|impugna'))
T('t146', ('Custas no processo de conhecimento (art. 789)', r'art\. 789|dois por cento|2%|custas|quatro vezes|recolhid'),
          ('Isenções (art. 790-A) e Fazenda Pública', r'isen|790-a|uniao|estados|municipios|autarquias|fazenda|ministerio publico'),
          ('Justiça gratuita (art. 790, §§ 3º e 4º) e emolumentos', r'justica gratuita|gratuidade|40%|quarenta por cento|insuficiencia|emolumento|art\. 789-b|art\. 790'))
T('t147', ('Capacidade postulatória e jus postulandi (art. 791; Súmula 425)', r'jus postulandi|art\. 791|sumula 425|pessoalmente|reclamar pessoalmente|capacidade'),
          ('Partes, representação e procuração (mandato tácito, preposto)', r'parte|representa|procura|mandato tacito|apud acta|preposto|sindicato|menor|substitui'))
T('t148', ('Assistência judiciária gratuita (Lei 5.584; sindicato)', r'assistencia judiciaria|5\.584|sindicato|gratuit'),
          ('Honorários de sucumbência (art. 791-A)', r'791-a|sucumbenc|cinco a quinze|5% a 15%|reciproca'),
          ('Honorários contratados e periciais', r'contratad|periciais|790-b|honorarios'))
T('t149', ('Conflitos de competência: conceito e quem julga (arts. 803 a 811)', r'conflito|art\. 80[3-9]|art\. 81[01]|suscit|competencia|jurisdicao'))
T('t150', ('Audiência: local, horário, presença das partes (arts. 813 a 817)', r'art\. 81[3-7]|audiencia|horario|oito e dezoito|cinco horas|quinze minutos|atraso'),
          ('Conciliação obrigatória (arts. 846 e 850)', r'concilia|art\. 846|art\. 850|proposta|acordo'),
          ('Instrução e julgamento (arts. 847 a 852)', r'instrucao|defesa|vinte minutos|razoes finais|art\. 84[7-9]|art\. 85[0-2]|julgamento'))
T('t151', ('Notificação das partes (art. 841)', r'notifica|art\. 841|cinco dias|edital|registrado'),
          ('Arquivamento e ausência do reclamante (art. 844)', r'arquivamento|arquiv|ausencia do reclamante|perempcao|custas'),
          ('Revelia e confissão ficta', r'revel|confissao|ficta|preposto|sumula 74|sumula 122'))
T('t152', ('Ônus da prova (art. 818)', r'onus|art\. 818|distribuicao dinamica|inversao'),
          ('Prova testemunhal (art. 821 e ss.)', r'testemunh|tres testemunhas|seis|contradita|art\. 82[1-9]'),
          ('Prova documental, pericial e depoimento pessoal', r'documento|documental|pericia|pericial|depoimento|interrogat|confissao'))
T('t153', ('Reclamação escrita e verbal (art. 840)', r'escrita|verbal|art\. 840|reduzida a termo|art\. 731|art\. 786|pedido certo'),
          ('Requisitos da petição inicial e notificação', r'requisitos|pedido certo|determinado|valor|indicac|notifica'),
          ('Legitimidade para ajuizar (art. 839) e substituição processual', r'legitim|art\. 839|substitui|sindicato|ministerio publico|empregados e empregadores'))
T('t154', ('Procedimento sumaríssimo (arts. 852-A a 852-I)', r'sumarissim|852-|quarenta salarios|duas testemunhas|quinze dias'),
          ('Procedimento ordinário e sumário (Lei 5.584)', r'ordinari|sumario|5\.584|alcada|dois salarios'))
T('t155', ('IDPJ no processo do trabalho (art. 855-A; CPC arts. 133 a 137)', r'desconsidera|855-a|incidente|personalidade juridica|133|137|socio'))
T('t156', ('Sentença: requisitos e publicação (arts. 831 a 832)', r'sentenca|art\. 83[1-2]|requisitos|fundamenta|dispositivo|relatorio|publica'),
          ('Coisa julgada e termo de conciliação (art. 831, parágrafo único)', r'coisa julgada|irrecorriv|termo de conciliacao|ação rescisoria|acao rescisoria|transito'),
          ('Embargos de declaração (art. 897-A)', r'embargos de declaracao|897-a|omissao|contradicao|obscuridade|erro material'))
T('t157', ('Homologação de acordo extrajudicial (arts. 855-B a 855-E)', r'855-[b-e]|extrajudicial|peticao conjunta|advogados distintos|quinze dias|homologa'))
T('t158', ('Liquidação por cálculos, arbitramento e artigos (art. 879)', r'liquida|art\. 879|calculo|arbitramento|artigos|procedimento comum'),
          ('Impugnação aos cálculos e atualização', r'impugna|oito dias|prazo comum|atualiza|correcao'))
T('t159', ('Execução provisória', r'provisori|art\. 899|ate a penhora'),
          ('Execução definitiva e títulos executivos (art. 876)', r'definitiv|titulo|art\. 876|termo de ajuste|tac|ccp|art\. 877|de oficio|art\. 878'))
T('t160', ('Execução por prestações sucessivas (arts. 890 a 892)', r'prestacoes sucessivas|art\. 89[0-2]|tempo determinado|tempo indeterminado'),
          ('Execução contra a Fazenda Pública (precatório, RPV)', r'fazenda|precatori|rpv|requisicao de pequeno valor|art\. 100|art\. 910|art\. 535'),
          ('Execução contra a massa falida e empresa em recuperação', r'massa falida|falencia|recuperacao judicial|juizo universal|11\.101|art\. 6\b'))
T('t161', ('Citação na execução (art. 880)', r'citac|art\. 880|quarenta e oito|48 horas|mandado de citacao'),
          ('Depósito da condenação e nomeação de bens (arts. 880 a 883)', r'deposito|nomea|art\. 88[1-3]|ordem preferencial|art\. 835'))
T('t162', ('Garantia do juízo (depósito, nomeação, penhora)', r'garantia|garantir|art\. 882|art\. 884|juizo'),
          ('Seguro-garantia judicial e fiança bancária', r'seguro-garantia|seguro garantia|fianca bancaria|trinta por cento'))
T('t163', ('Mandado de penhora e avaliação', r'mandado|avaliac|oficial de justica|auto de penhora'),
          ('Penhora: bens penhoráveis e impenhoráveis; ordem', r'penhor|impenhorav|bem de familia|art\. 833|art\. 835|ordem|salario'))
T('t164', ('Embargos à execução (art. 884)', r'embargos a execucao|art\. 884|cinco dias|trinta dias|materia|garantid'),
          ('Impugnação à sentença de liquidação', r'impugnacao|sentenca de liquidacao|exequente'),
          ('Embargos de terceiro (CPC, arts. 674 a 681)', r'terceiro|674|posse|art\. 675'))
T('t165', ('Praça e leilão (art. 888)', r'praca|leilao|leiloeiro|art\. 888|edital|vinte dias'),
          ('Arrematação, lance e adjudicação; remição', r'arremata|lance|sinal|vinte por cento|adjudic|remic|preco vil'),
          ('Custas na execução (art. 789-A)', r'789-a|custas|executado'))
T('t166', ('Recurso ordinário e regras gerais (efeito devolutivo, prazo de 8 dias)', r'recurso ordinario|oito dias|devolutivo|art\. 895|art\. 899|uniformidade'),
          ('Recurso de revista (art. 896; transcendência)', r'recurso de revista|896|transcend|divergencia'),
          ('Agravo de petição e agravo de instrumento (art. 897)', r'agravo de peticao|agravo de instrumento|art\. 897|delimitar'),
          ('Embargos no TST e recurso extraordinário', r'embargos|sdi|894|extraordinari'),
          ('Depósito recursal e preparo', r'deposito recursal|preparo|deserc|art\. 899|metade|isent'))
T('t167', ('PJe e processo eletrônico (Lei 11.419/2006)', r'11\.419|eletronic|pje|assinatura digital|credenciamento|diario eletronico|intimac'),
          ('Prazos e atos no meio eletrônico', r'prazo|vinte e quatro horas|24 horas|indisponibil|dez dias|consulta|ate as 24'))
T('t168', ('Reforma Trabalhista no processo: custas, gratuidade e honorários', r'gratuidade|honorarios|custas|790|791-a'),
          ('Reforma no processo: prazos, prescrição intercorrente, IDPJ, acordo extrajudicial', r'dias uteis|intercorrente|11-a|855-a|855-b|extrajudicial|desconsidera'),
          ('Reforma no processo: litigância de má-fé, ausência, preposto, transcendência', r'ma-fe|793-|preposto|arquivamento|transcend|revelia'))
T('t169', ('Súmulas do TST de processo', r'sumula'),
          ('OJs do TST de processo', r'orientacao jurisprudencial|\boj\b|sdi'))
T('t170', ('IN 39/2016, IN 41/2018 e outras instruções do TST', r'instrucao normativa|\bin 39|\bin 41|\bin\b'))
T('t171', ('Súmulas vinculantes do STF em processo do trabalho', r'sumula vinculante|\bsv\b'))
T('t172', ('Lei 6.858/1980: valores devidos a dependentes ou sucessores', r'6\.858|dependent|sucessor|fgts|pis|alvara|inventario|arrolamento'))
