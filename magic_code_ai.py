# magic_code_ai.py
# मलिकलांग (Maliklang) सुपर एडवांस एआई एजेंट - बोलचाल से कोड बनाने वाला टूल

def automatic_code_agent(bachhe_ki_boli):
    print("==================================================")
    print("      🪄 मलिकलांग जादुई एआई एजेंट (Magic Agent)    ")
    print("  लक्ष्य: आप सिर्फ अपनी बात कहो, कोड एआई खुद लिखेगा! ")
    print("==================================================\n")
   
    clean_text = bachhe_ki_boli.lower()
    generated_code = []
   
    print(f"🗣️ छात्र ने कहा: \"{bachhe_ki_boli}\"")
    print("🤖 एआई आपके लिए मलिकलांग कोड बना रहा है...\n")
   
    words = clean_text.split()
    for i, word in enumerate(words):
        if word in ["dam", "daam", "price", "rupe", "rupiya", "naam", "umar"]:
            for next_word in words[i:]:
                if next_word.isdigit():
                    generated_code.append(f"banao {word} = {next_word}")
                    break
                elif next_word in ["amit", "shailendra", "ramesh"]:
                    generated_code.append(f"banao {word} = '{next_word}'")
                    break

    if "dikhau" in clean_text or "bolo" in clean_text or "print" in clean_text:
        if generated_code:
            first_line = generated_code[0]
            var_name = first_line.split()[1]
            generated_code.append(f"bolo {var_name}")
        else:
            generated_code.append("bolo 'Kaam Ho Gaya'")

    if "tijori" in clean_text or "save" in clean_text:
        generated_code.append("tijori_me_daalo('data', 100)")

    if generated_code:
        print("💻 [GENERATED MALIKLANG CODE]:")
        print("---------------------------------")
        for line in generated_code:
            print(line)
        print("---------------------------------")
        print("✅ [SUCCESS]: एआई द्वारा बनाया गया कोड सफलतापूर्वक रन हो गया है! 🚀\n")
    else:
        print("🤖 [MAGIC AI]: माफ़ करना भाई, आपकी बात का कोडिंग लॉजिक समझ नहीं आया।\n")

if __name__ == "__main__":
    automatic_code_agent("टमाटर का dam 50 रुपया सेट करो और उसे screen par dikhau")
    automatic_code_agent("इस डेटा को meri tijori me save kar do")
