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
st.title("Stressometro per Atleti")
st.write("### Creato da Andrea Bertelli ©")

# Istruzioni per la compilazione
st.subheader("📝 Istruzioni")
st.write("""
Questo test ti aiuterà a valutare il tuo livello di stress attuale.  
- Si tratta di **uno strumento di auto-monitoraggio**. I risultati **non vengono registrati** né inviati ad alcuna piattaforma.  
- Per ogni area, assegna un punteggio da **1 (basso) a 10 (alto)**.  
- Alla fine, otterrai un'analisi dettagliata e consigli utili per gestire lo stress.  
""")

# Aree di valutazione con descrizioni
aree = {
    "Stanchezza fisica": "Quanto ti senti fisicamente affaticato dopo gli allenamenti o le competizioni?",
    "Qualità del sonno": "Dormo bene e mi sento riposato al mattino?",
    "Concentrazione": "Riesco a mantenere l'attenzione durante l'allenamento e la gara?",
    "Tensione muscolare": "Sento il mio corpo rigido o contratto senza un motivo apparente?",
    "Pressione mentale": "Sento il peso delle aspettative e la paura di fallire?",
    "Ansia pre-gara": "Mi sento nervoso o agitato prima di una competizione?",
    "Motivazione": "Ho voglia di allenarmi e migliorarmi ogni giorno?",
    "Umore generale": "Mi sento sereno e positivo nella vita quotidiana?",
    "Recupero": "Dopo uno sforzo, riesco a recuperare velocemente e in modo efficace?",
    "Gestione del tempo": "Sento di avere abbastanza tempo per gestire sport, studio/lavoro e vita personale?"
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

# Calcolo del punteggio totale
totale = sum(punteggi)
st.subheader(f"**Punteggio Totale: {totale}/100**")

# Analisi del risultato e consigli personalizzati
st.subheader("📊 Interpretazione del tuo stress")

if totale <= 30:
    st.success("**Basso Stress ✅** - Ottimo, continua a mantenere il tuo equilibrio!")
    st.write("""
    **Consigli per mantenere lo stato attuale:**  
    - Continua con una buona gestione del recupero e dello stress.  
    - Mantieni la tua routine di allenamenti e momenti di relax.  
    - Pratica tecniche di respirazione per consolidare il benessere mentale.  
    """)

elif totale <= 60:
    st.warning("**Medio Stress ⚠️** - Attenzione, potresti migliorare alcuni aspetti.")
    st.write("""
    **Consigli per ridurre lo stress:**  
    - Introduci tecniche di rilassamento come meditazione o stretching.  
    - Fai attenzione alla qualità del sonno e cerca di dormire almeno 7-8 ore a notte.  
    - Equilibra i tuoi impegni per non sovraccaricarti.  
    - Parla con il tuo allenatore o con un amico per affrontare eventuali preoccupazioni.  
    """)

else:
    st.error("**Alto Stress ❌** - Il tuo stress potrebbe compromettere le prestazioni e il benessere.")
    st.write("""
    **Strategie per affrontare lo stress:**  
    - Fai esercizi di rilassamento muscolare progressivo o mindfulness.  
    - Pianifica pause strategiche tra gli allenamenti per evitare il sovraccarico.  
    - Riduci l’auto-pressione e impara a concentrarti sul miglioramento progressivo.  
    - Se lo stress è troppo elevato, considera un confronto con un esperto di psicologia dello sport.  
    """)

# Messaggio finale in grande
st.markdown('<p class="large-text">🔄 Compila il test una volta a settimana per monitorare il tuo stress!</p>', unsafe_allow_html=True)
