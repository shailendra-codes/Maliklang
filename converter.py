# converter.py
# मलिकलांग (Maliklang) कोड को सीधे असली Python कोड में बदलने वाला ट्रांसलेटर

def badlo_maliklang_se_python(maliklang_code):
    """
    यह फंक्शन मलिकलांग के कीवर्ड्स को पायथन के असली कोड में बदलेगा।
    """
    python_code = maliklang_code
   
    # 1. 'banao ' को हटाकर नॉर्मल पायथन वेरिएबल बनाना
    # मलिकलांग: banao x = 10 -> पायथन: x = 10
    python_code = python_code.replace("banao ", "")
   
    # 2. 'bolo ' को पायथन के print() में बदलना
    # मलिकलांग: bolo x -> पायथन: print(x)
    if "bolo " in python_code:
        content = python_code.replace("bolo ", "").strip()
        python_code = f"print({content})"
       
    return python_code

# टेस्ट करने के लिए (जब आप इसे अलग से चलाएंगे)
if __name__ == "__main__":
    print("--- मलिकलांग से पायथन कनवर्टर टेस्ट रन ---")
   
    # मलिकलांग का कोड टेस्ट करना
    sample_1 = "banao x = 10"
    sample_2 = "bolo x"
   
    print(f"मलिकलांग कोड 1: {sample_1} ➡️ पायथन कोड: {badlo_maliklang_se_python(sample_1)}")
    print(f"मलिकलांग कोड 2: {sample_2} ➡️ पायथन कोड: {badlo_maliklang_se_python(sample_2)}")
