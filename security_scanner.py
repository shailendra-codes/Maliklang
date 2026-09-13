import os

# 🚨 खतरनाक शब्द और कमांड्स की लिस्ट जो सिस्टम को नुकसान पहुंचा सकते हैं
DANGEROUS_WORDS = ["os.system", "subprocess", "rmdir", "delete", "hack", "eval("]

def scan_my_project():
    print("🔍 [INFO] मलिकलांग (Maliklang) प्रोजेक्ट की सुरक्षा जांच शुरू हो रही है...\n")
    danger_found = False

    # प्रोजेक्ट के सारे फोल्डर और फाइलों को चेक करना
    for root, dirs, files in os.walk("."):
        for file in files:
            # खुद इस सिक्योरिटी फ़ाइल को और .git को छोड़कर बाकी सब चेक करें
            if file == "security_scanner.py" or file.endswith(".txt") or file.startswith("."):
                continue
               
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
               
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                       
                    for line_no, line in enumerate(lines, 1):
                        for word in DANGEROUS_WORDS:
                            if word in line:
                                print(f"⚠️ [WARNING] खतरा! फ़ाइल '{file}' की लाइन {line_no} में संदिग्ध शब्द '{word}' मिला।")
                                danger_found = True
                except Exception as e:
                    print(f"❌ फ़ाइल {file} को पढ़ने में दिक्कत आई: {e}")

    if not danger_found:
        print("\n✅ [SUCCESS] बधाई हो! आपका पूरा प्रोजेक्ट सुरक्षित है। कोई खतरा नहीं मिला।")
    else:
        print("\n❌ [ALERT] सुरक्षा जांच पूरी हुई। कृपया ऊपर दी गई चेतावनियों को देखें।")

if __name__ == "__main__":
    scan_my_project()
