import streamlit as st
import pandas as pd
import altair as alt

st.header("Junge Menschen engagieren sich für die Umwelt")
st.subheader("")

source = pd.DataFrame({
        'Anteil derer, die oft oder sehr oft so gehandelt haben(%)': [62, 49, 47, 36, 23, 13],
        'Engagement': ['nutzen das Rad oder öffentliche Verkehrsmittel für alltägliche Wege', 'verzichten auf Plastikverpackungen', 'kaufen Bio-Produkte', 'leihen oder teilen sich Dinge, statt sie neu zu kaufen', 'unterstützen Online-Petitionen', 'nehmen an Klimastreiks teil']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil derer, die oft oder sehr oft so gehandelt haben(%):Q',
        x='Engagement:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    2021
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Zukunft? Jugend fragen! / Volker Haese")