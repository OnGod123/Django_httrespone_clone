import json

# Function to convert binary data to UTF-8 string and break it into chunks
def chunk_binary_data(binary_data, chunk_size):
    utf8_string = binary_data.decode('utf-8')
    chunks = [utf8_string[i:i+chunk_size] for i in range(0, len(utf8_string), chunk_size)]
    return chunks

# Example binary data (you would read this from a file or another source)
binary_data = b'\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64'

# Convert binary data to chunks of UTF-8 encoded strings
chunk_size = 3
chunks = chunk_binary_data(binary_data, chunk_size)

# Convert chunks to JSON
json_data = json.dumps(chunks)

print(json_data)

