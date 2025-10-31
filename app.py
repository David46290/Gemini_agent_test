# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates') # name of the .py

# A humble variable to be put in the web.
# It can be a hole folder or database in the future
current_text = "Web Test"

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_text
    
    # 處理表單提交 (POST 請求)
    # submit processing list (POST request)
    if request.method == 'POST':
        # 從表單中獲取名為 'new_content' 的欄位值
        # Get a column call 'new_content' from the processing list.
        new_content = request.form.get('new_content')
        
        if new_content:
            # 更新全域變數中的字串內容
            # update the content of the global variable (the editable string)
            current_text = new_content
            # 重導向回 GET 請求，以避免使用者重新整理時重複提交
            # redirect GET request to avoid user submit multiple times after refreshing the page
            return redirect(url_for('index'))
    
    # 處理網頁顯示 (GET 請求)
    # process display of the web (GET request)
    # 將 current_text 傳遞給 HTML 模板
    # send editable variable to HTML module
    return render_template('index.html', content=current_text)

if __name__ == '__main__':
    # 啟動 Flask 應用程式
    # activate Flask app.
    app.run(debug=True) 
    # 'debug=True' 可以在程式碼變動時自動重載伺服器，方便開發
    # Setting debug to be Ture so that server is auto-reload once code is changed, just for convenience