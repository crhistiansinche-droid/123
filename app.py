import streamlit as st
import random
import time

# ==========================================
# BANCA DATI QUESITI COMPLETA (57 Domande)
# ==========================================
QUESTION_BANK = {
    "Modulo 1: Vettori e Geometria Vettoriale": [
        {"id": "M1_2021_T1A_Q2", "testo": "La norma del vettore x = (-2, √3, -1, 1) è:", "opzioni": {"a": "3", "b": "9", "c": "√3", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "||x|| = √((-2)² + (√3)² + (-1)² + 1²) = √(4 + 3 + 1 + 1) = √9 = 3.", "fonte": "Esame 2021 T1A (Quesito 2)"},
        {"id": "M1_2021_T1A_Q3", "testo": "Il valore di t per cui i vettori x1 = (1, 1, -1) e x2 = (t, -2, 2) sono linearmente dipendenti è:", "opzioni": {"a": "0", "b": "-2", "c": "2", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "I vettori sono proporzionali se x2 = -2 · x1 ⇒ t = -2.", "fonte": "Esame 2021 T1A (Quesito 3)"},
        {"id": "M1_2021_T2A_Q2", "testo": "Siano x = (1, 4, 0) e y = (-2, 5, 6). La distanza d(x, y) è:", "opzioni": {"a": "3", "b": "√17", "c": "√4", "d": "nessuna delle precedenti"}, "corretta": "d", "spiegazione": "d(x,y) = √((1 - (-2))² + (4 - 5)² + (0 - 6)²) = √(9 + 1 + 36) = √46, che non corrisponde ad a, b o c.", "fonte": "Esame 2021 T2A (Quesito 2)"},
        {"id": "M1_2021_T2A_Q4", "testo": "Quale tra le seguenti coppie costituisce una base di ℝ²?", "opzioni": {"a": "x1 = (2, 1) e x2 = (0, 2)", "b": "x1 = (1, 3) e x2 = (2, 6)", "c": "x1 = (0, 1) e x2 = (0, -1)", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "I due vettori (2,1) e (0,2) hanno determinante det = 4 - 0 = 4 ≠ 0, quindi sono linearmente indipendenti e formano una base.", "fonte": "Esame 2021 T2A (Quesito 4)"},
        {"id": "M1_2021_Sim_Q1", "testo": "Dati x = (2, 5, 1) e y = (a, 1, -3) in ℝ³, d(x,y) = 6 per:", "opzioni": {"a": "a = 0", "b": "a = -2", "c": "a = -1 oppure a = 0", "d": "nessuna delle precedenti"}, "corretta": "d", "spiegazione": "d(x,y)² = (a-2)² + 16 + 16 = 36 ⇒ (a-2)² = 4 ⇒ a = 0 oppure a = 4.", "fonte": "Simulazione 2021 (Quesito 1)"},
        {"id": "M1_2021_Sim_Q7", "testo": "I coefficienti c1, c2 della combinazione lineare del vettore x = (1, 2, 3) rispetto a y = (1, -1, 0) e z = (2, -1, 1) sono:", "opzioni": {"a": "c1 = 3 e c2 = -5", "b": "c1 = -5 e c2 = 3", "c": "c1 = -4 e c2 = 3", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "c1(1,-1,0) + c2(2,-1,1) = (1,2,3) ⇒ c2 = 3 e c1 + 2(3) = 1 ⇒ c1 = -5.", "fonte": "Simulazione 2021 (Quesito 7)"},
        {"id": "M1_2022_T1A_Q1", "testo": "La norma del vettore x = (-1, -2, 1, 2) è:", "opzioni": {"a": "10", "b": "0", "c": "3", "d": "nessuna delle precedenti"}, "corretta": "d", "spiegazione": "||x|| = √(1 + 4 + 1 + 4) = √10 ≈ 3.162 (la risposta a è 10, non √10).", "fonte": "Esame 2022 T1A (Quesito 1)"},
        {"id": "M1_2022_T1A_Q2", "testo": "I coefficienti c1, c2 della combinazione x = (2, 4, -3) rispetto a x1 = (0, 2, 1) e x2 = (1, 3, -1) sono:", "opzioni": {"a": "c1 = 1, c2 = 2", "b": "c1 = -1, c2 = 2", "c": "c1 = 2, c2 = -1", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "2 = c2 ⇒ c2 = 2; 4 = 2c1 + 3(2) ⇒ 2c1 = -2 ⇒ c1 = -1. Verifica terza componente: -1(1) + 2(-1) = -3.", "fonte": "Esame 2022 T1A (Quesito 2)"},
        {"id": "M1_2022_T2A_Q3", "testo": "Siano x = (3, 2, 0) e y = (1, -4, a). La distanza d(x, y) è pari a 7 per:", "opzioni": {"a": "a = 1", "b": "a = 3 oppure a = -3", "c": "a = 0", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "d(x,y)² = 4 + 36 + a² = 40 + a² = 49 ⇒ a² = 9 ⇒ a = ±3.", "fonte": "Esame 2022 T2A (Quesito 3)"},
        {"id": "M1_2022_T3A_Q1", "testo": "L'uguaglianza <(k, 2, 1) + (k, -1, 1), (k, 2, -2)> = 0 è vera per:", "opzioni": {"a": "k = 0", "b": "k = +2 e k = -2", "c": "k = +1 e k = -1", "d": "nessuna delle precedenti"}, "corretta": "c", "spiegazione": "Vettore somma: (2k, 1, 2). Prodotto scalare: 2k² + 2 - 4 = 2k² - 2 = 0 ⇒ k² = 1 ⇒ k = ±1.", "fonte": "Esame 2022 T3A (Quesito 1)"},
        {"id": "M1_2023_T1A_Q1", "testo": "La norma del vettore x = (-2, k, -1, 2k) è pari a 5 per:", "opzioni": {"a": "solo per k = 0", "b": "solo per k = 2", "c": "solo per k = 2 e k = -2", "d": "nessuna delle precedenti"}, "corretta": "c", "spiegazione": "||x||² = 4 + k² + 1 + 4k² = 5k² + 5 = 25 ⇒ 5k² = 20 ⇒ k = ±2.", "fonte": "Esame 2023 T1A (Quesito 1)"},
        {"id": "M1_2023_T2A_Q2", "testo": "La combinazione lineare dei vettori x1 = (1, -2, 3) e x2 = (0, -1, -2) con coefficienti c1 = 4 e c2 = 2 è il vettore z =", "opzioni": {"a": "(4, -10, 8)", "b": "(2, -10, 8)", "c": "(4, -10, 6)", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "4(1,-2,3) + 2(0,-1,-2) = (4, -8, 12) + (0, -2, -4) = (4, -10, 8).", "fonte": "Esame 2023 T2A (Quesito 2)"},
        {"id": "M1_2023_Sim_Q2", "testo": "Siano x = (0, 1, 1) e y = (k, k, 2). La distanza d(x, y) = 1 se e solo se:", "opzioni": {"a": "k = 0", "b": "k = 1", "c": "k = 2", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "d(x,y)² = 1 ⇒ 2k² - 2k + 1 = 0. Nessuna soluzione reale eccetto k=0. Quindi d) nessuna delle precedenti o k=0.", "fonte": "Simulazione 2023 (Quesito 2)"}
    ],
    "Modulo 2: Algebra Matriciale e Sistemi Lineari": [
        {"id": "M2_2021_T1A_Q1", "testo": "Siano A = [[0, 2], [1, 4]] e B = [[3, 1], [0, -1]]. Allora A + B =", "opzioni": {"a": "[[3, 2], [1, 3]]", "b": "[[3, 3], [0, 3]]", "c": "[[3, 3], [1, -4]]", "d": "[[3, 3], [1, 3]]"}, "corretta": "d", "spiegazione": "Somma componente per componente: [[0+3, 2+1], [1+0, 4+(-1)]] = [[3, 3], [1, 3]].", "fonte": "Esame 2021 T1A (Quesito 1)"},
        {"id": "M2_2021_T1A_Q4", "testo": "La matrice C = [[1, -1, k], [-1, 1, -1], [0, -1, 2]] è singolare:", "opzioni": {"a": "solo per k = 1", "b": "solo per k = 0", "c": "per ogni k ∈ ℝ", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "det(C) = 1 - 2 + k = k - 1. det(C) = 0 ⇔ k = 1.", "fonte": "Esame 2021 T1A (Quesito 4)"},
        {"id": "M2_2021_T1A_Q5", "testo": "Sia x ∈ ℝ⁴. Il sistema lineare [[1, -2, -2, 3], [1, -1, 2, 2]] x = [[4], [-1]] ammette:", "opzioni": {"a": "∞² soluzioni", "b": "un'unica soluzione", "c": "∞¹ soluzioni", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "Il sistema ha 2 equazioni e 4 incognite. Il rango è 2, per Rouché-Capelli vi sono ∞⁴⁻² = ∞² soluzioni.", "fonte": "Esame 2021 T1A (Quesito 5)"},
        {"id": "M2_2021_T2A_Q1", "testo": "Siano A = [[1, 4, 3], [2, 3, 1]] e B = [[3, 1], [-1, 2], [0, 1]]. Sia C = A · B. L'elemento c21 di C vale:", "opzioni": {"a": "non si può calcolare", "b": "vale 3", "c": "vale -1", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "c21 è il prodotto scalare tra la riga 2 di A e la colonna 1 di B: 6 - 3 + 0 = 3.", "fonte": "Esame 2021 T2A (Quesito 1)"},
        {"id": "M2_2021_T2A_Q3", "testo": "Per quali valori del parametro k ∈ ℝ il rango della matrice A = [[1, 4, k], [0, 3, 1], [0, 0, k]] è pari a 3?", "opzioni": {"a": "solo per k = 0", "b": "per ogni k ≠ 0", "c": "per ogni k ∈ ℝ", "d": "per ogni k ≥ 0"}, "corretta": "b", "spiegazione": "A è triangolare, det(A) = 3k. det(A) ≠ 0 ⇔ k ≠ 0. Quindi rg(A) = 3 per ogni k ≠ 0.", "fonte": "Esame 2021 T2A (Quesito 3)"},
        {"id": "M2_2022_T1A_Q4", "testo": "Il rango della matrice A = [[3, -3, -6], [-2, 2, 4]] è:", "opzioni": {"a": "rg(A) = 1", "b": "rg(A) = 2", "c": "rg(A) = 3", "d": "rg(A) = 0"}, "corretta": "a", "spiegazione": "La seconda riga è proporzionale alla prima: R2 = (-2/3)·R1. Tutte le sottomatrici 2x2 hanno det = 0. Il rango è 1.", "fonte": "Esame 2022 T1A (Quesito 4)"},
        {"id": "M2_2022_T2A_Q5", "testo": "Il rango della matrice B = [[1, 2, 2], [2, 4, 1], [-1, -2, 0]] è:", "opzioni": {"a": "Rg(B) = 1", "b": "Rg(B) = 2", "c": "Rg(B) = 3", "d": "Rg(B) = 0"}, "corretta": "b", "spiegazione": "La colonna 2 è il doppio della colonna 1, det(B) = 0. Trovando una sottomatrice 2x2 non singolare, il rango è 2.", "fonte": "Esame 2022 T2A (Quesito 5)"},
        {"id": "M2_2022_T2A_Q6", "testo": "Sia A = [[3, 1], [-2, 2]]. Allora det(A⁻¹) =", "opzioni": {"a": "4", "b": "1/4", "c": "1/8", "d": "nessuna delle precedenti"}, "corretta": "c", "spiegazione": "det(A) = (3)(2) - (1)(-2) = 8. Poiché det(A⁻¹) = 1 / det(A), si ottiene 1/8.", "fonte": "Esame 2022 T2A (Quesito 6)"},
        {"id": "M2_2022_T3A_Q2", "testo": "Siano A = [[-3, 1], [2, -2]] e B = [[2, -1], [-1, 0]]. Allora A - 3B =", "opzioni": {"a": "[[-6, -1], [3, -4]]", "b": "[[-9, 4], [5, -2]]", "c": "[[3, -2], [-1, -2]]", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "A - 3B = [[-3 - 6, 1 - (-3)], [2 - (-3), -2 - 0]] = [[-9, 4], [5, -2]].", "fonte": "Esame 2022 T3A (Quesito 2)"},
        {"id": "M2_2023_T1A_Q2", "testo": "Siano A = [[-1, 0, 0], [2, -3, 0]] e B = [[2, 3, 0], [1, 1, 0]]. Allora B - 2A =", "opzioni": {"a": "[[4, 3, 0], [-3, 7, 0]]", "b": "[[4, 3], [-3, 7]]", "c": "non esiste", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "B - 2A = [[2 - (-2), 3 - 0, 0 - 0], [1 - 4, 1 - (-6), 0 - 0]] = [[4, 3, 0], [-3, 7, 0]].", "fonte": "Esame 2023 T1A (Quesito 2)"},
        {"id": "M2_2023_T1A_Q3", "testo": "Sia A = [[0, -1, k], [0, k, 2], [1, 1-k, 2]] con k ∈ ℝ. Quale affermazione è vera?", "opzioni": {"a": "Se k = 1 allora det(A⁻¹) = 1/3", "b": "La matrice A è invertibile per ogni k ∈ ℝ", "c": "A⁻¹ esiste se e solo se k ≠ -2, 2", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "det(A) = -(k² + 2). Poiché k² + 2 > 0 per ogni k ∈ ℝ, det(A) ≠ 0 per ogni k. Quindi A è sempre invertibile.", "fonte": "Esame 2023 T1A (Quesito 3)"},
        {"id": "M2_2023_T2A_Q3", "testo": "Date A = [[1, 0, -1], [3, 1, 0], [0, 1, 0]] e B = [[2, -1, 4], [1, 0, -1]], quale delle seguenti è vera?", "opzioni": {"a": "A · B = B · A", "b": "le colonne di A sono linearmente dipendenti", "c": "Rango(B) = 2", "d": "nessuna delle precedenti"}, "corretta": "c", "spiegazione": "B ha 2 righe e 3 colonne con righe indipendenti, quindi Rango(B) = 2.", "fonte": "Esame 2023 T2A (Quesito 3)"}
    ],
    "Modulo 3: Proprietà Analitiche e Studio di Funzioni": [
        {"id": "M3_2021_T1A_Q6", "testo": "Date le funzioni f(x) = ln(x²) e g(x) = e^|x|, definite sui rispettivi domini:", "opzioni": {"a": "f è dispari e g è pari", "b": "f e g sono entrambe funzioni pari", "c": "f è pari e g è dispari", "d": "nessuna delle risposte precedenti"}, "corretta": "b", "spiegazione": "f(-x) = ln((-x)²) = ln(x²) = f(x) (pari); g(-x) = e^|-x| = e^|x| = g(x) (pari).", "fonte": "Esame 2021 T1A (Quesito 6)"},
        {"id": "M3_2021_T1A_Q8", "testo": "Il dominio della funzione f(x) = 1 / √(x² - 4x + 3) è:", "opzioni": {"a": "[1, 3]", "b": "(-∞, 1) ∪ (3, +∞)", "c": "(-∞, 1] ∪ [3, +∞)", "d": "(1, 3)"}, "corretta": "b", "spiegazione": "x² - 4x + 3 > 0 ⇒ x < 1 oppure x > 3.", "fonte": "Esame 2021 T1A (Quesito 8)"},
        {"id": "M3_2021_T1A_Q9", "testo": "Siano f(x) = 1 / x² e g(x) = ln(√x). Allora Dom(g ◦ f) =", "opzioni": {"a": "(0, +∞)", "b": "ℝ \\ {0}", "c": "(-∞, 0)", "d": "nessuna delle risposte precedenti"}, "corretta": "b", "spiegazione": "(g ◦ f)(x) = ln(√(1/x²)) = ln(1/|x|). L'argomento 1/|x| è definito e positivo per ogni x ≠ 0.", "fonte": "Esame 2021 T1A (Quesito 9)"},
        {"id": "M3_2021_T2A_Q6", "testo": "La funzione f(x) = 2x² + 2x è:", "opzioni": {"a": "superiormente limitata e max(f) = 1/2", "b": "inferiormente limitata e inf(f) = -1/2", "c": "illimitata sia inferiormente che superiormente", "d": "nessuna delle risposte precedenti"}, "corretta": "b", "spiegazione": "Trattasi di una parabola rivolta verso l'alto. Il vertice è in x_v = -1/2. Il minimo assoluto è f(-1/2) = -1/2.", "fonte": "Esame 2021 T2A (Quesito 6)"},
        {"id": "M3_2021_T2A_Q7", "testo": "Sia f: ℝ → ℝ definita da f(x) = ln(x+1) per x ≥ 0 e f(x) = -x² per x < 0. Allora f è:", "opzioni": {"a": "iniettiva e suriettiva", "b": "non iniettiva e Im(f) = [0, +∞)", "c": "iniettiva ma non suriettiva", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "Cresce da -∞ a 0 (escluso) e poi da 0 a +∞ in modo strettamente crescente. f è biettiva.", "fonte": "Esame 2021 T2A (Quesito 7)"},
        {"id": "M3_2022_T1A_Q9", "testo": "Siano f(x) = ln(x² - 2) e g(x) = e^x + 2. Allora g(f(x)) =", "opzioni": {"a": "x²", "b": "x² - 2", "c": "e^(ln(x²-2))", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "g(f(x)) = e^(ln(x²-2)) + 2 = (x² - 2) + 2 = x².", "fonte": "Esame 2022 T1A (Quesito 9)"},
        {"id": "M3_2022_T3A_Q5", "testo": "Date f(x) = x⁵ - 2x³ + 1, g(x) = x² e^|x|, h(x) = (x⁴ - x²) / (|x| + 1):", "opzioni": {"a": "f è dispari e g è pari", "b": "g e h sono funzioni pari", "c": "g è pari e h è dispari", "d": "nessuno dei precedenti"}, "corretta": "b", "spiegazione": "g(-x) = x² e^|x| = g(x) (pari); h(-x) = (x⁴ - x²) / (|x| + 1) = h(x) (pari).", "fonte": "Esame 2022 T3A (Quesito 5)"},
        {"id": "M3_2022_T3A_Q7", "testo": "Sia f(x) = e^(x³ + 1) - 2. L'espressione di f⁻¹ è:", "opzioni": {"a": "∛(ln(x+2) - 1)", "b": "∛(ln(x+2)) - 1", "c": "∛(ln(x+1) - 2)", "d": "f non è invertibile"}, "corretta": "b", "spiegazione": "y = e^(x³ + 1) - 2 ⇒ ln(y+2) = x³ + 1 ⇒ x = ∛(ln(y+2) - 1).", "fonte": "Esame 2022 T3A (Quesito 7)"},
        {"id": "M3_2023_T1A_Q8", "testo": "Il dominio della funzione f(x) = ln((x² - 2x) / (4 - x)) è:", "opzioni": {"a": "(-∞, 0)", "b": "(-∞, 0) ∪ (2, 4)", "c": "(-∞, 0] ∪ [2, 4)", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "La frazione è positiva per x < 0 oppure 2 < x < 4.", "fonte": "Esame 2023 T1A (Quesito 8)"},
        {"id": "M3_2023_T2A_Q5", "testo": "Date f(x) = e^(1-x²), g(x) = sin(x)/x, h(x) = x³ + x:", "opzioni": {"a": "f è dispari e g è pari", "b": "g e h sono funzioni dispari", "c": "g è pari e h è dispari", "d": "nessuna delle precedenti"}, "corretta": "c", "spiegazione": "g(-x) = sin(-x)/(-x) = sin(x)/x (pari); h(-x) = -(x³+x) (dispari).", "fonte": "Esame 2023 T2A (Quesito 5)"},
        {"id": "M3_2023_T2A_Q10", "testo": "Sia f(x) = 2 + ln(x - 1). L'espressione della funzione inversa f⁻¹ è:", "opzioni": {"a": "1 / (2 + ln(x-1))", "b": "e^(x-1) + 1", "c": "e^(x-2) + 1", "d": "e^(x-1) + 2"}, "corretta": "c", "spiegazione": "y - 2 = ln(x-1) ⇒ e^(y-2) = x - 1 ⇒ x = e^(y-2) + 1.", "fonte": "Esame 2023 T2A (Quesito 10)"}
    ],
    "Modulo 4: Topologia, Successioni e Teoria": [
        {"id": "M4_2021_T1A_Q11", "testo": "L'insieme dei punti di accumulazione di A = {3 - 1/n : n ∈ ℕ, n ≥ 1} è:", "opzioni": {"a": "[2, 3]", "b": "{3}", "c": "(2, 3)", "d": "nessuna delle risposte precedenti"}, "corretta": "b", "spiegazione": "Gli elementi tendono a 3 per n → +∞. L'unico punto di accumulazione è il valore limite 3.", "fonte": "Esame 2021 T1A (Quesito 11)"},
        {"id": "M4_2021_T2A_Q10", "testo": "La successione a_n = 1 se n è pari, a_n = n² se n è dispari:", "opzioni": {"a": "è divergente a +∞", "b": "è divergente a -∞", "c": "è irregolare", "d": "è convergente a 1"}, "corretta": "c", "spiegazione": "La sottosuccessione dei pari tende a 1, dei dispari a +∞. È irregolare.", "fonte": "Esame 2021 T2A (Quesito 10)"},
        {"id": "M4_2021_T2A_Q12", "testo": "Sia A = {x ∈ ℝ : 0 ≤ ln(x) ≤ 1} ∪ {5}. Allora:", "opzioni": {"a": "A è un insieme aperto", "b": "A è un insieme chiuso", "c": "A non è né aperto né chiuso", "d": "int(A) = ∅"}, "corretta": "b", "spiegazione": "0 ≤ ln(x) ≤ 1 ⇔ 1 ≤ x ≤ e. A = [1, e] ∪ {5}, chiuso.", "fonte": "Esame 2021 T2A (Quesito 12)"},
        {"id": "M4_2021_Sim_Q11", "testo": "L'insieme dei punti di frontiera dell'insieme A := {3, 5} ∪ [6, 10) è:", "opzioni": {"a": "{3, 4, 5}", "b": "{3, 5, 6, 10}", "c": "(6, 10)", "d": "{3, 4, 5, 6, 10}"}, "corretta": "b", "spiegazione": "Punti isolati 3,5. Estremi dell'intervallo 6,10. Frontiera = {3, 5, 6, 10}.", "fonte": "Simulazione 2021 (Quesito 11)"},
        {"id": "M4_2022_T1A_Q5", "testo": "Dato l'insieme A = {3 - 1/n² : n ∈ ℕ, n ≥ 1}:", "opzioni": {"a": "3 e 2 sono punti di accumulazione", "b": "tutti i punti di A sono isolati", "c": "0 è punto di frontiera", "d": "nessuna"}, "corretta": "b", "spiegazione": "Ciascun punto è distante dai suoi vicini, perciò è isolato (3 è di accumulazione ma non appartiene).", "fonte": "Esame 2022 T1A (Quesito 5)"},
        {"id": "M4_2023_T2A_Q7", "testo": "Sia (a_n)_{n≥0} una successione. Essa si dice STRETTAMENTE CRESCENTE se:", "opzioni": {"a": "a_n < a_{n+1} per ogni n ≥ 0", "b": "a_n ≤ a_{n+1} per ogni n ≥ 0", "c": "a_n > a_{n+1} per ogni n ≥ 0", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "Per definizione rigorosa: a_n < a_{n+1} per ogni n ≥ 0.", "fonte": "Esame 2023 T2A (Quesito 7)"},
        {"id": "M4_2023_T2A_Q11", "testo": "La successione a_n := (1 + log(n)) / (n³ + √n):", "opzioni": {"a": "è superiormente illimitata", "b": "converge a 0", "c": "è irregolare", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "Il polinomio n³ domina la crescita logaritmica del numeratore. Il limite è 0.", "fonte": "Esame 2023 T2A (Quesito 11)"},
        {"id": "M4_2023_Sim_Q7", "testo": "Un elemento M ∈ ℝ è un MAGGIORANTE per un insieme non vuoto A ⊆ ℝ se:", "opzioni": {"a": "x ≤ M per ogni x ∈ A", "b": "x ≥ M per ogni x ∈ A", "c": "x < M per ogni x ∈ A", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "Per definizione: x ≤ M per ogni x ∈ A.", "fonte": "Simulazione 2023 (Quesito 7)"}
    ],
    "Modulo 5: Limiti e Lettura Grafica": [
        {"id": "M5_2021_T1A_Q10", "testo": "Sia f(x) = 1/(x²-1) per x > -1 e f(x) = ∛(x-1) per x ≤ -1. Allora lim_{x → -1} f(x):", "opzioni": {"a": "0", "b": "non esiste", "c": "1", "d": "-∞"}, "corretta": "b", "spiegazione": "Da sx lim è ∛(-2). Da dx è -∞. I limiti differiscono, quindi non esiste.", "fonte": "Esame 2021 T1A (Quesito 10)"},
        {"id": "M5_2022_T1A_Q11", "testo": "Il valore del limite lim_{n → +∞} (√(9n² + 4) - 3n) è:", "opzioni": {"a": "+∞", "b": "0", "c": "1/2", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "Moltiplicando e dividendo per il coniugato: 4 / (√(9n²+4) + 3n) = 0.", "fonte": "Esame 2022 T1A (Quesito 11)"},
        {"id": "M5_2022_T1A_Q12", "testo": "Il limite lim_{x → +∞} (cos x - 4x²) / x è:", "opzioni": {"a": "-∞", "b": "0", "c": "+∞", "d": "-4"}, "corretta": "a", "spiegazione": "(cos x)/x - 4x = 0 - ∞ = -∞.", "fonte": "Esame 2022 T1A (Quesito 12)"},
        {"id": "M5_2022_T2A_Q1", "testo": "Il valore del limite lim_{x → 1} (x² - 3x + 2) / (x - 1) è:", "opzioni": {"a": "1", "b": "-1", "c": "0", "d": "nessuna delle precedenti"}, "corretta": "b", "spiegazione": "(x - 1)(x - 2) / (x - 1) = x - 2. In x=1 fa -1.", "fonte": "Esame 2022 T2A (Quesito 1)"},
        {"id": "M5_2022_T2A_Q2", "testo": "Il valore del limite lim_{n → +∞} (√(n² - 2) - √(n² - 4)) è:", "opzioni": {"a": "0", "b": "+∞", "c": "2", "d": "nessuna delle precedenti"}, "corretta": "a", "spiegazione": "Per coniugazione: 2 / (√(n²-2) + √(n²-4)) = 0.", "fonte": "Esame 2022 T2A (Quesito 2)"},
        {"id": "M5_2023_T1A_Q12", "testo": "Il limite lim_{x → -∞} (x³ + 1) / (x + e^x) è:", "opzioni": {"a": "-∞", "b": "0", "c": "+∞", "d": "1"}, "corretta": "c", "spiegazione": "Per x → -∞, e^x → 0. Rimane lim_{x → -∞} x³/x = +∞.", "fonte": "Esame 2023 T1A (Quesito 12)"},
        {"id": "M5_2023_Sim_Q9", "testo": "Il limite lim_{x → +∞} tan(1/x) · √(x² + x + e⁻ˣ) è:", "opzioni": {"a": "-∞", "b": "0", "c": "+∞", "d": "1"}, "corretta": "d", "spiegazione": "Per x → +∞, tan(1/x) ∼ 1/x e √(x² + x) ∼ x. (1/x)*x = 1.", "fonte": "Simulazione 2023 (Quesito 9)"}
    ],
    "Modulo 6: Grafici e Trasformazioni Geometriche": [
        {"id": "M6_2021_T2A_Q11", "testo": "Il grafico della funzione f(x) = |2^x - 4| si ottiene da 2^x traslando in basso di 4 e poi:", "opzioni": {"a": "ribaltando verso l'alto la porzione con y < 0 per l'effetto del valore assoluto", "b": "riflettendo specularmente la parte x ≥ 0", "c": "ruotando il grafico", "d": "nessuna"}, "corretta": "a", "spiegazione": "Il valore assoluto esterno ribalta la parte negativa creando un punto angoloso in (2, 0).", "fonte": "Esame 2021 T2A (Quesito 11)"},
        {"id": "M6_2022_T1A_Q10", "testo": "Per tracciare il grafico qualitativo di f(x) = ln|x - 2|, si applicano nell'ordine:", "opzioni": {"a": "traslazione a dx di 2 di ln(x) e simmetria speculare rispetto alla retta x = 2", "b": "valore assoluto su ln(x) e poi traslazione", "c": "ribaltamento verso l'alto per y < 0", "d": "nessuna"}, "corretta": "a", "spiegazione": "Il modulo dell'argomento riflette specularmente rispetto all'asintoto x = 2.", "fonte": "Esame 2022 T1A (Quesito 10)"},
        {"id": "M6_2022_T2A_Q12", "testo": "Il grafico qualitativo di f(x) = √|x + 1| presenta:", "opzioni": {"a": "un punto angoloso in (-1, 0) ed è simmetrico rispetto alla retta x = -1", "b": "un asintoto verticale in x = -1", "c": "un punto di massimo", "d": "nessuna"}, "corretta": "a", "spiegazione": "La traslazione a sx seguita dal modulo dell'argomento crea un punto angoloso simmetrico in x = -1.", "fonte": "Esame 2022 T2A (Quesito 12)"},
        {"id": "M6_2022_T3A_Q12", "testo": "Il grafico qualitativo di f(x) = e^|x| - 2 presenta un punto angoloso in:", "opzioni": {"a": "(0, -1)", "b": "(0, 1)", "c": "(2, 0)", "d": "nessuna"}, "corretta": "a", "spiegazione": "e^|x| ha punto angoloso in (0,1). Abbassato di 2 scende a (0, -1).", "fonte": "Esame 2022 T3A (Quesito 12)"},
        {"id": "M6_2023_T1A_Q10", "testo": "Il grafico della funzione f(x) = |ln(x - 1)| presenta:", "opzioni": {"a": "un punto angoloso sull'asse x nel punto (2, 0) con asintoto verticale in x = 1", "b": "asintoto orizzontale", "c": "massimo in x=2", "d": "nessuna"}, "corretta": "a", "spiegazione": "Il log si annulla in 2. Il modulo ribalta la parte sotto l'asse X creando il punto angoloso in (2,0).", "fonte": "Esame 2023 T1A (Quesito 10)"},
        {"id": "M6_2023_T2A_Q12", "testo": "Il grafico di f(x) = e^|x - 1| si ottiene da e^|x|:", "opzioni": {"a": "traslando il grafico a dx di 1 unità, ponendo il punto angoloso in (1, 1)", "b": "traslando in alto di 1 unità", "c": "ribaltando rispetto all'asse x", "d": "nessuna"}, "corretta": "a", "spiegazione": "x-1 genera traslazione verso destra di 1 unità.", "fonte": "Esame 2023 T2A (Quesito 12)"}
    ]
}

# ==========================================
# FUNZIONI LOGICHE DEL QUIZ
# ==========================================
def genera_quiz_bilanciato():
    quiz = []
    struttura_moduli = [
        ("Modulo 1: Vettori e Geometria Vettoriale", 2),
        ("Modulo 2: Algebra Matriciale e Sistemi Lineari", 2),
        ("Modulo 3: Proprietà Analitiche e Studio di Funzioni", 3),
        ("Modulo 4: Topologia, Successioni e Teoria", 2),
        ("Modulo 5: Limiti e Lettura Grafica", 2),
        ("Modulo 6: Grafici e Trasformazioni Geometriche", 1),
    ]

    domanda_num = 1
    for modulo_nome, quantita in struttura_moduli:
        quesiti_disponibili = QUESTION_BANK.get(modulo_nome, [])
        if quesiti_disponibili:
            estratti = random.sample(quesiti_disponibili, min(quantita, len(quesiti_disponibili)))
            for q in estratti:
                q_copy = dict(q)
                q_copy["numero_esame"] = domanda_num
                q_copy["modulo"] = modulo_nome
                quiz.append(q_copy)
                domanda_num += 1
    return quiz

# ==========================================
# INTERFACCIA STREAMLIT (Web-App iOS compatibile)
# ==========================================
st.set_page_config(page_title="Simulatore Matematica I", page_icon="🎓", layout="centered")

# Inizializza le variabili di sessione per gestire i passaggi della web-app
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'quiz' not in st.session_state:
    st.session_state.quiz = []
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

def go_to_quiz():
    st.session_state.quiz = genera_quiz_bilanciato()
    st.session_state.current_index = 0
    st.session_state.user_answers = {}
    st.session_state.start_time = time.time()
    st.session_state.page = 'quiz'

def go_to_results():
    st.session_state.page = 'results'


# --- SCHERMATA HOME ---
if st.session_state.page == 'home':
    st.title("🎓 Simulatore d'Esame")
    st.subheader("Matematica I (ECO0100)")
    
    st.markdown("""
    **Regolamento della Prova:**
    - **Durata:** 40 Minuti *(il timer si aggiorna ad ogni cambio di domanda)*
    - **Quesiti:** 12 domande a scelta multipla, bilanciate per Modulo
    - **Punteggio:** 1 punto a risposta, soglia minima **6/12**
    - Sviluppata per funzionare interamente su Browser / iOS
    """)
    
    st.info(f"📚 La banca dati attualmente caricata contiene **57 quesiti ufficiali** (Simulazioni 2021-2023).")
    
    if st.button("▶ AVVIA SIMULAZIONE (40 MINUTI)", type="primary"):
        go_to_quiz()
        st.rerun()

# --- SCHERMATA QUIZ ---
elif st.session_state.page == 'quiz':
    # Gestione Timer
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, 40 * 60 - elapsed)
    
    if remaining == 0:
        st.error("⏱ Tempo scaduto! La prova verrà consegnata automaticamente.")
        time.sleep(2)
        go_to_results()
        st.rerun()
        
    m, s = divmod(int(remaining), 60)
    st.info(f"⏱ **Tempo Rimanente:** {m:02d}:{s:02d}")

    # Domanda Corrente
    q = st.session_state.quiz[st.session_state.current_index]
    
    st.caption(f"📍 **Domanda {st.session_state.current_index + 1} di {len(st.session_state.quiz)}** | {q['modulo']}")
    st.markdown(f"#### {q['testo']}")
    
    # Formatta opzioni
    lettere_possibili = ['a', 'b', 'c', 'd']
    opzioni_testo = []
    mappa_scelte = {}
    
    for l in lettere_possibili:
        if l in q['opzioni']:
            testo_opzione = f"{l}) {q['opzioni'][l]}"
            opzioni_testo.append(testo_opzione)
            mappa_scelte[testo_opzione] = l
            
    # Recupera l'indice della risposta salvata (se l'utente torna indietro)
    risposta_salvata = st.session_state.user_answers.get(q['id'])
    idx_risposta = None
    if risposta_salvata:
        for i, testo_opt in enumerate(opzioni_testo):
            if mappa_scelte[testo_opt] == risposta_salvata:
                idx_risposta = i
                break
    
    # Radio Buttons Streamlit
    scelta = st.radio("Seleziona un'opzione:", opzioni_testo, index=idx_risposta, key=q['id'])
    
    if scelta:
        # Salva la lettera scelta dall'utente (estrapolandola tramite il mapping)
        st.session_state.user_answers[q['id']] = mappa_scelte[scelta]
        
    st.divider()
    
    # Bottoni di navigazione in colonne
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.session_state.current_index > 0:
            if st.button("◄ Precedente"):
                st.session_state.current_index -= 1
                st.rerun()
                
    with col2:
        if st.session_state.current_index < len(st.session_state.quiz) - 1:
            if st.button("Successiva ►"):
                st.session_state.current_index += 1
                st.rerun()
                
    with col3:
        if st.button("✓ CONCLUDI E INVIA", type="primary"):
            go_to_results()
            st.rerun()

# --- SCHERMATA RISULTATI ---
elif st.session_state.page == 'results':
    st.title("Esito della Simulazione")
    
    # Calcolo punteggio
    punteggio = sum(
        1 for q in st.session_state.quiz 
        if st.session_state.user_answers.get(q['id']) == q['corretta']
    )
            
    if punteggio >= 6:
        st.success(f"🎉 **PROVA SUPERATA!** Hai totalizzato {punteggio} / 12 punti.")
    else:
        st.error(f"❌ **PROVA NON SUPERATA.** Hai totalizzato {punteggio} / 12 punti. (Soglia minima: 6/12)")
        
    st.subheader("Revisione Dettagliata Quesiti")
    
    for i, q in enumerate(st.session_state.quiz):
        risposta_data = st.session_state.user_answers.get(q['id'], 'nessuna')
        esatta = (risposta_data == q['corretta'])
        
        icon = "✅" if esatta else "❌"
        with st.expander(f"{icon} Quesito {i+1} - {q['modulo']}"):
            st.markdown(f"**{q['testo']}**")
            st.write(f"La tua risposta: **[{risposta_data.upper()}]**")
            st.write(f"Risposta corretta: **[{q['corretta'].upper()}]**")
            
            if not esatta:
                st.warning("Hai commesso un errore o saltato il quesito in questa domanda.")
                
            st.info(f"💡 **Svolgimento:** {q['spiegazione']}")
            st.caption(f"Fonte originaria: {q['fonte']}")
            
    st.divider()
    if st.button("🔄 RITORNA ALLA HOME E RIPROVA"):
        st.session_state.page = 'home'
        st.rerun()
