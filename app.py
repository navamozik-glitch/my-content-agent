import os
from openai import OpenAI

# خواندن کلید از تنظیمات گیت‌هاب
API_KEY = os.environ.get("LLM7_API_KEY")

client = OpenAI(
    base_url="https://api.llm7.io/v1",
    api_key=API_KEY,
)

def generate_content(topic):
    prompt = f"""
    You are a professional social media content creator.
    Create a highly engaging Instagram caption about: "{topic}"
    
    The caption must:
    - Start with a strong hook that stops scrolling.
    - Be written in a conversational, relatable tone.
    - Use short paragraphs and line breaks.
    - End with a clear call-to-action (CTA).
    - Include 10-15 relevant hashtags.
    
    Output ONLY the final caption in English.
    """
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="default",
        temperature=0.7,
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    # موضوع را اینجا به صورت پیش‌فرض تنظیم می‌کنیم
    topic = "Artificial Intelligence in 2026"
    print(f"در حال تولید محتوا برای موضوع: {topic}")
    
    try:
        result = generate_content(topic)
        print("--- خروجی ---")
        print(result)
        print("------------")
    except Exception as e:
        print(f"خطا رخ داد: {e}")