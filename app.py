from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import os
from flask import jsonify
from flask import url_for

import os
from flask import jsonify
from flask import url_for

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
from keras.preprocessing import image

from tensorflow.keras.preprocessing.image import load_img

import tensorflow as tf

app = Flask(__name__,static_folder="static/")
# Define the path to the model file

# gemini api
import os

import google.generativeai as genai
api_key = "AIzaSyBmCY0csZo_fFovRoVnHkLDfE41N4jRUvQ"
genai.configure(api_key=api_key)

# genai.configure(api_key=os.environ[GoogleApiKey])

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


# define ends---- The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/crop_predict')
def crop_predict():
    city = request.args.get('city')
    return render_template('crop_predict.html', city=city)

@app.route('/index')
def index_move():
    city = request.args.get('city')
    return render_template('index.html', city=city)

@app.route('/pest_predict')
def pest_predict():
    return render_template('pest_predict.html')

@app.route('/weed_predict')
def weed_predict():
    return render_template('weed_predict.html')

# page movement end

#crop prediction model 
model = pickle.load(open('crop.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['nitrogen']
    data2 = request.form['phosphorus']
    data3 = request.form['potassium']
    data4 = request.form['temperature']
    data5 = request.form['humidity']
    data6 = request.form['ph']
    data7 = request.form['rainfall']
    
    # Define feature names
    feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
# Create NumPy array with feature names
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7]])

# Set feature names
    arr = pd.DataFrame(arr, columns=feature_names)
    pred = model.predict(arr)
    print(pred)
    return render_template('crop_result.html', data=pred)


#weed model and gemini
#weed model
weedmodel = load_model('weed_model.h5')
weedmodel.make_predict_function()

def predict_label(img_path):
    img = Image.open(img_path)
    img = img.resize((224, 224))  # Resize the image to the required size
    img_array = np.array(img) / 255.0  # Convert image to numpy array and normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    predictions = weedmodel.predict(img_array)
    return predictions[0]

WEED_NAMES = {
    0: "Amaranthus spp",
    1: "Chenopodium album",
    2: "Cirsium arvense",
    3: "Commelina benghalensis",
    4: "Convolvulus arvensis",
    5: "Cyperus rotundus",
    6: "Dactyloctenium aegyptium",
    7: "Echinochloa crus-galli",
    8: "Parthenium hysterophorus",
    9: "Phalaris minor"
}
# weed data
weed_data = {
    "Parthenium hysterophorus": {
        "Cname": "Congress grass",
        "Description": "One of the most problematic weeds in India, causing severe health issues (allergies, skin irritations) in humans and animals. Reduces crop yields significantly by competing for water, nutrients, and sunlight. Spreads rapidly through wind-dispersed seeds, making control challenging.",
        "prevention": "Prevent seed dispersal by timely removal and disposal. Use manual or mechanical methods to uproot plants before flowering. Biological control agents like insects can also be introduced for long-term management.",
        "chemical": "Apply pre-emergent herbicides like atrazine or post-emergent herbicides like glyphosate. Follow label instructions carefully to minimize environmental impact.",
        "cultural": "Implement crop rotation, mulching, and dense planting to suppress weed growth. Regular monitoring and hand weeding can help prevent Parthenium hysterophorus infestations."
    },
    "Echinochloa crus-galli": {
        "Cname": "Barnyard grass",
        "Description": "A major competitor in rice fields, aggressively competing with rice plants for essential resources like nutrients, light, and space. Reproduces rapidly by seeds, forming dense mats that can smother rice crops and hinder their growth. Difficult to control due to its ability to germinate underwater, allowing it to establish itself before rice seedlings.",
        "prevention": "Implement proper field sanitation practices to prevent weed establishment. Use stale seedbed techniques to encourage weed seed germination for easier removal. Regular cultivation and shallow tillage can disrupt weed growth.",
        "chemical": "Apply pre-emergent herbicides like pendimethalin or post-emergent herbicides like quinclorac. Herbicide application timing is crucial for effective control.",
        "cultural": "Optimize crop spacing and density to shade out weeds. Practice crop rotation and fallow periods to disrupt weed life cycles and reduce populations."
    },
    "Amaranthus spp": {
        "Cname": "Amaranth",
        "Description": "Common and diverse group of weeds found in agricultural fields, including grain amaranth and pigweed. Significantly reduce crop yields by competing with crops for water, nutrients, and sunlight. Fast-growing and prolific seed producers, allowing them to quickly establish large populations. Caution: While some Amaranthus species have edible leaves, be aware that certain varieties may be toxic.",
        "prevention": "Practice crop rotation and diverse cropping systems to reduce weed pressure. Hand removal of young plants before flowering can prevent seed production. Mulching and cover cropping can suppress weed growth.",
        "chemical": "Use pre-emergent herbicides like metolachlor or post-emergent herbicides like 2,4-D. Herbicide selection should consider weed species and stage of growth.",
        "cultural": "Maintain soil fertility and pH to promote crop competitiveness. Planting weed-suppressive crops as cover crops or intercrops can help manage Amaranthus spp. populations."
    },
    "Convolvulus arvensis": {
        "Cname": "Field bindweed",
        "Description": "A persistent problem in agriculture, vineyards, and orchards due to its extensive underground root system that makes eradication difficult. Competes fiercely with crops for water and nutrients, hindering their growth and productivity. Spreads both by seeds and by creeping roots, allowing it to quickly establish large infestations.",
        "prevention": "Implement deep tillage to bury weed seeds and disrupt root systems. Prevent seed spread by controlling mature plants before flowering. Hand weeding and cultivation can help manage small infestations.",
        "chemical": "Apply pre-emergent herbicides like trifluralin or post-emergent herbicides like dicamba. Herbicide choice should consider weed growth stage and surrounding vegetation.",
        "cultural": "Practice crop rotation with non-host crops to break weed cycles. Utilize mulching and cover crops to suppress Convolvulus arvensis growth and reduce seed bank buildup."
    },
    "Cyperus rotundus": {
        "Cname": "Nutgrass",
        "Description": "A perennial weed that infests agricultural fields and reduces crop yields by competing for resources. Forms tubers underground, enabling it to survive harsh conditions, reproduce asexually, and make control difficult. The extensive underground network of tubers allows nutgrass to regrow even after removal of the above-ground parts.",
        "prevention": "Minimize soil disturbance to prevent rhizome fragmentation and spread. Regularly remove and properly dispose of infested plant parts. Implement physical barriers like mulching or plastic sheeting to suppress weed emergence.",
        "chemical": "Apply pre-emergent herbicides like oxadiazon or post-emergent herbicides like halosulfuron-methyl. Timing is crucial for effective herbicide application to target emerging shoots.",
        "cultural": "Improve soil drainage and aeration to discourage Cyperus rotundus growth. Utilize competitive crops and proper crop spacing to reduce weed competition. Regular monitoring and manual removal can prevent weed establishment and spread."
    },
    "Chenopodium album": {
        "Cname": "Lamb's quarters",
        "Description": "Widespread weed in India, posing a significant problem during the monsoon season due to its rapid growth, especially in moist conditions. Competes with crops for water, nutrients, and sunlight, impacting their growth and yield. Fast-growing and matures quickly, taking advantage of the monsoon rains to establish itself and compete with crops. Produces large quantities of seeds that can remain viable in the soil for many years, ensuring its persistence.",
        "prevention": "Remove weeds before flowering to prevent seed production. Implement mulching and cover cropping to suppress weed emergence. Regular cultivation and shallow tillage can disrupt weed growth.",
        "chemical": "Apply pre-emergent herbicides like pendimethalin or post-emergent herbicides like glyphosate. Follow label instructions carefully to minimize environmental impact.",
        "cultural": "Maintain soil fertility and pH to promote crop competitiveness. Planting weed-suppressive crops as cover crops or intercrops can help manage Chenopodium album populations."
    },
    "Phalaris minor": {
        "Cname": "Little seed canary grass",
        "Description": "A major weed in wheat fields of India, competing with wheat plants for resources and reducing yields. Winter-annual grass that germinates in the fall and matures in the spring, potentially outcompeting spring-sown wheat. Difficult to control in the early stages due to its resemblance to wheat seedlings, making identification and removal challenging.",
        "prevention": "Practice crop rotation and diverse cropping systems to reduce weed pressure. Hand removal of young plants before flowering can prevent seed production. Mulching and cover cropping can suppress weed growth.",
        "chemical": "Use pre-emergent herbicides like metolachlor or post-emergent herbicides like 2,4-D. Herbicide selection should consider weed species and stage of growth.",
        "cultural": "Optimize crop spacing and density to shade out weeds. Practice crop rotation and fallow periods to disrupt weed life cycles and reduce populations."
    },
    "Cirsium arvense": {
        "Cname": "Canada thistle",
        "Description": "An invasive weed that aggressively competes with crops for water and nutrients, reducing their growth and productivity. Spreads rapidly by both seeds and creeping roots, forming dense patches that crowd out crops and hinder their access to sunlight. Difficult to control due to its extensive root system that allows it to regenerate even after removal of the above-ground parts.",
        "prevention": "Implement deep tillage to bury weed seeds and disrupt root systems. Prevent seed spread by controlling mature plants before flowering. Hand weeding and cultivation can help manage small infestations.",
        "chemical": "Apply pre-emergent herbicides like trifluralin or post-emergent herbicides like dicamba. Herbicide choice should consider weed growth stage and surrounding vegetation.",
        "cultural": "Practice crop rotation with non-host crops to break weed cycles. Utilize mulching and cover crops to suppress Cirsium arvense growth and reduce seed bank buildup."
    },
    "Commelina benghalensis": {
        "Cname": "Benghal dayflower",
        "Description": "Found in various crops like rice, sugarcane, and maize, reducing yields by competing for water, nutrients, and sunlight. Low-growing, spreading weed that forms dense mats, smothering crops and hindering their growth. Prolific seed producer, allowing it to spread quickly and establish large populations in a short period.",
        "prevention": "Minimize soil disturbance to prevent rhizome fragmentation and spread. Regularly remove and properly dispose of infested plant parts. Implement physical barriers like mulching or plastic sheeting to suppress weed emergence.",
        "chemical": "Apply pre-emergent herbicides like oxadiazon or post-emergent herbicides like halosulfuron-methyl. Timing is crucial for effective herbicide application to target emerging shoots.",
        "cultural": "Improve soil drainage and aeration to discourage Commelina benghalensis growth. Utilize competitive crops and proper crop spacing to reduce weed competition. Regular monitoring and manual removal can prevent weed establishment and spread."
    },
    "Dactyloctenium aegyptium": {
        "Cname": "Crowfoot grass",
        "Description": "Widespread weed in India, particularly problematic in dryland agriculture, where it competes with crops for scarce water resources. Matures quickly and produces a large number of seeds that can stay viable in the soil for several years, ensuring its persistence even during dry periods. This allows crowfoot grass to readily establish itself and compete with crops for moisture as soon as rains arrive.",
        "prevention": "Remove weeds before flowering to prevent seed production. Implement mulching and cover cropping to suppress weed emergence. Regular cultivation and shallow tillage can disrupt weed growth.",
        "chemical": "Apply pre-emergent herbicides like pendimethalin or post-emergent herbicides like glyphosate. Follow label instructions carefully to minimize environmental impact.",
        "cultural": "Maintain soil fertility and pH to promote crop competitiveness. Planting weed-suppressive crops as cover crops or intercrops can help manage Dactyloctenium aegyptium populations."
    }
}


@app.route("/submit", methods=['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "static/" + img.filename
        img.save(img_path)
        confidences = predict_label(img_path)

    sorted_indices = np.argsort(confidences)[::-1]  # Get indices for descending sort
    weed_names = [WEED_NAMES[i] for i in sorted_indices]  # Sort weed names using indices
    confidences = confidences[sorted_indices]  # Sort confidences using indices

    weed_analysis = zip(weed_names,confidences)  # Zip sorted lists

    # top_confidence = confidences[0]
    # if top_confidence > 0.85:
    #         # Confidence high enough, skip Gemini
    #         gemini_result = weed_names[0]
    # else:
    try:
            model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
            )
            files = [upload_to_gemini(img_path)]
            chat_session = model.start_chat(
            history=[
    {
      "role": "user",
      "parts": [
        files[0],
        "**Can you identify the weed in this image?**\n"
                        "If it's not a weed, please indicate that as well. \n"
                        "Here are some possible weed names for reference (but the image might not be a weed):\n"
                        "{}\n".format(", ".join(WEED_NAMES.values()))
        # "Is this image a weed belonging to any of the following:\nWEED_NAMES = {\n    0: \"Amaranthus spp\",\n    1: \"Chenopodium album\",\n    2: \"Cirsium arvense\",\n    3: \"Commelina benghalensis\",\n    4: \"Convolvulus arvensis\",\n    5: \"Cyperus rotundus\",\n    6: \"Dactyloctenium aegyptium\",\n    7: \"Echinochloa crus-galli\",\n    8: \"Parthenium hysterophorus\",\n    9: \"Phalaris minor\"\n}. \nif so only say the name",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Amaranthus spp \n",
      ],
    },
  ]
            )
            confidence_message = "\n".join([f"{weed_names}: {confidences:.2f}" for weed_names, confidences in weed_analysis])
            message = (
            "First check whther the uploaded image is a weed or not, if it is not a weed then responde with it is not a weed Please upload correct image,If it's a weed then check whether it is from my dataset and use my model confidence rates to correctly identify the weed name, if it is present in my dataset then only say the exact name of the weed. **Here are the confidence scores from my initial model:**\n"
            "{}\n"
            "**Note:** There's a chance the image might not be a weed at all or the model might have predicted wrongly.\n".format(confidence_message)
        ) 
                # f"Is this image a weed belonging to any of the following:\n{str(WEED_NAMES)}\nif so only say the name. Here are the confidence scores from another model:\n{confidence_message}. Note there might be chances that the image is not a weed"

            response = chat_session.send_message(message)#"Is this image a weed belonging to any of the following:\n" + str(WEED_NAMES) + "\nif so only say the name"
            gemini_result = response.text
    except Exception as e:
             gemini_result=weed_names[0]
            
    correct_weed_data = weed_data.get(gemini_result.strip())

    return render_template("weed_result.html", data=confidences, weed_name=correct_weed_data, img_path=img_path,final_results=gemini_result,new_weed = correct_weed_data,weed_list = weed_names)



# pest identification===================================

model_path = 'newpest_ince.tflite'
# Load the TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

pest_data = {
    "Anoplophora chinensis": {
        "Sname": "Anoplophora chinensis",
        "Cname": "Citrus Longhorn Beetle",
        "Description": "The Citrus Longhorn Beetle is an invasive pest that attacks various trees, including citrus, causing extensive damage to bark and wood. It can lead to tree decline and death if left unchecked.",
        "Prevention": "Implement strict quarantine measures to prevent pest spread. Regular monitoring and early detection are crucial. Remove and destroy infested trees promptly to prevent further spread.",
        "Chemical": "Use insecticides containing imidacloprid or fipronil to target adults and larvae. Follow label instructions carefully to minimize environmental impact.",
        "Cultural": "Practice good sanitation by removing and destroying infested plant debris. Utilize pheromone traps to monitor pest populations and reduce mating success."
    },
    "Apriona germari hope": {
        "Sname": "Apriona germari hope",
        "Cname": "Apriona Beetle",
        "Description": "The Apriona Beetle is a destructive pest of fruit and ornamental trees, particularly in orchards and urban landscapes. It feeds on foliage, causing defoliation and weakening the trees.",
        "Prevention": "Monitor trees regularly for signs of beetle activity and damage. Prune and remove infested branches to reduce beetle populations. Implement cultural practices to enhance tree health and resilience.",
        "Chemical": "Apply systemic insecticides containing dinotefuran or acetamiprid to target adult beetles and larvae. Use targeted trunk injections for effective control.",
        "Cultural": "Promote tree vigor through proper irrigation, fertilization, and pruning practices. Utilize mulching to conserve moisture and suppress weed competition."
    },
    "Drosicha contrahens male": {
        "Sname": "Drosicha contrahens male",
        "Cname": "Mulberry Looper Male",
        "Description": "The Mulberry Looper Male is a moth species that mates with females to facilitate reproduction. It plays a role in the lifecycle of the mulberry looper pest.",
        "Prevention": "Implement monitoring programs to detect moth activity and population dynamics. Utilize pheromone traps to monitor male moth populations.",
        "Chemical": "Apply mating disruption techniques using synthetic pheromones to reduce male moth mating success. Use biological insecticides for targeted control.",
        "Cultural": "Promote tree health through proper pruning, watering, and fertilization. Utilize mulching and physical barriers to disrupt moth mating and reduce egg-laying."
    },
    "Erthesina fullo": {
        "Sname": "Erthesina fullo",
        "Cname": "Brown Marmorated Stink Bug",
        "Description": "The Brown Marmorated Stink Bug is an invasive pest that feeds on various crops and ornamental plants. It damages fruits, vegetables, and ornamentals by piercing and sucking sap.",
        "Prevention": "Implement exclusion techniques such as sealing cracks and crevices to prevent bug entry. Use pheromone traps to monitor and reduce bug populations.",
        "Chemical": "Apply insecticides containing pyrethroids or neonicotinoids to target adult bugs. Use insecticidal soaps or oils for control in organic systems.",
        "Cultural": "Implement proper sanitation practices to reduce overwintering sites and eliminate food sources. Utilize physical barriers and mesh netting to protect crops from infestation."
    },
    "Hyphantria cunea": {
        "Sname": "Hyphantria cunea",
        "Cname": "Fall Webworm",
        "Description": "The Fall Webworm is a defoliating pest of deciduous trees, particularly in forests. It forms communal nests and feeds on leaves, causing extensive defoliation and tree stress.",
        "Prevention": "Implement monitoring programs to detect webworm activity and larval populations. Prune and remove infested branches to reduce webworm populations.",
        "Chemical": "Apply biological insecticides containing Bacillus thuringiensis (Bt) to target webworm larvae. Use physical removal of nests for control in small trees.",
        "Cultural": "Promote tree health through proper pruning, watering, and fertilization. Utilize biological control agents like parasitic wasps and predators."
    },
    "Latoia consocia Walker": {
        "Sname": "Latoia consocia Walker",
        "Cname": "Citrus Psyllid",
        "Description": "The Citrus Psyllid is a sap-sucking pest of citrus trees, particularly affecting new growth and young plants. It can transmit plant pathogens, causing disease and reducing crop yield.",
        "Prevention": "Implement monitoring programs to detect psyllid activity and population dynamics. Remove and destroy infested plant material to reduce psyllid populations.",
        "Chemical": "Apply insecticides containing systemic neonicotinoids to target psyllids. Utilize reflective mulches to deter psyllids from settling on citrus trees.",
        "Cultural": "Promote tree health through proper pruning, watering, and fertilization. Utilize biological control agents like parasitic wasps for long-term psyllid management."
    },
    "Psilogramma menephron": {
        "Sname": "Psilogramma menephron",
        "Cname": "Psilogramma Moth",
        "Description": "The Psilogramma Moth is a nocturnal insect species belonging to the family Erebidae. It is characterized by its mottled appearance and is known to feed on various plant species.",
        "Prevention": "Implement monitoring programs to detect moth activity and egg-laying. Handpick and destroy moth eggs and larvae where feasible.",
        "Chemical": "Apply biological insecticides containing Bacillus thuringiensis (Bt) to target moth larvae. Use pheromone traps to monitor moth populations.",
        "Cultural": "Promote plant diversity to attract natural enemies of moth larvae. Implement proper sanitation practices to reduce moth populations and protect vulnerable plants."
    },
    "Spilarctia subcarnea Walker": {
        "Sname": "Spilarctia subcarnea Walker",
        "Cname": "Spilarctia Caterpillar",
        "Description": "The Spilarctia Caterpillar is the larval stage of a moth species belonging to the family Erebidae. It is characterized by its fuzzy appearance and voracious appetite. The larvae feed on plant foliage, causing defoliation and weakening of plants.",
        "Prevention": "Implement monitoring programs to detect caterpillar activity and feeding damage. Handpick and destroy caterpillars where feasible.",
        "Chemical": "Apply biological insecticides containing Bacillus thuringiensis (Bt) to target caterpillars. Use insecticidal soaps or oils for control.",
        "Cultural": "Promote plant diversity to attract natural enemies of caterpillars. Implement proper sanitation practices to reduce caterpillar populations and protect vulnerable plants."
    },
    "ants": {
        "Sname": "Ants",
        "Cname": "Ants",
        "Description": "Ants are pests in agriculture, known for farming aphids and other pests that harm crops. They create underground nests, disturbing plant roots and soil structure, leading to reduced crop yields and plant health.",
        "Prevention": "Maintain field sanitation, remove plant debris, and disrupt ant trails. Use bait stations and traps strategically around crop areas. Regularly monitor ant activity to prevent infestations.",
        "Chemical": "Apply ant-specific insecticides like bifenthrin or permethrin directly to nests and trails. Use granular baits for targeted control. Always follow label instructions to ensure safe application and minimize environmental impact.",
        "Cultural": "Implement crop rotation and intercropping to disrupt ant colonies. Use organic mulches and cover crops to deter ants. Encourage natural predators like birds and beneficial insects to reduce ant populations."
    },
    "beetle": {
        "Sname": "Coleoptera",
        "Cname": "Beetle",
        "Description": "Beetles, belonging to the order Coleoptera, are one of the most diverse groups of insects, with over 350,000 species worldwide. They range in size from tiny, barely visible species to large, conspicuous ones. Beetles typically have hardened forewings called elytra, which cover the membranous hindwings and protect the body. They exhibit a wide range of feeding habits, with some species being herbivores, others predators, and some scavengers.",
        "Prevention": "Preventing beetle infestations in agricultural settings involves various strategies. Crop rotation is effective in breaking the life cycle of many beetle species, as it disrupts their access to preferred host plants. Additionally, physical barriers such as row covers or netting can be deployed to prevent adult beetles from laying eggs on crops. Maintaining healthy soil with proper drainage and avoiding excessive use of nitrogen-rich fertilizers can also discourage beetle populations.",
        "Chemical": "In cases where beetle populations reach damaging levels, chemical control may be necessary. Insecticides formulated with active ingredients like neem oil, pyrethrins, or spinosad can provide effective control of beetles. It's essential to apply insecticides according to label instructions and consider their potential impact on non-target organisms.",
        "Cultural": "Cultural practices play a crucial role in managing beetle populations sustainably. Regular scouting and monitoring of crops help detect beetle presence early, allowing for timely intervention. Maintaining proper sanitation in fields and storage areas by removing crop residues and weeds reduces beetle breeding sites. Implementing integrated pest management (IPM) strategies that combine cultural, biological, and chemical control methods can effectively mitigate beetle damage while minimizing environmental impact."
    },
    "caterpillar": {
        "Sname": "Lepidoptera larvae",
        "Cname": "Caterpillar",
        "Description": "Caterpillars, the larval stage of butterflies and moths, are voracious feeders with cylindrical bodies and multiple pairs of legs. They undergo a series of molts as they grow, often causing extensive damage to foliage, fruits, and other plant parts. Caterpillars exhibit a wide range of colors and patterns, often blending in with their surroundings to avoid detection by predators.",
        "Prevention": "Preventing caterpillar damage in farming environments requires a multi-faceted approach. Implementing cultural practices such as crop rotation can disrupt the life cycle of caterpillars by removing their preferred host plants from the growing area. Installing physical barriers like floating row covers or mesh netting can prevent adult butterflies and moths from laying eggs on crops. Additionally, introducing natural enemies such as parasitic wasps and predatory beetles can help keep caterpillar populations in check.",
        "Chemical": "When caterpillar populations exceed tolerable levels, chemical control may be necessary. Biological insecticides containing Bacillus thuringiensis (Bt) are highly effective against many caterpillar species while posing minimal risk to beneficial insects and the environment. Insecticidal soaps and botanical insecticides derived from plants like pyrethrum or neem oil can also provide control.",
        "Cultural": "Cultural practices that promote plant health and resilience can help minimize caterpillar damage. Providing adequate nutrition and irrigation to crops helps them withstand feeding pressure from caterpillars. Removing plant debris and weeds reduces hiding places for caterpillars and their natural enemies. Introducing companion plants that repel or deter caterpillars, such as marigolds or chives, can further enhance pest management efforts."
    },
    "earwig": {
        "Sname": "Dermaptera",
        "Cname": "Earwig",
        "Description": "Earwigs are nocturnal insects characterized by elongated bodies and pincer-like cerci at the end of their abdomens. Despite their intimidating appearance, earwigs are omnivorous scavengers, feeding on a variety of plant material, insects, and decaying organic matter. They are often found in damp, sheltered locations such as under rocks, logs, and in garden debris.",
        "Prevention": "Managing earwig populations in agricultural settings requires a combination of cultural and mechanical control methods. Implementing cultural practices such as reducing moisture levels and removing organic debris can make the environment less favorable for earwigs. Installing traps baited with materials like rolled-up newspaper or cardboard tubes filled with straw or paper can help capture and reduce earwig numbers.",
        "Chemical": "In situations where earwig populations pose a significant threat to crops, chemical control may be warranted. Insecticides containing pyrethrins or carbaryl can provide effective control when applied according to label instructions. However, it's essential to consider the potential impact of chemical treatments on non-target organisms and the environment.",
        "Cultural": "Cultural practices that promote a healthy growing environment can help deter earwigs from becoming problematic. Mulching with materials like gravel or diatomaceous earth creates inhospitable conditions for earwigs by reducing moisture and shelter. Pruning and thinning plants to improve airflow and reduce humidity levels can also discourage earwig infestations."
    },
    "grasshopper": {
        "Sname": "Caelifera",
        "Cname": "Grasshopper",
        "Description": "Grasshoppers are herbivorous insects belonging to the order Caelifera, characterized by powerful hind legs adapted for jumping. They typically feed on a wide range of plants, including grasses, cereals, and legumes, and can cause significant damage to crops during outbreaks. Grasshoppers undergo incomplete metamorphosis, with nymphs resembling miniature versions of adults.",
        "Prevention": "Preventing and managing grasshopper damage in agricultural settings requires a combination of cultural, mechanical, and biological control methods. Implementing cultural practices such as crop diversification and planting trap crops can help reduce grasshopper pressure on valuable crops. Installing physical barriers like mesh screens or row covers can prevent grasshoppers from accessing vulnerable plants.",
        "Chemical": "In cases where grasshopper populations exceed tolerable levels, chemical control may be necessary. Insecticides containing active ingredients such as malathion, permethrin, or cyfluthrin can provide effective control when applied during peak grasshopper activity. It's essential to follow label instructions carefully and consider the potential impact on non-target organisms and the environment.",
        "Cultural": "Cultural practices that promote ecosystem diversity and resilience can help minimize grasshopper damage over the long term. Maintaining good weed control reduces grasshopper habitat and competition for resources. Mowing vegetation around fields and removing crop residues after harvest eliminates hiding places for grasshoppers and reduces overwintering sites."
    },
    "slug":{
        "Sname": "Slug",
        "Cname": "Slug",
        "Description": "Slugs are soft-bodied mollusks with a voracious appetite for young plant tissue. They thrive in moist environments and can cause significant damage to crops, especially seedlings and low-growing plants. Slugs feed by scraping away the outer layers of plant tissue, leaving behind characteristic slime trails. They are most active at night and on cloudy days when humidity levels are high.",
        "Prevention": "Managing slug populations in agricultural settings requires a combination of cultural, mechanical, and biological control methods. Implementing cultural practices such as mulching with materials that slugs dislike, such as gravel or diatomaceous earth, creates inhospitable conditions for slug activity. Installing physical barriers like copper tape or diatomaceous earth around vulnerable plants can prevent slugs from accessing them.",
        "Chemical": "In cases where slug populations exceed tolerable levels, chemical control may be necessary. Iron phosphate-based baits are effective and environmentally friendly options for controlling slugs. These baits work by attracting slugs, which then consume the bait and die. It's important to follow label instructions carefully when using slug baits and to avoid overapplication to minimize the risk of non-target impacts.",
        "Cultural":"Cultural practices that promote a healthy growing environment can help deter slug damage. Watering plants in the morning allows the soil surface to dry out during the day, reducing favorable conditions for slug activity. Handpicking slugs after sunset, when they are most active, can also help reduce populations."       
    },
    "weevil":{
        "Sname": "Weevil",
        "Cname": "Weevil",
        "Description": "Weevils are small beetles with elongated snouts and chewing mouthparts. They infest stored grains, nuts, and seeds, causing contamination and loss of quality. Weevils undergo complete metamorphosis, with adults emerging from pupae laid in grains or other organic matter. Adult weevils typically feed on the exterior of grains, while larvae develop inside, consuming the nutritious inner contents. Infestations are often detected by the presence of small round exit holes in stored products and the accumulation of flour-like frass.",
        "Prevention": "Preventing weevil infestations in stored products requires meticulous sanitation and monitoring. Store grains, nuts, and seeds in airtight containers to prevent adult weevils from accessing them and laying eggs. Regularly inspect stored products for signs of weevil activity, including the presence of exit holes, frass, or adult weevils. Dispose of infested products promptly to prevent the spread of infestations to other stored goods.",
        "Chemical": "In cases where weevil infestations are detected, chemical control measures may be necessary. Treating stored grains with diatomaceous earth or silica gel can effectively kill weevils and prevent further infestations. These desiccant dusts work by absorbing the waxy outer layer of the insect's exoskeleton, leading to dehydration and death. It's essential to apply desiccant dusts evenly and thoroughly to ensure adequate coverage and efficacy against weevils.",
        "Cultural": "Cultural practices that promote proper storage and handling of grains, nuts, and seeds can help prevent weevil infestations. Rotate stored products frequently to prevent prolonged exposure to weevil populations and to ensure that older stocks are used first. Inspect new grain shipments for signs of weevil infestation before storage and quarantine suspect products to prevent the spread of infestations to other stored goods."      
    }
}

# Function to preprocess the image
def preprocess_image(image_path, target_size=(224, 224)):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img = np.array(img) / 255.0  # Normalize to [0, 1]
    img = img.astype(np.float32)  # Convert to FLOAT32
    img = np.expand_dims(img, axis=0)
    interpreter.set_tensor(input_details[0]['index'], img)
        # Run the model
    interpreter.invoke()
    # Get the predicted class
    output_data = interpreter.get_tensor(output_details[0]['index'])
    class_probabilities = output_data.squeeze()  # Remove extra dimensions

    # predicted_class = np.argmax(output_data)

    return class_probabilities
# Updated PEST_NAMES dictionary
PEST_NAMES = {
    0: "Anoplophora chinensis",
    1: "Apriona germari hope",
    2: "Drosicha contrahens male",
    3: "Erthesina fullo",
    4: "Hyphantria cunea",
    5: "Latoia consocia Walker",
    6: "Psilogramma menephron",
    7: "Spilarctia subcarnea Walker",
    8: "ants",
    9: "beetle",
    10: "caterpillar",
    11: "earwig",
    12: "grasshopper",
    13: "slug",
    14: "weevil"
}


@app.route("/pestsubmit", methods = ['GET', 'POST'])
def get_prediction():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save(img_path)
        confidences = preprocess_image(img_path)
        
    sorted_indices = np.argsort(confidences)[::-1]  # Get indices for descending sort
    pest_names = [PEST_NAMES[i] for i in sorted_indices]  # Sort weed names using indices
    confidences = confidences[sorted_indices]  # Sort confidences using indices
    pest_model = zip(pest_names, confidences)  # Zip sorted lists
    # gemini 
    try:
            pmodel = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
            )
            files = [upload_to_gemini(img_path)]
            chat_session = pmodel.start_chat(
            history=[
    {
      "role": "user",
      "parts": [
        files[0],
        "**Can you identify the pest in this image?**\n"
                        "If it's not a pest, please indicate that as well. \n"
                        "Here are some possible pest names for reference (but the image might not be a pest):\n"
                        "{}\n".format(", ".join(PEST_NAMES.values()))
        # "Is this image a pest belonging to any of the following:\nPEST_NAMES = {\n    0: \"Anoplophora chinensis\",\n    1: \"Apriona germari hope\",\n    2: \"Drosicha contrahens male\",\n    3: \"Erthesina fullo\",\n    4: \"Hyphantria cunea\",\n    5: \"Latoia consocia Walker\",\n    6: \"Psilogramma menephron\",\n    7: \"Spilarctia subcarnea Walker\",\n    8: \"ants\",\n    9: \"beetle\",\n    10: \"caterpillar\",\n    11: \"earwig\",\n    12: \"grasshopper\",\n    13: \"slug\",\n    14: \"weevil\"\n}\nif so only say the name\",\n\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "ants \n",
      ],
    },
  ]
            )
            confidence_message = "\n".join([f"{pest_names}: {confidences:.2f}" for pest_names, confidences in pest_model])
            messagepest = (
            "first check whether the uploaded image is a pest or not, If it is not a pest then respond `The image is not a pest, Please Upload correct image`, If it is a pest then identify whther the pest belongs to my dataset, if it is present use myown model confidence score to correctly identify the pest name and respond only the pest name, If is a pest and not present in my dataset respond with `The pest is not avaliable in dataset please upload someother pest`**Here are the confidence scores from my initial model:**\n"
            "{}\n"
            "**Note:** There's a chance the image might not be a pest at all or the model might have predicted wrongly.\n".format(confidence_message)
            ) 
            # message = f"Is this image a pest belonging to any of the following:\n{str(PEST_NAMES)}\nif so only say the name. Here are the confidence scores from another model:\n{confidence_message}"

            response = chat_session.send_message(messagepest)#Is this image a pest belonging to any of the following:\n" + str(PEST_NAMES) + "\nif so only say the name
            gemini_result = response.text
    except Exception as e:
             gemini_result=pest_names[0] 

    correct_pest_data = pest_data.get(gemini_result.strip())
    return render_template("pest_result.html",pest_det=correct_pest_data, data=pest_names[0],pest_model=pest_model,img_path=img_path,result =gemini_result)

# designing works starts here
crop_descriptions = {
    "banana.jpg": "Bananas thrive in warm, humid environments, making your climate ideal for their growth. Additionally, the well-drained soil suggested by your NPK levels is optimal for banana cultivation, promoting healthy root development and nutrient uptake.",
    "blackgram.png": "Blackgram is well-suited to warm climates with moderate rainfall, aligning perfectly with your environmental conditions. Its ability to fix nitrogen makes it beneficial for soil health, while its tolerance to drier conditions ensures resilience during periods of reduced rainfall.",
    "chickpea.jpg": "Chickpeas, being nitrogen-fixing legumes, are particularly suited for areas with moderate rainfall. Their ability to thrive in drier conditions makes them resilient to fluctuations in precipitation, while their nitrogen-fixing ability enriches the soil, benefiting future crops.",
    "coconut.png": "Coconut palms thrive in warm, humid climates, making them an excellent fit for your land. Their deep root systems and tolerance to high temperatures ensure their resilience in your environmental conditions, while their moderate water needs align well with your rainfall patterns.",
    "coffee.png": "Coffee plants prefer slightly acidic soil, and your specific pH level suggests an environment conducive to their growth. With the right soil conditions and adequate moisture, coffee plants can thrive in your climate, producing high-quality beans for harvest.",
    "cotton.png": "Cotton thrives in warm temperatures, making your climate ideal for its cultivation. The combination of warm temperatures and the well-drained soil suggested by your data provides optimal conditions for cotton growth, promoting healthy plant development and fiber production.",
    "grapes.png": "Grapes prefer warm temperatures and abundant sunlight, both of which are characteristic of your climate. With the right conditions, including well-drained soil and adequate sunlight, grapevines can flourish on your land, producing high-quality fruit for harvest.",
    "groundnuts.png": "Groundnuts thrive in warm temperatures and are relatively drought tolerant, making them well-suited for your climate. Additionally, their ability to fix nitrogen enriches the soil, benefiting future crops, while their moderate water needs align with your rainfall patterns, reducing irrigation demands.",
    "jute.png": "Jute thrives in warm and humid conditions, which align well with your temperature and humidity levels. Its moderate water needs and tolerance to varying soil conditions make it a suitable crop for your land, potentially reducing irrigation demands and promoting sustainable cultivation practices.",
    "kidneybeans.jpg": "Kidney beans prefer warm climates, as indicated by your temperature data. Additionally, their moderate water needs align with your rainfall patterns, reducing irrigation demands. Their ability to fix nitrogen enriches the soil, benefiting future crops, particularly if nitrogen levels are slightly low.",
    "lentil.png": "Lentils, like other legumes, fix nitrogen from the air and deposit it in the soil, enriching it for future crops. This nitrogen-fixing ability makes lentils beneficial for soil health, while their moderate water needs align with your rainfall patterns, reducing irrigation demands.",
    "maize.jpeg": "Maize has a moderate to high demand for nutrients, and the NPK levels you provided might be favorable for its growth. Additionally, the warm temperatures and well-drained soil suggested by your data align well with maize's preference for good drainage and optimal growing conditions, promoting healthy plant development and yield.",
    "mango.png": "Mangoes thrive in warm climates with well-drained soil, both of which are characteristic of your land. The combination of warm temperatures and optimal soil conditions provides an ideal environment for mango trees to flourish, producing high-quality fruit for harvest.",
    "mothbean.png": "Mothbeans are an ideal choice for your land due to their drought tolerance and ability to grow in a wide range of soil conditions. These characteristics make them resilient to fluctuations in rainfall and soil type, ensuring consistent yields even under variable environmental conditions.",
    "mungbeans.png": "Mungbeans are an excellent choice for your land because they are legumes and thrive in warm conditions. Their ability to fix nitrogen enriches the soil, benefiting future crops, while their moderate water needs align with your rainfall patterns, potentially reducing irrigation demands and promoting sustainable cultivation practices.",
    "muskmelon.png": "Muskmelon's high water content complements moderate rainfall, potentially reducing irrigation needs. Hence, it is the most favorable plant for your land, ensuring optimal fruit development and yield under your environmental conditions.",
    "orange.jpeg": "Oranges have the potential to flourish on your land due to their deep root systems and moderate water needs, which align well with your rainfall patterns. Their ability to access nutrients lower in the soil ensures consistent growth and fruit production, making them an ideal crop for your environmental conditions.",
    "papaya.png": "Papaya thrives in tropical climates and doesn't require excessive water, potentially making it adaptable to your rainfall patterns. Its ability to tolerate a range of soil conditions ensures resilience in varying environmental conditions, promoting sustainable cultivation practices and consistent yields.",
    "pigeonpeas.png": "Pigeonpea is well-suited for your land due to its deep root system, drought tolerance, and nitrogen-fixing ability. These characteristics enable pigeonpeas to access nutrients lower in the soil and enrich it for future crops, while their ability to thrive in warm climates ensures consistent growth and yield under your environmental conditions.",
    "pomegranate.png": "Pomegranate tolerates a range of soil conditions, making it adaptable to your land. The NPK balance and well-drained soil suggested by your data align well with pomegranate's needs, promoting healthy fruit development and yield under your environmental conditions.",
    "rice.jpg": "Rice appears well-suited for your land, thriving in warm, humid conditions with a good water supply. Paddy rice cultivation is a productive choice for your land, potentially ensuring high yields and profitability under your environmental conditions.",
    "watermelon.png": "Watermelon could be a good fit for your land due to warm temperatures, moderate rainfall, and well-drained soil indicated by your NPK levels. These conditions provide an optimal environment for watermelon cultivation, ensuring high-quality fruit development and yield under your environmental conditions."
}

@app.route("/")
def Display_IMG():
    IMG_LIST = os.listdir("static/img")
    IMG_LIST = ["img/" + i for i in IMG_LIST]
    return render_template("crop_predict.html", imagelist=IMG_LIST, static_url_path=app.static_url_path)

if __name__ == "__main__":
    app.run(debug=True)