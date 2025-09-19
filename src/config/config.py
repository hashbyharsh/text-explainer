import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = int(os.getenv("REDIS_PORT"))
    SECRET_KEY = os.getenv("SECRET_KEY")
    EXPECTED_MESSAGE = os.getenv("EXPECTED_MESSAGE")
    RATE_LIMIT = int(os.getenv("RATE_LIMIT"))
    RATE_LIMIT_WINDOW = int(os.getenv("RATE_LIMIT_WINDOW"))

    CACHE_TTL = 3600

    VALID_LOCALES = ["en", "hi", "te", "ta", "pb", "mr"]

    LANGUAGE_MAP = {
    "en": "English",
    "hi": "Hindi",
    "te": "Telugu",
    "ta": "Tamil",
    "pb": "Punjabi",
    "mr": "Marathi"
}

    NO_CONTEXT_MESSAGE = {
    "en": "Without additional context, it is difficult to provide a meaningful explanation for this single word.",
    "hi": "अतिरिक्त संदर्भ के बिना, इस एकल शब्द के लिए सार्थक व्याख्या देना कठिन है।",
    "te": "అదనపు సందర్భం లేకుండా, ఈ ఒక్క పదానికి అర్థవంతమైన వివరణ ఇవ్వడం కష్టం.",
    "ta": "கூடுதல் சூழல் இல்லாமல், இந்த ஒற்றை வார்த்தைக்கு அர்த்தமுள்ள விளக்கம் அளிப்பது கடினம்.",
    "pb": "ਬਿਨਾਂ ਵਾਧੂ ਪ੍ਰਸੰਗ ਦੇ, ਇਸ ਸਿੰਗਲ ਸ਼ਬ्द ਲਈ ਅਰਥਪੂਰਨ ਵਿਆਖਿਆ ਪ੍ਰਦਾਨ ਕਰਨਾ ਮੁਸ਼ਕਲ ਹੈ।",
    "mr": "अतिरिक्त संदर्भाशिवाय, या एकाच शब्दासाठी अर्थपूर्ण स्पष्टीकरण देणे कठीण आहे."
}

    GIBBERISH_MESSAGE = {
    "en": "The selected text {selected_text} does not provide sufficient information for me to provide a meaningful explanation.",
    "hi": "चयनित पाठ {selected_text} मेरे लिए अर्थपूर्ण व्याख्या प्रदान करने के लिए पर्याप्त जानकारी नहीं देता।",
    "te": "ఎంపిక చేసిన పాఠ్యం {selected_text} నాకు అర్థవంతమైన వివరణ ఇవ్వడానికి తగినంత సమాచారాన్ని అందించదు.",
    "ta": "தேர்ந்தெடுக்கப்பட்ட உரை {selected_text} எனக்கு அர்த்தமுள்ள விளக்கம் அளிப்பதற்கு போதுமான தகவலை வழங்கவில்லை.",
    "pb": "ਚੁਣਿਆ ਗਿਆ ਟੈਕਸਟ {selected_text} ਮੇਰੇ ਲਈ ਅਰਥਪੂਰਨ ਸਪੱਸ਼ਟੀਕਰਨ ਪ੍ਰਦਾਨ ਕਰਨ ਲਈ ਕافی ਜਾਣਕਾਰੀ ਨਹੀਂ ਦਿੰਦਾ।",
    "mr": "निवडलेले मजकूर {selected_text} मला अर्थपूर्ण स्पष्टीकरण देण्यासाठी पुरेसे माहिती पुरवत नाही."
}
    
    STATIC_CONTEXTS = {
    "TRUCKS": """
    The selected text pertains to trucks, heavy-duty vehicles designed for transporting goods in logistics, construction, and agriculture. Key aspects include:
    1. **Specifications**: Trucks range from light-duty pickups (0.5–2 tons) to heavy-duty semi-trucks (10+ tons). Engines (diesel, electric) deliver 200–600 hp, with axle setups (4x2, 6x4) for varied terrains. Features like telematics and driver-assistance systems boost efficiency.
    2. **Maintenance**: Regular oil changes (10,000–25,000 miles), tire checks, and brake inspections ensure safety and compliance with DOT standards. Predictive maintenance reduces downtime.
    3. **Load Capacity**: Payloads reach 80,000 pounds for semi-trucks, with proper load distribution critical for stability.
    4. **Industry Standards**: FMCSA regulates driver hours; EPA Tier 4/Euro 6 mandates low emissions. Trends include electric and autonomous trucks.
    Explain truck-related queries with technical details and compliance focus, using clear examples.
    """,
    "BUSES": """
    The selected text pertains to buses, passenger vehicles for urban, intercity, or school transport, prioritizing safety and comfort. Key aspects include:
    1. **Specifications**: Buses range from minibuses (10–25 passengers) to articulated models (100+). Diesel, CNG, or electric engines (200–400 hp) power them, with features like low floors and AVL systems.
    2. **Maintenance**: Daily checks (brakes, tires) and oil changes (5,000–10,000 miles) ensure reliability. Predictive maintenance via IoT minimizes disruptions.
    3. **Load Capacity**: A 40-foot bus carries 40–60 passengers; GVW reaches 60,000 pounds for articulated models.
    4. **Industry Standards**: NHTSA mandates ABS; ADA ensures accessibility. EPA 2010/Euro 6 drives electric bus adoption.
    Explain bus queries with emphasis on specs, maintenance, capacity, and regulations, using clear examples.
    """,
    "TRACTORS": """
    The selected text pertains to tractors, versatile vehicles for farming and construction tasks like plowing and towing. Key aspects include:
    1. **Specifications**: Tractors range from compact (20–50 hp) to large models (100–600 hp). Diesel or electric engines, 2WD/4WD, and three-point hitches support implements. GPS and auto-steer enhance precision.
    2. **Maintenance**: Oil changes (every 100–200 hours), hydraulic checks, and tire maintenance prevent downtime. Software updates ensure precision tool accuracy.
    3. **Load Capacity**: Mid-sized tractors tow 5–10 tons; hydraulic lifts handle 2,000–10,000 pounds. Ballasting optimizes traction.
    4. **Industry Standards**: OSHA mandates ROPS; EPA Tier 4/EU Stage V requires low-emission engines. Autonomous and electric tractors are emerging trends.
    Address tractor queries with focus on specs, maintenance, capacity, and standards, using practical examples.
    """,
    "THREE_WHEELERS": """
    The selected text pertains to three-wheelers, compact vehicles for passenger or cargo transport in urban settings. Key aspects include:
    1. **Specifications**: Powered by 5–15 hp petrol, CNG, or electric engines, three-wheelers carry 200–500 kg. Features include digital meters and electric start.
    2. **Maintenance**: Oil changes (every 2,000–3,000 km), brake checks, and tire inspections ensure safety. Electric models need battery monitoring.
    3. **Load Capacity**: Passenger models carry 2–6 people; cargo variants handle 200–500 kg. Weight distribution prevents tipping.
    4. **Industry Standards**: CMVR in India mandates mirrors and indicators; Bharat Stage VI pushes electric options. GPS integration aids ride-hailing.
    Address three-wheeler queries with focus on specs, maintenance, capacity, and regional standards, using clear examples.
    """
}



config = Config()


