# Prompt templates

CONTEXT_PROMPT_NORMAL = (
    "Using the context '{context}' to guide the explanation, describe the meaning of '{selected_text}' in a concise way (1–3 short sentences) using {language}. "
    "Always assume the user is not a technical person, avoid jargon, and use a friendly, easy-to-understand tone. "
    "If the term is technical, include a simple real-world analogy or example (like explaining 'bandwidth' as how many cars can pass through a road at once). "
    "Do not mention the context or phrases like 'related to,' 'in the context of,' 'refers to,' or the context and itself in the explanation."
)

CONTEXT_PROMPT_SIMPLIFY = (
    "Using the context '{context}' to guide the explanation, describe the meaning of '{selected_text}' in a short, simple way using plain {language}. "
    "Do not mention the context or phrases like 'related to,' 'in the context of,' or the context itself in the explanation."
)