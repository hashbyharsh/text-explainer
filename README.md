**Text Explainer**

A FastAPI-based web application that provides contextual explanations for selected text using the Groq API, with caching, token authentication, and rate limiting.

**Overview**

The Text Explainer application allows users to input a piece of text and its context (e.g., a webpage snippet) to receive a concise explanation in a specified language. It leverages the Groq API for natural language processing, Redis for caching and rate limiting, and includes enterprise-level features like token-based authentication.

**Features**

- Contextual Explanations: Explains selected text based on provided context or generically if no context is available.
- Multi-Language Support: Supports English, Hindi, Telugu, Tamil, Punjabi, and Marathi.
- Caching: Uses Redis to cache explanations for 1 hour to reduce API calls.
- Token Authentication: Requires a valid Bearer token for API access.
- Rate Limiting: Limits requests to 100 per hour per token.
- Gibberish Detection: Filters out meaningless or random text inputs.

**Prerequisites**

Python 3.9+
Redis server
Git (for version control)
