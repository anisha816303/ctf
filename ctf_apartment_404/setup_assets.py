import os
import random
import wave
import struct
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def create_glitched_image():
    # Create a dark, noisy image
    width, height = 640, 480
    img = Image.new('RGB', (width, height), color=(10, 10, 10))
    pixels = img.load()
    
    for i in range(width):
        for j in range(height):
            if random.random() > 0.9:
                pixels[i, j] = (0, 50, 0) # Greenish noise
            if random.random() > 0.99:
                 pixels[i, j] = (50, 50, 50) # White noise

    draw = ImageDraw.Draw(img)
    # Draw "Last Motion Detected" text
    # Default font
    draw.text((10, 10), "CAM_01 [LIVING ROOM]", fill=(0, 255, 0))
    draw.text((10, 30), "REC: 11:42 PM", fill=(255, 0, 0))
    
    img_path = os.path.join(ASSETS_DIR, "scene.jpg")
    img.save(img_path)
    
    # Append the hidden clue
    with open(img_path, "ab") as f:
        f.write(b"\n\n[EXIF_DATA_CORRUPT] Note_to_self: Encrypted_Journal_Pass: VIGENERE")
    
    print(f"Created {img_path}")

def create_corrupted_audio():
    # Create a wav file with high pitched noise
    audio_path = os.path.join(ASSETS_DIR, "evidence_audio.wav")
    
    sample_rate = 44100
    duration = 5 # seconds
    frequency = 2000 # High pitch
    
    n_samples = int(sample_rate * duration)
    
    with wave.open(audio_path, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        for i in range(n_samples):
            # Generate a sine wave + noise
            value = int(32767.0 * 0.5 * (
                (i % (sample_rate // frequency)) / (sample_rate // frequency)
            ))
            # Add random noise
            value += random.randint(-1000, 1000)
            data = struct.pack('<h', max(-32768, min(32767, value)))
            wav_file.writeframes(data)
            
    # Append the hidden clue (simulating spectrogram/reverse audio find)
    with open(audio_path, "ab") as f:
        f.write(b"\n\n[SPECTRAL_ANALYSIS_RESULT]: It was a deepfake. Marcus is innocent.")

    print(f"Created {audio_path}")

def create_cat_image():
    # Create a simple image for the cat
    width, height = 300, 300
    img = Image.new('RGB', (width, height), color=(200, 200, 200))
    draw = ImageDraw.Draw(img)
    
    # Draw a crude cat face
    draw.ellipse((50, 50, 250, 250), fill=(255, 165, 0)) # Orange head
    draw.polygon([(50, 100), (50, 50), (100, 50)], fill=(255, 165, 0)) # Left ear
    draw.polygon([(200, 50), (250, 50), (250, 100)], fill=(255, 165, 0)) # Right ear
    draw.ellipse((100, 120, 120, 140), fill=(0, 0, 0)) # Left eye
    draw.ellipse((180, 120, 200, 140), fill=(0, 0, 0)) # Right eye
    draw.polygon([(140, 180), (160, 180), (150, 190)], fill=(255, 192, 203)) # Nose
    
    # Caption
    try:
        # Try to load a font, otherwise use default
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
        
    draw.text((120, 260), "Fluffy", fill=(0, 0, 0), font=font)
    
    img_path = os.path.join(ASSETS_DIR, "cat.jpg")
    img.save(img_path)
    print(f"Created {img_path}")

if __name__ == "__main__":
    create_glitched_image()
    create_corrupted_audio()
    create_cat_image()
