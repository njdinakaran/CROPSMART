
const fullcropdata = [
    {
        name: 'Banana',
        description: 'Bananas thrive in warm, humid environments, making your climate ideal for their growth. Additionally, the well-drained soil suggested by your NPK levels is optimal for banana cultivation, promoting healthy root development and nutrient uptake.',
        image: 'banana.jpg'
    },
    {
        name: 'Blackgram',
        description: 'Blackgram is well-suited to warm climates with moderate rainfall, aligning perfectly with your environmental conditions. Its ability to fix nitrogen makes it beneficial for soil health, while its tolerance to drier conditions ensures resilience during periods of reduced rainfall.',
        image: 'blackgram.png'
    },
    {
        name: 'Chickpea',
        description: 'Chickpeas, being nitrogen-fixing legumes, are particularly suited for areas with moderate rainfall. Their ability to thrive in drier conditions makes them resilient to fluctuations in precipitation, while their nitrogen-fixing ability enriches the soil, benefiting future crops.',
        image: 'chickpea.jpg'
    },
    {
        name: 'Coconut',
        description: 'Coconut palms thrive in warm, humid climates, making them an excellent fit for your land. Their deep root systems and tolerance to high temperatures ensure their resilience in your environmental conditions, while their moderate water needs align well with your rainfall patterns.',
        image: 'coconut.png'
    },
    {
        name: 'Coffee',
        description: 'Coffee plants prefer slightly acidic soil, and your specific pH level suggests an environment conducive to their growth. With the right soil conditions and adequate moisture, coffee plants can thrive in your climate, producing high-quality beans for harvest.',
        image: 'coffee.png'
    },
    {
        name: 'Cotton',
        description: 'Cotton thrives in warm temperatures, making your climate ideal for its cultivation. The combination of warm temperatures and the well-drained soil suggested by your data provides optimal conditions for cotton growth, promoting healthy plant development and fiber production.',
        image: 'cotton.png'
    },
    {
        name: 'Grapes',
        description: 'Grapes prefer warm temperatures and abundant sunlight, both of which are characteristic of your climate. With the right conditions, including well-drained soil and adequate sunlight, grapevines can flourish on your land, producing high-quality fruit for harvest.',
        image: 'grapes.png'
    },
    {
        name: 'Groundnuts',
        description: 'Groundnuts thrive in warm temperatures and are relatively drought tolerant, making them well-suited for your climate. Additionally, their ability to fix nitrogen enriches the soil, benefiting future crops, while their moderate water needs align with your rainfall patterns, reducing irrigation demands.',
        image: 'groundnuts.png'
    },
    {
        name: 'Jute',
        description: 'Jute thrives in warm and humid conditions, which align well with your temperature and humidity levels. Its moderate water needs and tolerance to varying soil conditions make it a suitable crop for your land, potentially reducing irrigation demands and promoting sustainable cultivation practices.',
        image: 'jute.png'
    },
    {
        name: 'KidneyBeans',
        description: 'Kidney beans prefer warm climates, as indicated by your temperature data. Additionally, their moderate water needs align with your rainfall patterns, reducing irrigation demands. Their ability to fix nitrogen enriches the soil, benefiting future crops, particularly if nitrogen levels are slightly low.',
        image: 'kidneybeans.jpg'
    },
    {
        name: 'Lentil',
        description: 'Lentils, like other legumes, fix nitrogen from the air and deposit it in the soil, enriching it for future crops. This nitrogen-fixing ability makes lentils beneficial for soil health, while their moderate water needs align with your rainfall patterns, reducing irrigation demands.',
        image: 'lentil.png'
    },
    {
        name: 'Maize',
        description: 'Maize has a moderate to high demand for nutrients, and the NPK levels you provided might be favorable for its growth. Additionally, the warm temperatures and well-drained soil suggested by your data align well with maize\'s preference for good drainage and optimal growing conditions, promoting healthy plant development and yield.',
        image: 'maize.jpeg'
    },
    {
        name: 'Mango',
        description: 'Mangoes thrive in warm climates with well-drained soil, both of which are characteristic of your land. The combination of warm temperatures and optimal soil conditions provides an ideal environment for mango trees to flourish, producing high-quality fruit for harvest.',
        image: 'mango.png'
    },
    {
        name: 'Mothbeans',
        description: 'Mothbeans are an ideal choice for your land due to their drought tolerance and ability to grow in a wide range of soil conditions. These characteristics make them resilient to fluctuations in rainfall and soil type, ensuring consistent yields even under variable environmental conditions.',
        image: 'mothbean.png'
    },
    {
        name: 'Mungbean',
        description: 'Mungbeans are an excellent choice for your land because they are legumes and thrive in warm conditions. Their ability to fix nitrogen enriches the soil, benefiting future crops, while their moderate water needs align with your rainfall patterns, potentially reducing irrigation demands and promoting sustainable cultivation practices.',
        image: 'mungbeans.png'
    },
    {
        name: 'Muskmelon',
        description: 'Muskmelon\'s high water content complements moderate rainfall, potentially reducing irrigation needs. Hence, it is the most favorable plant for your land, ensuring optimal fruit development and yield under your environmental conditions.',
        image: 'muskmelon.png'
    },
    {
        name: 'Orange',
        description: 'Oranges have the potential to flourish on your land due to their deep root systems and moderate water needs, which align well with your rainfall patterns. Their ability to access nutrients lower in the soil ensures consistent growth and fruit production, making them an ideal crop for your environmental conditions.',
        image: 'orange.jpeg'
    },
    {
        name: 'Papaya',
        description: 'Papaya thrives in tropical climates and doesn\'t require excessive water, potentially making it adaptable to your rainfall patterns. Its ability to tolerate a range of soil conditions ensures resilience in varying environmental conditions, promoting sustainable cultivation practices and consistent yields.',
        image: 'papaya.png'
    },
    {
        name: 'Pigeonpeas',
        description: 'Pigeonpea is well-suited for your land due to its deep root system, drought tolerance, and nitrogen-fixing ability. These characteristics enable pigeonpeas to access nutrients lower in the soil and enrich it for future crops, while their ability to thrive in warm climates ensures consistent growth and yield under your environmental conditions.',
        image: 'pigeonpeas.png'
    },
    {
        name: 'Pomegranate',
        description: 'Pomegranate tolerates a range of soil conditions, making it adaptable to your land. The NPK balance and well-drained soil suggested by your data align well with pomegranate\'s needs, promoting healthy fruit development and yield under your environmental conditions.',
        image: 'pomegranate.png'
    },
    {
        name: 'Rice',
        description: 'Rice appears well-suited for your land, thriving in warm, humid conditions with a good water supply. Paddy rice cultivation is a productive choice for your land, potentially ensuring high yields and profitability under your environmental conditions.',
        image: 'rice.jpg'
    },
    {
        name: 'Watermelon',
        description: 'Watermelon could be a good fit for your land due to warm temperatures, moderate rainfall, and well-drained soil indicated by your NPK levels. These conditions provide an optimal environment for watermelon cultivation, ensuring high-quality fruit development and yield under your environmental conditions.',
        image: 'wmelon.jpg'
    }

];

const fullpestdata = [
    {
        name: 'Anoplophora chinensis',
        commonName: 'Citrus Longhorn Beetle',
        description: 'The Citrus Longhorn Beetle is an invasive pest that attacks various trees, including citrus, causing extensive damage to bark and wood. It can lead to tree decline and death if left unchecked.',
        imageName: 'pest1.jpg'
    },
    {
        name: 'Apriona germari hope',
        commonName: 'Apriona Beetle',
        description: 'The Apriona Beetle is a destructive pest of fruit and ornamental trees, particularly in orchards and urban landscapes. It feeds on foliage, causing defoliation and weakening the trees.',
        imageName: 'pest2.jpg'
    },
    {
        name: 'Drosicha contrahens male',
        commonName: 'Mulberry Looper Male',
        description: 'The Mulberry Looper Male is a moth species that mates with females to facilitate reproduction. It plays a role in the lifecycle of the mulberry looper pest.',
        imageName: 'pest3.jpg'
    },
    {
        name: 'Erthesina fullo',
        commonName: 'Brown Marmorated Stink Bug',
        description: 'The Brown Marmorated Stink Bug is an invasive pest that feeds on various crops and ornamental plants. It damages fruits, vegetables, and ornamentals by piercing and sucking sap.',
        imageName: 'pest4.jpg'
    },
    {
        name: 'Hyphantria cunea',
        commonName: 'Fall Webworm',
        description: 'The Fall Webworm is a defoliating pest of deciduous trees, particularly in forests. It forms communal nests and feeds on leaves, causing extensive defoliation and tree stress.',
        imageName: 'pest5.jpg'
    },
    {
        name: 'Latoia consocia Walker',
        commonName: 'Citrus Psyllid',
        description: 'The Citrus Psyllid is a sap-sucking pest of citrus trees, particularly affecting new growth and young plants. It can transmit plant pathogens, causing disease and reducing crop yield.',
        imageName: 'pest6.jpg'
    },
    {
        name: 'Psilogramma menephron',
        commonName: 'Psilogramma Moth',
        description: 'The Psilogramma Moth is a nocturnal insect species belonging to the family Erebidae. It is characterized by its mottled appearance and is known to feed on various plant species.',
        imageName: 'pest7.jpg'
    },
    {
        name: 'Spilarctia subcarnea Walker',
        commonName: 'Spilarctia Caterpillar',
        description: 'The Spilarctia Caterpillar is the larval stage of a moth species belonging to the family Erebidae. It is characterized by its fuzzy appearance and voracious appetite. The larvae feed on plant foliage, causing defoliation and weakening of plants.',
        imageName: 'pest8.jpg'
    },
    {
        name: 'ants',
        commonName: 'Ants',
        description: 'Ants are pests in agriculture, known for farming aphids and other pests that harm crops. They create underground nests, disturbing plant roots and soil structure, leading to reduced crop yields and plant health.',
        imageName: 'pest9.jpg'
    },
    {
        name: 'beetle',
        commonName: 'Beetle',
        description: 'Beetles, belonging to the order Coleoptera, are one of the most diverse groups of insects, with over 350,000 species worldwide. They range in size from tiny, barely visible species to large, conspicuous ones. Beetles typically have hardened forewings called elytra, which cover the membranous hindwings and protect the body. They exhibit a wide range of feeding habits, with some species being herbivores, others predators, and some scavengers.',
        imageName: 'pest10.jpg'
    },
    {
        name: 'caterpillar',
        commonName: 'Caterpillar',
        description: 'Caterpillars, the larval stage of butterflies and moths, are voracious feeders with cylindrical bodies and multiple pairs of legs. They undergo a series of molts as they grow, often causing extensive damage to foliage, fruits, and other plant parts. Caterpillars exhibit a wide range of colors and patterns, often blending in with their surroundings to avoid detection by predators.',
        imageName: 'pest11.jpg'
    },
    {
        name: 'earwig',
        commonName: 'Earwig',
        description: 'Earwigs are nocturnal insects characterized by elongated bodies and pincer-like cerci at the end of their abdomens. Despite their intimidating appearance, earwigs are omnivorous scavengers, feeding on a variety of plant material, insects, and decaying organic matter. They are often found in damp, sheltered locations such as under rocks, logs, and in garden debris.',
        imageName: 'pest12.jpg'
    },
    {
        name: 'grasshopper',
        commonName: 'Grasshopper',
        description: 'Grasshoppers are herbivorous insects belonging to the order Caelifera, characterized by powerful hind legs adapted for jumping. They typically feed on a wide range of plants, including grasses, cereals, and legumes, and can cause significant damage to crops during outbreaks. Grasshoppers undergo incomplete metamorphosis, with nymphs resembling miniature versions of adults.',
        imageName: 'pest13.jpg'
    },
    {
        name: 'slug',
        commonName: 'Slug',
        description: 'Slugs are soft-bodied mollusks with a voracious appetite for young plant tissue. They thrive in moist environments and can cause significant damage to crops, especially seedlings and low-growing plants. Slugs feed by scraping away the outer layers of plant tissue, leaving behind characteristic slime trails. They are most active at night and on cloudy days when humidity levels are high.',
        imageName: 'pest14.jpg'
    },
    {
        name: 'weevil',
        commonName: 'Weevil',
        description: 'Weevils are small beetles with elongated snouts and chewing mouthparts. They infest stored grains, nuts, and seeds, causing contamination and loss of quality. Weevils undergo complete metamorphosis, with adults emerging from pupae laid in grains or other organic matter. Adult weevils typically feed on the exterior of grains, while larvae develop inside, consuming the nutritious inner contents. Infestations are often detected by the presence of small round exit holes in stored products and the accumulation of flour-like frass.',
        imageName: 'pest15.jpg'
    }
];
const weedData = [
    {
        name: 'Parthenium hysterophorus',
        commonName: 'Congress grass',
        description: 'One of the most problematic weeds in India, causing severe health issues (allergies, skin irritations) in humans and animals. Reduces crop yields significantly by competing for water, nutrients, and sunlight. Spreads rapidly through wind-dispersed seeds, making control challenging.',
        image: 'weed8.jpg'
    },
    {
        name: 'Echinochloa crus-galli',
        commonName: 'Barnyard grass',
        description: 'A major competitor in rice fields, aggressively competing with rice plants for essential resources like nutrients, light, and space. Reproduces rapidly by seeds, forming dense mats that can smother rice crops and hinder their growth. Difficult to control due to its ability to germinate underwater, allowing it to establish itself before rice seedlings.',
        image: 'weed7.jpg'
    },
    {
        name: 'Amaranthus spp',
        commonName: 'Amaranth',
        description: 'Common and diverse group of weeds found in agricultural fields, including grain amaranth and pigweed. Significantly reduce crop yields by competing with crops for water, nutrients, and sunlight. Fast-growing and prolific seed producers, allowing them to quickly establish large populations. Caution: While some Amaranthus species have edible leaves, be aware that certain varieties may be toxic.',
        image: 'weed0.jpeg'
    },
    {
        name: 'Convolvulus arvensis',
        commonName: 'Field bindweed',
        description: 'A persistent problem in agriculture, vineyards, and orchards due to its extensive underground root system that makes eradication difficult. Competes fiercely with crops for water and nutrients, hindering their growth and productivity. Spreads both by seeds and by creeping roots, allowing it to quickly establish large infestations.',
        image: 'weed4.jpg'
    },
    {
        name: 'Cyperus rotundus',
        commonName: 'Nutgrass',
        description: 'A perennial weed that infests agricultural fields and reduces crop yields by competing for resources. Forms tubers underground, enabling it to survive harsh conditions, reproduce asexually, and make control difficult. The extensive underground network of tubers allows nutgrass to regrow even after removal of the above-ground parts.',
        image: 'weed5.jpg'
    },
    {
        name: 'Chenopodium album',
        commonName: 'Lamb\'s quarters',
        description: 'Widespread weed in India, posing a significant problem during the monsoon season due to its rapid growth, especially in moist conditions. Competes with crops for water, nutrients, and sunlight, impacting their growth and yield. Fast-growing and matures quickly, taking advantage of the monsoon rains to establish itself and compete with crops. Produces large quantities of seeds that can remain viable in the soil for many years, ensuring its persistence.',
        image: 'weed1.jpg'
    },
    {
        name: 'Phalaris minor',
        commonName: 'Little seed canary grass',
        description: 'A major weed in wheat fields of India, competing with wheat plants for resources and reducing yields. Winter-annual grass that germinates in the fall and matures in the spring, potentially outcompeting spring-sown wheat. Difficult to control in the early stages due to its resemblance to wheat seedlings, making identification and removal challenging.',
        image: 'weed9.jpg'
    },
    {
        name: 'Cirsium arvense',
        commonName: 'Canada thistle',
        description: 'An invasive weed that aggressively competes with crops for water and nutrients, reducing their growth and productivity. Spreads rapidly by both seeds and creeping roots, forming dense patches that crowd out crops and hinder their access to sunlight. Difficult to control due to its extensive root system that allows it to regenerate even after removal of the above-ground parts.',
        image: 'weed2.jpg'
    },
    {
        name: 'Commelina benghalensis',
        commonName: 'Benghal dayflower',
        description: 'Found in various crops like rice, sugarcane, and maize, reducing yields by competing for water, nutrients, and sunlight. Low-growing, spreading weed that forms dense mats, smothering crops and hindering their growth. Prolific seed producer, allowing it to spread quickly and establish large populations in a short period.',
        image: 'weed3.jpg'
    },
    {
        name: 'Dactyloctenium aegyptium',
        commonName: 'Crowfoot grass',
        description: 'Widespread weed in India, particularly problematic in dryland agriculture, where it competes with crops for scarce water resources. Matures quickly and produces a large number of seeds that can stay viable in the soil for several years, ensuring its persistence even during dry periods. This allows crowfoot grass to readily establish itself and compete with crops for moisture as soon as rains arrive.',
        image: 'weed6.jpg'
    }
];


let currentIndex = 0;
let pestIndex = 0;
let weedIndex =0;

const staticUrlPath = '{{ static_url_path }}';

function showCrop(index) {
    const crop = fullcropdata[index];
    if (!crop || !crop.image) {
        console.error('Invalid crop data or image missing for index', index);
        return;
    }
    const imagePath = `static/img/${crop.image}`;
    document.getElementById('crop-image').src = imagePath;
    document.getElementById('crop-title').textContent = crop.name;
    document.getElementById('crop-description').textContent = crop.description;
    showPest(pestIndex);
}

function showPest(index) {
    const pest = fullpestdata[index];
    if (!pest || !pest.imageName) {
        console.error('Invalid pest data or image missing for index', index);
        return;
    }
    const imagePath = `static/img/${pest.imageName}`;
    document.getElementById('pestname').textContent = pest.name;
    document.getElementById('pest-image').src = imagePath;
    document.getElementById('pest-title').textContent = pest.commonName;
    document.getElementById('pest-description').textContent = pest.description;
}

function showWeed(index) {
    const weed = weedData[index];
    if (!weed || !weed.image) {
        console.error('Invalid pest data or image missing for index', index);
        return;
    }
    const imagePath = `static/img/${weed.image}`;
    document.getElementById('weedname').textContent = weed.name;

    document.getElementById('weed-image').src = imagePath;
    document.getElementById('weed-title').textContent = weed.commonName;
    document.getElementById('weed-description').textContent = weed.description;
}

document.getElementById('pbutton').addEventListener('click', () => {
    currentIndex = (currentIndex === 0) ? fullcropdata.length - 1 : currentIndex - 1;
    showCrop(currentIndex);
});

document.getElementById('nbutton').addEventListener('click', () => {
    currentIndex = (currentIndex === fullcropdata.length - 1) ? 0 : currentIndex + 1;
    showCrop(currentIndex);
});

document.getElementById('ppestbutton').addEventListener('click', () => {
    console.log("Previous pest button clicked");
    pestIndex = (pestIndex === 0) ? fullpestdata.length - 1 : pestIndex - 1;
    showPest(pestIndex);
});

document.getElementById('npestbutton').addEventListener('click', () => {
    console.log("Next pest button clicked");
    pestIndex = (pestIndex === fullpestdata.length - 1) ? 0 : pestIndex + 1;
    showPest(pestIndex);
});
// weed button

document.getElementById('pweedbutton').addEventListener('click', () => {
    console.log("Previous pest button clicked");
    weedIndex = (weedIndex === 0) ? weedData.length - 1 : weedIndex - 1;
    showWeed(weedIndex);
});

document.getElementById('nweedbutton').addEventListener('click', () => {
    console.log("Next pest button clicked");
    weedIndex = (weedIndex === weedData.length - 1) ? 0 : weedIndex + 1;
    showWeed(weedIndex);
});

setInterval(() => {
    currentIndex = (currentIndex === fullcropdata.length - 1) ? 0 : currentIndex + 1;
    showCrop(currentIndex);
}, 10000);

setInterval(() => {
    pestIndex = (pestIndex === fullpestdata.length - 1) ? 0 : pestIndex + 1;
    showPest(pestIndex);
}, 10000);
setInterval(() => {
    weedIndex = (weedIndex === weedData.length - 1) ? 0 : weedIndex + 1;
    showWeed(weedIndex);
}, 10000);


// Initial display
showCrop(currentIndex);
showPest(pestIndex);
showWeed(weedIndex);



// let currentIndex = 0;
// let pestindex=0

// const staticUrlPath = '{{ static_url_path }}';

// function showCrop(index) {
//     const crop = fullcropdata[index];
//     if (!crop || !crop.image) {
//         return;
//     }
//     console.log(fullcropdata)
//     var imagepath = `static/img/${crop.image}`;
//     document.getElementById('crop-image').src = imagepath;
//     document.getElementById('crop-title').textContent = crop.name;
//     document.getElementById('crop-description').textContent = crop.description;
//     showpest(pestindex);
// }

// document.getElementById('pbutton').addEventListener('click', () => {
//     currentIndex = (currentIndex === 0) ? fullcropdata.length - 1 : currentIndex - 1;
//     showCrop(currentIndex);
// });

// document.getElementById('nbutton').addEventListener('click', () => {
//     currentIndex = (currentIndex === fullcropdata.length - 1) ? 0 : currentIndex + 1;
//     showCrop(currentIndex);
// });

// setInterval(() => {
//     currentIndex = (currentIndex === fullcropdata.length - 1) ? 0 : currentIndex + 1;
//     showCrop(currentIndex);
// }, 10000);




// function showpest(index) {
//     const crop = fullpestdata[index];
//     if (!crop || !crop.image) {
//         return;
//     }
//     console.log(fullpestdata)
//     var imagepath = `static/img/${crop.imageName}`;
//     document.getElementById('pest-image').src = imagepath;
//     document.getElementById('pest-title').textContent = crop.name;
//     document.getElementById('pest-description').textContent = crop.description;
// }

// document.getElementById('ppestbutton').addEventListener('click', () => {
//     console.log("perv clicked")

//     pestindex = (pestindex === 0) ? fullpestdata.length - 1 : pestindex - 1;
//     showpest(pestindex);
// });

// document.getElementById('npestbutton').addEventListener('click', () => {
//     console.log("nextbutton clicked")
//     pestindex = (pestindex === fullpestdata.length - 1) ? 0 : pestindex + 1;
//     showpest(pestindex);
// });

// setInterval(() => {
//     pestindex = (pestindex === fullpestdata.length - 1) ? 0 : pestindex + 1;
//     showpest(pestindex);
// }, 10000);

// // Initial display

// // Initial display
// showCrop(currentIndex);
// showpest(pestindex);