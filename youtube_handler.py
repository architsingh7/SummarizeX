from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
import urllib.parse as urlparse

def extract_video_id(url):
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]
    elif "youtube.com" in url:
        parsed_url = urlparse.urlparse(url)
        video_id = urlparse.parse_qs(parsed_url.query).get("v")
        if video_id:
            return video_id[0]
    return None

def extract_youtube_transcript(url):
    video_id = extract_video_id(url)

    if not video_id:
        return "Error: Invalid YouTube URL format. Please ensure it is a valid youtube.com or youtu.be link."

    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.fetch(video_id)

        full_transcript = " ".join([segment.text for segment in transcript_list])
        return full_transcript

    except TranscriptsDisabled:
        return "Error: The creator has disabled transcripts/subtitles for this video."
    except NoTranscriptFound:
        return "Error: No playable transcript found. The video may not have English subtitles."
    except VideoUnavailable:
        return "Error: This video is unavailable, deleted, or set to private."
    except Exception as e:
        return f"Error fetching transcript: An unexpected error occurred ({str(e)})."