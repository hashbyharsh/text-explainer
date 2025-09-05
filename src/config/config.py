import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = int(os.getenv("REDIS_PORT"))
    SECRET_KEY = os.getenv("SECRET_KEY")
    RATE_LIMIT = int(os.getenv("RATE_LIMIT"))
    RATE_LIMIT_WINDOW = int(os.getenv("RATE_LIMIT_WINDOW"))

    CACHE_TTL = 3600
    EXPECTED_MESSAGE = "qwerty"

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


config = Config()


