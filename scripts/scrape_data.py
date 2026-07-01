import os
import json

def main():
    print("Démarrage de la génération des données de santé enrichies...")
    
    # Créer le répertoire de données
    os.makedirs("data", exist_ok=True)
    
    # 1. Prévention du Paludisme (Source: SP/Palu, INSD EDSBF-V 2021 & Ministère de la Santé)
    palu_content = """# Prévention et Prise en Charge du Paludisme au Burkina Faso
*Source des données : Secrétariat Permanent pour l'élimination du paludisme (SP/Palu) & Institut National de la Statistique et de la Démographie (INSD) - Enquête Démographique et de Santé (EDSBF-V 2021)*

## 1. Contexte épidémiologique
Le paludisme demeure le principal motif de consultation et d'hospitalisation au Burkina Faso. Il frappe de manière disproportionnée les enfants de moins de 5 ans et les femmes enceintes. Selon les données de l'INSD (EDSBF-V 2021) et les rapports de veille du SP/Palu, la prévalence reste préoccupante avec de fortes disparités régionales (les régions des Cascades et du Sud-Ouest affichant les taux de prévalence les plus élevés par rapport à la moyenne nationale).

## 2. Stratégies Nationales de Prévention et de Lutte
Le Ministère de la Santé et de l'Hygiène Publique met en œuvre plusieurs interventions clés, coordonnées par le SP/Palu :

*   **Chimio-prévention du paludisme saisonnier (CPS) :**
    *   **Cible :** Enfants de 3 à 59 mois.
    *   **Protocole :** Administration mensuelle d'une combinaison d'antipaludiques (Sulfadoxine-Pyriméthamine + Amodiaquine) durant la haute saison de transmission (généralement de juillet à octobre). La CPS permet d'éviter plus de 75 % des cas de paludisme simple et grave chez cette population vulnérable.
*   **Vaccination antipaludique (Vaccin RTS,S) :**
    *   **Introduction :** Le Burkina Faso a intégré le vaccin antipaludique (RTS,S) dans son Programme Élargi de Vaccination (PEV) de routine.
    *   **Schéma vaccinal :** Composé de 4 doses administrées respectivement aux âges de 5 mois, 6 mois, 7 mois, et une dose de rappel à 15 mois.
*   **Moustiquaires Imprégnées d'Insecticide à Longue Durée d'Action (MILDA) :**
    *   Le ministère organise périodiquement des campagnes nationales de distribution gratuite de MILDA.
    *   La recommandation officielle est de faire dormir chaque membre de la famille, en priorité les femmes enceintes et les enfants de moins de 5 ans, sous une MILDA toutes les nuits de l'année.
*   **Traitement Préventif Intermittent chez la femme enceinte (TPIg) :**
    *   Administration systématique et gratuite de la Sulfadoxine-Pyriméthamine (SP) lors des Consultations Prénatales (CPN) à partir du deuxième trimestre de grossesse. Au moins 3 doses de SP sont indispensables pour protéger la mère et le fœtus.

## 3. Symptômes, Diagnostic et Gratuité des Soins
*   **Symptômes suspects :** Fièvre élevée ou modérée, frissons, maux de tête (céphalées), douleurs musculaires, fatigue générale et vomissements.
*   **Test de Diagnostic Rapide (TDR) :** Devant tout cas suspect de fièvre, il est impératif de se rendre immédiatement dans une formation sanitaire (CSPS, CM) pour effectuer un TDR. Le diagnostic précoce permet d'éviter les complications graves.
*   **Politique de gratuité des soins :** Les soins de santé liés au diagnostic (TDR) et aux traitements du paludisme simple ou grave sont **entièrement gratuits** pour les enfants de moins de 5 ans et les femmes enceintes dans toutes les formations sanitaires publiques du pays.
*   **Danger de l'automédication :** Traiter une fièvre suspecte sans diagnostic médical (TDR ou microscopie) comporte le risque d'évolution vers un paludisme grave (complications neurologiques, anémie sévère, décès). Les traitements de référence pour le paludisme simple sont les Combinaisons Thérapeutiques à base d'Artémisinine (CTA) prescrites par un agent de santé qualifié.
"""

    with open(os.path.join("data", "prevention_paludisme.md"), "w", encoding="utf-8") as f:
        f.write(palu_content)
    print("- Fichier prevention_paludisme.md créé.")
        
    # 2. Prévention de la Dengue (Source: Ministère de la Santé & OMS)
    dengue_content = """# Prévention et Symptômes de la Dengue au Burkina Faso
*Source des données : Ministère de la Santé et de l'Hygiène Publique du Burkina Faso & Organisation Mondiale de la Santé (OMS)*

## 1. Description de la maladie
La dengue est une arbovirose transmise par la piqûre de moustiques femelles infectés du genre *Aedes* (notamment *Aedes aegypti*, appelé moustique tigre). Au Burkina Faso, le nombre de cas augmente généralement en fin de saison des pluies (entre septembre et novembre), particulièrement dans les centres urbains comme Ouagadougou et Bobo-Dioulasso.

## 2. Lutte Vectorielle et Mesures de Prévention
Le vecteur de la dengue (*Aedes*) se distingue de l'anophèle (vecteur du paludisme) par ses habitudes : il pique principalement durant la journée (au lever du soleil et en fin d'après-midi) et se reproduit dans des collections d'eau propre stagnante à proximité immédiate des habitations.

*   **Destruction des gîtes larvaires (Action prioritaire) :**
    *   Vider et nettoyer au moins une fois par semaine les coupelles des pots de fleurs, les récipients en plastique et les boîtes de conserve abandonnés.
    *   Éliminer les pneus usagés qui recueillent l'eau de pluie.
    *   Couvrir de façon hermétique tous les réservoirs et jarres de stockage d'eau domestique.
*   **Protection individuelle contre les piqûres diurnes :**
    *   Porter des vêtements amples, longs et de couleur claire pour couvrir la peau.
    *   Appliquer des répulsifs cutanés anti-moustiques agréés (contenant du DEET, de l'Icaridine ou de l'IR3535).
    *   Dormir sous une moustiquaire imprégnée (MILDA), y compris en journée pour les nourrissons, les femmes enceintes et les personnes malades.
    *   Utiliser des moustiquaires aux fenêtres et aux portes des habitations.

## 3. Symptômes et Alerte Médicale
*   **Symptômes caractéristiques :** Fièvre bruteale et très élevée (40°C), céphalées intenses, douleur rétro-orbitaire (derrière les yeux), arthralgies et myalgies (douleurs articulaires et musculaires prononcées, appelées "fièvre brise-os"), nausées, vomissements et éruption cutanée.
*   **Formes sévères :** Dans certains cas, la maladie évolue vers la dengue sévère (ou dengue hémorragique), caractérisée par des saignements des gencives, du nez ou gastro-intestinaux, des douleurs abdominales sévères et une défaillance circulatoire.
*   **CONSIGNE DE SÉCURITÉ CRITIQUE (Contre-indication médicamenteuse) :**
    *   En cas de suspicion de dengue, **l'utilisation d'acide acétylsalicylique (Aspirine), d'Ibuprofène ou de tout autre Anti-Inflammatoire Non Stéroïdien (AINS) est STRICTEMENT INTERDITE**. Ces molécules fluidifient le sang et majorent dramatiquement le risque d'hémorragies mortelles.
    *   Le seul traitement symptomatique autorisé de première intention est le **Paracétamol** pour soulager la douleur et faire baisser la fièvre (respecter la posologie maximale de 3g par jour chez l'adulte et les doses pédiatriques appropriées).
    *   Consulter d'urgence le centre de santé (CSPS ou CMA) le plus proche pour une évaluation clinique.
"""

    with open(os.path.join("data", "prevention_dengue.md"), "w", encoding="utf-8") as f:
        f.write(dengue_content)
    print("- Fichier prevention_dengue.md créé.")

    # 3. Directives Nutritionnelles (Source: ST/Nut, Direction de la Nutrition & Politique Nationale)
    nutrition_content = """# Nutrition et Bonnes Pratiques Alimentaires au Burkina Faso
*Source des données : Secrétariat technique chargé de la multisectorialité pour la nutrition (ST/Nut) & Direction de la Nutrition - Ministère de la Santé du Burkina Faso*

## 1. Défis de la transition nutritionnelle et malnutrition
Le Burkina Faso est confronté à la persistance de la malnutrition sous toutes ses formes (retard de croissance ou malnutrition chronique, émaciation ou malnutrition aiguë, et carences en micronutriments), ainsi qu'à l'émergence du surpoids et de l'obésité en milieu urbain.
*   **Malnutrition Chronique (Retard de croissance) :** Touche près d'un enfant de moins de 5 ans sur cinq. Elle a des conséquences permanentes sur le développement physique et les facultés cognitives.
*   **Malnutrition Aiguë (Émaciation) :** Les taux dépassent parfois les seuils d'alerte (10 à 15 %) dans les régions soumises à l'insécurité alimentaire ou aux déplacements de populations (Est, Sahel, Nord, Centre-Nord), affectant l'accès aux terres agricoles et aux marchés.

## 2. Bonnes pratiques de Nutrition Maternelle, du Nourrisson et du Jeune Enfant (NM-ANJE)
La Direction de la Nutrition formule les recommandations prioritaires suivantes :
*   **Mise au sein précoce :** Allaiter le nouveau-né dans l'heure qui suit l'accouchement. Le colostrum (premier lait jaunâtre) est le premier vaccin naturel de l'enfant car il contient des concentrations élevées d'anticorps protecteurs.
*   **Allaitement Maternel Exclusif (AME) :** Administrer exclusivement du lait maternel au nourrisson de la naissance jusqu'à 6 mois révolus. Aucun autre aliment solide ou liquide (ni même de l'eau, sauf médicament prescrit par un médecin) ne doit être administré (Campagne nationale « Plus fort avec le lait maternel uniquement »).
*   **Alimentation de complément diversifiée :** À partir de 6 mois, introduire de manière progressive des aliments semi-solides puis solides (bouillies enrichies) de bonne qualité nutritionnelle tout en poursuivant l'allaitement maternel jusqu'à 2 ans ou au-delà.

## 3. Valorisation et utilisation des ressources alimentaires locales
Pour satisfaire les besoins nutritionnels et prévenir les anémies et autres carences (fer, vitamine A), il convient d'inclure les groupes d'aliments locaux suivants dans les repas :
1.  **Aliments Énergétiques :** Fournissent l'énergie essentielle à l'organisme.
    *   *Sources burkinabè :* Mil rouge et blanc, sorgho blanc, maïs jaune, riz local, patate douce, igname, manioc, beurre de karité, huile de coton raffinée.
2.  **Aliments Constructeurs (Protéines) :** Nécessaires pour la croissance cellulaire et musculaire.
    *   *Sources burkinabè :* Haricot local (Niébé), soja dégraissé, graines d'arachide, poulet local, œufs de volaille, poisson séché ou frais, chenilles de karité (Chitoumou - d'une grande richesse en protéines biodisponibles et en fer).
3.  **Aliments Protecteurs (Vitamines et Sels Minéraux) :** Stimulent le système immunitaire pour lutter contre les agressions infectieuses (paludisme, infections respiratoires).
    *   *Sources burkinabè :* Feuilles fraîches ou séchées de Moringa oleifera (riche en calcium, fer, protéines et vitamines), feuilles de baobab, soumbala (néré fermenté - excellent régulateur de la pression artérielle et riche en fer), patate douce à chair orange (très riche en bêtacarotène / vitamine A), mangues, papayes locales, goyaves, tomates fraîches.

## 4. Recommandations de préparation des bouillies de sevrage (6-23 mois)
Une bouillie composée uniquement d'eau et de farine de céréales est carencée et expose l'enfant à la malnutrition. Il convient de préparer des **bouillies locales enrichies** :
*   Enrichir la farine de mil ou de maïs avec de la farine de soja torréfié ou de la pâte d'arachide (apport en protéines).
*   Ajouter du sucre raffiné ou un filet d'huile végétale locale (apport en énergie concentrée).
*   Intégrer de la poudre de feuilles de Moringa séchées ou quelques gouttes de citron/mangue écrasée (apport en micronutriments et vitamine C qui favorise l'absorption du fer).

## 5. Hygiène alimentaire et prévention hydrique
Pour prévenir les maladies diarrhéiques et la typhoïde qui aggravent l'état nutritionnel des enfants :
*   Toujours se laver les mains à l'eau courante et au savon avant de préparer ou de consommer les repas.
*   **Faire bouillir l'eau de boisson** provenant de sources non contrôlées ou incertaines (puits, marigots) avant de la consommer ou de l'utiliser pour préparer les aliments des jeunes enfants.
"""

    with open(os.path.join("data", "directives_nutrition.md"), "w", encoding="utf-8") as f:
        f.write(nutrition_content)
    print("- Fichier directives_nutrition.md créé.")

    # 4. Annuaire des Pharmacies (Ouagadougou & Bobo-Dioulasso)
    pharmacies_data = {
        "Ouagadougou": [
            {"nom": "Pharmacie Agoro Rood-Woko", "quartier": "Centre-ville (Rood-Woko)", "adresse": "Marché Rood-Woko, face à DIACFA Librairie", "tel": "+226 25 30 88 90", "garde_groupe": "A"},
            {"nom": "Pharmacie Dapoya", "quartier": "Dapoya", "adresse": "Face immeuble Acimex, Sankar-Yaaré", "tel": "+226 25 31 32 01", "garde_groupe": "A"},
            {"nom": "Pharmacie de la Patte d'Oie", "quartier": "Patte d'Oie", "adresse": "Près de l'échangeur de la Patte d'Oie, face station Shell", "tel": "+226 25 38 01 02", "garde_groupe": "A"},
            {"nom": "Pharmacie Sangoulé Lamizana", "quartier": "Centre-ville", "adresse": "Avenue Yennega, à côté de Marina Market", "tel": "+226 25 41 13 00", "garde_groupe": "B"},
            {"nom": "Pharmacie Cathédrale", "quartier": "Centre-ville", "adresse": "38 Avenue de la Cathédrale, face à la station TOTAL", "tel": "+226 25 31 28 40", "garde_groupe": "B"},
            {"nom": "Pharmacie Karpala", "quartier": "Karpala", "adresse": "Avenue principale de Karpala, face au marché", "tel": "+226 25 48 30 11", "garde_groupe": "B"},
            {"nom": "Pharmacie Cité An III", "quartier": "Larlé", "adresse": "En face de la maternité Pogbi", "tel": "+226 25 33 19 66", "garde_groupe": "C"},
            {"nom": "Pharmacie Yobi", "quartier": "Paspanga", "adresse": "A 200m de la Gendarmerie Nationale", "tel": "+226 25 31 16 30", "garde_groupe": "C"},
            {"nom": "Pharmacie Dassasgho", "quartier": "Dassasgho", "adresse": "A 100m du musée national, sur l'avenue Babanguida", "tel": "+226 25 36 12 12", "garde_groupe": "C"},
            {"nom": "Pharmacie Koulouba", "quartier": "Koulouba", "adresse": "A 200m côté Ouest du marché de Boins-Yaaré", "tel": "+226 25 31 19 18", "garde_groupe": "D"},
            {"nom": "Pharmacie Amaro", "quartier": "Gounghin", "adresse": "Avenue du Kadiogo, Petit Paris", "tel": "+226 25 34 33 28", "garde_groupe": "D"},
            {"nom": "Pharmacie de l'Aéroport", "quartier": "Cosec / Zone Résidentielle", "adresse": "Avenue de l'Aéroport, face entrée fret", "tel": "+226 25 31 05 06", "garde_groupe": "D"},
            {"nom": "Pharmacie de la Liberté", "quartier": "Cité An III", "adresse": "Près du rond-point de la Liberté, Ouagadougou", "tel": "+226 25 30 73 34", "garde_groupe": "A"},
            {"nom": "Pharmacie du Centre", "quartier": "Centre-ville", "adresse": "Avenue de la Nation, face à la BOA", "tel": "+226 25 31 10 93", "garde_groupe": "B"},
            {"nom": "Pharmacie Song-Taaba", "quartier": "Wemtenga", "adresse": "Boulevard Tensoba, face station Total Wemtenga", "tel": "+226 25 36 31 92", "garde_groupe": "C"}
        ],
        "Bobo-Dioulasso": [
            {"nom": "Pharmacie Sya", "quartier": "Centre-ville", "adresse": "Avenue de la République, face grand marché", "tel": "+226 20 97 12 25", "garde_groupe": "A"},
            {"nom": "Pharmacie Sarfalao", "quartier": "Sarfalao", "adresse": "Boulevard principal de Sarfalao, face lycée privé", "tel": "+226 20 98 05 06", "garde_groupe": "B"},
            {"nom": "Pharmacie de la Guimbi", "quartier": "Guimbi", "adresse": "Près du rond-point de la femme, face station Total", "tel": "+226 20 97 32 32", "garde_groupe": "C"},
            {"nom": "Pharmacie Accart-Ville", "quartier": "Accart-ville", "adresse": "Face au CSPS d'Accart-Ville", "tel": "+226 20 97 18 19", "garde_groupe": "D"},
            {"nom": "Pharmacie de l'Amitié", "quartier": "Zone Commerciale", "adresse": "Avenue Blaise Compaoré, Bobo-Dioulasso", "tel": "+226 20 97 11 02", "garde_groupe": "A"},
            {"nom": "Pharmacie Houet", "quartier": "Centre-ville", "adresse": "Près de la place de la Nation, Bobo", "tel": "+226 20 97 22 45", "garde_groupe": "B"}
        ]
    }
    
    # Écrire les pharmacies en JSON
    with open(os.path.join("data", "annuaire_pharmacies.json"), "w", encoding="utf-8") as f:
        json.dump(pharmacies_data, f, ensure_ascii=False, indent=4)
    print("- Fichier annuaire_pharmacies.json créé.")
        
    # Écrire les pharmacies en MD pour la vectorisation
    pharma_md = """# Annuaire et Fonctionnement des Pharmacies au Burkina Faso
*Source des données : Ordre National des Pharmaciens du Burkina Faso & Ministère de la Santé (Santé.gov.bf)*

## 1. Fonctionnement des Gardes Pharmaceutiques
Le service de garde pharmaceutique à Ouagadougou et Bobo-Dioulasso est régi par une rotation stricte organisée en quatre groupes principaux : **Groupe A, Groupe B, Groupe C, et Groupe D**.
*   **Durée de la garde :** Chaque groupe assure le service de garde (ouverture en continu la nuit, les week-ends et jours fériés) pour une période définie, généralement d'une semaine (du samedi midi au samedi midi suivant).
*   **Disponibilité des listes de garde :** Bien que le site officiel du ministère (`sante.gov.bf`) compile des ressources statistiques et de la réglementation pharmaceutique, la liste nominative en temps réel du groupe de garde en cours est publiée chaque semaine par l'Ordre National des Pharmaciens, la presse locale écrite, et les applications mobiles sanitaires agréées du Burkina Faso.

## 2. Répertoire des Pharmacies Référencées

"""
    for ville, list_ph in pharmacies_data.items():
        pharma_md += f"### Ville de {ville}\n"
        for p in list_ph:
            pharma_md += f"*   **{p['nom']}**\n"
            pharma_md += f"    *   **Quartier :** {p['quartier']}\n"
            pharma_md += f"    *   **Adresse :** {p['adresse']}\n"
            pharma_md += f"    *   **Téléphone :** {p['tel']}\n"
            pharma_md += f"    *   **Groupe de Garde :** Groupe {p['garde_groupe']}\n\n"
            
    with open(os.path.join("data", "annuaire_pharmacies.md"), "w", encoding="utf-8") as f:
        f.write(pharma_md)
    print("- Fichier annuaire_pharmacies.md créé.")

    # 5. Annuaire des Structures de Santé (CHU, CMA, CSPS, Hopitaux Confessionnels)
    structures_data = [
        {
            "nom": "CHU Yalgado Ouédraogo (CHU-YO)",
            "type": "Centre Hospitalier Universitaire (CHU)",
            "ville": "Ouagadougou",
            "quartier": "Paspanga",
            "adresse": "Avenue d'Oubritenga, face au parc urbain Bangr Weogo",
            "tel": "+226 25 31 16 55",
            "role": "Hôpital national de référence supérieure de 3ème niveau de la pyramide sanitaire. Assure les soins médicaux spécialisés complexes, les interventions de chirurgie majeure, les urgences nationales et l'enseignement clinique universitaire."
        },
        {
            "nom": "CHU de Bogodogo",
            "type": "Centre Hospitalier Universitaire (CHU)",
            "ville": "Ouagadougou",
            "quartier": "Gounghin / Wemtenga (Est)",
            "adresse": "Secteur 30, Boulevard Tensoba (circulaire)",
            "tel": "+226 76 89 78 63",
            "role": "Hôpital universitaire moderne de 3ème niveau spécialisé notamment dans la gynécologie-obstétrique (maternité de référence), la pédiatrie d'urgence, et la médecine générale spécialisée."
        },
        {
            "nom": "CHU de Tengandogo",
            "type": "Centre Hospitalier Universitaire (CHU)",
            "ville": "Ouagadougou",
            "quartier": "Tengandogo (Sud-Ouest)",
            "adresse": "Sortie Sud de Ouagadougou, route de Léo",
            "tel": "+226 25 37 88 00",
            "role": "Hôpital de 3ème niveau (ex-Hôpital National Blaise Compaoré) doté d'équipements de haute technologie pour la cardiologie, l'oncologie, l'imagerie médicale par résonance magnétique (IRM), la traumatologie et la chirurgie spécialisée."
        },
        {
            "nom": "CHU Pédiatrique Charles De Gaulle (CHUP-CDG)",
            "type": "Centre Hospitalier Universitaire (CHU)",
            "ville": "Ouagadougou",
            "quartier": "Zone d'activités diverses (ZAD)",
            "adresse": "Près de l'avenue de l'Europe, Ouagadougou",
            "tel": "+226 25 36 67 76",
            "role": "Établissement pédiatrique universitaire national de référence absolue pour les enfants. Soins spécialisés en pédiatrie médicale, néonatologie et chirurgie pédiatrique."
        },
        {
            "nom": "CHU Souro Sanou (CHUSS)",
            "type": "Centre Hospitalier Universitaire (CHU)",
            "ville": "Bobo-Dioulasso",
            "quartier": "Centre-ville",
            "adresse": "Avenue du Gouverneur William Ponty, Bobo-Dioulasso",
            "tel": "+226 20 97 00 11",
            "role": "Structure hospitalière de référence universitaire majeure de 3ème niveau pour toute la région sanitaire de l'Ouest du Burkina Faso (région des Hauts-Bassins)."
        },
        {
            "nom": "Hôpital Saint-Camille de Ouagadougou (HASC)",
            "type": "Hôpital Confessionnel conventionné (CHU)",
            "ville": "Ouagadougou",
            "quartier": "Secteur 15",
            "adresse": "Avenue de la Cathédrale, Ouagadougou",
            "tel": "+226 25 36 03 48",
            "role": "Structure confessionnelle de soins d'utilité publique associée au service public de santé, offrant des soins spécialisés en obstétrique, pédiatrie, laboratoire de biologie et médecine interne."
        },
        {
            "nom": "Hôpital Paul VI",
            "type": "Hôpital Confessionnel conventionné (CMA)",
            "ville": "Ouagadougou",
            "quartier": "Secteur 22 (Sig-Noghin)",
            "adresse": "Sortie Nord de Ouagadougou, route de Ouahigouya",
            "tel": "+226 70 43 83 84",
            "role": "Établissement sanitaire confessionnel conventionné fonctionnant comme centre de référence (CMA) pour le district sanitaire du Nord (Sig-Noghin), équipé d'un bloc opératoire complet et d'une maternité."
        },
        {
            "nom": "CMA de Pissy",
            "type": "Centre Médical avec Antenne Chirurgicale (CMA)",
            "ville": "Ouagadougou",
            "quartier": "Pissy",
            "adresse": "Secteur 17, près du rond-point de Pissy",
            "tel": "+226 25 43 64 08",
            "role": "Établissement sanitaire public de référence secondaire pour le district de Boulmiougou. Fournit les interventions chirurgicales de base, les césariennes d'urgence, les analyses de laboratoire de district et les soins d'urgence généraux."
        },
        {
            "nom": "CMA Schiphra",
            "type": "Centre Médical Confessionnel avec Antenne Chirurgicale (CMA)",
            "ville": "Ouagadougou",
            "quartier": "Tanghin (Secteur 17)",
            "adresse": "Près du pont de Tanghin, Tanghin",
            "tel": "+226 25 33 32 29",
            "role": "Centre de santé confessionnel conventionné d'utilité publique assurant le rôle de CMA pour le district sanitaire concerné (consultations, chirurgie, césariennes, hospitalisations et vaccination)."
        },
        {
            "nom": "CSPS de Karpala",
            "type": "Centre de Santé et de Promotion Sociale (CSPS)",
            "ville": "Ouagadougou",
            "quartier": "Karpala",
            "adresse": "Secteur 47, à proximité du grand marché de Karpala",
            "tel": "+226 25 48 11 22",
            "role": "Structure publique de premier échelon du district sanitaire de Bogodogo. Assure le paquet minimum d'activités (PMA) : consultations externes pour adultes/enfants, accouchements (maternité de base), vaccinations du PEV, suivi de la croissance et dépistage de la malnutrition."
        },
        {
            "nom": "CSPS de Gounghin",
            "type": "Centre de Santé et de Promotion Sociale (CSPS)",
            "ville": "Ouagadougou",
            "quartier": "Gounghin (Nord)",
            "adresse": "Secteur 9, à côté de l'école primaire publique",
            "tel": "+226 25 34 02 01",
            "role": "Soins curatifs et préventifs primaires, distribution gratuite de moustiquaires MILDA, supplémentation nutritionnelle des nourrissons et traitement du paludisme simple chez l'enfant."
        },
        {
            "nom": "CSPS de Larlé",
            "type": "Centre de Santé et de Promotion Sociale (CSPS)",
            "ville": "Ouagadougou",
            "quartier": "Larlé",
            "adresse": "Près du marché de Larlé",
            "tel": "+226 25 33 08 09",
            "role": "Soins infirmiers primaires, suivi de la grossesse (consultations prénatales), supplémentation en fer et acide folique, et administration de la CPS lors des campagnes saisonnières."
        }
    ]
    
    # Écrire les structures en JSON
    with open(os.path.join("data", "annuaire_structures_sante.json"), "w", encoding="utf-8") as f:
        json.dump(structures_data, f, ensure_ascii=False, indent=4)
    print("- Fichier annuaire_structures_sante.json créé.")
        
    # Écrire en MD pour la base vectorielle
    struct_md = """# Répertoire et Organisation des Structures de Santé au Burkina Faso
*Source des données : Ministère de la Santé et de l'Hygiène Publique du Burkina Faso (Santé.gov.bf)*

## 1. Pyramide Sanitaire du Burkina Faso
Le système de soins au Burkina Faso est structuré sous forme d'une pyramide sanitaire à trois niveaux distincts :
*   **Premier niveau (Périphérique) :** Constitue le point d'entrée. Il comprend les **CSPS (Centres de Santé et de Promotion Sociale)** et les **CM (Centres Médicaux)** qui mettent en œuvre le Paquet Minimum d'Activités (PMA). Au second échelon de ce niveau se trouvent les **CMA (Centres Médicaux avec Antenne Chirurgicale)**, qui servent de structures de référence du district pour le Paquet Complémentaire d'Activités (PCA - chirurgie de base, maternité de référence).
*   **Deuxième niveau (Intermédiaire) :** Comprend les **CHR (Centres Hospitaliers Régionaux)** offrant des soins plus complets à l'échelle de chaque région.
*   **Troisième niveau (Central / National) :** Comprend les **CHU (Centres Hospitaliers Universitaires)** de référence tertiaire nationale, équipés de plateaux techniques hautement spécialisés et d'unités de recherche clinique.

## 2. Collecte et Suivi des Données Épidémiologiques
L'ensemble des formations sanitaires collecte et télétransmet de manière systématique les données de santé de base (veille épidémiologique sur le paludisme, la dengue, la malnutrition et autres maladies à déclaration obligatoire) via la base de données nationale **Endos-BF** basée sur la plateforme open source **DHIS2** (District Health Information Software 2), permettant ainsi au ministère d'éditer des bulletins hebdomadaires de veille.

## 3. Liste des Structures de Santé Référencées

"""
    for s in structures_data:
        struct_md += f"### {s['nom']}\n"
        struct_md += f"*   **Type de structure :** {s['type']}\n"
        struct_md += f"*   **Localisation :** {s['ville']}, Quartier {s['quartier']}\n"
        struct_md += f"*   **Adresse :** {s['adresse']}\n"
        struct_md += f"*   **Téléphone :** {s['tel']}\n"
        struct_md += f"*   **Rôle et services :** {s['role']}\n\n"
        
    with open(os.path.join("data", "annuaire_structures_sante.md"), "w", encoding="utf-8") as f:
        f.write(struct_md)
    print("- Fichier annuaire_structures_sante.md créé.")
    
    print("Génération des données terminée avec succès !")

if __name__ == "__main__":
    main()
