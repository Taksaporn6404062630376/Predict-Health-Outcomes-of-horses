import streamlit as st
import pickle
import pandas as pd


model_path = "C:\\Users\\USER\\mlweb\\randomforest.pkl"
with open(model_path, 'rb') as file:
    classifier = pickle.load(file)
# Set Streamlit theme with a brown color
st.set_page_config(
    page_title="Horse Health Prediction",
    page_icon="🐴",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS to set a light blue theme
custom_css = """
    body {
        background-color: #add8e6; /* Light Blue color */
    }
    .sidebar .sidebar-content {
        background-color: #87ceeb; /* Sky Blue color */
        color: white;
    }
    .block-container {
        background-color: #b0e0e6; /* Powder Blue color */
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
"""

# Set custom CSS
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

def user_input_features():

    st.title("User Input Parameters")
    surgery_opt = ['Yes', 'No']
    surgery = st.radio('**Surgery History**', surgery_opt)
    surgery = 1 if surgery == 'No' else 0 
    
    age_opt = ['Adult', 'Young']
    age = st.radio('**Age**', age_opt)
    age = 0 if age == 'Adult' else 1
    
    rectal_temp = st.number_input('**Insert a rectal temperature**')
    
    pulse = st.slider('Insert a pulse', min_value=0, max_value=200, value=0, step=1)
    
    respiratory_rate = st.slider('**Respiratory Rate**')
    
    temp_of_extremities_opt = ['Warm', 'Cool', 'Normal']
    temp_of_extremities = st.selectbox('**Temperature of Extremities**',  temp_of_extremities_opt)
    temp_of_extremities = 0 if temp_of_extremities == 'Warm' else (1 if temp_of_extremities == 'Cool' else 2)

    
    peripheral_pulse_opt = ['Absent', 'Reduced', 'Normal', 'Increased']
    peripheral_pulse = st.selectbox('**Peripheral Pulse**',  peripheral_pulse_opt)
    peripheral_pulse = 0 if peripheral_pulse == 'Absent' else (1 if peripheral_pulse == 'Increased' else (2 if peripheral_pulse == 'Normal' else 3))
    
    
    mucous_membrane_opt  =   ['Bright Pink', 'Bright Red', 'Dark Cyanotic', 'Normal Pink', 'Pale Cyanotic', 'Pale Pink' ]
    mucous_membrane = st.selectbox('**Mucous membrane**',  mucous_membrane_opt)
    mucous_membrane = mucous_membrane_opt.index(mucous_membrane)
    
    
    capillary_refill_time_opt = ['Less than 3 seconds', 'More than 3 seconds']
    capillary_refill_time = st.selectbox('**Capillary refill time**', capillary_refill_time_opt)
    capillary_refill_time = capillary_refill_time_opt.index(capillary_refill_time)
    
    pain_opt = ['Alert', 'Depressed', 'Extreme pain', 'Mild Pain', 'Severe Pain','None' ]
    pain = st.selectbox('**Pain**', pain_opt)
    pain = pain_opt.index(pain)
    
    
    peristalsis_opt = ['Absent','Distend_small','Hypermotile', 'Hypomotile', 'Normal' ]
    peristalsis = st.selectbox('**Peristalsis**', peristalsis_opt)
    peristalsis = peristalsis_opt.index(peristalsis)
    
    abdominal_distention_opt = ['Moderate','None' ,'Severe', 'Slight' ]
    abdominal_distention = st.selectbox('**Abdominal distention**', abdominal_distention_opt)
    abdominal_distention = abdominal_distention_opt.index(abdominal_distention)
    
    nasogastric_tube_opt = ['None', 'Significant', 'Slight' ]
    nasogastric_tube = st.selectbox('**Nasogastric tube**', nasogastric_tube_opt)
    nasogastric_tube =  nasogastric_tube_opt.index(nasogastric_tube)
    
    nasogastric_reflux_opt = ['Less 1 liter' ,'More 1 liter' ,'None']
    nasogastric_reflux = st.selectbox('**Nasogastric reflux**', nasogastric_reflux_opt)
    nasogastric_reflux =   nasogastric_reflux_opt.index(nasogastric_reflux)
    
    
    nasogastric_reflux_ph = st.number_input('**Insert a nasogastric reflux PH**')
    
    rectal_exam_feces_opt = ['Absent','Decreased', 'Increased', 'Normal', 'Serosanguious' ]
    rectal_exam_feces = st.selectbox('**Rectal exam feces** ', rectal_exam_feces_opt)
    rectal_exam_feces   =  rectal_exam_feces_opt.index(rectal_exam_feces)
    
    abdomen_opt = [ 'Distend large','Distend small', 'Firm', 'Normal' ,'Other' ]
    abdomen = st.selectbox('**Abdomen**', abdomen_opt)
    abdomen =  abdomen_opt.index(abdomen)
    
    packed_cell_volume = st.slider('**Insert a packed cell volume**')
    
    total_protein = st.number_input('**Insert a total protein**')
    
    abdomo_appearance_opt = ['Clear','Cloudy', 'Serosanguious']
    abdomo_appearance = st.selectbox('**Abdomo appearance**', abdomo_appearance_opt)
    abdomo_appearance =  abdomo_appearance_opt.index(abdomo_appearance)
    
    abdomo_protein  =  st.number_input('**Insert a abdomo protein**')
   
    surgical_lesion_opt = ['No','Yes' ]
    surgical_lesion  = st.selectbox('**Surgical lesion**', surgical_lesion_opt)
    surgical_lesion =  surgical_lesion_opt.index(surgical_lesion)
    
    
    cp_data_opt = ['No', 'Yes']
    cp_data = st.selectbox('**CP data**', cp_data_opt)
    cp_data =  cp_data_opt.index(cp_data)
    
    site_of_lesion_opt = ['00- None', '1- Gastric', '2- sm intestine', '3- Lg colon', '4- G colon and cecum', 
                          '5- Cecum', '6- Transverse colon', '7- Retum/Descending colon' , '8- Uterus', '9- Bladder' ]
    site_of_lesion = st.selectbox('**Site of lesion**',  site_of_lesion_opt)
    site_of_lesion =  site_of_lesion_opt.index(site_of_lesion)
    
    
    type_of_lesion_opt = ['0- None', '1- Simple' , '2- Strangulation', '3- Inflammation', '4- Other']
    type_of_lesion = st.selectbox('**Type of lesion**', type_of_lesion_opt)
    type_of_lesion  =  type_of_lesion_opt.index(type_of_lesion)
    
    subtype_of_lesion_opt = ['0- N/A','1- Mechanical', '2- Paralytic']
    subtype_of_lesion  = st.selectbox('**Subtype of lesion**', subtype_of_lesion_opt)
    subtype_of_lesion  =   subtype_of_lesion_opt.index(subtype_of_lesion)
    
    specific_code_of_lesion_opt = ['0- N/A', '1- Obturation','2- intrinsic', '3- Extrinsic', '4- Adynamic', '5- Volvulus/torsion',
                              '6- Intussuption', '7- Thromboembolic', '8- hernia', '9- Lipoma/slenic incarceration', '10- Displacement' ]
    specific_code_of_lesion = st.selectbox('**Specific code of lesion**',  specific_code_of_lesion_opt)
    specific_code_of_lesion =   specific_code_of_lesion_opt.index(specific_code_of_lesion)
    
   
    
    user_input_data = {
                    'id': 0,
                    'surgery': surgery,
                    'age': age,
                    'rectal_temp': rectal_temp,
                    'pulse': pulse,
                    'respiratory_rate': respiratory_rate,
                    'temp_of_extremities': temp_of_extremities,
                    'peripheral_pulse' : peripheral_pulse,
                    'mucous_membrane' : mucous_membrane,
                    'capillary_refill_time' : capillary_refill_time,
                    'pain': pain,
                    'peristalsis' : peristalsis,
                    'abdominal_distention' : abdominal_distention,
                    'nasogastric_tube' : nasogastric_tube,
                    'nasogastric_reflux' : nasogastric_reflux,
                    'nasogastric_reflux_ph' : nasogastric_reflux_ph,
                    'rectal_exam_feces' : rectal_exam_feces,
                    'abdomen' : abdomen,
                    'packed_cell_volume' : packed_cell_volume,
                    'total_protein' : total_protein,
                    'abdomo_appearance' : abdomo_appearance,
                    'abdomo_protein' : abdomo_protein,
                    'surgical_lesion' : surgical_lesion,
                    'cp_data' : cp_data,
                    'site_of_lesion' : site_of_lesion,
                    'type_of_lesion' :type_of_lesion,
                    'subtype_of_lesion' : subtype_of_lesion,
                    'specific_code_of_lesion': specific_code_of_lesion
                
                      }

    features = pd.DataFrame(user_input_data, index=[0])     ## create dataframe for user's inputs'

    return features

# Display part
labels = ['died', 'euthanized' , 'lived']

def main():

    st.sidebar.title("Predict Health Outcomes of Horses")

    # Add CSS styling to move the sidebar to the right and make it full-width
    st.markdown(
        """
        <style>
            .reportview-container .main .block-container {
                padding-top: 1rem;
                padding-right: 5rem;
                padding-left: 1rem;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    df = user_input_features()
    
  
    # Assuming df is your DataFrame
    columns_to_display = [col for col in df.columns if col not in ['id']]

    # Transpose the DataFrame for vertical display
    df_transposed = df[columns_to_display].T

    st.sidebar.subheader('User Input Parameters')
    st.sidebar.table(df_transposed)

    prediction = classifier.predict(df)
    prediction_probabilities = classifier.predict_proba(df)

    st.sidebar.subheader('Prediction')
    st.sidebar.write(labels[prediction[0]])

    st.sidebar.subheader('Prediction Probability')
    # prediction_labels = [labels[pred] for pred in prediction]
    probabilities_df = pd.DataFrame(prediction_probabilities, columns=labels)
    st.sidebar.table(probabilities_df)

    st.sidebar.subheader('Prediction Probability Chart')
    chart_data = pd.DataFrame({'labels': labels, 'probabilities': prediction_probabilities[0]})
    st.sidebar.bar_chart(chart_data.set_index('labels'), width=470, height=400)

if __name__ == "__main__":
    main()