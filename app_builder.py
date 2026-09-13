# app_builder.py
# मलिकलांग (Maliklang) का आसान ऐप मेकर मॉड्यूल

def banao_app_screen(title_naam):
    """
    यह फंक्शन सिर्फ एक नाम लेकर कंप्यूटर स्क्रीन का ढांचा (HTML/Layout) तैयार करेगा।
    """
    print(f"📱 [APP BUILDER]: आपके नए ऐप के लिए स्क्रीन बनाई जा रही है...")
   
    # एक साधारण स्क्रीन का लेआउट
    html_layout = f"""
    ============ {title_naam} ============
    [ Home ]  [ About ]  [ Contact ]
    --------------------------------------
    मलिकलांग ऐप मेकर में आपका स्वागत है!
    ======================================
    """
    return html_layout

# टेस्ट करने के लिए (जब आप इसे अलग से चलाएंगे)
if __name__ == "__main__":
    print("--- ऐप बिल्डर टेस्ट रन ---")
   
    # यूज़र ने ऐप का नाम दिया
    mera_app = banao_app_screen("Mera Pehla Hinglish App")
    print(mera_app)
