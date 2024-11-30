import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Synology Markdown Editor", layout="wide")

# Custom HTML/JavaScript component with original styling
markdown_editor_html = """
<div style="font-family: Arial, sans-serif;">
    <h1 style="text-align: center; color: #FFF; margin-bottom: 20px;">Synology Markdown Editor</h1>
    
    <div style="display: flex; margin-bottom: 20px;">
        <div style="flex: 1; margin-right: 20px;">
            <div class="toolbar" style="background-color: #f8f9fa; padding: 10px; border-radius: 4px; margin-bottom: 15px;">
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('*', '*')">Bold</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('_', '_')">Italic</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('~', '~')">Strikethrough</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('* ', '')">List</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('> ', '')">Quote</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('>>>', '')">Multi-line Quote</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('`', '`')">Inline Code</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="applyMarkdown('```\\n', '\\n```')">Code Block</button>
                <button style="background-color: #007bff; color: white; border: none; padding: 8px 12px; margin-right: 5px; border-radius: 4px; cursor: pointer;" onclick="insertLink()">Link</button>
            </div>
            
            <div style="display: flex;">
                <textarea id="editor" style="flex: 1; height: 400px; padding: 15px; border: 1px solid #ddd; border-radius: 4px; font-family: monospace; font-size: 14px; line-height: 1.5;"
                          placeholder="Enter your Markdown text here..."></textarea>
                          
                <div style="flex: 1; margin-left: 20px; padding: 15px; background-color: #f8f9fa; border: 1px solid #ddd; border-radius: 4px;">
                    <h2 style="margin-top: 0; color: #333;">Markdown Guide</h2>
                    <ul style="padding-left: 20px; margin: 0;">
                        <li style="margin-bottom: 10px;"><strong>Bold:</strong> Use <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">*text*</code></li>
                        <li style="margin-bottom: 10px;"><strong>Italic:</strong> Use <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">_text_</code></li>
                        <li style="margin-bottom: 10px;"><strong>Strikethrough:</strong> Use <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">~text~</code></li>
                        <li style="margin-bottom: 10px;"><strong>List:</strong> Use <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">* Item 1</code></li>
                        <li style="margin-bottom: 10px;"><strong>Quote:</strong> Use <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">&gt; text</code></li>
                        <li style="margin-bottom: 10px;"><strong>Multi-line Quote:</strong> Use <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">&gt;&gt;&gt;</code></li>
                        <li style="margin-bottom: 10px;"><strong>Inline Code:</strong> Use <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">`code`</code></li>
                        <li style="margin-bottom: 10px;"><strong>Code Block:</strong> Use <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">```</code></li>
                        <li style="margin-bottom: 10px;"><strong>Link:</strong> Use <code style="background-color: #eee; padding: 2px 4px; border-radius: 3px;">&lt;URL&gt;text</code></li>
                    </ul>
                </div>
            </div>
            
            <div style="margin-top: 20px; display: flex; gap: 10px; justify-content: center;">
                <button style="background-color: #28a745; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;" onclick="copyContent()">Copy Content</button>
                <button style="background-color: #dc3545; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;" onclick="clearContent()">Clear Content</button>
                <button style="background-color: #17a2b8; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;" onclick="downloadMarkdown()">Download .md File</button>
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
            const url = prompt('Enter URL:');
            const text = prompt('Enter display text:');
            if (url && text) {
                applyMarkdown('<', `>${text}(${url})`);
            }
        }
        
        function copyContent() {
            editor.select();
            document.execCommand('copy');
            alert('Content copied to clipboard!');
        }
        
        function clearContent() {
            if (confirm('Are you sure you want to clear all content?')) {
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
