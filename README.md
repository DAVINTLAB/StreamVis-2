# StreamVis 2.0

## ⚙️ Installation
##### Clone the repository
```bash
git clone https://github.com/DAVINTLAB/StreamVis-2.git
cd StreamVis-2
```

##### Setup venv (recommended):
```bash
python3 -m venv ambiente_youtube
```
If using windows:
```bash
.\ambiente_youtube\Scripts\activate
```

If using linux:
```bash
source ambiente_youtube/bin/activate
```

##### Install dependencies
```bash
pip install -r requirements.txt
```

##### Create a .env file and insert your GOOGLE API key and Youtube Video ID
```bash
7 - GOOGLE_API_KEY = ''
8 - VIDEO_ID = ''
```

## 🔎 Gathering Data
Before running StreamVis, you will need a file with YouTube comments data.

To collect YouTube comments from a video, run the script video_main.py
```bash
python3 video_main.py
```
The output file will be saved as `youtube_comments.json`.

You can also define a different name for the output file using the parameter -o when running the script:
```bash
python3 video_main.py -o custom_output_name.json
```

## 🚀Run
```bash
streamlit run app.py
```
