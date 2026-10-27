import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import random

# ==========================================
# IMPOSTAZIONI PAGINA STREAMLIT
# ==========================================
st.set_page_config(
    page_title="Simulatore Esame - Storia Economica (Primo Parziale)",
    page_icon="📜",
    layout="centered"
)

# ==========================================
# BANCA DATI QUESITI COMPLETA (Q1 - Q81)
# ==========================================
ALL_VF_QUESTIONS = [
    {"id": 1, "text": "La Produttività Totale dei Fattori (TFP) è la differenza tra incremento del reddito e incremento ponderato dei fattori produttivi.", "correct": "VERO", "explanation": "VERO [Ref: Q1 Primo Parziale]. La TFP misura l'efficienza nell'uso combinato degli input."},
    {"id": 2, "text": "La Produttività Totale dei Fattori è la differenza tra la crescita totale del prodotto e la crescita della forza lavoro.", "correct": "FALSO", "explanation": "FALSO [Ref: Q2 Primo Parziale]. La TFP considera l'insieme ponderato di capitale, terra e lavoro, non solo la forza lavoro."},
    {"id": 6, "text": "Tra le innovazioni che favorirono la crescita europea alla fine del primo millennio troviamo la diffusione del mulino ad acqua.", "correct": "VERO", "explanation": "VERO [Ref: Q6 Primo Parziale]. Il mulino ad acqua rappresentò un fondamentale salto energetico inanimato."},
    {"id": 9, "text": "L'effetto frontiera è generato dalle alte tariffe doganali.", "correct": "FALSO", "explanation": "FALSO [Ref: Q9 Primo Parziale]. L'effetto frontiera è legato principalmente ai costi di transazione e confini istituzionali."},
    {"id": 11, "text": "Il livello di istruzione delle donne è un buon previsore della fertilità.", "correct": "VERO", "explanation": "VERO [Ref: Q11 Primo Parziale]. L'istruzione femminile alza il costo opportunità della prole e ne riduce la fecondità."},
    {"id": 12, "text": "Ester Boserup ha sostenuto che il vincolo della terra è stato uno stimolo alle innovazioni tecnologiche.", "correct": "VERO", "explanation": "VERO [Ref: Q12 Primo Parziale]. La scarsità di risorsa stimola l'adozione di tecniche più intensive (meccanismo boserupiano)."},
    {"id": 15, "text": "La servitù della gleba è un esempio di istituzione efficiente e duratura.", "correct": "FALSO", "explanation": "FALSO [Ref: Q15 Primo Parziale]. È un'istituzione inefficiente ma persista per tutelare gli interessi dei proprietari."},
    {"id": 17, "text": "Nel corso dei secoli XVI-XVIII la leadership economica europea si spostò da Italia e Spagna a Paesi Bassi e Francia.", "correct": "FALSO", "explanation": "FALSO [Ref: Q17 Primo Parziale]. Si spostò da Italia e Spagna a Paesi Bassi e Inghilterra."},
    {"id": 23, "text": "La conoscenza tecnologica è un bene rivale.", "correct": "FALSO", "explanation": "FALSO [Ref: Q23 Primo Parziale]. La conoscenza è un bene NON rivale, l'uso da parte di uno non ne limita la disponibilità per altri."},
    {"id": 25, "text": "La costruzione delle ferrovie fu uno dei motori della rivoluzione industriale nell'Europa continentale del XIX secolo.", "correct": "VERO", "explanation": "VERO [Ref: Q25 Primo Parziale]. Abbatté i costi di trasporto e stimolò l'industria siderurgica."},
    {"id": 27, "text": "La spinning jenny è un esempio di tecnologia general purpose.", "correct": "FALSO", "explanation": "FALSO [Ref: Q27 Primo Parziale]. La spinning jenny è una tecnologia settoriale del tessile, non GPT."},
    {"id": 28, "text": "Il telaio è un esempio di tecnologia general purpose.", "correct": "FALSO", "explanation": "FALSO [Ref: Q28 Primo Parziale]. Come la jenny, è una macchina specifica del settore tessile."},
    {"id": 32, "text": "La moneta segno è una moneta priva di valore intrinseco.", "correct": "VERO", "explanation": "VERO [Ref: Q32 Primo Parziale]. Il valore è fiduciario/legale, non legato al metallo contenuto."},
    {"id": 33, "text": "La moneta fiduciaria è stata comunemente usata nei principali paesi europei dal XIV secolo.", "correct": "VERO", "explanation": "VERO [Ref: Q33 Primo Parziale]. Si diffuse tramite fedi di deposito e lettere di cambio."},
    {"id": 34, "text": "L'Inghilterra è caratterizzata da un sistema finanziario del tipo 'transaction banking'.", "correct": "VERO", "explanation": "VERO [Ref: Q34 Primo Parziale]. Modello orientato ai mercati finanziari e autofinanziamento."},
    {"id": 36, "text": "Le banche di emissione divennero banche centrali assumendo le funzioni di 'lender of last resort' nella seconda metà del XIX secolo.", "correct": "VERO", "explanation": "VERO [Ref: Q36 Primo Parziale]. Essenziale per frenare le crisi di liquidità esterne."},
    {"id": 39, "text": "L'espansione europea oltreoceano nei secoli XVI e XVII favorì l'aumento della domanda aggregata e lo sviluppo tecnologico in Europa.", "correct": "VERO", "explanation": "VERO [Ref: Q39 Primo Parziale]. Stimolò i commerci a lunga distanza e l'estensione dei mercati."},
    {"id": 40, "text": "L'espansione europea oltreoceano nei secoli XVI e XVII ebbe effetti negativi sulle economie spagnola e portoghese a causa delle ingenti spese militari.", "correct": "FALSO", "explanation": "FALSO [Ref: Q40 Primo Parziale]. L'effetto fu guidato da dinamiche inflazionistiche (rivoluzione dei prezzi) e allocative."},
    {"id": 42, "text": "La Banca d'Inghilterra venne fondata sul finire del XVII secolo (1694).", "correct": "VERO", "explanation": "VERO [Ref: Q42 Primo Parziale]. Sostenne il debito pubblico e la stabilità monetaria britannica."},
    {"id": 45, "text": "I dati storici suggeriscono che in età preindustriale le crisi di mortalità hanno effetti solo transitori sul livello demografico.", "correct": "VERO", "explanation": "VERO [Ref: Q45 Primo Parziale]. Erano seguite da riprese rapide della fecondità."},
    {"id": 46, "text": "Il rallentamento della crescita della popolazione europea nel XVII secolo fu dovuto alla più elevata età al matrimonio.", "correct": "VERO", "explanation": "VERO [Ref: Q46 Primo Parziale]. Tipico del modello demografico europeo (freni preventivi)."},
    {"id": 48, "text": "Sul finire del Quattrocento, gli spagnoli aprono una nuova via per le Indie circumnavigando l'Africa.", "correct": "FALSO", "explanation": "FALSO [Ref: Q48 Primo Parziale]. Furono i Portoghesi (Vasco da Gama), non gli Spagnoli."},
    {"id": 50, "text": "Le crisi dei mercati azionari hanno sempre effetti sistemici.", "correct": "FALSO", "explanation": "FALSO [Ref: Q50 Primo Parziale]. Non tutte le crisi di borsa si trasmettono all'economia reale."},
    {"id": 51, "text": "Le crisi dei mercati azionari non hanno mai effetti sistemici.", "correct": "FALSO", "explanation": "FALSO [Ref: Q51 Primo Parziale]. In diversi casi storici (es. 1929) hanno avuto gravi impatti sistemici."},
    {"id": 52, "text": "Gli atti di navigazione ebbero un effetto negativo sul potenziamento della marina commerciale inglese.", "correct": "FALSO", "explanation": "FALSO [Ref: Q52 Primo Parziale]. Sostennero il monopolio del naviglio mercantilista britannico."},
    {"id": 54, "text": "Nell'Europa preindustriale l'urbanizzazione è correlata a una maggiore produttività in agricoltura.", "correct": "VERO", "explanation": "VERO [Ref: Q54 Primo Parziale]. Più città richiedono surplus agricolo generato da alta produttività."},
    {"id": 55, "text": "Nell'Olanda del XVII secolo l'urbanizzazione non è correlata con una maggiore produttività agricola.", "correct": "FALSO", "explanation": "FALSO [Ref: Q55 Primo Parziale]. L'Olanda presentava un'agricoltura highly specializzata per i mercati urbani."},
    {"id": 57, "text": "La Total Factor Productivity per l'epoca preindustriale si può stimare indirettamente osservando il tasso di urbanizzazione.", "correct": "VERO", "explanation": "VERO [Ref: Q57 Primo Parziale]. L'urbanizzazione riflette la capacità di sfamare popolazione non agricola."},
    {"id": 58, "text": "I diritti di proprietà privata possono essere considerati una soluzione a inefficienze generate dai diritti di proprietà collettiva.", "correct": "VERO", "explanation": "VERO [Ref: Q58 Primo Parziale]. Evitano la 'tragedia dei beni comuni'."},
    {"id": 64, "text": "I mercati sottili garantiscono l'efficiente circolazione di informazioni sui prezzi dei prodotti scambiati.", "correct": "FALSO", "explanation": "FALSO [Ref: Q64 Primo Parziale]. I mercati sottili (pochi operatori) hanno prezzi volatili e informazioni lente."},
    {"id": 65, "text": "Nella seconda metà del Cinquecento, il governo inglese adottò principalmente una politica mercantilistico-protezionistica.", "correct": "VERO", "explanation": "VERO [Ref: Q65 Primo Parziale]. Per proteggere e sviluppare le manifatture nazionali."},
    {"id": 70, "text": "Durante la seconda metà del XIX secolo i tassi di investimento inglesi furono più contenuti di quelli statunitensi.", "correct": "VERO", "explanation": "VERO [Ref: Q70 Primo Parziale]. Fenomeno legato al rallentamento vittoriano."},
    {"id": 71, "text": "Il metodo Gilchrist Thomas permise l'ampliamento della dotazione di risorse in agricoltura.", "correct": "VERO", "explanation": "VERO [Ref: Q71 Primo Parziale]. Il sottoprodotto ricco di fosforo (scorie Thomas) divenne un prezioso fertilizzante."}
]

ALL_MC_QUESTIONS = [
    {
        "id": 3,
        "question": "In presenza di bassa domanda aggregata (bassa densità di popolazione), quali tecnologie tendono a prevalere?",
        "options": [
            "A) Alti costi fissi e bassi costi variabili",
            "B) Bassi costi fissi e alti costi variabili",
            "C) Alti costi fissi e alti costi variabili",
            "D) Esclusivamente tecnologie con automazione"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q3 Primo Parziale]. Sotto bassi volumi di domanda non si ammortizzano elevati costi fissi."
    },
    {
        "id": 4,
        "question": "Quando la domanda aggregata diventa elevata, quali tecnologie si affermano?",
        "options": [
            "A) Bassi costi fissi e alti costi variabili",
            "B) Alti costi fissi e bassi costi variabili",
            "C) Bassi costi fissi e bassi costi variabili",
            "D) Esclusivamente lavoro manuale"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q4 Primo Parziale]. Domanda alta permette di ammortizzare grandi impianti a bassi costi unitari."
    },
    {
        "id": 7,
        "question": "L'effetto frontiera ('border effect') nel commercio internazionale è associato a:",
        "options": [
            "A) La scomparsa delle tariffe doganali",
            "B) I costi di transazione al variare dei confini",
            "C) La perfetta convergenza dei salari",
            "D) L'annullamento della legge del prezzo unico"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q7 Primo Parziale]. I confini aumentano la curva dei costi di transazione."
    },
    {
        "id": 13,
        "question": "La transizione demografica del XIX secolo fu caratterizzata da:",
        "options": [
            "A) Tassi di natalità e mortalità entrambi in aumento",
            "B) Tassi di natalità elevati e mortalità decrescenti",
            "C) Crollo immediato sia di natalità che di mortalità",
            "D) Tassi di mortalità superiori alla natalità"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q13 Primo Parziale]. Il calo della mortalità anticipa di decenni quello della fecondità."
    },
    {
        "id": 16,
        "question": "La servitù della gleba nell'Europa occidentale scomparve principalmente per effetto:",
        "options": [
            "A) Della peste nera e dell'aumento della popolazione successiva",
            "B) Dell'aumento della popolazione che rese il lavoro abbondante e svalutò i salari",
            "C) Di decreti religiosi papali",
            "D) Dell'introduzione delle banconote"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q16 Primo Parziale]. La crescita della popolazione rese superfluo il vincolo coercitivo alla terra."
    },
    {
        "id": 18,
        "question": "Nel corso dei secoli XVI-XVIII la leadership economica europea si spostò:",
        "options": [
            "A) Da Germania e Russia a Francia e Spagna",
            "B) Da Italia e Spagna a Paesi Bassi e Inghilterra",
            "C) Da Inghilterra a Italia e Grecia",
            "D) Da Olanda e Belgio a Portogallo"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q18 Primo Parziale]. La 'piccola divergenza' sposta il baricentro dal Mediterraneo al Mare del Nord."
    },
    {
        "id": 19,
        "question": "Indicare quale tra le seguenti NON è una caratteristica di un'economia moderna:",
        "options": [
            "A) Mercati dei fattori ben funzionanti",
            "B) Tutela dei diritti di proprietà",
            "C) Potere esecutivo libero da vincoli",
            "D) Presenza di istituzioni finanziarie"
        ],
        "correct": 2,
        "explanation": "Opzione C [Ref: Q19 Primo Parziale]. Un'economia moderna richiede vincoli costituzionali/istituzionali al potere esecutivo."
    },
    {
        "id": 21,
        "question": "Quale tra le seguenti tecnologie NON favorì l'espansione economica europea alla fine del primo millennio?",
        "options": [
            "A) Il mulino ad acqua",
            "B) L'aratro pesante a ruote",
            "C) Il mulino manuale",
            "D) La rotazione triennale"
        ],
        "correct": 2,
        "explanation": "Opzione C [Ref: Q21 Primo Parziale]. Il mulino manuale è la tecnologia primitiva 'povera' a lavoro intensivo."
    },
    {
        "id": 24,
        "question": "Affermare che la conoscenza tecnologica è un 'bene non rivale' significa che:",
        "options": [
            "A) Nessuno la può acquistare sul mercato",
            "B) L'uso da parte di un individuo non ne riduce la disponibilità per gli altri",
            "C) Ha un prezzo fisso stabilito dallo Stato",
            "D) Può essere usata solo nei paesi ricchi"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q24 Primo Parziale]. Definizione fondamentale di bene non rivale."
    },
    {
        "id": 26,
        "question": "Quale tra queste innovazioni è considerata una 'General Purpose Technology' (GPT)?",
        "options": [
            "A) La spinning jenny",
            "B) La diffusione dell'energia elettrica",
            "C) Il telaio meccanico da seta",
            "D) L'aratro in ferro"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q26 Primo Parziale]. L'elettricità si applica trasversalmente a tutti i settori dell'economia."
    },
    {
        "id": 31,
        "question": "La convergenza beta è:",
        "options": [
            "A) Condizione sufficiente ma non necessaria per la convergenza sigma",
            "B) Condizione necessaria ma non sufficiente per la convergenza sigma",
            "C) Sinonimo di convergenza dei tassi d'interesse",
            "D) L'azzeramento automatico dei dazi doganali"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q31 Primo Parziale]. Affinché la dispersione (sigma) si riduca, i paesi poveri devono crescere più velocemente (beta)."
    },
    {
        "id": 35,
        "question": "Nel corso dell'Ottocento, la principale caratteristica delle banche universali (miste) era:",
        "options": [
            "A) Evitare il credito industriale",
            "B) Concedere finanziamenti di lungo periodo ed entrare nel capitale delle imprese",
            "C) Emettere esclusivamente moneta cartacea non convertibile",
            "D) Lavorare solo su depositi statali"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q35 Primo Parziale]. Tipico modello tedesco a sostegno dell'industria pesante."
    },
    {
        "id": 38,
        "question": "Rispetto al rapporto con i governi, storicamente le banche centrali:",
        "options": [
            "A) Sono sempre state totalmente sottomesse al ministero del tesoro",
            "B) Abbiano goduto in prospettiva storica di un'ampia indipendenza dai rispettivi governi",
            "C) Non hanno mai avuto ruoli di regolazione finanziaria",
            "D) Operavano solo per il settore agricolo"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q38 Primo Parziale]. L'autonomia ha garantito la difesa del valore della moneta."
    },
    {
        "id": 41,
        "question": "L'espansione europea oltreoceano nei secoli XVI e XVII:",
        "options": [
            "A) Favorì l'aumento della domanda aggregata e il commercio di lunga distanza",
            "B) Ridusse gli scambi commerciali globali",
            "C) Bloccò lo sviluppo della navigazione britannica",
            "D) Azzerò l'uso della moneta metallica"
        ],
        "correct": 0,
        "explanation": "Opzione A [Ref: Q41 Primo Parziale]. Integrò nuovi mercati e prodotti a valore elevato."
    },
    {
        "id": 43,
        "question": "La Banca centrale assolve funzioni:",
        "options": [
            "A) Solo microeconomiche di prestito personale",
            "B) Sia macroeconomiche (offerta di moneta) sia microeconomiche (supervisione intermediari)",
            "C) Esclusivamente fiscali per conto dei comuni",
            "D) Di gestione diretta delle fabbriche statali"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q43 Primo Parziale]. Duplice pilastro della banca centrale."
    },
    {
        "id": 44,
        "question": "La banca universale si affermò principalmente:",
        "options": [
            "A) In Inghilterra nel XVII secolo",
            "B) In Germania a fine Ottocento",
            "C) In Spagna nel Cinquecento",
            "D) Negli Stati Uniti durante la guerra di secessione"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q44 Primo Parziale]. Sostenne il modello industriale capitally-intensive tedesco."
    },
    {
        "id": 53,
        "question": "Le principali innovazioni tecnologiche della Rivoluzione industriale inglese riguardano i settori:",
        "options": [
            "A) Agricolo, chimico e spaziale",
            "B) Tessile cotone, metallurgico ed energetico (macchina a vapore)",
            "C) Ferroviario, telegrafico e nucleare",
            "D) Ceramica, manifattura di pelli e silvicoltura"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q53 Primo Parziale]. Cotone, ferro/acciaio e carbone/vapore."
    },
    {
        "id": 56,
        "question": "Le stime relative alla produttività (TFP) in agricoltura nella Francia d'Ancien Régime mostrano che la TFP:",
        "options": [
            "A) Cresceva a tassi costanti dell'8% in tutte le province",
            "B) Ha avuto fasi di crescita e di stagnazione e significative differenze regionali",
            "C) È rimasta identica a quella dell'impero romano senza variazioni",
            "D) Era più alta nelle colonie tropicali"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q56 Primo Parziale]. Studi di Hoffman mostrano dinamiche regionali eterogenee."
    },
    {
        "id": 59,
        "question": "Il costo opportunità della prole è:",
        "options": [
            "A) Più basso nel XX secolo rispetto all'età preindustriale",
            "B) Più elevato nel XX secolo che in età preindustriale",
            "C) Invariato lungo tutta la storia umana",
            "D) Pari a zero nelle società urbane"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q59 Primo Parziale]. Con l'aumento dei salari e dell'istruzione femminile, accudire i figli costa più tempo redditizio."
    },
    {
        "id": 60,
        "question": "L'evoluzione dei sistemi di pagamento storici si è fondata sui seguenti strumenti in ordine cronologico:",
        "options": [
            "A) Banconota / Carte di credito / Baratto",
            "B) Bene durevole (sale) / Moneta metallica / Cambiale / Banconota / Deposito bancario",
            "C) Deposito bancario / Moneta d'oro / Baratto",
            "D) Moneta fiduciaria / Baratto / Cambiale"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q60 Primo Parziale]. Sequenza storica della smaterializzazione del pagamento."
    },
    {
        "id": 61,
        "question": "Rispetto al ruolo delle fiere nell'Europa medievale, esse erano:",
        "options": [
            "A) Inutili ostacoli alle dogane",
            "B) Funzionali ad affrontare i problemi di mercati in cui le informazioni erano difficili da ottenere",
            "C) Luoghi dove era vietato usare la moneta",
            "D) Riservate esclusivamente al commercio di grano"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q61 Primo Parziale]. Concentravano domanda e offerta riducendo asimmetrie informative."
    },
    {
        "id": 67,
        "question": "Relativamente agli elementi alla base della ripresa economica nei secoli IX-XIV, si può sostenere che:",
        "options": [
            "A) La peste nera bloccò i mercati per tre secoli",
            "B) Il ripristino dell'autorità politica e delle istituzioni rese il commercio più sicuro",
            "C) L'oro americano inondò le piazze europee",
            "D) Scomparvero tutte le città della pianura padana"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q67 Primo Parziale]. La riduzione dell'incertezza e del brigantaggio favorì i mercati."
    },
    {
        "id": 68,
        "question": "La 'rivoluzione industriosa', che secondo alcuni storici ha preceduto la Rivoluzione Industriale, fu caratterizzata da:",
        "options": [
            "A) Distruzione delle fabbriche da parte dei contadini",
            "B) Un cambiamento nei modelli di consumo e un aumento del tempo dedicato al lavoro per il mercato",
            "C) Scomparsa del lavoro femminile",
            "D) La totale chiusura dei mercati esteri"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q68 Primo Parziale]. Teoria di Jan de Vries: maggiore riorientamento verso i beni di consumo di mercato."
    },
    {
        "id": 72,
        "question": "La Germania ha avuto un'industrializzazione tardiva ma poi è cresciuta più rapidamente del Regno Unito grazie a:",
        "options": [
            "A) Libero scambio assoluto senza tariffe",
            "B) Sussidi del governo, banche universali e sostegno all'industria pesante",
            "C) Esclusivo sviluppo dell'agricoltura di sussistenza",
            "D) Rinuncia alla rete ferroviaria"
        ],
        "correct": 1,
        "explanation": "Opzione B [Ref: Q72 Primo Parziale]. Il modello latecomer tedesco ha sfruttato grandi concentrazioni industriali e credito integrato."
    }
]

ALL_DROPDOWN_QUESTIONS = [
    {
        "id": 10,
        "title": "Formazione dell'Europa e forze coesive",
        "template_parts": [
            "La formazione dell'Europa è stata un lungo percorso storico. L'aspetto più sorprendente è dato dalla ",
            " sul piano geo-economico nel corso degli ultimi millenni. Il grande paradosso sta nel fatto che il continente è rimasto omogeneo sul piano culturale e ",
            " per via di potenti forze coesive. La più potente è l'interazione ",
            ". L'intensità degli scambi è stata stimolata dalla prossimità e dalla ",
            " tra le nazioni."
        ],
        "dropdowns": [
            {"var_name": "q10_d1", "options": ["PERSISTENZA", "discontinuità", "frammentazione"], "correct": "PERSISTENZA"},
            {"var_name": "q10_d2", "options": ["ISTITUZIONALE", "militare", "linguistico"], "correct": "ISTITUZIONALE"},
            {"var_name": "q10_d3", "options": ["COMMERCIALE", "militare", "religiosa"], "correct": "COMMERCIALE"},
            {"var_name": "q10_d4", "options": ["SOMIGLIANZA", "diversità", "rivalità"], "correct": "SOMIGLIANZA"}
        ],
        "explanation": "Ref: Q10 Primo Parziale. L'omogeneità istituzionale europea è derivata dai flussi continui di scambi commerciali."
    },
    {
        "id": 14,
        "title": "Popolazione, forze Smithiane e Malthusiane",
        "template_parts": [
            "La crescita della popolazione determina due effetti ",
            " sul prodotto e sul reddito pro capite. Vi sono buoni motivi per credere che la crescita determini ",
            " della domanda aggregata. Inoltre la creazione di idee è correlata ",
            " alle dimensioni della popolazione. Se le forze smithiane superano quelle malthusiane, si determina un reddito posizionato ",
            " al reddito di sussistenza."
        ],
        "dropdowns": [
            {"var_name": "q14_d1", "options": ["DI SEGNO OPPOSTO", "identici", "nulli"], "correct": "DI SEGNO OPPOSTO"},
            {"var_name": "q14_d2", "options": ["UN INCREMENTO", "una riduzione", "un blocco"], "correct": "UN INCREMENTO"},
            {"var_name": "q14_d3", "options": ["POSITIVAMENTE", "negativamente", "inversamente"], "correct": "POSITIVAMENTE"},
            {"var_name": "q14_d4", "options": ["SUPERIORE", "inferiore", "pari"], "correct": "SUPERIORE"}
        ],
        "explanation": "Ref: Q14 Primo Parziale. Quando la divisione del lavoro smithiana batte i rendimenti decrescenti malthusiani, il reddito cresce."
    },
    {
        "id": 22,
        "title": "I Paesi Bassi Meridionali nel Medioevo",
        "template_parts": [
            "Nel corso dei secoli XI-XV i Paesi Bassi ",
            " furono i protagonisti di uno sviluppo eccezionale, secondi solo al polo ",
            ". La produzione più importante era quella dei ",
            " e i centri internazionali d'affari più importanti erano localizzati a ",
            "."
        ],
        "dropdowns": [
            {"var_name": "q22_d1", "options": ["MERIDIONALI", "settentrionali", "orientali"], "correct": "MERIDIONALI"},
            {"var_name": "q22_d2", "options": ["ITALIANO", "spagnolo", "inglese"], "correct": "ITALIANO"},
            {"var_name": "q22_d3", "options": ["PANNILANA", "metalli pesanti", "spezie"], "correct": "PANNILANA"},
            {"var_name": "q22_d4", "options": ["BRUGES E ANVERSA", "Amsterdam e Rotterdam", "Londra e Bristol"], "correct": "BRUGES E ANVERSA"}
        ],
        "explanation": "Ref: Q22 Primo Parziale. Le Fiandre (Paesi Bassi meridionali) erano il cuore tessile europeo assieme all'Italia centro-settentrionale."
    },
    {
        "id": 29,
        "title": "Gerschenkron e il vantaggio dell'arretratezza",
        "template_parts": [
            "I paesi meno ricchi godono del ",
            " dell'arretratezza (Gerschenkron). Il Regno Unito crebbe più ",
            " di paesi meno ricchi prima del 1914. Tra le due guerre la convergenza ",
            " in seguito ",
            " delle barriere protezionistiche."
        ],
        "dropdowns": [
            {"var_name": "q29_d1", "options": ["VANTAGGIO", "svantaggio", "rischio"], "correct": "VANTAGGIO"},
            {"var_name": "q29_d2", "options": ["LENTAMENTE", "rapidamente", "esponenzialmente"], "correct": "LENTAMENTE"},
            {"var_name": "q29_d3", "options": ["NON CONTINUÒ", "accelerò", "si stabilizzò"], "correct": "NON CONTINUÒ"},
            {"var_name": "q29_d4", "options": ["ALL'AUMENTO", "alla riduzione", "all'azzeramento"], "correct": "ALL'AUMENTO"}
        ],
        "explanation": "Ref: Q29 Primo Parziale. Il protezionismo tra le due guerre interruppe i processi di convergenza."
    },
    {
        "id": 37,
        "title": "Origine delle crisi finanziarie e prestatore di ultima istanza",
        "template_parts": [
            "La storia delle crisi finanziarie è molto ",
            ". Le crisi di ",
            " hanno origine dal sistema a riserva proporzionale e sono state contenute con ",
            " da parte delle banche centrali, mentre le crisi di solvibilità sono storicamente più difficili."
        ],
        "dropdowns": [
            {"var_name": "q37_d1", "options": ["LUNGA", "breve", "recente"], "correct": "LUNGA"},
            {"var_name": "q37_d2", "options": ["LIQUIDITÀ", "solvibilità", "cambio"], "correct": "LIQUIDITÀ"},
            {"var_name": "q37_d3", "options": ["L'ASSUNZIONE DEL RUOLO DI PRESTATORE DI ULTIMA ISTANZA", "il blocco dei depositi", "la svalutazione"], "correct": "L'ASSUNZIONE DEL RUOLO DI PRESTATORE DI ULTIMA ISTANZA"}
        ],
        "explanation": "Ref: Q37 Primo Parziale. Il prestatore di ultima istanza previene il panico bancario sulle riserve frazionarie."
    },
    {
        "id": 62,
        "title": "Origine delle Lettere di Cambio",
        "template_parts": [
            "Prima della moneta cartacea, gli scambi si realizzavano con le ",
            ". Il loro sviluppo fu avviato dai mercanti banchieri ",
            " e costituivano promesse del ",
            " di corrispondere la somma dovuta al creditore."
        ],
        "dropdowns": [
            {"var_name": "q62_d1", "options": ["LETTERE DI CAMBIO", "azioni di borsa", "fedi privilegiate"], "correct": "LETTERE DI CAMBIO"},
            {"var_name": "q62_d2", "options": ["ITALIANI", "inglesi", "tedeschi"], "correct": "ITALIANI"},
            {"var_name": "q62_d3", "options": ["DEBITORE", "sovrano", "papa"], "correct": "DEBITORE"}
        ],
        "explanation": "Ref: Q62 Primo Parziale. Strumento creditizio fondamentale creato dai banchieri italiani medievali."
    },
    {
        "id": 63,
        "title": "Le Corporazioni e la Lega Anseatica",
        "template_parts": [
            "Le corporazioni erano associazioni che ",
            " la concorrenza esterna mantenendo i prezzi ",
            ". Corporazioni mercantili come ",
            " ebbero un ruolo decisivo ",
            " nella difesa dei diritti dei propri membri."
        ],
        "dropdowns": [
            {"var_name": "q63_d1", "options": ["LIMITAVANO", "stimolavano", "azzeravano"], "correct": "LIMITAVANO"},
            {"var_name": "q63_d2", "options": ["ALTI", "bassi", "nulli"], "correct": "ALTI"},
            {"var_name": "q63_d3", "options": ["LA LEGA ANSEATICA", "la Compagnia delle Indie", "la Bank of England"], "correct": "LA LEGA ANSEATICA"},
            {"var_name": "q63_d4", "options": ["DURANTE IL MEDIOEVO", "nell'Ottocento", "nel Novecento"], "correct": "DURANTE IL MEDIOEVO"}
        ],
        "explanation": "Ref: Q63 Primo Parziale. Le corporazioni proteggevano i mercanti e la reputazione commerciale."
    },
    {
        "id": 69,
        "title": "Brevetti e innovazione nell'Ottocento",
        "template_parts": [
            "I grandi progressi derivanti da indagine teorica e verifica empirica ebbero luogo nella seconda metà del ",
            " secolo. In Spagna e Portogallo si nota ",
            " numero di domande di brevetti, mentre a livello europeo si osserva ",
            " fino alla Prima Guerra Mondiale."
        ],
        "dropdowns": [
            {"var_name": "q69_d1", "options": ["DICIANNOVESIMO", "diciottesimo", "ventesimo"], "correct": "DICIANNOVESIMO"},
            {"var_name": "q69_d2", "options": ["IL BASSO", "l'elevato", "il record"], "correct": "IL BASSO"},
            {"var_name": "q69_d3", "options": ["UN LENTO INCREMENTO", "un crollo", "un'interruzione"], "correct": "UN LENTO INCREMENTO"}
        ],
        "explanation": "Ref: Q69 Primo Parziale. I brevetti dell'800 rispecchiano la concentrazione della conoscenza scientifica in centro-nord Europa."
    },
    {
        "id": 73,
        "title": "Joel Mokyr e l'Illuminismo Industriale",
        "template_parts": [
            "Secondo Joel Mokyr l'illuminismo industriale fu un fenomeno ",
            ". Tuttavia alcune regioni come ",
            " non fornirono contributi significativi. Le peculiari condizioni ",
            " dell'Europa favorirono l'accumulazione ",
            "."
        ],
        "dropdowns": [
            {"var_name": "q73_d1", "options": ["EUROPEO E DELLE PROPAGAGGINI", "esclusivamente asiatico", "latinoamericano"], "correct": "EUROPEO E DELLE PROPAGAGGINI"},
            {"var_name": "q73_d2", "options": ["L'EUROPA ORIENTALE", "l'Inghilterra", "la Scozia"], "correct": "L'EUROPA ORIENTALE"},
            {"var_name": "q73_d3", "options": ["ISTITUZIONALI", "geografiche", "militari"], "correct": "ISTITUZIONALI"},
            {"var_name": "q73_d4", "options": ["DELLE CONOSCENZE UTILI", "di metalli preziosi", "di schiavi"], "correct": "DELLE CONOSCENZE UTILI"}
        ],
        "explanation": "Ref: Q73 Primo Parziale. L'accumulazione di 'useful knowledge' è la cifra dell'illuminismo industriale."
    },
    {
        "id": 76,
        "title": "Urbanizzazione e Legge di Engel",
        "template_parts": [
            "I residenti nei centri urbani sono attivi nella produzione ",
            ". Quando l'urbanizzazione cresce, la domanda di beni ",
            " è in crescita perché l'elasticità della domanda di cibo è ",
            " rispetto a quella dei beni non alimentari. Questa regolarità è la ",
            "."
        ],
        "dropdowns": [
            {"var_name": "q76_d1", "options": ["NON ALIMENTARE", "agricola di sussistenza", "forestale"], "correct": "NON ALIMENTARE"},
            {"var_name": "q76_d2", "options": ["NON DI PRIMA NECESSITÀ", "esclusivamente di pane", "di sementi"], "correct": "NON DI PRIMA NECESSITÀ"},
            {"var_name": "q76_d3", "options": ["INFERIORE", "superiore", "uguale"], "correct": "INFERIORE"},
            {"var_name": "q76_d4", "options": ["LEGGE DI ENGEL", "trappola malthusiana", "legge di Gresham"], "correct": "LEGGE DI ENGEL"}
        ],
        "explanation": "Ref: Q76 Primo Parziale. La legge di Engel stabilisce il calo della quota di cibo nei consumi al crescere del reddito."
    }
]

ALL_GRAPH_QUESTIONS = [
    {
        "id": 77,
        "title": "Grafico della Transizione Demografica (CBR e CDR)",
        "graph_type": "transizione_demografica",
        "questions": [
            {"sub_id": "q77_1", "text": "Durante la transizione demografica si verifica un aumento della popolazione complessiva.", "correct": "VERO", "explanation": "VERO [Ref: Q77]. Il divario tra natalità alta e mortalità in calo genera forte crescita demografica."},
            {"sub_id": "q77_2", "text": "Durante la transizione demografica il tasso di natalità comincia a declinare prima di quello di mortalità.", "correct": "FALSO", "explanation": "FALSO [Ref: Q77]. È il tasso di mortalità (CDR) a scendere per primo."},
            {"sub_id": "q77_3", "text": "Prima e dopo la transizione demografica i tassi di natalità e di mortalità sono molto simili tra loro.", "correct": "VERO", "explanation": "VERO [Ref: Q77]. Si passa da un regime ad alta pressione a uno a bassa pressione in equilibrio."}
        ]
    },
    {
        "id": 78,
        "title": "Convergenza Beta in Europa (1950-1975)",
        "graph_type": "beta_1950_1975",
        "questions": [
            {"sub_id": "q78_1", "text": "Il grafico mostra una relazione negativa tra il livello di reddito iniziale nel 1950 e il tasso di crescita del PIL pro capite.", "correct": "VERO", "explanation": "VERO [Ref: Q78]. La pendenza negativa della retta indica che i paesi più poveri sono cresciuti più in fretta."},
            {"sub_id": "q78_2", "text": "Il grafico mostra che l'Inghilterra (GB) è cresciuta di più rispetto ad economie relativamente più povere tra 1950 e 1975.", "correct": "FALSO", "explanation": "FALSO [Ref: Q78]. L'Inghilterra figura in basso a destra con una delle crescite più lente."},
            {"sub_id": "q78_3", "text": "Il grafico dimostra il verificarsi della convergenza beta in Europa.", "correct": "VERO", "explanation": "VERO [Ref: Q78]. Tipica evidenza empirica della Golden Age del dopoguerra."}
        ]
    },
    {
        "id": 79,
        "title": "Assenza di Convergenza tra le due Guerre (1914-1950)",
        "graph_type": "no_convergenza_1914_1950",
        "questions": [
            {"sub_id": "q79_1", "text": "Il grafico mostra il verificarsi di convergenza beta in Europa nel periodo 1914-1950.", "correct": "FALSO", "explanation": "FALSO [Ref: Q79]. La retta ha inclinazione positiva/piatta: il protezionismo ha bloccato la convergenza."},
            {"sub_id": "q79_2", "text": "Il grafico mostra che la chiusura agli scambi favorisce i paesi di prima industrializzazione come il Regno Unito.", "correct": "VERO", "explanation": "VERO [Ref: Q79]. La frammentazione ha penalizzato soprattutto i paesi ritardatari."},
            {"sub_id": "q79_3", "text": "Il grafico mostra che la crescita economica tra 1914 e 1950 è stata direttamente proporzionale alla ricchezza iniziale.", "correct": "FALSO", "explanation": "FALSO [Ref: Q79]. Non c'era relazione di convergenza sistematica."}
        ]
    },
    {
        "id": 80,
        "title": "Convergenza Beta nella Prima Globalizzazione (1870-1914)",
        "graph_type": "beta_1870_1914",
        "questions": [
            {"sub_id": "q80_1", "text": "Il grafico mostra una relazione negativa tra reddito iniziale nel 1870 e crescita economica fino al 1914.", "correct": "VERO", "explanation": "VERO [Ref: Q80]. Evidenza di convergenza beta favorita dalla prima era di globalizzazione e Gold Standard."},
            {"sub_id": "q80_2", "text": "Il grafico mostra il verificarsi di convergenza sigma in Europa.", "correct": "FALSO", "explanation": "FALSO [Ref: Q80]. Il grafico mostra la convergenza beta, che è condizione necessaria ma distinta dalla convergenza sigma."},
            {"sub_id": "q80_3", "text": "Il grafico mostra che l'Inghilterra è cresciuta di più rispetto ad economie relativamente più povere tra 1870 e 1914.", "correct": "FALSO", "explanation": "FALSO [Ref: Q80]. I paesi ritardatari (es. Scandinavia) sono cresciuti più velocemente del Regno Unito."}
        ]
    },
    {
        "id": 81,
        "title": "Guadagni della Specializzazione e Vantaggio Comparato",
        "graph_type": "specializzazione_ricardo",
        "questions": [
            {"sub_id": "q81_1", "text": "Il grafico rappresenta i guadagni derivanti dalla specializzazione produttiva e dal commercio.", "correct": "VERO", "explanation": "VERO [Ref: Q81]. Mostra come la curva delle possibilità di consumo si sposti all'esterno con la specializzazione."},
            {"sub_id": "q81_2", "text": "Il grafico mostra i vantaggi dell'autosufficienza e dell'autarchia.", "correct": "FALSO", "explanation": "FALSO [Ref: Q81]. Dimostra esattamente l'opposto: il commercio supera i limiti dell'autarchia."},
            {"sub_id": "q81_3", "text": "Il grafico mostra che il costo opportunità di produrre il bene specializzato diminuisce all'aumentare della specializzazione.", "correct": "VERO", "explanation": "VERO [Ref: Q81]. Rappresenta la concavità/struttura dei vantaggi comparati."}
        ]
    }
]

# ==========================================
# GENERATORE GRAFICI MATPLOTLIB
# ==========================================
def generate_matplotlib_figure(graph_type):
    fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=100)

    if graph_type == "transizione_demografica":
        years = np.linspace(0, 150, 100)
        cdr = 30 - 22 / (1 + np.exp(-(years - 40) / 15))
        cbr = 32 - 24 / (1 + np.exp(-(years - 85) / 15))
        ax.plot(years, cbr, color='#d9534f', linewidth=2.5, label='CBR (Tasso Natalità)')
        ax.plot(years, cdr, color='#1f4e78', linestyle='--', linewidth=2.5, label='CDR (Tasso Mortalità)')
        ax.fill_between(years, cbr, cdr, where=(cbr > cdr), color='#f0ad4e', alpha=0.3, label='Crescita Popolazione')
        ax.set_title('Modello di Transizione Demografica Storica Europea', fontsize=8, fontweight='bold')
        ax.set_xlabel('Anni dalla transizione', fontsize=8)
        ax.set_ylabel('Tassi per mille', fontsize=8)
        ax.grid(True, linestyle=':', alpha=0.5)
        ax.legend(loc='upper right', fontsize=8)

    elif graph_type == "beta_1950_1975":
        x = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
        y = np.array([5.2, 4.8, 4.5, 4.1, 3.8, 3.4, 3.1, 2.7, 2.5, 2.1])
        countries = ['GR', 'ES', 'IT', 'AT', 'DE', 'FR', 'NO', 'BE', 'SE', 'GB']
        ax.scatter(x, y, color='#1f4e78', s=45, zorder=3)
        for i, txt in enumerate(countries):
            ax.annotate(txt, (x[i] + 120, y[i] + 0.08), fontsize=8, fontweight='bold')
        m, b = np.polyfit(x, y, 1)
        ax.plot(x, m * x + b, color='#d9534f', linestyle='--', linewidth=2, label='Beta-Convergenza (Inclinazione -)')
        ax.set_title('Convergenza Beta in Europa: Crescita PIL (1950-75) vs PIL 1950', fontsize=8, fontweight='bold')
        ax.set_xlabel('PIL pro capite iniziale 1950 ($)', fontsize=8)
        ax.set_ylabel('Crescita PIL pro capite (%)', fontsize=8)
        ax.grid(True, linestyle=':', alpha=0.5)
        ax.legend(loc='upper right', fontsize=8)

    elif graph_type == "no_convergenza_1914_1950":
        x = np.array([800, 1200, 1600, 2200, 2800, 3200, 3800, 4200])
        y = np.array([0.2, 0.6, 0.5, 0.4, 0.7, 1.4, 1.8, 2.2])
        countries = ['BG', 'YUG', 'GR', 'ES', 'IT', 'FR', 'DK', 'BE']
        ax.scatter(x, y, color='#e74c3c', s=45, zorder=3)
        for i, txt in enumerate(countries):
            ax.annotate(txt, (x[i] + 80, y[i] + 0.05), fontsize=8, fontweight='bold')
        m, b = np.polyfit(x, y, 1)
        ax.plot(x, m * x + b, color='#2c3e50', linestyle='-', linewidth=2, label='Assenza Convergenza (Retta Positiva/Piatta)')
        ax.set_title('Assenza di Convergenza in Europa tra le due Guerre (1914-1950)', fontsize=8, fontweight='bold')
        ax.set_xlabel('PIL pro capite iniziale 1914 ($)', fontsize=8)
        ax.set_ylabel('Crescita PIL pro capite (%)', fontsize=8)
        ax.grid(True, linestyle=':', alpha=0.5)
        ax.legend(loc='upper left', fontsize=8)

    elif graph_type == "beta_1870_1914":
        x = np.array([800, 1200, 1500, 2000, 2400, 2800, 3200])
        y = np.array([1.3, 1.2, 1.0, 0.9, 0.8, 0.5, 0.3])
        countries = ['YUG', 'GR', 'ES', 'IT', 'FR', 'BE', 'NL']
        ax.scatter(x, y, color='#2ecc71', s=45, zorder=3)
        for i, txt in enumerate(countries):
            ax.annotate(txt, (x[i] + 60, y[i] + 0.04), fontsize=8, fontweight='bold')
        m, b = np.polyfit(x, y, 1)
        ax.plot(x, m * x + b, color='#16a085', linestyle='--', linewidth=2, label='Beta Convergenza 1870-1914')
        ax.set_title('Convergenza Beta nella Prima Globalizzazione (1870-1914)', fontsize=8, fontweight='bold')
        ax.set_xlabel('PIL pro capite iniziale 1870 ($)', fontsize=8)
        ax.set_ylabel('Crescita PIL pro capite (%)', fontsize=8)
        ax.grid(True, linestyle=':', alpha=0.5)
        ax.legend(loc='upper right', fontsize=8)

    elif graph_type == "specializzazione_ricardo":
        x = np.linspace(0, 10, 100)
        y_autarchia = 10 - x
        y_commercio = 12 - 0.8 * x
        ax.plot(x, y_autarchia, color='#7f8c8d', linestyle=':', linewidth=2, label='Frontiera Autarchica')
        ax.plot(x, y_commercio, color='#2980b9', linewidth=2.5, label='Frontiera con Specializzazione/Scambio')
        ax.set_title('Vantaggi della Specializzazione Produttiva (David Ricardo)', fontsize=8, fontweight='bold')
        ax.set_xlabel('Quantità Bene A', fontsize=8)
        ax.set_ylabel('Quantità Bene B', fontsize=8)
        ax.grid(True, linestyle=':', alpha=0.5)
        ax.legend(loc='upper right', fontsize=8)

    fig.tight_layout()
    return fig

# ==========================================
# GESTIONE STATO DI SESSIONE E RANDOMIZZAZIONE
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

if 'active_vf' not in st.session_state:
    st.session_state.active_vf = []
if 'active_mc' not in st.session_state:
    st.session_state.active_mc = []
if 'active_drop' not in st.session_state:
    st.session_state.active_drop = []
if 'active_graph' not in st.session_state:
    st.session_state.active_graph = []

def start_exam():
    st.session_state.page = 'exam'
    st.session_state.start_time = time.time()
    
    st.session_state.vf_answers = {}
    st.session_state.mc_answers = {}
    st.session_state.drop_answers = {}
    st.session_state.graph_answers = {}
    
    # Estrazione casuale dal BANCO DOMANDE COMPLETO
    st.session_state.active_vf = random.sample(ALL_VF_QUESTIONS, min(10, len(ALL_VF_QUESTIONS)))
    st.session_state.active_mc = random.sample(ALL_MC_QUESTIONS, min(5, len(ALL_MC_QUESTIONS)))
    st.session_state.active_drop = random.sample(ALL_DROPDOWN_QUESTIONS, min(3, len(ALL_DROPDOWN_QUESTIONS)))
    st.session_state.active_graph = random.sample(ALL_GRAPH_QUESTIONS, min(2, len(ALL_GRAPH_QUESTIONS)))

def submit_exam():
    st.session_state.page = 'results'

# ==========================================
# INTERFACCIA STREAMLIT
# ==========================================

# --- SCHERMATA HOME ---
if st.session_state.page == 'home':
    st.title("📜 Prova d'Esame: Storia Economica")
    st.subheader("Simulatore Ufficiale Primo Parziale (Banco Domande Completo)")

    st.markdown("""
    **Modalità d'Esame:**
    - **Durata:** 30 Minuti *(timer integrato)*
    - **Sezione 1:** 10 Domande Vero / Falso *(estratte casualmente)*
    - **Sezione 2:** 5 Domande a Risposta Multipla *(estratte casualmente)*
    - **Sezione 3:** 3 Testi da completare con menu a tendina *(estratti casualmente)*
    - **Sezione 4:** 2 Grafici con 3 quesiti V/F ciascuno *(estratti casualmente)*
    
    *Ad ogni nuovo avvio verrà generata una combinazione di domande completamente diversa.*
    """)

    if st.button("▶ AVVIA SIMULAZIONE ESAME (30 MINUTI)", type="primary"):
        start_exam()
        st.rerun()

# --- SCHERMATA ESAME ---
elif st.session_state.page == 'exam':

    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, 30 * 60 - elapsed)

    if remaining == 0:
        st.error("⏱ Tempo scaduto! La prova verrà inviata automaticamente per il calcolo del punteggio.")
        time.sleep(2)
        submit_exam()
        st.rerun()

    m, s = divmod(int(remaining), 60)
    st.info(f"⏱ **Tempo Rimanente:** {m:02d}:{s:02d}")

    tab1, tab2, tab3, tab4 = st.tabs([
        "1. Vero / Falso (10)",
        "2. Risposta Multipla (5)",
        "3. Testi a Tendina (3)",
        "4. Analisi Grafici (2)"
    ])

    # SEZIONE 1
    with tab1:
        st.markdown("### Sezione 1: Vero / Falso")
        st.caption("Rispondi VERO o FALSO a ciascuna delle 10 domande estratte dal banco.")

        for i, q in enumerate(st.session_state.active_vf):
            st.markdown(f"**{i+1}. {q['text']}** *(Ref Banco: Q{q['id']})*")
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

    # SEZIONE 2
    with tab2:
        st.markdown("### Sezione 2: Risposta Multipla")
        st.caption("Seleziona l'unica opzione corretta per ciascuno dei 5 quesiti estratti.")

        for i, q in enumerate(st.session_state.active_mc):
            st.markdown(f"**{i+1}. {q['question']}** *(Ref Banco: Q{q['id']})*")
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

    # SEZIONE 3
    with tab3:
        st.markdown("### Sezione 3: Testi da Completare")
        st.caption("Seleziona il termine corretto dai menu a tendina per completare i 3 brani.")

        for i, t_item in enumerate(st.session_state.active_drop):
            st.markdown(f"#### Testo {i+1}: {t_item['title']} *(Ref Banco: Q{t_item['id']})*")
            parts = t_item['template_parts']
            dropdowns = t_item['dropdowns']

            for p in range(len(parts)):
                st.write(parts[p])
                if p < len(dropdowns):
                    d_info = dropdowns[p]
                    var_name = d_info['var_name']
                    curr_val = st.session_state.drop_answers.get(var_name, "-- Scegli --")

                    opts = ["-- Scegli --"] + d_info['options']
                    opt_idx = opts.index(curr_val) if curr_val in opts else 0

                    sel = st.selectbox(
                        f"Spazio vuoto [{p+1}]:",
                        opts,
                        index=opt_idx,
                        key=f"drop_{var_name}"
                    )
                    st.session_state.drop_answers[var_name] = sel

            st.divider()

    # SEZIONE 4
    with tab4:
        st.markdown("### Sezione 4: Analisi dei Grafici")
        st.caption("Osserva i grafici e rispondi VERO o FALSO ai quesiti associati.")

        for i, g_item in enumerate(st.session_state.active_graph):
            st.markdown(f"#### Grafico {i+1}: {g_item['title']} *(Ref Banco: Q{g_item['id']})*")

            fig = generate_matplotlib_figure(g_item['graph_type'])
            st.pyplot(fig)
            plt.close(fig)

            for j, sub_q in enumerate(g_item['questions']):
                st.markdown(f"**Quesito {i+1}.{j+1} - {sub_q['text']}**")
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

    if st.button("✓ INVIA ESAME E CALCOLA PUNTEGGIO", type="primary"):
        submit_exam()
        st.rerun()

# --- SCHERMATA RISULTATI ---
elif st.session_state.page == 'results':
    st.title("🏆 Esito Finale e Report Esame")

    score_vf = 0
    score_mc = 0
    score_drop = 0
    score_graph = 0

    for q in st.session_state.active_vf:
        if st.session_state.vf_answers.get(q['id']) == q['correct']:
            score_vf += 1

    for q in st.session_state.active_mc:
        if st.session_state.mc_answers.get(q['id']) == q['correct']:
            score_mc += 2

    for t_item in st.session_state.active_drop:
        for d in t_item['dropdowns']:
            if st.session_state.drop_answers.get(d['var_name']) == d['correct']:
                score_drop += 1

    for g_item in st.session_state.active_graph:
        for sub_q in g_item['questions']:
            if st.session_state.graph_answers.get(sub_q['sub_id']) == sub_q['correct']:
                score_graph += 1

    max_vf = len(st.session_state.active_vf)
    max_mc = len(st.session_state.active_mc) * 2
    max_drop = sum(len(t['dropdowns']) for t in st.session_state.active_drop)
    max_graph = sum(len(g['questions']) for g in st.session_state.active_graph)

    total_score = score_vf + score_mc + score_drop + score_graph
    max_score = max_vf + max_mc + max_drop + max_graph

    if total_score >= (max_score * 0.6):
        st.success(f"🎉 **ESAME SUPERATO!** Punteggio Totale: **{total_score} / {max_score}**")
    else:
        st.error(f"❌ **ESAME NON SUPERATO.** Punteggio Totale: **{total_score} / {max_score}**")

    st.markdown(f"""
    **Dettaglio Punteggi:**
    - Vero / Falso: **{score_vf} / {max_vf}**
    - Risposta Multipla: **{score_mc} / {max_mc}**
    - Testi a Tendina: **{score_drop} / {max_drop}**
    - Analisi Grafici: **{score_graph} / {max_graph}**
    """)

    st.divider()
    st.subheader("📋 Correzione Dettagliata per Sezione")

    with st.expander("Sezione 1: Vero / Falso"):
        for q in st.session_state.active_vf:
            ans = st.session_state.vf_answers.get(q['id'], 'Non data')
            icon = "✅" if ans == q['correct'] else "❌"
            st.markdown(f"{icon} **{q['text']}** *(Ref Banco: Q{q['id']})*")
            st.write(f"- Tua risposta: **{ans}** | Risposta corretta: **{q['correct']}**")
            st.info(f"💡 Spiegazione: {q['explanation']}")
            st.divider()

    with st.expander("Sezione 2: Risposta Multipla"):
        for q in st.session_state.active_mc:
            ans_idx = st.session_state.mc_answers.get(q['id'])
            ans_str = q['options'][ans_idx] if ans_idx is not None else "Non data"
            corr_str = q['options'][q['correct']]
            icon = "✅" if ans_idx == q['correct'] else "❌"

            st.markdown(f"{icon} **{q['question']}** *(Ref Banco: Q{q['id']})*")
            st.write(f"- Tua risposta: **{ans_str}**")
            st.write(f"- Risposta corretta: **{corr_str}**")
            st.info(f"💡 Spiegazione: {q['explanation']}")
            st.divider()

    with st.expander("Sezione 3: Testi a Tendina"):
        for t_item in st.session_state.active_drop:
            st.markdown(f"#### {t_item['title']} *(Ref Banco: Q{t_item['id']})*")
            for d in t_item['dropdowns']:
                ans = st.session_state.drop_answers.get(d['var_name'], 'Non data')
                icon = "✅" if ans == d['correct'] else "❌"
                st.write(f"{icon} Spazio `[{d['var_name']}]` -> Tua risposta: **{ans}** | Corretta: **{d['correct']}**")
            st.info(f"💡 Spiegazione: {t_item['explanation']}")
            st.divider()

    with st.expander("Sezione 4: Analisi Grafici"):
        for g_item in st.session_state.active_graph:
            st.markdown(f"#### {g_item['title']} *(Ref Banco: Q{g_item['id']})*")
            for sub_q in g_item['questions']:
                ans = st.session_state.graph_answers.get(sub_q['sub_id'], 'Non data')
                icon = "✅" if ans == sub_q['correct'] else "❌"
                st.markdown(f"{icon} **{sub_q['text']}**")
                st.write(f"- Tua risposta: **{ans}** | Corretta: **{sub_q['correct']}**")
                st.info(f"💡 Spiegazione: {sub_q['explanation']}")
            st.divider()

    if st.button("🔄 AVVIA UNA NUOVA PROVA (ALTRE DOMANDE)"):
        st.session_state.page = 'home'
        st.rerun()
