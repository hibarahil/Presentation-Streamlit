import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta, time, date
import numpy as np
import plotly.express as px
import random



st.set_page_config(
    page_title="Projet IA - Streamlit",
    layout="wide",
    initial_sidebar_state="collapsed",
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Intro", "Streamlit", "Pourquoi Streamlit", "Exemples d'utilisation", "Conclusion"])

with tab1:
    st.title("🐍 Python : simple, puissant… et pas qu’un serpent !")
    st.subheader("📜 La grande histoire de Python, étape par étape")

    # Intro texte court
    st.markdown("""
    **Python** est un langage de programmation créé en **1989** par *Guido van Rossum*, dans le but de simplifier le langage éducatif **ABC**.  
    Contrairement à des langages comme **HTML**, **CSS** ou **JavaScript**, Python est **généraliste** : il peut être utilisé pour le web, l’IA, l’automatisation, la data, les logiciels…
    Son nom vient de la troupe comique britannique **Monty Python**, et non du serpent 🐍 — mais le symbole est resté !

    Aujourd’hui, Python est devenu l’un des langages les plus **populaires au monde** grâce à :
    - Sa **syntaxe simple et lisible**
    - Sa **courbe d’apprentissage douce**
    - Sa **polyvalence** (scripting, développement, IA, etc.)
    - Son **immense communauté** et ses **librairies puissantes** (comme *Pandas*, *Matplotlib*, *Scikit-learn*…)
    """)
    # Timeline des langages
    events = [
        ("1957", "🧮 **Fortran** – Le tout premier langage haut niveau, utilisé pour le calcul scientifique."),
        ("1972", "⚙️ **C** – Un langage performant qui servira de base à de nombreux autres."),
        ("1991", "🐍 **Python** – Facile à lire, puissant, utilisé aujourd’hui partout."),
        ("1995", "🌐 **JavaScript** – Le langage du web, devenu incontournable côté client comme serveur."),
        ("2014", "📱 **Swift** – Le langage moderne d’Apple pour développer des apps iOS/Mac."),
    ]

    cols = st.columns(len(events))

    for col, (year, description) in zip(cols, events):
        with col:
            st.markdown(f"### {year}")
            st.markdown(description)

    st.markdown("---")
    st.caption("✨ Made with ❤️ by Hiba")


with tab2:
    col_title, col_logo = st.columns([4, 1])

    with col_title:
        st.title("⚡ Découverte de Streamlit")

    with col_logo:
        st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")

    st.subheader("Créer des apps web interactives... en quelques lignes de Python")

    st.markdown("""
    **Streamlit** est un framework open source qui permet de transformer des scripts Python en **applications web interactives**.  
    Idéal pour la **data science**, les **dashboards** ou les **prototypes rapides**.
    """)

    st.markdown("### 🚀 Pourquoi c’est cool ?")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("🧠 **Simple**")
        st.caption("Pas besoin de HTML/CSS/JS")

    with col2:
        st.markdown("🎨 **Intuitif**")
        st.caption("Interface en Python pur")

    with col3:
        st.markdown("⚙️ **Interactif**")
        st.caption("Sliders, boutons, formulaires… en 1 ligne")

    st.markdown("### 💡 Ce qu’on peut créer avec Streamlit :")
    st.markdown("""
    - 📊 Dashboards de données  
    - 🤖 Interfaces pour modèles d’IA  
    - 📦 Outils internes (RH, marketing, etc.)  
    - 🧪 Prototypes d’outils interactifs
    """)

    st.success("🎯 *Avec Streamlit, tu fais des apps comme tu écris un notebook.*")

with tab3:
    st.title("🙋 Pourquoi j’ai choisi Streamlit ?")

    # Colonnes : texte à gauche, GIF à droite
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Un outil parfait pour transformer une idée en app fonctionnelle")

        st.markdown("""
        Quand on a voulu créer une interface interactive pour présenter un projet de data (**CoffeeShop**),  
        on s’est tourné naturellement vers **Streamlit** parce que c’était :
        
        - ✅ **Rapide** à prendre en main  
        - ✅ **Adapté aux datas et visualisations**  
        - ✅ **Sans besoin de maîtriser le web**  

        👉 En quelques heures, on avait une app claire, intuitive, et prête à être partagée.
        """)

        st.markdown("### 🔗 Découvrez le projet :")
        st.markdown("[☕ coffeshop.streamlit.app](https://coffeshop.streamlit.app/)", unsafe_allow_html=True)



    with col2:
        st.image("https://nationalcoffee.blog/wp-content/uploads/2016/09/coffee-wink.gif?w=603&h=451", use_container_width=True)

with tab4:
    st.title("🧪 Des cas d’usage concrets de Streamlit")

    subtab1, subtab2, subtab3,  = st.tabs([
        "📊 Dashboard interactif",
        "🤖 Generateur de Planning pour Memoire",
        "🍳 Generateur de recettes"
    ])

    with subtab1:
        st.title("📊 Dashboard interactif de révision mémoire")
        # Données simulées
        sujets = ["Introduction", "Méthodologie", "Analyse", "Résultats", "Conclusion"]
        start_date = datetime.today()
        dates = [start_date + timedelta(days=i) for i in range(14)]
        data = []

        for d in dates:
            for s in sujets:
                data.append({
                    "Date": d,
                    "Sujet": s,
                    "Heures_travail": round(random.uniform(0.5, 2.5), 2),
                    "Énergie": random.randint(50, 100)
                })

        df = pd.DataFrame(data)

        # --- Filtres ---
        st.sidebar.header("🎛️ Filtres")
        selected_sujets = st.sidebar.multiselect("📚 Sélectionner les sujets", sujets, default=sujets)
        date_range = st.sidebar.date_input("📅 Période", [dates[0].date(), dates[-1].date()])

        df_filtered = df[
            df["Sujet"].isin(selected_sujets) &
            (df["Date"].dt.date >= date_range[0]) &
            (df["Date"].dt.date <= date_range[1])
        ]

       # --- Statistiques bonus fun ---
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("### 🧠 Camille & les psyco")
            st.metric(label="Rencontres suspectes", value="13", delta="⚠️ 2 cette semaine")
        with col2 :
            st.markdown("### 🎬 Magdat au cinéma")
            st.metric(label="Films vus ce mois-ci", value="27", delta="✔️ Aucun raté")

        with col3:
            st.markdown("### 🗣️ Manal & Minho")
            st.metric(label="Mentions de Minho", value="+999", delta="🔥 234 rien qu’hier")
        with col4:
            st.markdown("### 🍕 Emma et le sport")
            st.metric(label="Reprises du sport annoncées", value="47", delta="❌ 0 effectives")

        # --- Graphiques ---
        st.markdown("### 📈 Heures travaillées par jour")
        fig1 = px.line(df_filtered, x="Date", y="Heures_travail", color="Sujet", markers=True)
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown("### 📊 Heures totales par sujet")
        fig2 = px.bar(df_filtered.groupby("Sujet")["Heures_travail"].sum().reset_index(), x="Sujet", y="Heures_travail", color="Sujet", text_auto=True)
        st.plotly_chart(fig2, use_container_width=True)

        # --- Détails tableau ---
        st.markdown("### 📄 Détail des sessions")
        st.dataframe(df_filtered.sort_values(by=["Date", "Sujet"]))


    with subtab2:
        st.markdown("## 📆 Planificateur de révisions intelligent")
        st.markdown("Optimisé avec de la **répétition espacée** et des créneaux bien répartis")

        sujets = st.text_area("📚 Liste des thèmes à réviser (1 par ligne)", placeholder="Intro\nMéthodo\nAnalyse\nConclusion")
        deadline = st.date_input("📅 Date de soutenance", min_value=date.today() + timedelta(days=1))

        dispo_start = st.time_input("🕘 Début des révisions chaque jour", value=time(8, 0))
        dispo_end = st.time_input("🕕 Fin des révisions chaque jour", value=time(19, 0))
        duree_session = st.number_input("⏱️ Durée de chaque session (min)", 30, 120, 60)

        if st.button("🗓️ Générer le planning"):
            sujets_liste = [s.strip() for s in sujets.split("\n") if s.strip()]
            if not sujets_liste:
                st.warning("Merci d’entrer au moins un sujet.")
            else:
                nb_jours = (deadline - date.today()).days + 1
                all_dates = [date.today() + timedelta(days=i) for i in range(nb_jours)]

                # Créneaux disponibles pour chaque jour
                heures_base = pd.date_range(
                    datetime.combine(date.today(), dispo_start),
                    datetime.combine(date.today(), dispo_end),
                    freq=f"{duree_session}min"
                ).time

                creneaux_disponibles = {jour: list(heures_base) for jour in all_dates}

                planning = []
                sujet_index = 0
                rep_map = {}  # sujet: [dates de révision]

                # Étape 1 : sessions de découverte
                for jour in all_dates:
                    while creneaux_disponibles[jour]:
                        heure = creneaux_disponibles[jour].pop(0)
                        if sujet_index >= len(sujets_liste):
                            break

                        sujet = sujets_liste[sujet_index]
                        planning.append({
                            "Date": jour.strftime("%a %d %b"),
                            "Heure": heure.strftime("%H:%M"),
                            "Sujet": f"(Découverte) {sujet}"
                        })

                        # Planifier répétitions à J+1, J+3, J+7
                        rep_map[sujet] = []
                        for delta in [1, 3, 7]:
                            rep_date = jour + timedelta(days=delta)
                            if rep_date in creneaux_disponibles and creneaux_disponibles[rep_date]:
                                rep_map[sujet].append(rep_date)
                        sujet_index += 1

                # Étape 2 : sessions de répétition
                for sujet, dates in rep_map.items():
                    for d in dates:
                        if creneaux_disponibles[d]:
                            heure = creneaux_disponibles[d].pop(0)
                            planning.append({
                                "Date": d.strftime("%a %d %b"),
                                "Heure": heure.strftime("%H:%M"),
                                "Sujet": f"(Révision) {sujet}"
                            })

                df = pd.DataFrame(planning).sort_values(by=["Date", "Heure"])
                st.success("✅ Planning généré avec créneaux répartis !")
                st.dataframe(df)

    with subtab3:
        st.markdown("## 🍳 Générateur de recettes")
        st.markdown("Tape les ingrédients que tu as dans ton frigo (séparés par des virgules) et découvre quoi cuisiner !")

        API_KEY = "58bfe6b9893b4b159748de36d1ebc38e"
        ingredients_input = st.text_input("🧺 Ingrédients :", placeholder="ex: tomato, oil etc... ")

        if st.button("🔍 Trouver des recettes") and ingredients_input:
            with st.spinner("Recherche en cours..."):
                try:
                    url = "https://api.spoonacular.com/recipes/findByIngredients"
                    params = {
                        "ingredients": ingredients_input,
                        "number": 3,
                        "ranking": 1,
                        "ignorePantry": True,
                        "apiKey": API_KEY
                    }
                    response = requests.get(url, params=params)
                    response.raise_for_status()
                    results = response.json()

                    if results:
                        for i in range(0, len(results), 3):
                            cols = st.columns(3)
                            for col, recipe in zip(cols, results[i:i+3]):
                                with col:
                                    st.markdown(f"### 🥘 {recipe['title']}")
                                    st.image(recipe['image'], use_container_width=True)
                                    used = ', '.join([ing['name'] for ing in recipe['usedIngredients']])
                                    missed = ', '.join([ing['name'] for ing in recipe['missedIngredients']])
                                    st.markdown(f"**✅ Ingrédients utilisés :** {used}")
                                    st.markdown(f"**❌ Ingrédients manquants :** {missed}")
                                    st.markdown("---")
                    else:
                        st.warning("Aucune recette trouvée. Essaie avec d’autres ingrédients.")
                except Exception as e:
                    st.error(f"Erreur lors de la récupération des recettes : {e}")

with tab5:
    col1, col2 = st.columns(2)
    with col1 :
        st.title("🎉 Merci d'avoir suivi cette présentation !")
        st.subheader("Et n’oubliez pas...")

        # Blague finale

        st.markdown("### ❤️ Streamlit, c’est magique parce que…")

        subcol1, subcol2 = st.columns(2)

        with subcol1:
            st.markdown("✔️ Rapide")
            st.markdown("✔️ Fun à coder")
            st.markdown("✔️ 100% Python")

        with subcol2:
            st.markdown("🚀 Idéal pour les projets étudiants")
            st.markdown("💡 Parfait pour les idées last-minute")
            st.markdown("😎 Impressionne les profs (et les collègues)")
    with col2 :
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzJ0ZDNhdDJjaWRtYnp6dGt6ZHAzNGhncnVpNDVoa2QxNWtpNHhvbyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l3vRlT2k2L35Cnn5C/giphy.gif", caption="Moi quand j'ai fini ma présentation")







