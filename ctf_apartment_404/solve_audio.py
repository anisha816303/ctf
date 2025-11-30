import wave
import struct

def analyze_audio(file_path):
    print(f"--- Analyzing {file_path} ---")
    
    # 1. Check for appended text (Strings method)
    with open(file_path, 'rb') as f:
        content = f.read()
        # Look for the known header of our hidden clue or just scan for readable text
        try:
            # Find text starting with '[' near the end
            last_chars = content[-100:]
            print(f"[Strings Analysis] Tail of file: {last_chars}")
        except Exception as e:
            print(f"Error reading file tail: {e}")

    # 2. Check for RIFF Metadata (Metadata method)
    try:
        # We manually parse the RIFF chunks because standard wave module ignores them
        with open(file_path, 'rb') as f:
            f.seek(0)
            header = f.read(12)
            if header[:4] != b'RIFF' or header[8:] != b'WAVE':
                print("Not a valid WAVE file")
                return

            while True:
                chunk_header = f.read(8)
                if len(chunk_header) < 8: break
                
                chunk_id = chunk_header[:4]
                chunk_size = struct.unpack('<I', chunk_header[4:])[0]
                
                if chunk_id == b'LIST':
                    print(f"[Metadata Analysis] Found LIST chunk of size {chunk_size}")
                    list_type = f.read(4)
                    print(f"  Type: {list_type}")
                    
                    # Read sub-chunks
                    bytes_read = 4
                    while bytes_read < chunk_size:
                        sub_id = f.read(4)
                        sub_size = struct.unpack('<I', f.read(4))[0]
                        sub_data = f.read(sub_size)
                        
                        # Pad byte if size is odd
                        if sub_size % 2 == 1:
                            f.read(1)
                            bytes_read += 1
                            
                        print(f"  Tag: {sub_id}, Value: {sub_data}")
                        bytes_read += 8 + sub_size
                else:
                    # Skip other chunks
                    f.seek(chunk_size, 1)
                    
    except Exception as e:
        print(f"Error parsing metadata: {e}")

if __name__ == "__main__":
    analyze_audio("assets/evidence_audio.wav")
