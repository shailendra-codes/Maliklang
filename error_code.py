# error_guru.py
# मलिकलांग (Maliklang) का स्मार्ट एरर गुरु जो गलतियों को सरल भाषा में समझाता है

def samjhao_error(user_code):
    """
    यह फंक्शन कोड को चेक करेगा और अगर कोई आम गलती है,
    तो उसे आसान हिंग्लिश में समझाएगा।
    """
    words = user_code.split()
   
    # 1. 'banao' की स्पेलिंग मिस्टेक चेक करना
    wrong_banao = ["bnao", "banau", "bnaou", "banmo"]
    for wrong in wrong_banao:
        if wrong in words:
            return f"💡 [ERROR GURU]: अरे भाई! आपने डेटा सुरक्षित करने के लिए '{wrong}' लिखा है। इसे सही करके 'banao' लिखो, फिर कोड दौड़ेगा! 👍"

    # 2. 'bolo' की स्पेलिंग मिस्टेक चेक करना
    wrong_bolo = ["blo", "bolou", "boolo", "bol"]
    for wrong in wrong_bolo:
        if wrong in words:
            return f"💡 [ERROR GURU]: थोड़ा ध्यान दें! स्क्रीन पर दिखाने वाले कमांड '{wrong}' की स्पेलिंग गलत है। इसे सही करके 'bolo' लिखिए। 😊"

    # 3. 'pucho' की स्पेलिंग मिस्टेक चेक करना
    wrong_pucho = ["pcho", "puchu", "puch", "push"]
    for wrong in wrong_pucho:
        if wrong in words:
            return f"💡 [ERROR GURU]: यूज़र से इनपुट मांगने के लिए '{wrong}' नहीं, बल्कि सही स्पेलिंग 'pucho' का इस्तेमाल करें। 🎯"

    # 4. अगर कोई आम गलती नहीं मिली
    return "✅ [ERROR GURU]: कोड का यह हिस्सा देखने में ठीक लग रहा है!"

# टेस्ट करने के लिए (जब आप इसे अलग से चलाएंगे)
if __name__ == "__main__":
    print("--- एरर गुरु टेस्ट रन ---")
    गलत_कोड = "bnao x = 5"
    print(f"यूज़र का कोड: {गलत_कोड}")
    print(samjhao_error(गलत_कोड))
 
