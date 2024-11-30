# Synology Chat Markdown Editor

The Synology Markdown Editor is a tool designed to simplify creating and editing Markdown content. It features quick formatting options via buttons for bold, italic, lists, and more, along with a Markdown syntax guide for easy reference. Users can input text, apply formatting, copy content, clear the editor, or download the result as a .md file. This tool is ideal for streamlining Markdown usage in platforms like Synology Chat, enhancing message formatting and clarity.

![image](https://github.com/user-attachments/assets/bf867531-5bb7-4b5b-b4db-940edd24a13a)


## Features

- **Visual Markdown Formatting**: Apply Markdown formatting through buttons
- **Real-time Preview**: See your formatted text as you type
- **Auto-save**: Content automatically saved to localStorage
- **Multiple Formatting Options**:
  - Bold text
  - Italic text
  - Strikethrough
  - Bullet lists
  - Block quotes
  - Multi-line quotes
  - Inline code
  - Code blocks
  - Hyperlinks
- **Export Options**: 
  - Copy to clipboard
  - Download as .md file
  - Clear content

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/D-Mad/GUI_Markdown_Synology_Chat.git
cd GUI_Markdown_Synology_Chat
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Packages
```bash
pip install streamlit
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The application will open automatically in your default web browser at `http://localhost:8501`.

## Usage

1. **Start the Editor**: After running the application, the editor interface will appear in your web browser.

2. **Write or Paste Text**: Enter your text in the left panel.

3. **Format Text**:
   - Select the text you want to format
   - Click the appropriate formatting button in the toolbar
   - The Markdown syntax will be automatically applied

4. **Save Your Work**:
   - Content is automatically saved in your browser
   - Use the "Download .md File" button to save your work locally

5. **Reference Guide**:
   - Markdown syntax guide is available in the right panel
   - Shows examples of all supported formatting options

## Deployment Options

### Local Network Deployment
To make the editor available on your local network:

```bash
streamlit run markdown_editor.py --server.address 0.0.0.0
```

### Cloud Deployment
To deploy on cloud platforms:

1. **Streamlit Cloud**:
   - Push your code to GitHub
   - Connect your repository to Streamlit Cloud
   - Deploy with one click

2. **Custom Server**:
   - Install required packages
   - Set up a reverse proxy (nginx/apache)
   - Run with systemd or similar service manager

## Configuration

You can customize the editor by modifying the following:

- `markdown_editor.py`: Main application logic
- Styling: Modify the CSS in the HTML component
- Port: Use `--server.port` flag when running

## Browser Compatibility

Tested and working on:
- Google Chrome (recommended)
- Mozilla Firefox
- Microsoft Edge
- Safari

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Support

For support, please create an issue in the GitHub repository or contact your IT department.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Inspired by classic Markdown editors
- Designed for internal company use
