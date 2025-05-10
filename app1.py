from gtts import gTTS
import streamlit as st
import os
from moviepy.editor import VideoFileClip, TextClip, AudioFileClip, CompositeVideoClip

st.title("Text-to-Video App")
text_input = st.text_input("Enter text:")

if st.button("Convert to Video"):
    if text_input:
        # Step 1: Convert text to speech
        tts = gTTS(text_input)
        audio_path = "output.mp3"
        tts.save(audio_path)

        # Step 2: Create video with text
        text_clip = TextClip(text_input, fontsize=50, color='white', bg_color='black', size=(1280, 720), print_cmd=True)
        text_clip = text_clip.set_duration(10)  # Duration of the video

        # Step 3: Load the audio file
        audio_clip = AudioFileClip(audio_path)

        # Step 4: Set the audio for the video
        video_clip = text_clip.set_audio(audio_clip)

        # Step 5: Save and display the video
        video_path = "output_video.mp4"
        video_clip.write_videofile(video_path, fps=24)

        # Display the video in Streamlit
        st.video(video_path)
        
        # Clean up the saved files
        os.remove(audio_path)
        os.remove(video_path)
