import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import time

# ==========================================
# IMPOSTAZIONI PAGINA STREAMLIT
# ==========================================
st.set_page_config(
    page_title="Simulatore Esame - Storia Economica",
    page_icon="📜",
    layout="centered"
)

# ==========================================
# BANCA DATI QUESITI
# ==========================================
VF_QUESTIONS = [
    {
        "id": 1,
        "text": "1. La Produttività Totale dei Fattori (TFP) è la differenza tra incremento del reddito e incremento ponderato dei fattori produttivi.",
        "correct": "VERO",
        "explanation": "Corretto [Ref: Domanda 1 banco domande / Appunti Cap 4]. La TFP misura l'aumento dell'efficienza produttiva non spiegato dal semplice aumento quantitativo degli input."
    },
    {
        "id": 2,
        "text": "2. La conoscenza tecnologica è un bene rivale.",
        "correct": "FALSO",
        "explanation": "Falso [Ref: Domanda 23 banco domande / Appunti Cap 1]. La conoscenza è un bene non rivale in quanto l'uso da parte di un individuo non ne riduce la disponibilità per altri."
    },
    {
        "id": 3,
        "text": "3. Ester Boserup ha sostenuto che il vincolo della scarsità di terra sia stato uno stimolo fondamentale alle innovazioni tecnologiche agricole.",
        "correct": "VERO",
        "explanation": "Corretto [Ref: Domanda 12 banco domande / Appunti Cap 4]. La pressione demografica e la scarsità inducono l'adozione di tecniche più intensive."
    },
    {
        "id": 4,
        "text": "4. La servitù della gleba è un esempio di istituzione efficiente e duratura.",
        "correct": "FALSO",
        "explanation": "Falso [Ref: Domanda 15 banco domande / Appunti Cap 5]. È un'istituzione inefficiente che è persistita principalmente per tutelare gli interessi dei proprietari terrieri."
    },
    {
        "id": 5,
        "text": "5. La moneta segno (fiduciaria) è una moneta priva di valore intrinseco.",
        "correct": "VERO",
        "explanation": "Corretto [Ref: Domanda 32 banco domande / Appunti Cap 7]. Il suo valore si basa sulla fiducia e sulle disposizioni dell'autorità emittente."
    },
    {
        "id": 6,
        "text": "6. L'Inghilterra è storicamente caratterizzata da un sistema finanziario del tipo 'transaction banking' (market-oriented).",
        "correct": "VERO",
        "explanation": "Corretto [Ref: Domanda 34 banco domande / Appunti Cap 7]. Il modello inglese si è sviluppato attorno ai mercati dei capitali e all'autofinanziamento."
    },
    {
        "id": 7,
        "text": "7. Il livello di istruzione delle donne è un valido previsore della riduzione dei tassi di fertilità.",
        "correct": "VERO",
        "explanation": "Corretto [Ref: Domanda 11 banco domande / Appunti Cap 4]. L'aumento dell'istruzione femminile incrementa il costo opportunità del tempo e sposta l'investimento sulla qualità dei figli."
    },
    {
        "id": 8,
        "text": "8. La spinning jenny e il telaio meccanico sono classici esempi di 'General Purpose Technology'.",
        "correct": "FALSO",
        "explanation": "Falso [Ref: Domande 27-28 banco domande]. L'energia elettrica e la macchina a vapore sono GPT, mentre la spinning jenny è una tecnologia settoriale."
    },
    {
        "id": 9,
        "text": "9. In età preindustriale le crisi di mortalità (peste, carestie) avevano effetti demografici ed economici permanenti e irreversibili.",
        "correct": "FALSO",
        "explanation": "Falso [Ref: Domanda 45 banco domande / Appunti Cap 3-4]. I dati mostrano che le crisi di mortalità avevano effetti solo transitori, seguiti da una rapida ripresa demografica."
    },
    {
        "id": 10,
        "text": "10. La Banca d'Inghilterra venne fondata sul finire del XVII secolo (1694).",
        "correct": "VERO",
        "explanation": "Corretto [Ref: Domanda 42 banco domande / Appunti Cap 7]. Rappresentò un pilastro decisivo per la stabilizzazione del debito e dello sviluppo finanziario britannico."
    }
]

MC_QUESTIONS = [
    {
        "id": 1,
        "question": "1. In presenza di bassa domanda aggregata e bassa densità di popolazione, quali tecnologie tendono a prevalere?",
        "options": [
            "A) Tecnologie con alti costi fissi e bassi costi variabili",
            "B) Tecnologie con bassi costi fissi e alti costi variabili (es. lavoro umano)",
            "C) Tecnologie con alti costi fissi e alti costi variabili",
            "D) Esclusivamente tecnologie General Purpose"
        ],
        "correct": 1,  # Indice opzione B
        "explanation": "Corretto B [Ref: Domanda 3 banco domande / Appunti Cap 3]. Sotto una certa soglia di domanda dominano tecniche a basso costo fisso."
    },
    {
        "id": 2,
        "question": "2. L'effetto frontiera ('border effect') nel commercio internazionale è associato a:",
        "options": [
            "A) Un abbattimento generale dei dazi doganali",
            "B) Un aumento significativo dei costi di transazione al variare dei confini",
            "C) La scomparsa della legge del prezzo unico",
            "D) La riduzione dell'elasticità della domanda"
        ],
        "correct": 1,
        "explanation": "Corretto B [Ref: Domande 7-8 banco domande]. L'effetto frontiera comporta uno spostamento verso l'alto nella curva dei costi del commercio."
    },
    {
        "id": 3,
        "question": "3. Nel corso dei secoli XVI-XVIII la leadership economica europea si spostò:",
        "options": [
            "A) Da Italia e Spagna a Paesi Bassi e Francia",
            "B) Da Italia e Spagna a Paesi Bassi e Inghilterra",
            "C) Da Inghilterra e Olanda all'area Mediterranea",
            "D) Dalla Germania alla Russia imperiale"
        ],
        "correct": 1,
        "explanation": "Corretto B [Ref: Domanda 18 banco domande / Appunti Cap 3]. La cosiddetta 'piccola divergenza' sposta il baricentro dal Mediterraneo al Mare del Nord."
    },
    {
        "id": 4,
        "question": "4. Nel corso dell'Ottocento, la principale caratteristica distintiva delle Banche Universali (miste) tedesche era:",
        "options": [
            "A) Operare esclusivamente sul credito a brevissimo termine",
            "B) Concedere finanziamenti di lungo periodo ed essere presenti negli organi delle imprese",
            "C) Evitare qualsiasi tipo di raccolta di depositi dal pubblico",
            "D) Emettere direttamente moneta legale esente da riserva"
        ],
        "correct": 1,
        "explanation": "Corretto B [Ref: Domanda 35, 44 banco domande / Appunti Cap 7]. La banca universale (es. Deutsche Bank) ha sostenuto l'industria capital-intensive tedesca."
    },
    {
        "id": 5,
        "question": "5. Secondo la teoria economica del vantaggio comparato di David Ricardo, il commercio tra nazioni dipende da:",
        "options": [
            "A) Differenze nella dotazione monetaria e riserve auree",
            "B) Differenze nella produttività relativa del lavoro tra i paesi",
            "C) Applicazione di dazi doganali protezionistici",
            "D) Perfetta eguaglianza dei tassi di cambio"
        ],
        "correct": 1,
        "explanation": "Corretto B [Ref: Domanda 26, 62, 84 banco domande / Appunti Cap 6-8]. Ricardo dimostra che il vantaggio comparato scaturisce dai divari di produttività del lavoro."
    }
]

TEXT_DROPDOWN_QUESTIONS = [
    {
        "id": 1,
        "title": "Testo 1: Omogeneità e Istituzioni Europee",
        "template_parts": [
            "La formazione dell'Europa è stata un lungo percorso storico. L'aspetto più sorprendente è dato dalla ",
            " sul piano geo-economico. Il grande paradosso sta nel fatto che, nonostante le forze distruttive, il continente è rimasto omogeneo sul piano culturale e ",
            " per via di potenti forze coesive. La più potente tra queste è l'interazione ",
            "."
        ],
        "dropdowns": [
            {"var_name": "t1_d1", "options": ["PERSISTENZA", "discontinuità", "frammentazione"], "correct": "PERSISTENZA"},
            {"var_name": "t1_d2", "options": ["ISTITUZIONALE", "militare", "linguistico"], "correct": "ISTITUZIONALE"},
            {"var_name": "t1_d3", "options": ["COMMERCIALE", "militare", "religiosa"], "correct": "COMMERCIALE"}
        ],
        "explanation": "Ref: Domanda 10 banco domande. L'Europa ha mantenuto omogeneità istituzionale e culturale grazie all'intensità degli scambi commerciali."
    },
    {
        "id": 2,
        "title": "Testo 2: Strumenti di Pagamento Storici",
        "template_parts": [
            "Prima della diffusione della moneta cartacea, gli scambi internazionali e interregionali si realizzavano soprattutto attraverso le ",
            ". Il loro sviluppo fu avviato dai mercanti banchieri ",
            " e costitutivo essenzialmente promesse del ",
            " di corrispondere la somma dovuta al creditore in un determinato momento futuro."
        ],
        "dropdowns": [
            {"var_name": "t2_d1", "options": ["LETTERE DI CAMBIO", "obbligazioni di stato", "monete fiat"], "correct": "LETTERE DI CAMBIO"},
            {"var_name": "t2_d2", "options": ["ITALIANI", "inglesi", "fiamminghi"], "correct": "ITALIANI"},
            {"var_name": "t2_d3", "options": ["DEBITORE", "sovrano", "banchiere centrale"], "correct": "DEBITORE"}
        ],
        "explanation": "Ref: Domanda 62 banco domande / Appunti Cap 7. Le lettere di cambio permisero di superare il rischio del trasporto di moneta metallica."
    },
    {
        "id": 3,
        "title": "Testo 3: Urbanizzazione e Consumi (Legge di Engel)",
        "template_parts": [
            "I residenti nei centri urbani sono attivi nella produzione non alimentare. Quando l'urbanizzazione cresce, aumenta la domanda di beni non di prima necessità perché l'elasticità al reddito della domanda di beni alimentari è ",
            " rispetto a quella dei beni non alimentari. Questa regolarità empirica è nota come ",
            " e dimostra che all'aumentare del reddito la quota destinata al cibo ",
            "."
        ],
        "dropdowns": [
            {"var_name": "t3_d1", "options": ["INFERIORE", "superiore", "pari"], "correct": "INFERIORE"},
            {"var_name": "t3_d2", "options": ["LEGGE DI ENGEL", "trappola malthusiana", "legge di Gresham"], "correct": "LEGGE DI ENGEL"},
            {"var_name": "t3_d3", "options": ["DIMINUISCE", "aumenta", "resta invariata"], "correct": "DIMINUISCE"}
        ],
        "explanation": "Ref: Domanda 76 banco domande / Appunti Cap 3. La legge di Engel stabilisce che la percentuale di reddito spesa in cibo cala al crescere della ricchezza."
    }
]

GRAPH_QUESTIONS = [
    {
        "id": 1,
        "title": "Grafico 1: Convergenza Beta in Europa (1950-1975)",
        "graph_type": "beta_convergence",
        "questions": [
            {
                "sub_id": "g1_q1",
                "text": "1.1 Il grafico mostra una relazione negativa tra il livello di reddito iniziale (1950) e il tasso di crescita del PIL pro capite.",
                "correct": "VERO",
                "explanation": "VERO [Ref: Domanda 78 banco domande]. La pendenza negativa della retta indica che i paesi più poveri nel 1950 sono cresciuti più rapidamente."
            },
            {
                "sub_id": "g1_q2",
                "text": "1.2 Il grafico dimostra che il Regno Unito (GB) è cresciuto a tassi superiori rispetto ad economie inizialmente più povere come Grecia (GR) e Spagna (ES).",
                "correct": "FALSO",
                "explanation": "FALSO [Ref: Domanda 78 banco domande]. Il Regno Unito figura nella parte inferiore destra (bassa crescita, alto reddito iniziale)."
            },
            {
                "sub_id": "g1_q3",
                "text": "1.3 Il grafico conferma empiricamente il verificarsi della convergenza beta tra i paesi europei nel periodo 1950-1975.",
                "correct": "VERO",
                "explanation": "VERO [Ref: Domanda 78 banco domande / Appunti Cap 6]. La convergenza beta è la condizione necessaria per l'agganciamento (catch-up)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Grafico 2: Il Trilemma delle Economie Aperte (Mundell-Fleming)",
        "graph_type": "trilemma",
        "questions": [
            {
                "sub_id": "g2_q1",
                "text": "2.1 Il regime di Gold Standard (1870-1914) combinava tassi di cambio fissi e libera circolazione dei capitali, rinunciando all'autonomia monetaria.",
                "correct": "VERO",
                "explanation": "VERO [Ref: Domande 58, 95, 100 banco domande]. Nel Gold Standard le autorità non potevano condurre politiche monetarie autonome."
            },
            {
                "sub_id": "g2_q2",
                "text": "2.2 Il sistema di Bretton Woods (1945-1973) manteneva tassi di cambio fissi ed autonomia monetaria, richiedendo vincoli alla mobilità dei capitali.",
                "correct": "VERO",
                "explanation": "VERO [Ref: Domande 33, 34, 100 banco domande]. Il trilemma imponeva restrizioni sui capitali per preservare la parità col dollaro e l'autonomia."
            },
            {
                "sub_id": "g2_q3",
                "text": "2.3 Nel sistema monetario attuale (post-1973), i paesi mantengono tassi di cambio fissi con libera mobilità dei capitali ed autonomia monetaria simultanea.",
                "correct": "FALSO",
                "explanation": "FALSO [Ref: Domande 32, 96, 100 banco domande]. Impossibile per il trilemma: il sistema attuale adotta tassi FLESSIBILI per avere mobilità di capitali e autonomia."
            }
        ]
    }
]

# ==========================================
# GENERATORE GRAFICI MATPLOTLIB
# ==========================================
def generate_matplotlib_figure(graph_type):
    fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=100)

    if graph_type == "beta_convergence":
        x = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
        y = np.array([5.2, 4.8, 4.5, 4.1, 3.8, 3.4, 3.1, 2.7, 2.5, 2.1])
        countries = ['GR', 'ES', 'IT', 'AT', 'DE', 'FR', 'NO', 'BE', 'SE', 'GB']

        ax.scatter(x, y, color='#1f4e78', s=45, zorder=3)
        for i, txt in enumerate(countries):
            ax.annotate(txt, (x[i] + 120, y[i] + 0.08), fontsize=8, fontweight='bold')

        m, b = np.polyfit(x, y, 1)
        ax.plot(x, m * x + b, color='#d9534f', linestyle='--', linewidth=2, label='Linea di Regressione (Beta-Convergenza)')

        ax.set_title('Convergenza Beta: Tasso crescita PIL pro capite (1950-75) vs PIL 1950', fontsize=8, fontweight='bold')
        ax.set_xlabel('PIL pro capite iniziale nel 1950 ($)', fontsize=8)
        ax.set_ylabel('Crescita medio annua (%)', fontsize=8)
        ax.grid(True, linestyle=':', alpha=0.5)
        ax.legend(loc='upper right', fontsize=8)

    elif graph_type == "trilemma":
        ax.axis('off')
        circle1 = patches.Circle((0.3, 0.55), 0.22, color='#3498db', alpha=0.4)
        circle2 = patches.Circle((0.7, 0.55), 0.22, color='#e74c3c', alpha=0.4)
        circle3 = patches.Circle((0.5, 0.25), 0.22, color='#2ecc71', alpha=0.4)

        ax.add_patch(circle1)
        ax.add_patch(circle2)
        ax.add_patch(circle3)

        ax.text(0.2, 0.65, 'Tassi di Cambio\nFissi', fontsize=8, fontweight='bold', ha='center')
        ax.text(0.8, 0.65, 'Libera Mobilità\nCapitali', fontsize=8, fontweight='bold', ha='center')
        ax.text(0.5, 0.12, 'Autonomia Monetaria', fontsize=8, fontweight='bold', ha='center')

        ax.text(0.5, 0.66, 'Gold Standard\n(1870-1914)', fontsize=8, fontweight='bold', color='navy', ha='center')
        ax.text(0.33, 0.35, 'Bretton Woods\n(1945-1973)', fontsize=8, fontweight='bold', color='darkred', ha='center')
        ax.text(0.67, 0.35, 'Sistema Attuale\n(Post-1973)', fontsize=8, fontweight='bold', color='darkgreen', ha='center')

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.85)
        ax.set_title('Il Trilemma delle Economie Aperte nei Regimi Monetari Storici', fontsize=8, fontweight='bold')

    fig.tight_layout()
    return fig


# ==========================================
# GESTIONE STATO DI SESSIONE
# ==========================================
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

if 'vf_answers' not in st.session_state:
    st.session_state.vf_answers = {}
if 'mc_answers' not in st.session_state:
    st.session_state.mc_answers = {}
if 'drop_answers' not in st.session_state:
    st.session_state.drop_answers = {}
if 'graph_answers' not in st.session_state:
    st.session_state.graph_answers = {}


def start_exam():
    st.session_state.page = 'exam'
    st.session_state.start_time = time.time()
    st.session_state.vf_answers = {}
    st.session_state.mc_answers = {}
    st.session_state.drop_answers = {}
    st.session_state.graph_answers = {}


def submit_exam():
    st.session_state.page = 'results'


# ==========================================
# INTERFACCIA STREAMLIT
# ==========================================

# --- SCHERMATA HOME ---
if st.session_state.page == 'home':
    st.title("📜 Prova d'Esame: Storia Economica")
    st.subheader("Simulatore Ufficiale Banco Domande & Appunti Lezione")

    st.markdown("""
    **Struttura della Prova:**
    - **Durata:** 30 Minuti *(timer integrato)*
    - **Sezione 1:** 10 Domande Vero / Falso *(1 punto ciascuna)*
    - **Sezione 2:** 5 Domande a Risposta Multipla *(2 punti ciascuna)*
    - **Sezione 3:** 3 Testi da completare con menu a tendina *(1 punto a spazio - 9 punti tot)*
    - **Sezione 4:** 2 Grafici con 3 quesiti V/F ciascuno *(1 punto a risposta - 6 punti tot)*
    
    **Punteggio Massimo:** 35 Punti
    """)

    if st.button("▶ AVVIA SIMULAZIONE ESAME (30 MINUTI)", type="primary"):
        start_exam()
        st.rerun()


# --- SCHERMATA ESAME ---
elif st.session_state.page == 'exam':

    # Timer display
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, 30 * 60 - elapsed)

    if remaining == 0:
        st.error("⏱ Tempo scaduto! La prova verrà inviata automaticamente per il calcolo del punteggio.")
        time.sleep(2)
        submit_exam()
        st.rerun()

    m, s = divmod(int(remaining), 60)
    st.info(f"⏱ **Tempo Rimanente:** {m:02d}:{s:02d}")

    # TAB DELLE SEZIONI
    tab1, tab2, tab3, tab4 = st.tabs([
        "1. Vero / Falso (10)",
        "2. Risposta Multipla (5)",
        "3. Testi a Tendina (3)",
        "4. Analisi Grafici (2)"
    ])

    # SEZIONE 1: VERO / FALSO
    with tab1:
        st.markdown("### Sezione 1: Vero / Falso")
        st.caption("Rispondi VERO o FALSO a ciascuna delle 10 domande.")

        for q in VF_QUESTIONS:
            st.markdown(f"**{q['text']}**")
            current_ans = st.session_state.vf_answers.get(q['id'])
            idx = ["VERO", "FALSO"].index(current_ans) if current_ans in ["VERO", "FALSO"] else None

            ans = st.radio(
                "La tua risposta:",
                ["VERO", "FALSO"],
                index=idx,
                key=f"vf_{q['id']}"
            )
            st.session_state.vf_answers[q['id']] = ans
            st.divider()

    # SEZIONE 2: RISPOSTA MULTIPLA
    with tab2:
        st.markdown("### Sezione 2: Risposta Multipla")
        st.caption("Seleziona l'unica opzione corretta per ciascuno dei 5 quesiti.")

        for q in MC_QUESTIONS:
            st.markdown(f"**{q['question']}**")
            current_ans = st.session_state.mc_answers.get(q['id'])

            ans = st.radio(
                "Seleziona un'opzione:",
                q['options'],
                index=current_ans if current_ans is not None else None,
                key=f"mc_{q['id']}"
            )
            if ans:
                st.session_state.mc_answers[q['id']] = q['options'].index(ans)
            st.divider()

    # SEZIONE 3: TESTI A TENDINA
    with tab3:
        st.markdown("### Sezione 3: Testi da Completare")
        st.caption("Seleziona il termine corretto dai menu a tendina per completare i 3 brani.")

        for t_item in TEXT_DROPDOWN_QUESTIONS:
            st.markdown(f"#### {t_item['title']}")
            parts = t_item['template_parts']
            dropdowns = t_item['dropdowns']

            # Costruzione dinamica testo + tendine
            for i in range(len(parts)):
                st.write(parts[i])
                if i < len(dropdowns):
                    d_info = dropdowns[i]
                    var_name = d_info['var_name']
                    curr_val = st.session_state.drop_answers.get(var_name, "-- Scegli --")

                    opts = ["-- Scegli --"] + d_info['options']
                    idx = opts.index(curr_val) if curr_val in opts else 0

                    sel = st.selectbox(
                        f"Spazio vuoto [{i+1}]:",
                        opts,
                        index=idx,
                        key=f"drop_{var_name}"
                    )
                    st.session_state.drop_answers[var_name] = sel

            st.divider()

    # SEZIONE 4: GRAFICI
    with tab4:
        st.markdown("### Sezione 4: Analisi dei Grafici")
        st.caption("Osserva i grafici e rispondi VERO o FALSO ai 3 quesiti associati ciascuno.")

        for g_item in GRAPH_QUESTIONS:
            st.markdown(f"#### {g_item['title']}")

            # Render figura Matplotlib
            fig = generate_matplotlib_figure(g_item['graph_type'])
            st.pyplot(fig)
            plt.close(fig)

            for sub_q in g_item['questions']:
                st.markdown(f"**{sub_q['text']}**")
                current_ans = st.session_state.graph_answers.get(sub_q['sub_id'])
                idx = ["VERO", "FALSO"].index(current_ans) if current_ans in ["VERO", "FALSO"] else None

                ans = st.radio(
                    "Risposta:",
                    ["VERO", "FALSO"],
                    index=idx,
                    key=f"g_{sub_q['sub_id']}"
                )
                st.session_state.graph_answers[sub_q['sub_id']] = ans

            st.divider()

    # BOTTONE CONSEGNA
    if st.button("✓ INVIA ESAME E CALCOLA PUNTEGGIO", type="primary"):
        submit_exam()
        st.rerun()


# --- SCHERMATA RISULTATI ---
elif st.session_state.page == 'results':
    st.title("🏆 Esito Finale e Report Esame")

    # Calcolo punteggi
    score_vf = 0
    score_mc = 0
    score_drop = 0
    score_graph = 0

    # 1. Check V/F
    for q in VF_QUESTIONS:
        if st.session_state.vf_answers.get(q['id']) == q['correct']:
            score_vf += 1

    # 2. Check MC
    for q in MC_QUESTIONS:
        if st.session_state.mc_answers.get(q['id']) == q['correct']:
            score_mc += 2

    # 3. Check Dropdowns
    for t_item in TEXT_DROPDOWN_QUESTIONS:
        for d in t_item['dropdowns']:
            if st.session_state.drop_answers.get(d['var_name']) == d['correct']:
                score_drop += 1

    # 4. Check Graphs
    for g_item in GRAPH_QUESTIONS:
        for sub_q in g_item['questions']:
            if st.session_state.graph_answers.get(sub_q['sub_id']) == sub_q['correct']:
                score_graph += 1

    total_score = score_vf + score_mc + score_drop + score_graph
    max_score = 35

    if total_score >= 21:
        st.success(f"🎉 **ESAME SUPERATO!** Punteggio Totale: **{total_score} / {max_score}**")
    else:
        st.error(f"❌ **ESAME NON SUPERATO.** Punteggio Totale: **{total_score} / {max_score}** (Soglia minima: 21/35)")

    st.markdown(f"""
    **Dettaglio Punteggi:**
    - Vero / Falso: **{score_vf} / 10**
    - Risposta Multipla: **{score_mc} / 10**
    - Testi a Tendina: **{score_drop} / 9**
    - Analisi Grafici: **{score_graph} / 6**
    """)

    st.divider()
    st.subheader("📋 Correzione Dettagliata per Sezione")

    # REPORT V/F
    with st.expander("Sezione 1: Vero / Falso"):
        for q in VF_QUESTIONS:
            ans = st.session_state.vf_answers.get(q['id'], 'Non data')
            icon = "✅" if ans == q['correct'] else "❌"
            st.markdown(f"{icon} **Q{q['id']}:** {q['text']}")
            st.write(f"- Tua risposta: **{ans}** | Risposta corretta: **{q['correct']}**")
            st.info(f"💡 Spiegazione: {q['explanation']}")
            st.divider()

    # REPORT MC
    with st.expander("Sezione 2: Risposta Multipla"):
        for q in MC_QUESTIONS:
            ans_idx = st.session_state.mc_answers.get(q['id'])
            ans_str = q['options'][ans_idx] if ans_idx is not None else "Non data"
            corr_str = q['options'][q['correct']]
            icon = "✅" if ans_idx == q['correct'] else "❌"

            st.markdown(f"{icon} **Q{q['id']}:** {q['question']}")
            st.write(f"- Tua risposta: **{ans_str}**")
            st.write(f"- Risposta corretta: **{corr_str}**")
            st.info(f"💡 Spiegazione: {q['explanation']}")
            st.divider()

    # REPORT TENDINE
    with st.expander("Sezione 3: Testi a Tendina"):
        for t_item in TEXT_DROPDOWN_QUESTIONS:
            st.markdown(f"#### {t_item['title']}")
            for d in t_item['dropdowns']:
                ans = st.session_state.drop_answers.get(d['var_name'], 'Non data')
                icon = "✅" if ans == d['correct'] else "❌"
                st.write(f"{icon} Spazio `[{d['var_name']}]` -> Tua risposta: **{ans}** | Corretta: **{d['correct']}**")
            st.info(f"💡 Spiegazione: {t_item['explanation']}")
            st.divider()

    # REPORT GRAFICI
    with st.expander("Sezione 4: Analisi Grafici"):
        for g_item in GRAPH_QUESTIONS:
            st.markdown(f"#### {g_item['title']}")
            for sub_q in g_item['questions']:
                ans = st.session_state.graph_answers.get(sub_q['sub_id'], 'Non data')
                icon = "✅" if ans == sub_q['correct'] else "❌"
                st.markdown(f"{icon} **Q{sub_q['sub_id']}:** {sub_q['text']}")
                st.write(f"- Tua risposta: **{ans}** | Corretta: **{sub_q['correct']}**")
                st.info(f"💡 Spiegazione: {sub_q['explanation']}")
            st.divider()

    if st.button("🔄 TORNA ALLA HOME E RIPROVA"):
        st.session_state.page = 'home'
        st.rerun()
