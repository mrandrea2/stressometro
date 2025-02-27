import streamlit as st

# Imposta lo sfondo verde chiaro
st.markdown(
    """
    <style>
    body {
        background-color: #d4edda; /* Verde chiaro */
    }
    h2 {
        font-size: 22px;
    }
    h3 {
        font-size: 20px;
    }
    .large-text {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #2d6a4f; /* Verde scuro */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titolo e autore
st.title("🏅 Stressometro per Atleti")
st.write("### Creato da Andrea Bertelli ©")

# Istruzioni per la compilazione
st.subheader("📝 Istruzioni")
st.write("""
Questo test ti aiuterà a valutare il tuo livello di stress sportivo.  
- **Si tratta di uno strumento di auto-monitoraggio**. I risultati **non vengono registrati** né inviati ad alcuna piattaforma.  
- Per ogni area, assegna un punteggio da **1 (basso) a 10 (alto)**.  
- Alla fine, otterrai un'analisi dettagliata e consigli utili per gestire lo stress sportivo.  
""")

# Aree di valutazione con descrizioni
aree = {
    "Stanchezza fisica": "Mi sento fisicamente affaticato dopo gli allenamenti o le gare.",
    "Qualità del sonno": "Dormo bene e mi sento riposato al mattino.",
    "Concentrazione": "Riesco a mantenere il focus in allenamento e in gara.",
    "Tensione muscolare": "Avverto rigidità e tensione muscolare senza una causa evidente.",
    "Pressione mentale": "Sento un carico mentale pesante a causa delle aspettative e della competizione.",
    "Ansia pre-gara": "Mi sento nervoso o agitato prima di competere.",
    "Motivazione": "Ho voglia di allenarmi e migliorarmi ogni giorno.",
    "Umore generale": "Mi sento sereno e positivo nella vita quotidiana e sportiva.",
    "Recupero": "Dopo uno sforzo, riesco a recuperare velocemente e in modo efficace.",
    "Gestione del tempo": "Riesco a organizzare bene allenamenti, studio/lavoro e vita personale."
}

# Creazione degli slider con descrizione
punteggi = []
for area, descrizione in aree.items():
    st.markdown(f"### **{area}**")  # Testo più grande e in grassetto
    st.write(f"*{descrizione}*")  
    punteggio = st.slider(f"{area}", 1, 10, 5, key=area)

    # Se l'area è positiva, inverto il punteggio senza indicarlo
    if area in ["Qualità del sonno", "Concentrazione", "Motivazione", "Umore generale", "Recupero", "Gestione del tempo"]:
        punteggio = 11 - punteggio  # Esempio: se scelgo 9, diventa 2

    punteggi.append(punteggio)

# Calcolo dell'indice di stress (0-100)
stress_index = int((sum(punteggi) / (10 * len(punteggi))) * 100)
st.subheader(f"**Indice di Stress: {stress_index}/100**")

# Analisi dettagliata con consigli specifici per atleti
st.subheader("📊 Interpretazione del tuo stress")

if stress_index <= 20:
    st.success("**Nessuno Stress ✅** - Ottima gestione mentale e fisica!")
    st.write("""
    **Consigli per mantenere il benessere sportivo:**  
    - Continua con il giusto equilibrio tra allenamenti, recupero e vita personale.  
    - Mantieni un focus positivo e lavora sulla consapevolezza corporea.  
    - Utilizza tecniche di visualizzazione e goal setting per consolidare il mindset vincente.  
    """)

elif stress_index <= 40:
    st.success("**Stress Moderato 🟢** - Sei in un buon equilibrio, ma puoi migliorare.")
    st.write("""
    **Strategie per ottimizzare la performance:**  
    - Cura il recupero con sonno regolare e stretching post-allenamento.  
    - Lavora sulla respirazione per migliorare la gestione della pressione pre-gara.  
    - Introduci tecniche di rilassamento muscolare progressivo per ridurre tensioni.  
    """)

elif stress_index <= 60:
    st.warning("**Stress Medio ⚠️** - Lo stress inizia a farsi sentire.")
    st.write("""
    **Azioni per migliorare la gestione dello stress:**  
    - Regola meglio il carico di allenamento per evitare overtraining.  
    - Fai esercizi di concentrazione e mindfulness per migliorare il focus in gara.  
    - Parla con il tuo coach o preparatore mentale per identificare strategie di miglioramento.  
    """)

elif stress_index <= 80:
    st.error("**Stress Alto 🟠** - Il tuo stress sta influenzando la performance.")
    st.write("""
    **Strategie di intervento:**  
    - Riduci la pressione interna con tecniche di self-talk positivo.  
    - Aumenta i momenti di defaticamento e cura la qualità del recupero.  
    - Se avverti sintomi di burnout, prenditi una pausa e riprogramma gli obiettivi.  
    """)

else:
    st.error("**Stress Molto Alto 🔴** - Attenzione, il livello di stress è critico!")
    st.write("""
    **Azioni urgenti per ridurre lo stress:**  
    - Consulta un esperto di psicologia dello sport per sviluppare strategie di gestione mentale.  
    - Riconsidera la programmazione degli allenamenti per ridurre il rischio di infortuni.  
    - Impara a gestire l'ansia con tecniche di rilassamento avanzate (meditazione, biofeedback).  
    """)

# Messaggio finale in grande
st.markdown('<p class="large-text">🔄 Compila il test una volta a settimana per monitorare il tuo stress!</p>', unsafe_allow_html=True)
