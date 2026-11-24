# Mapa de cobertura do banco de questões por tópico, subitem e nível (fácil, média, difícil).
# Uso: python3 ferramentas/cobertura.py "<lote e data>"  (rodar na raiz do repositório)
# Saídas: questoes/COBERTURA.md, questoes/cobertura.json e ferramentas/cobertura.xlsx (base da planilha
# "EDITAL TRT — Cobertura do app" no Google Drive).
# A classificação por subitem é automática: procura palavras-chave (ferramentas/subitens.py) no enunciado, na alternativa
# certa e na base legal de cada questão do tópico. Pode errar para mais ou para menos; serve de controle, não de prova.
import json, sys, re, collections, os
sys.path.insert(0, os.path.dirname(__file__))
from subitens import S, norm

R = 'questoes/'
NIV = {1: 'Fácil', 2: 'Média', 3: 'Difícil'}
TWIN = {'t074': ['t084'], 't075': ['t085'], 't076': ['t086'], 't077': ['t087'], 't078': ['t088'], 't079': ['t089', 't091']}
# linha da aba "Edital verticalizado" da planilha EDITAL TRT que corresponde a cada tópico do app
def linha(t):
    n = int(t[1:])
    esp = {'t015': '19 e 20', 't016': '21', 't017': '21', 't065': '69 e 70', 't066': '71 e 72', 't067': '73', 't068': '74',
           't069': '75', 't070': '75', 't071': '75', 't090': '—', 't091': '94', 't092': '95', 't093': '96', 't094': '97',
           't095': '98', 't096': '99 e 100'}
    return esp.get(t, str(n + 4))

def carregar():
    Q = []
    for f in json.load(open(R + 'bancos/index.json'))['arquivos']:
        for q in json.load(open(R + 'bancos/' + f)):
            Q.append(q)
    return Q

def texto(q):
    a = q.get('a', [])
    ok = a[q['g']] if len(a) > 2 else ''
    b = re.split(r'Texto conferido|A parte doutrin', q.get('b', '') or '')[0]
    return norm(' '.join([q.get('e', ''), ok, b]))

def main(rotulo):
    E = json.load(open(R + 'edital.json'))
    Q = carregar()
    por_t = collections.defaultdict(list)
    for q in Q: por_t[q['t']].append(q)
    sub_hits = {}
    sem_sub = 0
    for t in [e['id'] for e in E]:
        for q in por_t[t]:
            tx = texto(q); achou = False
            for k, (lab, rx) in enumerate(S[t]):
                if rx.search(tx):
                    sub_hits.setdefault((t, k), []).append(q); achou = True
            if not achou: sem_sub += 1
    topicos, subitens = [], []
    for e in E:
        t = e['id']; qs = por_t[t]
        niv = collections.Counter(q['n'] for q in qs)
        gem = TWIN.get(t, [])
        qs_gem = [q for g in gem for q in por_t[g]]
        subs = []
        for k, (lab, _) in enumerate(S[t]):
            own = sub_hits.get((t, k), [])
            via = [q for g in gem for kk, (lab2, _) in enumerate(S[g]) if lab2 == lab for q in sub_hits.get((g, kk), [])]
            if own: sit = 'Com questão'
            elif via: sit = 'Via tópico gêmeo'
            else: sit = 'Sem questão'
            nv = collections.Counter(q['n'] for q in own)
            subs.append(dict(t=t, m=e['m'], a=e['a'], s=e['s'], sub=lab, n=len(own), f=nv[1], md=nv[2], d=nv[3],
                             sit=sit, ex=', '.join(q['id'] for q in (own or via)[:3])))
        faltam_niv = [NIV[n] for n in (1, 2, 3) if not niv[n]]
        sem = [s['sub'] for s in subs if s['sit'] == 'Sem questão']
        if faltam_niv or sem:
            sit = 'Incompleto'
        else:
            sit = 'Completo'
        obs = ''
        if gem: obs = 'Lei 8.112 em Dir. Administrativo; o app também mostra as questões de ' + ' e '.join(gem) + ' (Legislação).'
        topicos.append(dict(t=t, linha=linha(t), m=e['m'], a=e['a'], s=e['s'], n=len(qs), f=niv[1], md=niv[2], d=niv[3],
                            nsub=len(subs), csub=len(subs) - len(sem), faltam_niv=', '.join(faltam_niv) or '—',
                            sem_sub='; '.join(sem) or '—', sit=sit, obs=obs, gem=len(qs_gem)))
        subitens.extend(subs)
    resumo = collections.OrderedDict()
    for tp in topicos:
        r = resumo.setdefault(tp['m'], dict(top=0, q=0, f=0, md=0, d=0, comp=0, nsub=0, csub=0))
        r['top'] += 1; r['q'] += tp['n']; r['f'] += tp['f']; r['md'] += tp['md']; r['d'] += tp['d']
        r['comp'] += tp['sit'] == 'Completo'; r['nsub'] += tp['nsub']; r['csub'] += tp['csub']
    json.dump(dict(rotulo=rotulo, total=len(Q), sem_subitem=sem_sub, resumo=resumo, topicos=topicos, subitens=subitens),
              open(R + 'cobertura.json', 'w', encoding='utf8'), ensure_ascii=False, indent=0)
    escrever_md(rotulo, Q, sem_sub, resumo, topicos, subitens)
    escrever_xlsx(rotulo, len(Q), sem_sub, resumo, topicos, subitens)
    tot_sub = sum(r['nsub'] for r in resumo.values()); cob = sum(r['csub'] for r in resumo.values())
    print(len(Q), 'questões;', sum(tp['sit'] == 'Completo' for tp in topicos), 'de', len(topicos), 'tópicos completos;',
          cob, 'de', tot_sub, 'subitens com questão (próprias);', sem_sub, 'questões sem subitem identificado')

def escrever_md(rotulo, Q, sem_sub, resumo, topicos, subitens):
    L = []
    L.append('# Mapa de cobertura do banco de questões (Anexo II do Edital 01/2022, TRT3)\n')
    L.append(f'Gerado em {rotulo} por `ferramentas/cobertura.py`, a partir de `edital.json` (172 tópicos), de `ferramentas/subitens.py` '
             f'(divisão de cada tópico em {len(subitens)} subitens, pelos institutos que o Anexo II lista) e de `bancos/*.json` ({len(Q)} questões). '
             'A planilha **EDITAL TRT — Cobertura do app**, no Google Drive (pasta TRT MG), traz os mesmos números.\n')
    L.append('**Como ler.** Um tópico está *completo* quando tem questões dos três níveis (fácil, média e difícil) e todos os seus subitens têm '
             'pelo menos uma questão. A ligação entre questão e subitem é automática, por palavras-chave no enunciado, na alternativa certa e na '
             f'base legal; ela pode errar, e {sem_sub} questões não casaram com nenhum subitem (contam no tópico, não no subitem). '
             'Os níveis seguem o critério: **fácil** = um fato direto da lei ou da definição; **média** = aplicar a regra a um caso ou distinguir '
             'conceitos próximos; **difícil** = combinar regras, exceções e números, ou três afirmativas que exigem domínio do tópico inteiro.\n')
    L.append('## Resumo por matéria\n')
    L.append('| Matéria | Tópicos | Completos | Questões | Fáceis | Médias | Difíceis | Subitens com questão |')
    L.append('|---|---:|---:|---:|---:|---:|---:|---:|')
    for m, r in resumo.items():
        L.append(f"| {m} | {r['top']} | {r['comp']} | {r['q']} | {r['f']} | {r['md']} | {r['d']} | {r['csub']} de {r['nsub']} |")
    T = {k: sum(r[k] for r in resumo.values()) for k in ('top', 'comp', 'q', 'f', 'md', 'd', 'csub', 'nsub')}
    L.append(f"| **Total** | **{T['top']}** | **{T['comp']}** | **{T['q']}** | **{T['f']}** | **{T['md']}** | **{T['d']}** | **{T['csub']} de {T['nsub']}** |\n")
    inc = [tp for tp in topicos if tp['sit'] != 'Completo']
    L.append('## O que ainda falta\n')
    if not inc:
        L.append('- Nenhum tópico incompleto: todos têm os três níveis e todos os subitens com pelo menos uma questão.\n')
    for tp in inc:
        L.append(f"- {tp['t']} ({tp['s']}): níveis que faltam: {tp['faltam_niv']}; subitens sem questão: {tp['sem_sub']}.")
    L.append('- Os tópicos t074 a t079 (Lei 8.112 em Direito Administrativo) têm questões próprias desde o lote 7, e o app também mostra as '
             'questões dos tópicos gêmeos de Legislação; subitens marcados como “via tópico gêmeo” só têm questão do lado de Legislação.\n')
    L.append('## Tópico por tópico\n')
    atual = None
    for tp in topicos:
        if tp['m'] != atual:
            atual = tp['m']
            L.append(f'\n### {atual}\n')
            L.append('| Tópico | Assunto | Subtópico | Questões | Fáceis | Médias | Difíceis | Subitens com questão | Situação |')
            L.append('|---|---|---|---:|---:|---:|---:|---:|---|')
        L.append(f"| {tp['t']} | {tp['a']} | {tp['s']} | {tp['n']} | {tp['f']} | {tp['md']} | {tp['d']} | {tp['csub']} de {tp['nsub']} | {tp['sit']} |")
    L.append('\n## Subitens\n')
    atual = None
    for s in subitens:
        if s['m'] != atual:
            atual = s['m']
            L.append(f'\n### {atual}\n')
            L.append('| Tópico | Subitem | Questões | Fáceis | Médias | Difíceis | Situação | Exemplos |')
            L.append('|---|---|---:|---:|---:|---:|---|---|')
        L.append(f"| {s['t']} | {s['sub']} | {s['n']} | {s['f']} | {s['md']} | {s['d']} | {s['sit']} | {s['ex']} |")
    open(R + 'COBERTURA.md', 'w', encoding='utf8').write('\n'.join(L) + '\n')

def escrever_xlsx(rotulo, total, sem_sub, resumo, topicos, subitens):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
    wb = Workbook()
    H = Font(bold=True, color='FFFFFF'); HF = PatternFill('solid', fgColor='1F5C99')
    OK = PatternFill('solid', fgColor='D9EAD3'); NO = PatternFill('solid', fgColor='F4CCCC'); GE = PatternFill('solid', fgColor='FFF2CC')
    def tabela(ws, cab, linhas, larg, sit_col=None):
        ws.append(cab)
        for c in ws[ws.max_row]:
            c.font = H; c.fill = HF; c.alignment = Alignment(wrap_text=True, vertical='center')
        hdr = ws.max_row
        for l in linhas:
            ws.append(l)
            if sit_col is not None:
                v = l[sit_col]
                f = OK if v in ('Completo', 'Com questão') else GE if v == 'Via tópico gêmeo' else NO
                ws.cell(ws.max_row, sit_col + 1).fill = f
        for i, w in enumerate(larg, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        ws.freeze_panes = ws.cell(hdr + 1, 1)
        ws.auto_filter.ref = f"A{hdr}:{get_column_letter(len(cab))}{ws.max_row}"
    ws = wb.active; ws.title = 'Cobertura por tópico'
    ws.append([f'Cobertura do app de questões por tópico do edital (base: Anexo II do Edital 01/2022) — atualizado em {rotulo}'])
    ws['A1'].font = Font(bold=True, size=13)
    ws.append([f'{total} questões no app. “Completo” = questões dos 3 níveis e todos os subitens com pelo menos uma questão. A coluna B indica a linha correspondente na aba “Edital verticalizado” da planilha EDITAL TRT.'])
    ws.append([])
    tabela(ws, ['ID no app', 'Linha na EDITAL TRT', 'Disciplina', 'Assunto', 'Tópico (subtópico do app)', 'Questões no app', 'Fáceis', 'Médias',
                'Difíceis', 'Níveis que faltam', 'Subitens', 'Subitens com questão', 'Subitens sem questão', 'Situação', 'Observação'],
           [[tp['t'], tp['linha'], tp['m'], tp['a'], tp['s'], tp['n'], tp['f'], tp['md'], tp['d'], tp['faltam_niv'], tp['nsub'], tp['csub'],
             tp['sem_sub'], tp['sit'], tp['obs']] for tp in topicos],
           [9, 11, 26, 30, 40, 10, 8, 8, 8, 14, 9, 11, 40, 12, 50], sit_col=13)
    ws2 = wb.create_sheet('Cobertura por subitem')
    ws2.append([f'Subitens de cada tópico (divisão feita pelos institutos que o Anexo II lista) — atualizado em {rotulo}'])
    ws2['A1'].font = Font(bold=True, size=13)
    ws2.append([f'Classificação automática por palavras-chave; {sem_sub} questões não casaram com nenhum subitem e contam só no tópico.'])
    ws2.append([])
    tabela(ws2, ['ID no app', 'Disciplina', 'Tópico', 'Subitem', 'Questões', 'Fáceis', 'Médias', 'Difíceis', 'Situação', 'Exemplos de questões'],
           [[s['t'], s['m'], s['s'], s['sub'], s['n'], s['f'], s['md'], s['d'], s['sit'], s['ex']] for s in subitens],
           [9, 26, 38, 60, 10, 8, 8, 8, 16, 34], sit_col=8)
    ws3 = wb.create_sheet('Resumo e lotes')
    ws3.append([f'Resumo por matéria — {rotulo}']); ws3['A1'].font = Font(bold=True, size=13)
    ws3.append([])
    tabela(ws3, ['Matéria', 'Tópicos', 'Tópicos completos', 'Questões', 'Fáceis', 'Médias', 'Difíceis', 'Subitens', 'Subitens com questão'],
           [[m, r['top'], r['comp'], r['q'], r['f'], r['md'], r['d'], r['nsub'], r['csub']] for m, r in resumo.items()],
           [34, 9, 12, 10, 8, 8, 8, 10, 14])
    ws3.append([])
    for l in LOG:
        ws3.append([l])
    wb.save('ferramentas/cobertura.xlsx')

LOG = [
 'Histórico do controle',
 'Lotes 1 a 6 (até 22/11/2026): 1.254 questões; todos os tópicos com questões próprias, exceto t074 a t079 (usavam as de Legislação).',
 'Lote 7 (24/11/2026): 141 questões escritas para as lacunas: 43 subitens sem questão, níveis que faltavam em 99 tópicos e 18 questões próprias para t074 a t079. Código de Ética do TRT3 atualizado para a Resolução GP 434/2026 (oito questões reescritas).',
 'Critério de nível: fácil = um fato direto da lei ou da definição; média = aplicar a regra a um caso ou distinguir conceitos próximos; difícil = combinar regras, exceções e números, ou três afirmativas que exigem o tópico inteiro.',
 'A cada lote: rodar ferramentas/cobertura.py, escrever primeiro para os tópicos e subitens incompletos e atualizar esta planilha.',
]

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'data não informada')
