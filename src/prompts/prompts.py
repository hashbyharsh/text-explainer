# Prompt templates

CONTEXT_PROMPT_NORMAL = (
    "Explain the meaning of '{selected_text}' in the following page context: '{context}'. "
    "Provide a concise explanation tailored to the context in {language}."
)

CONTEXT_PROMPT_SIMPLIFY = (
    "Explain the meaning of '{selected_text}' in the following page context: '{context}'. "
    "Provide a short, simple explanation in plain {language}, avoiding technical terms."
)

GENERIC_PROMPT_NORMAL = (
    "Provide a concise, generic explanation of the meaning of '{selected_text}' in {language}."
)

GENERIC_PROMPT_SIMPLIFY = (
    "Provide a short, simple, generic explanation of the meaning of '{selected_text}' in plain {language}."
)