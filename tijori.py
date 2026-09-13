# tijori.py
# मलिकलांग (Maliklang) का हिंग्लिश डेटाबेस सिस्टम जो डेटा सुरक्षित रखता है

# डेटा को सुरक्षित रखने के लिए एक खाली तिजोरी (Dictionary)
MERA_DATA = {}

def tijori_me_daalo(chabhi, value):
    """
    यह फंक्शन तिजोरी में नया डेटा सुरक्षित (Save) करेगा।
    """
    MERA_DATA[chabhi] = value
    print(f"🔒 [TIJORI]: सफलता! आपकी तिजोरी में '{chabhi}' के नाम पर डेटा सुरक्षित कर दिया गया है।")

def tijori_se_nikalo(chabhi):
    """
    यह फंक्शन तिजोरी से पुराना डेटा ढूंढकर बाहर लाएगा।
    """
    if chabhi in MERA_DATA:
        return MERA_DATA[chabhi]
    else:
        return f"❌ [TIJORI ERORR]: अरे भाई! तिजोरी में '{chabhi}' नाम का कोई डेटा नहीं मिला।"

# टेस्ट करने के लिए (जब आप इसे अलग से चलाएंगे)
if __name__ == "__main__":
    print("--- तिजोरी डेटाबेस टेस्ट रन ---")
   
    # डेटा डालना (Save करना)
    tijori_me_daalo("naam", "Shailendra")
    tijori_me_daalo("role", "Python Developer")
   
    print("\n--- डेटा बाहर निकालना ---")
    # डेटा निकालना (Fetch करना)
    print("नाम:", tijori_se_nikalo("naam"))
    print("रोल:", tijori_se_nikalo("role"))
    print("गलत चॉइस:", tijori_se_nikalo("umar"))
 
