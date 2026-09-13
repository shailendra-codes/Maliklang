# offline_ai.py
# मलिकलांग (Maliklang) का ऑफलाइन AI सिस्टम जो बिना इंटरनेट के काम करता है

# ऑफलाइन ज्ञान का भंडार (Offline Knowledge Base)
AI_GNYAN = {
    "loop kya hai": "🤖 [OFFLINE AI]: लूप का मतलब है किसी काम को बार-बार करना। मलिकलांग में इसके लिए 'jab_tak' का इस्तेमाल करें।",
    "variable kya hai": "🤖 [OFFLINE AI]: वेरिएबल एक डिब्बे की तरह है जिसमें डेटा रखते हैं। मलिकलांग में इसके लिए 'banao' लिखें।",
    "print kaise kare": "🤖 [OFFLINE AI]: स्क्रीन पर कुछ भी दिखाने के लिए 'bolo' कीवर्ड का इस्तेमाल करें।"
}

def offline_pucho_ai(sawaal):
    """
    यह फंक्शन बिना इंटरनेट के छात्र के सवाल का जवाब देगा।
    """
    sawaal_clean = sawaal.lower().strip()
   
    # सवाल को ज्ञान के भंडार में ढूंढना
    if sawaal_clean in AI_GNYAN:
        return AI_GNYAN[sawaal_clean]
    else:
        return "🤖 [OFFLINE AI]: माफ़ करना भाई, यह सवाल मेरी ऑफलाइन मेमोरी में नहीं है। मैं इसे जल्द ही सीख लूँगा!"

# टेस्ट करने के लिए (जब आप इसे अलग से चलाएंगे)
if __name__ == "__main__":
    print("--- ऑफलाइन AI टेस्ट रन (बिना इंटरनेट) ---")
   
    # छात्र का सवाल
    sawaal_1 = "loop kya hai"
    print(f"छात्र का सवाल: {sawaal_1}")
    print(offline_pucho_ai(sawaal_1))
 
