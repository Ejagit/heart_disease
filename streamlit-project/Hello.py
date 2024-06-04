import streamlit as st

st.set_page_config(
    page_title="Homepage",
)

st.markdown("# Welcome to my Web! 👋")

st.markdown(
    """
    ## FYI :
    According to the CDC, heart disease is the leading cause of death for most races in the United States (African Americans, Native Americans, and Caucasians). About half of all Americans (47%) have at least 1 of 3 major risk factors for heart disease: high blood pressure, high cholesterol, and smoking. Other indicators include diabetes status, obesity (high BMI), lack of physical activity, or excessive alcohol consumption. Identifying and preventing the factors with the greatest impact on heart disease is crucial in healthcare.

    ## DATASET?
    You can access the dataset on [DATASET](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease/data)
        
    ## About Dataset
    -HeartDisease: This column contains information about whether someone has heart disease or not.

    -BMI: Abbreviation for Body Mass Index, which measures the proportion of weight to height of an individual.

    -Smoking: This column may store information about whether someone smokes or not.

    -AlcoholDrinking: Information about whether someone consumes alcoholic beverages or not.

    -Stroke: May contain information about whether someone has ever had a stroke or not.

    -PhysicalHealth: This column may describe someone's physical health condition.

    -MentalHealth: Indicates someone's mental health condition.

    -DiffWalking: Likely to store information about whether someone has difficulty walking or not.

    -Sex: Indicates someone's gender.

    -AgeCategory: Groups someone's age into specific categories.

    -Race: Stores information about someone's race or ethnicity.

    -Diabetic: Information about whether someone has diabetes or not.

    -PhysicalActivity: Indicates how active someone is in physical activities.

    -GenHealth: Describes someone's overall health condition.

    -SleepTime: Someone's sleep time, which can be an indicator of sleep health.

    -Asthma: Information about whether someone has asthma or not.

    -KidneyDisease: May contain information about whether someone has kidney disease or not.

    -SkinCancer: Information about whether someone has skin cancer or not.
    
"""
)