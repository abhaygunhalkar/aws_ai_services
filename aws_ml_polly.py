
## ---------------------TEXT to SPEECH -----------------------------
import boto3
import time

def synthesize_speech(text, voice_id, output_format="mp3",engine="standard"):
    """
    Synthesizes speech from the given text using Amazon Polly.

    Args:
        text (str): The text to synthesize.
        voice_id (str): The ID of the voice to use (e.g., 'Salli', 'Matthew').
        output_format (str): The format of the output audio (e.g., 'mp3', 'pcm', 'ogg_vorbis').

    Returns:
        bytes: The synthesized speech as bytes, or None on error.
    """
    try:
        client = boto3.client('polly')
        response = client.synthesize_speech(
            Text=text,
            VoiceId=voice_id,
            OutputFormat=output_format,
            Engine=engine
        )
        if "AudioStream" in response:
            return response["AudioStream"].read()
        return None
    except Exception as e:
        print(f"Error during speech synthesis: {e}")
        return None

def save_audio(audio_data, filename):
    """
    Saves the audio data to a file.

    Args:
        audio_data (bytes): The audio data to save.
        filename (str): The name of the file to save to.
    """
    try:
        with open(filename, 'wb') as f:
            f.write(audio_data)
        print(f"Audio saved to {filename}")
    except Exception as e:
        print(f"Error saving audio: {e}")

def play_audio(filename):
    """
    Plays the audio file.  This is a simplified example and may not work on all systems.
    For cross-platform compatibility, consider using a library like simpleaudio or playsound.
    """
    import os
    if os.name == 'nt':  # Windows
        os.system(f"start {filename}")
    elif os.name == 'posix':  # macOS or Linux
        os.system(f"afplay {filename}")  #  macOS
        #  For Linux, you might use:
        #  os.system(f"aplay {filename}")  #  or
        #  os.system(f"mpg123 {filename}")
    else:
        print(f"Unsupported operating system: {os.name}.  Cannot play audio.")

def main():
    """
    Main function to demonstrate text-to-speech using Amazon Polly.
    """
    
    #Trying with Hindi language. The output is amazing !
    text_to_speak = " ​शायरी के माध्यम से हम अपनी भावनाओं को न केवल व्यक्त कर सकते हैं, बल्कि दूसरों की भावनाओं को भी समझ सकते हैं। यह एक ऐसा सशक्त माध्यम है जो भाषा की सीमाओं को पार कर सभी दिलों को जोड़ता है। मिर्ज़ा ग़ालिब, मीर तकी मीर, फैज़ अहमद फैज़, अहमद फ़राज़, गुलज़ार, और जावेद अख्तर जैसे शायरों ने शायरी को नई ऊँचाइयों पर पहुँचाया है। उनकी रचनाएँ आज भी पाठकों के दिलों में बसती हैं और उन्हें प्रेरित करती हैं।"
    voice_id = 'Kajal'  #  Choose a voice (e.g., 'Salli', 'Matthew', 'Joanna')
    output_format = 'mp3'  #  Choose an output format ('mp3', 'pcm', 'ogg_vorbis')
    audio_filename = "polly_output.mp3"
    engine = 'neural' #  Choose the engine: 'standard', 'neural', or 'long-form'

    audio_data = synthesize_speech(text_to_speak, voice_id, output_format,engine)

    if audio_data:
        save_audio(audio_data, audio_filename)
        #  Add a delay before attempting to play the audio
        time.sleep(1)
        play_audio(audio_filename)
    else:
        print("Speech synthesis failed.")

if __name__ == "__main__":
    main()

