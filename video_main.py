import json
import os
import requests
import argparse
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GOOGLE_API_KEY')
VIDEO_ID = os.getenv('VIDEO_ID')
WAIT_TIME = 10  # Tempo de espera em segundos

params = {
    "part": "snippet",
    "videoId": VIDEO_ID,
    "key": API_KEY,
    "maxResults": 100  # Pega até 100 comentários por página
}

def get_video_comments(output_file):
    comments = []
    next_page_token = None

    while True:
        if next_page_token:
            params["pageToken"] = next_page_token
        
        response = requests.get("https://www.googleapis.com/youtube/v3/commentThreads", params=params)
        data = response.json()

        if "items" not in data:
            print("No comment found")
            break
        
        for item in data["items"]:
            comment = item["snippet"]["topLevelComment"]
            author = comment["snippet"]["authorDisplayName"]
            message = comment["snippet"]["textDisplay"]
            like_count = comment["snippet"]["likeCount"]
            time = comment["snippet"]["publishedAt"]
            comments.append({"author": author, "message": message, "like_count": like_count, "time": time})

        next_page_token = data.get("nextPageToken")
        if not next_page_token:
            break
    
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(comments, file, ensure_ascii=False, indent=4)

    print(f"Ammount of comments collected: {len(comments)}")
    print(f"Comments saved in: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collects comments in a YouTube video.")
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="youtube_comments.json",
        help="Output file name (default: youtube_comments.json)"
    )
    args = parser.parse_args()
    get_video_comments(output_file=args.output)
