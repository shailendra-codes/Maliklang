# student_tracker.py
# मलिकलांग (Maliklang) छात्र ट्रैकिंग, रजिस्ट्रेशन और प्रोफाइल सिस्टम

import datetime

# सभी छात्रों का पूरा रिकॉर्ड सुरक्षित रखने के लिए डिजिटल डेटाबेस
STUDENT_DATABASE = {}

def naya_registration(naam, umar, email, desh):
    """
    यह फंक्शन छात्र का नाम, उम्र, ईमेल और देश लेकर एक नया प्रोफाइल और रजिस्ट्रेशन नंबर बनाएगा।
    """
    # 14 साल की उम्र का चेक लगाना
    if umar < 14:
        print(f"⚠️ [REGISTRATION ALERT]: माफ़ करना {naam}, यह स्पेशल रोज़गार मिशन 14 साल या उससे बड़े बच्चों के लिए है। आपकी उम्र अभी {umar} साल है।")
        return None

    # रजिस्ट्रेशन नंबर बनाने का सरल लॉजिक (जैसे: ML-1001)
    kul_students = len(STUDENT_DATABASE)
    reg_no = f"ML-{1001 + kul_students}"
   
    # छात्र का पूरा नया प्रोफाइल डेटाबेस में सेव करना
    STUDENT_DATABASE[reg_no] = {
        "Naam": naam,
        "Umar": umar,
        "Email": email,
        "Desh": desh,
        "Daily_Time_Minutes": 0,
        "Last_Login": datetime.date.today().strftime("%Y-%m-%d")
    }
   
    print(f"🎉 [REGISTRATION]: बधाई हो {naam}! आपका रजिस्ट्रेशन सफल रहा।")
    print(f"🆔 रजिस्ट्रेशन नंबर: {reg_no} | उम्र: {umar} साल | ईमेल: {email} | देश: {desh}\n")
    return reg_no

def time_track_karo(reg_no, kitni_der_padha):
    """
    यह फंक्शन रिकॉर्ड रखेगा कि छात्र ने आज कितनी देर (Minutes) पढ़ाई की।
    """
    if reg_no in STUDENT_DATABASE:
        # पुराने समय में नया समय जोड़ना
        STUDENT_DATABASE[reg_no]["Daily_Time_Minutes"] += kitni_der_padha
        kul_time = STUDENT_DATABASE[reg_no]["Daily_Time_Minutes"]
        छात्र_का_नाम = STUDENT_DATABASE[reg_no]["Naam"]
       
        print(f"⏱️ [TIME TRACKER]: छात्र {छात्र_का_नाम} (ID: {reg_no}) ने आज {kitni_der_padha} मिनट पढ़ाई की।")
        print(f"📊 कुल पढ़ाई का समय: {kul_time} मिनट।")
       
        # 30 मिनट का डेली लक्ष्य चेक करना
        if kul_time >= 30:
            print(f"🌟 बहुत बढ़िया {छात्र_का_नाम}! आपने आज का 30 मिनट का लक्ष्य पूरा कर लिया है। आप जॉब पाने के और करीब बढ़ रहे हैं! 🚀\n")
    else:
        print(f"❌ [ERROR]: रजिस्ट्रेशन नंबर {reg_no} का कोई रिकॉर्ड नहीं मिला।\n")

# टेस्ट करने के लिए (जब आप इसे अलग से चलाएंगे)
if __name__ == "__main__":
    print("--- मलिकलांग छात्र एडवांस ट्रैकिंग सिस्टम टेस्ट रन ---\n")
   
    # 1. छात्रों का रजिस्ट्रेशन टेस्ट करना (उम्र और ईमेल के साथ)
    student1 = naya_registration("Ramesh Kumar", 15, "ramesh@email.com", "India")
    student2 = naya_registration("Aman Singh", 12, "aman@email.com", "India") # यह 14 से छोटा है
    student3 = naya_registration("Sita Thapa", 16, "sita@email.com", "Nepal")
   
    print("--- टाइम ट्रैकिंग टेस्ट रन ---")
    # 2. पढ़ाई का समय ट्रैक करना
    if student1:
        time_track_karo(student1, 20)
        time_track_karo(student1, 10) # 20 + 10 = 30 मिनट पूरे हुए
