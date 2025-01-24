import pandas as pd
import pickle

# Create a sample music dataset
music_data = {
    'song': [
        'Shape of You', 'Blinding Lights', 'Dance Monkey', 'Sunflower', 'Stay',
        'Believer', 'Perfect', 'Havana', 'Closer', 'Despacito'
    ],
    'artist': [
        'Ed Sheeran', 'The Weeknd', 'Tones and I', 'Post Malone', 'The Kid LAROI',
        'Imagine Dragons', 'Ed Sheeran', 'Camila Cabello', 'The Chainsmokers', 'Luis Fonsi'
    ],
    'genre': [
        'Pop', 'Synth-pop', 'Dance-pop', 'Hip hop', 'Pop',
        'Pop rock', 'Pop', 'Pop', 'EDM', 'Reggaeton pop'
    ]
}

# Create DataFrame
df = pd.DataFrame(music_data)

# Create a simple similarity matrix (dummy data for example)
# In a real recommendation system, you'd calculate this based on actual features
n_songs = len(df)
similarity = [[1 if i == j else 0.5 for j in range(n_songs)] for i in range(n_songs)]

# Save the DataFrame and similarity matrix
with open('df.pkl', 'wb') as f:
    pickle.dump(df, f)

with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

print("Files created successfully!") 