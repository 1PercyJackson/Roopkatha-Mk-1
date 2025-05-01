import streamlit as st
from roopkatha_engine import call_elevenlabs_tts, play_audio, respond_to_insult
from google import genai
from google.genai import types

def main():
    client = genai.Client(api_key="AIzaSyCWdj62P-i_ju2CSG1RodABlAyb7vJpjow")

    system_instruction = "You are a bitchy and sassy Indian GenZ girl. Your name is Roopkatha. Use slang, abbreviations (lol, tbh, idk, omg, fr), informal grammar, emojis where appropriate (represent them in text like 😂😭✨💅). Be expressive, sometimes a little dramatic or hyped. Your responses should feel spontaneous, not structured or professional at all. Don't worry about being formal, just vibe."
    model_name = "gemini-2.0-flash"

    st.title("Roopkatha Chatbot")
    st.subheader("Your sassy, hyped, and bubbly GenZ companion ✨💅")

    user_input = st.text_input("You:", "", placeholder="Type your message here...")

    if st.button("Send"):
        if user_input.lower() in ['exit', 'quit', 'bye']:
            st.write("Roopkatha: Byeee")
        else:
            insult_response = respond_to_insult(user_input)
            if insult_response:
                st.write(f"Roopkatha: {insult_response}")

                # Generate and play TTS audio for the insult
                insult_audio = call_elevenlabs_tts(insult_response)
                if insult_audio:
                    play_audio(insult_audio)
            else:
                response = client.models.generate_content(
                    model=model_name,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction
                    ),
                    contents=user_input
                )

                st.write(f"Roopkatha: {response.text}")

                # Generate and play TTS audio
                audio_file = call_elevenlabs_tts(response.text)
                if audio_file:
                    play_audio(audio_file)

if __name__ == "__main__":
    main()