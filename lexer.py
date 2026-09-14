# Maliklang Advanced Lexer Engine
# इसका काम हिंग्लिश कोड को कंप्यूटर टोकन्स में बदलना है

import re

# 1. सभी टोकन्स के प्रकार तय करना (Token Types)
TOKEN_TYPES = [
    ('KEYWORD',    r'\b(banao|bolo|pucho|agar|magar|jab_tak|loop_end)\b'),
    ('INT_NUMBER', r'\d+'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('OPERATOR',   r'[=\+\-\*/><=]+'),
    ('STRING',     r'"[^"]*"'),
    ('SKIP',       r'[ \t]+'),          # खाली जगह (Spaces) को छोड़ने के लिए
    ('NEWLINE',    r'\n'),              # नई लाइन के लिए
    ('MISMATCH',   r'.'),               # अगर कोई गलत शब्द लिखे तो पकड़ने के लिए
]

def maliklang_lexer(code_text):
    # सभी नियमों को एक साथ जोड़ना
    master_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)
    tokens_list = []
    line_number = 1

    # कोड की एक-एक लाइन को स्कैन करना
    for match in re.finditer(master_regex, code_text):
        kind = match.lastgroup
        value = match.group(kind)
       
        if kind == 'SKIP':
            continue
        elif kind == 'NEWLINE':
            line_number += 1
        elif kind == 'MISMATCH':
            print(f"❌ [मलिकलैंग लेक्सर एरर]: लाइन {line_number} पर गलत शब्द मिला: '{value}'")
            return None
        else:
            # कंप्यूटर के लिए टोकन तैयार करना
            tokens_list.append({'type': kind, 'value': value, 'line': line_number})
           
    return tokens_list

# 🚀 लाइव टेस्ट (यह देखने के लिए कि यह कैसे काम करता है)
if __name__ == "__main__":
    test_code = 'banao marks = 85'
    print("📝 इनपुट कोड:", test_code)
   
    result_tokens = maliklang_lexer(test_code)
    print("\n🤖 कंप्यूटर के लिए जनरेट हुए एडवांस्ड टोकन्स:")
    for token in result_tokens:
        print(token)
 
