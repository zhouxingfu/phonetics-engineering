import pdfplumber
import pyttsx3
import sys
import os
import weakref

# 
def pdf2audio(filename):
    pdf = pdfplumber.open(filename)

    # 读取每一页
    page_index = 0
    for page in pdf.pages:
        cur_page_text = page.extract_text()
        print(cur_page_text)
        if cur_page_text is not None and page_index > 9:
            cur_page = cur_page_text.replace('.', '')
            print(cur_page)
            engine = pyttsx3.init()
            engine.save_to_file(cur_page_text, str(page_index) + ".wav")
            engine.runAndWait()
        else:
            print("---------------- current page is blank")
            
        page_index += 1
    
    





if __name__ == '__main__':
    filename = sys.argv[1]
    print(filename)
    if os.path.exists(filename):
        pdf2audio(filename)


