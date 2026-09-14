# Maliklang Advanced Parser Engine
# इसका काम टोकन्स को जोड़कर सही व्याकरण (Syntax Tree) जांचना है

class MaliklangParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_pos = 0

    # वर्तमान टोकन को देखने के लिए
    def current_token(self):
        if self.current_pos < len(self.tokens):
            return self.tokens[self.current_pos]
        return None

    # अगले टोकन पर जाने के लिए
    def consume(self, expected_type=None):
        token = self.current_token()
        if token is None:
            print("❌ [मलिकलैंग पार्सर एरर]: कोड अचानक खत्म हो गया!")
            return None
        
        if expected_type and token['type'] != expected_type:
            print(f"❌ [मलिकलैंग सिंटैक्स एरर]: लाइन {token['line']} पर गड़बड़ी। हमें '{expected_type}' चाहिए था, लेकिन '{token['type']}' मिला।")
            return None
            
        self.current_pos += 1
        return token

    # 'banao marks = 85' जैसी लाइनों को पार्स (चेक) करने का नियम
    def parse_assignment(self):
        # 1. पहले 'banao' कीवर्ड होना चाहिए
        keyword = self.consume('KEYWORD')
        if not keyword: return None
        
        # 2. फिर वेरिएबल का नाम (Identifier) होना चाहिए
        identifier = self.consume('IDENTIFIER')
        if not identifier: return None
        
        # 3. फिर बराबर का निशान (=) होना चाहिए
        operator = self.consume('OPERATOR')
        if not operator or operator['value'] != '=':
            print(f"❌ [मलिकलैंग सिंटैक्स एरर]: वेरिएबल नाम के बाद '=' होना ज़रूरी है।")
            return None
            
        # 4. अंत में कोई संख्या या वैल्यू होनी चाहिए
        value = self.consume('INT_NUMBER') or self.consume('STRING')
        if not value: return None
        
        # अगर सब सही है, तो एक सुंदर सिंटैक्स ट्री का ढांचा वापस करना
        return {
            'node_type': 'ASSIGNMENT',
            'variable_name': identifier['value'],
            'assigned_value': value['value']
        }

# 🚀 लाइव टेस्ट (यह देखने के लिए कि पार्सर व्याकरण कैसे चेक करता है)
if __name__ == "__main__":
    # मान लेते हैं कि लेक्सर ने हमें ये टोकन्स दिए हैं
    mock_tokens = [
        {'type': 'KEYWORD', 'value': 'banao', 'line': 1},
        {'type': 'IDENTIFIER', 'value': 'marks', 'line': 1},
        {'type': 'OPERATOR', 'value': '=', 'line': 1},
        {'type': 'INT_NUMBER', 'value': '85', 'line': 1}
    ]
    
    print("🤖 पार्सर इंजन को दिए गए टोकन्स की जांच हो रही है...")
    parser = MaliklangParser(mock_tokens)
    ast = parser.parse_assignment()
    
    if ast:
        print("\n✅ [व्याकरण शुद्ध है!] जनरेट हुआ Abstract Syntax Tree (AST):")
        print(ast)

