import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Markdown Editor ", layout="wide")

# Custom HTML/JavaScript component with original styling
markdown_editor_html = """
<div style="font-family: Arial, sans-serif;">
    <h1 style="text-align: center; color: #FFF; margin-bottom: 20px;">Markdown Editor </h1>
    
    <div style="display: flex; margin-bottom: 20px;">
        <div style="flex: 1; margin-right: 20px;">
            <div class="toolbar" style="background-color: #f8f9fa; padding: 10px; border-radius: 4px; margin-bottom: 15px;">
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('*', '*')">In đậm</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('_', '_')">In nghiêng</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('~', '~')">Gạch ngang</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('* ', '')">Danh sách</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('> ', '')">Trích dẫn</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('>>>', '')">Nhiều dòng trích dẫn</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('`', '`')">Mã inline</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('```\\n', '\\n```')">Khối mã</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="insertLink()">Liên kết</button>
            </div>
            
            <div style="display: flex;">
                <textarea id="editor" style="flex: 1; height: 400px; padding: 15px; border: 1px solid #ddd; border-radius: 4px; font-family: monospace; font-size: 14px; line-height: 1.5;"
                          placeholder="Nhập Markdown của bạn tại đây..."></textarea>
                          
                <div style="flex: 1; margin-left: 20px; padding: 15px; background-color: #f8f9fa; border: 1px solid #ddd; border-radius: 4px;">
                    <h2 style="margin-top: 0; color: #333;">Hướng dẫn Markdown</h2>
                    <ul style="padding-left: 20px; margin: 0;">
                        <li style="margin-bottom: 10px;"><strong>In đậm:</strong> Dùng <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">*văn bản*</code></li>
                        <li style="margin-bottom: 10px;"><strong>In nghiêng:</strong> Dùng <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">_văn bản_</code></li>
                        <li style="margin-bottom: 10px;"><strong>Gạch ngang:</strong> Dùng <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">~văn bản~</code></li>
                        <li style="margin-bottom: 10px;"><strong>Danh sách:</strong> Dùng <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">* Mục 1</code></li>
                        <li style="margin-bottom: 10px;"><strong>Trích dẫn:</strong> Dùng <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">&gt; văn bản</code></li>
                        <li style="margin-bottom: 10px;"><strong>Nhiều dòng trích dẫn:</strong> Dùng <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">&gt;&gt;&gt;</code></li>
                        <li style="margin-bottom: 10px;"><strong>Mã inline:</strong> Dùng <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">`mã`</code></li>
                        <li style="margin-bottom: 10px;"><strong>Khối mã:</strong> Dùng <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">```</code></li>
                        <li style="margin-bottom: 10px;"><strong>Liên kết:</strong> Dùng <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">&lt;URL&gt;văn bản</code></li>
                    </ul>
                </div>
            </div>
            
            <div style="margin-top: 20px; display: flex; gap: 10px; justify-content: center;">
                <button style="background-color: #28a745; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;" onclick="copyContent()">Sao chép nội dung</button>
                <button style="background-color: #dc3545; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;" onclick="clearContent()">Xóa nội dung</button>
                <button style="background-color: #17a2b8; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;" onclick="downloadMarkdown()">Tải về file .md</button>
            </div>
        </div>
    </div>

    <script>
        const editor = document.getElementById('editor');
        
        function applyMarkdown(startTag, endTag) {
            const start = editor.selectionStart;
            const end = editor.selectionEnd;
            const selection = editor.value.substring(start, end);
            const before = editor.value.substring(0, start);
            const after = editor.value.substring(end);
            editor.value = before + startTag + selection + endTag + after;
            editor.focus();
            saveToLocalStorage();
        }
        
        function insertLink() {
            const url = prompt('Nhập URL:');
            const text = prompt('Nhập văn bản hiển thị:');
            if (url && text) {
                applyMarkdown('<', `>${text}(${url})`);
            }
        }
        
        function copyContent() {
            editor.select();
            document.execCommand('copy');
            alert('Đã sao chép nội dung vào clipboard!');
        }
        
        function clearContent() {
            if (confirm('Bạn có chắc muốn xóa toàn bộ nội dung?')) {
                editor.value = '';
                editor.focus();
                saveToLocalStorage();
            }
        }
        
        function downloadMarkdown() {
            const content = editor.value;
            const blob = new Blob([content], { type: 'text/markdown' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'markdown-content.md';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        }
        
        function saveToLocalStorage() {
            localStorage.setItem('markdownContent', editor.value);
        }
        
        // Load saved content
        const savedContent = localStorage.getItem('markdownContent');
        if (savedContent) {
            editor.value = savedContent;
        }
        
        // Save content when changed
        editor.addEventListener('input', saveToLocalStorage);
    </script>
</div>
"""

# Hide Streamlit default elements
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Display the custom editor
components.html(markdown_editor_html, height=800, scrolling=True)