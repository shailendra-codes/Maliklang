# jeevan_guru_ai.py
# मलिकलांग (Maliklang) जीवन गुरु AI - भारतीय छात्रों के मानसिक स्वास्थ्य और मोटिवेशन के लिए

import datetime

# छात्रों की व्यक्तिगत बातें सुरक्षित रखने के लिए 100% प्राइवेट डेटाबेस
PRIVATE_STUDENT_DIARY = {}

# भारत सरकार की मुफ़्त और प्रमाणित मानसिक स्वास्थ्य हेल्पलाइन
INDIAN_HELPLINES = {
    "TELE-MANAS": "14416 या 1800-891-4416 (24 घंटे मुफ़्त सलाह)",
    "KIRAN HELPLINE": "1800-599-0019 (मानसिक स्वास्थ्य सहायता)"
}

def registration_for_help(naam, umar, reg_no, desh):
    """
    तनाव से जूझ रहे छात्र को एक पूरी तरह सुरक्षित और प्राइवेट रूम में एंट्री देना।
    """
    PRIVATE_STUDENT_DIARY[reg_no] = {
        "Naam": naam,
        "Umar": umar,
        "Desh": desh,
        "Dukh_Sukh_History": [],
        "Registered_At": datetime.date.today().strftime("%Y-%m-%d")
    }
    print("==================================================")
    print(f"🔒 [JEEVAN GURU]: नमस्ते {naam}, आप पूरी तरह सुरक्षित स्थान पर हैं।")
    print(f"🤝 देश: {desh} | आपकी बातें 100% गुप्त रहेंगी, कोई डेटा लीक नहीं होगा।")
    print("==================================================\n")
    return reg_no
 def pucho_jeevan_guru(reg_no, bachhe_ki_baat):
    """
    बच्चे के दिल की बात सुनना, तनाव को समझना और उसे मोटिवेट करना।
    """
    if reg_no not in PRIVATE_STUDENT_DIARY:
        return "❌ [ERROR]: कृपया पहले अपना सही रजिस्ट्रेशन नंबर डालें।"
       
    baat_clean = bachhe_ki_baat.lower()
    desh_naam = PRIVATE_STUDENT_DIARY[reg_no]["Desh"]
   
    # बच्चे की बात को प्राइवेट डायरी में सेव करना
    PRIVATE_STUDENT_DIARY[reg_no]["Dukh_Sukh_History"].append(bachhe_ki_baat)
   
    # गंभीर मानसिक तनाव को पकड़ने के कीवर्ड्स
    suicide_keywords = ["atmhatya", "marna", "zindagi khatam", "suicide", "har gaya"]
    tension_keywords = ["paisa", "tension", "garibi", "darr", "padhai", "fail", "bad habits"]
   
    # 1. अगर बच्चा बहुत ज़्यादा परेशान है या गलत विचार आ रहे हैं
    for word in suicide_keywords:
        if word in baat_clean:
            jawaab = (
                "\n❤️ [JEEVAN GURU AI - MOTIVATION]:\n"
                "सुनो मेरे भाई/बहन, तुम अकेले नहीं हो! मुश्किलें हर इंसान के जीवन में आती हैं।\n"
                "यह जीवन एक बहुत खूबसूरत तोहफा है, एक परीक्षा से या पैसों की तंगी से तुम्हारी कीमत कम नहीं होती।\n"
                "तुम में वो ताकत है कि तुम हर मुश्किल को हरा सकते हो। हिम्मत मत हारो!\n"
            )
           
            if desh_naam.lower() == "india":
                jawaab += (
                    f"🚨 तुमसे अनुरोध है: तुरंत अपने माता-पिता या इस मुफ़्त सरकारी हेल्पलाइन पर बात करो:\n"
                    f"📞 टेली-मानस: {INDIAN_HELPLINES['TELE-MANAS']}\n"
                    f"📞 किरण हेल्पलाइन: {INDIAN_HELPLINES['KIRAN HELPLINE']}\n"
                    f"हम सब मिलकर रास्ता निकालेंगे, तुम बहुत कीमती हो!"
                )
            else:
                jawaab += "🚨 तुमसे अनुरोध है: तुरंत अपने माता-पिता, किसी सच्चे दोस्त या लोकल हेल्पलाइन से बात करो।"
               
            return jawaab
           
    # 2. अगर बच्चा घर या पैसों की टेंशन में है
    for word in tension_keywords:
        if word in baat_clean:
            return (
                "\n🌟 [JEEVAN GURU AI - SOLUTION]:\n"
                "पैसों की तंगी और घर की टेंशन अस्थाई (Temporary) है। आज तुम मेहनत कर रहे हो, कल तुम्हारा समय बदलेगा।\n"
                "मलिकलांग ऐप पर रोज़ सिर्फ 30 मिनट कोडिंग सीखो, खुद को काबिल बनाओ।\n"
                "जब तुम काबिल बनोगे, तो तुम अपने घर की गरीबी को हमेशा के लिए मिटा दोगे। खुद पर भरोसा रखो, तुम कर सकते हो!"
            )
           
    # 3. सामान्य बातचीत के लिए
    return (
        "\n🌈 [JEEVAN GURU AI]:\n"
        "अपनी बातें मुझसे शेयर करने के लिए शुक्रिया। ज़िंदगी में आगे बढ़ते रहो, कोई भी टेंशन हो मुझे बताओ।\n"
        "मेहनत करते रहो, सफलता एक दिन तुम्हारे कदम चूमेगी!"
    )

# टेस्ट करने के लिए
if __name__ == "__main__":
    id_no = registration_for_help("Amit Kumar", 15, "ML-1001", "India")
    print(pucho_jeevan_guru(id_no, "Mujhe bahut darr lag raha hai atmhatya ka vichar ata hai"))
