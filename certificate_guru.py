import webbrowser
import os

def generate_maliklang_certificate(student_name, course_name="Advanced Hinglish Coding"):
    # 📜 सर्टिफिकेट का सुंदर और साफ HTML डिज़ाइन (बिना किसी ऐप के सीधे ब्राउज़र में खुलेगा)
    HTML_CERTIFICATE = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Maliklang Official Certificate</title>
        <style>
            body {{ font-family: 'Georgia', serif; background: #f5f5f5; padding: 50px; text-align: center; }}
            .certificate-border {{ max-width: 800px; margin: 0 auto; border: 10px solid #2c3e50; padding: 50px; background: white; box-shadow: 0 4px 15px rgba(0,0,0,0.1); position: relative; }}
            .certificate-inner {{ border: 3px double #e67e22; padding: 40px; }}
            h1 {{ color: #2c3e50; font-size: 42px; margin-bottom: 10px; }}
            h2 {{ color: #e67e22; font-size: 24px; font-weight: normal; font-style: italic; margin-top: 0; }}
            .presented {{ font-size: 18px; color: #7f8c8d; margin: 30px 0 10px 0; }}
            .name {{ font-size: 36px; color: #2c3e50; font-weight: bold; border-bottom: 2px solid #ddd; display: inline-block; padding: 0 50px; }}
            .reason {{ font-size: 18px; color: #34495e; line-height: 1.6; margin: 30px 40px; }}
            .footer-area {{ display: flex; justify-content: space-between; margin-top: 50px; padding: 0 40px; }}
            .signature {{ font-size: 16px; color: #2c3e50; border-top: 1px solid #2c3e50; width: 150px; padding-top: 5px; }}
            .security-tag {{ font-size: 12px; color: #27ae60; font-weight: bold; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="certificate-border">
            <div class="certificate-inner">
                <h1>MALIKLANG ECOSYSTEM</h1>
                <h2>Official Certificate of Completion</h2>
               
                <p class="presented">This is proudly presented to</p>
                <p class="name">{student_name}</p>
               
                <p class="reason">
                    For successfully mastering the concepts of <b>{course_name}</b>, compiling local structures,
                    and deploying applications within the native Hinglish programming interpreter setup.
                </p>
               
                <div class="footer-area">
                    <div>
                        <p class="signature"><b>Shailendra Kumar</b><br>Founder, Maliklang</p>
                    </div>
                    <div>
                        <p class="signature"><b>Verified AI Agent</b><br>Security Officer</p>
                    </div>
                </div>
               
                <p class="security-tag">🔒 Secured & Verified under Maliklang Super AI Protection Protocol</p>
            </div>
        </div>
    </body>
    </html>
    """
   
    # 💾 बिना किसी ऐप के सीधे फाइल को कंप्यूटर में सेव करना
    file_name = f"certificate_{student_name.lower().replace(' ', '_')}.html"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(HTML_CERTIFICATE)
       
    print(f"🎉 बधाई हो! {student_name} का सर्टिफिकेट सफलतापूर्वक तैयार हो गया है।")
   
    # 🖥️ सीधे ब्राउज़र में सर्टिफिकेट को ओपन करना (यूजर इसे तुरंत प्रिंट कर सकता है)
    webbrowser.open(os.path.abspath(file_name))

if __name__ == "__main__":
    print("🎓 --- मलिकलैंग सर्टिफिकेट गुरु (Certificate Guru) ---")
    naam = input("कृपया छात्र का पूरा नाम दर्ज करें: ")
    if naam:
        generate_maliklang_certificate(naam)
 
