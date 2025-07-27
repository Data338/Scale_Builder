print("""
  ____            _        ____        _ _     _            
 / ___|  ___ __ _| | ___  | __ ) _   _(_) | __| | ___ _ __  
 \___ \ / __/ _` | |/ _ \ |  _ \| | | | | |/ _` |/ _ \ '__| 
  ___) | (_| (_| | |  __/ | |_) | |_| | | | (_| |  __/ |    
 |____/ \___\__,_|_|\___| |____/ \__,_|_|_|\__,_|\___|_|    
                                                            
      """)

def Chromatic_table (scale_notes):
    
    print(f"""
Interval        Semitones From Tonic    NOTE
--------------- -------------------- -----------
Tonic:                  0                 {scale_notes[0]}

Minor 2nd:              1                 {scale_notes[1]}
Major 2nd:              2                 {scale_notes[2]}

Minor 3rd:              3                 {scale_notes[3]}
Major 3rd:              4                 {scale_notes[4]}

Perfect 4th:            5                 {scale_notes[5]}
Augmented 4th:          6                 {scale_notes[6]}
Diminished 5th:         6                 {scale_notes[6]}

Perfect 5th:            7                 {scale_notes[7]}
Augmented 5th:          8                 {scale_notes[8]}
Minor 6th:              8                 {scale_notes[8]}

Major 6th:              9                 {scale_notes[9]}
Augmented 6th:          10                {scale_notes[10]}
Minor 7th:              10                {scale_notes[10]}

Major 7th:              11                {scale_notes[11]}
Octave:                 12                {scale_notes[12]}

Minor 9th:              13                {scale_notes[1]}
Major 9th:              14                {scale_notes[2]}
Augmented 9th:          15                {scale_notes[3]}

Perfect 11th:           17                {scale_notes[5]}
Augmented 11th:         18                {scale_notes[6]}

Diminished 13th:        19                {scale_notes[7]}
Minor 13th:             20                {scale_notes[8]}
Major 13th:             21                {scale_notes[9]}
    """)

def Major_table (scale_notes):
        
         print(f"""
Interval        Semitones From Tonic    NOTE         Explanation
--------------- -------------------- ----------- ------------------------
Tonic:                  0                 {scale_notes[0]}     Root note
Major 2nd:              2                 {scale_notes[2]}     2nd degree
Major 3rd:              4                 {scale_notes[4]}     3rd degree
Perfect 4th:            5                 {scale_notes[5]}     4th degree
Perfect 5th:            7                 {scale_notes[7]}     5th degree
Major 6th:              9                 {scale_notes[9]}     6th degree
Major 7th:              11                {scale_notes[11]}    7th degree
Octave:                 12                {scale_notes[12]}    Same as tonic (1 + 8va)

--- Extensions (repetitions above octave) ---
Minor 9th:              13                {scale_notes[1]}     ♭2 + octave
Major 9th:              14                {scale_notes[2]}     2nd degree + octave
Augmented 9th:          15                {scale_notes[3]}     ♯2 (or ♭3) + octave
Perfect 11th:           17                {scale_notes[5]}     4th degree + octave
Augmented 11th:         18                {scale_notes[6]}     ♯4 (tritone) + octave
Diminished 13th:        19                {scale_notes[7]}     ♭5 + octave
Minor 13th:             20                {scale_notes[8]}     ♭6 + octave
Major 13th:             21                {scale_notes[9]}     6th degree + octave
    """)

def Dorian_table (scale_notes):
        
         print(f"""
Interval         Semitones From Tonic    NOTE        Explanation
---------------  --------------------   --------    -------------------------
Tonic:                  0                {scale_notes[0]}      Root note
Major 2nd:              2                {scale_notes[2]}      2nd
Minor 3rd:              3                {scale_notes[3]}      ♭3
Perfect 4th:            5                {scale_notes[5]}      4th
Perfect 5th:            7                {scale_notes[7]}      5th
Major 6th:              9                {scale_notes[9]}      6th
Minor 7th:              10               {scale_notes[10]}     ♭7
Octave:                 12               {scale_notes[12]}     Same as tonic (1 + 8va)

--- Extensions ---
Major 9th:              14               {scale_notes[2]}      2nd + octave
Perfect 11th:           17               {scale_notes[5]}      4th + octave
Major 13th:             21               {scale_notes[9]}      6th + octave
    """)
        
def Phrygian_table (scale_notes):
         print(f"""
Interval         Semitones From Tonic    NOTE        Explanation
---------------  --------------------   --------    -------------------------
Tonic:                  0                {scale_notes[0]}      Root note
Minor 2nd:              1                {scale_notes[1]}      ♭2
Minor 3rd:              3                {scale_notes[3]}      ♭3
Perfect 4th:            5                {scale_notes[5]}      4th
Perfect 5th:            7                {scale_notes[7]}      5th
Minor 6th:              8                {scale_notes[8]}      ♭6
Minor 7th:              10               {scale_notes[10]}     ♭7
Octave:                 12               {scale_notes[12]}     Same as tonic (1 + 8va)

--- Extensions ---
Minor 9th:              13               {scale_notes[1]}      ♭2 + octave
Perfect 11th:           17               {scale_notes[5]}      4th + octave
Minor 13th:             20               {scale_notes[8]}      ♭6 + octave
    """)
                 
def Lydian_table (scale_notes):
        
        print(f"""Interval         Semitones From Tonic    NOTE        Explanation
---------------  --------------------   --------    -------------------------
Tonic:                  0                {scale_notes[0]}      Root note
Major 2nd:              2                {scale_notes[2]}      2nd degree
Major 3rd:              4                {scale_notes[4]}      3rd degree
Augmented 4th:          6                {scale_notes[6]}      #4 / Tritone
Perfect 5th:            7                {scale_notes[7]}      5th degree
Major 6th:              9                {scale_notes[9]}      6th degree
Major 7th:              11               {scale_notes[11]}     7th degree
Octave:                 12               {scale_notes[12]}     Same as tonic (1 + 8va)

--- Extensions ---
Major 9th:              14               {scale_notes[2]}      2nd + octave
Augmented 11th:         18               {scale_notes[6]}      #4 + octave
Major 13th:             21               {scale_notes[9]}      6th + octave
""")
        
def Mixolydian_table (scale_notes):
        
        print(f"""
              
Interval         Semitones From Tonic    NOTE        Explanation
---------------  --------------------   --------    -------------------------
Tonic:                  0                {scale_notes[0]}      Root note
Major 2nd:              2                {scale_notes[2]}      2nd degree
Major 3rd:              4                {scale_notes[4]}      3rd degree
Perfect 4th:            5                {scale_notes[5]}      4th degree
Perfect 5th:            7                {scale_notes[7]}      5th degree
Major 6th:              9                {scale_notes[9]}      6th degree
Minor 7th:              10               {scale_notes[10]}     ♭7
Octave:                 12               {scale_notes[12]}     Same as tonic (1 + 8va)

--- Extensions ---
Major 9th:              14               {scale_notes[2]}      2nd + octave
Perfect 11th:           17               {scale_notes[5]}      4th + octave
Major 13th:             21               {scale_notes[9]}      6th + octave
""")

def Aeolian_table (scale_notes):
        
        print(f"""

Interval         Semitones From Tonic    NOTE        Explanation
---------------  --------------------   --------    -------------------------
Tonic:                  0                {scale_notes[0]}      Root note
Major 2nd:              2                {scale_notes[2]}      2nd degree
Minor 3rd:              3                {scale_notes[3]}      ♭3
Perfect 4th:            5                {scale_notes[5]}      4th degree
Perfect 5th:            7                {scale_notes[7]}      5th degree
Minor 6th:              8                {scale_notes[8]}      ♭6
Minor 7th:              10               {scale_notes[10]}     ♭7
Octave:                 12               {scale_notes[12]}     Same as tonic (1 + 8va)

--- Extensions ---
Major 9th:              14               {scale_notes[2]}      2nd + octave
Perfect 11th:           17               {scale_notes[5]}      4th + octave
Minor 13th:             20               {scale_notes[8]}      ♭6 + octave

    """)

def Locrian_table (scale_notes):
        
        print(f"""

Interval         Semitones From Tonic    NOTE        Explanation
---------------  --------------------   --------    -------------------------
Tonic:                  0                {scale_notes[0]}      Root note
Minor 2nd:              1                {scale_notes[1]}      ♭2
Minor 3rd:              3                {scale_notes[3]}      ♭3
Perfect 4th:            5                {scale_notes[5]}      4th
Diminished 5th:         6                {scale_notes[6]}      ♭5
Minor 6th:              8                {scale_notes[8]}      ♭6
Minor 7th:              10               {scale_notes[10]}     ♭7
Octave:                 12               {scale_notes[12]}     Same as tonic (1 + 8va)

--- Extensions ---
Minor 9th:              13               {scale_notes[1]}      ♭2 + octave
Perfect 11th:           17               {scale_notes[5]}      4th + octave
Minor 13th:             20               {scale_notes[8]}      ♭6 + octave

    """)

def Harmonic_Minor_table (scale_notes):
        
        print(f"""
Interval         Semitones From Tonic    NOTE        Explanation
---------------  --------------------   --------    -------------------------
Tonic:                  0                {scale_notes[0]}      Root note
Major 2nd:              2                {scale_notes[2]}      2nd degree
Minor 3rd:              3                {scale_notes[3]}      ♭3
Perfect 4th:            5                {scale_notes[5]}      4th
Perfect 5th:            7                {scale_notes[7]}      5th
Minor 6th:              8                {scale_notes[8]}      ♭6
Major 7th:              11               {scale_notes[11]}     7th degree
Octave:                 12               {scale_notes[12]}     Same as tonic (1 + 8va)

--- Extensions ---
Major 9th:              14               {scale_notes[2]}      2nd + octave
Perfect 11th:           17               {scale_notes[5]}      4th + octave
Minor 13th:             20               {scale_notes[8]}      ♭6 + octave

    """)

def Melodic_Minor_table (scale_notes):
        
        print(f"""

Interval          Semitones From Tonic    NOTE            Explanation
----------------  ---------------------   --------        ----------------------------
Tonic:                  0                 {scale_notes[0]}       Root note
Major 2nd:              2                 {scale_notes[2]}       2nd degree
Minor 3rd:              3                 {scale_notes[3]}       ♭3
Perfect 4th:            5                 {scale_notes[5]}       4th
Perfect 5th:            7                 {scale_notes[7]}       5th
Major 6th (Asc):        9                 {scale_notes[9]}       6th (natural ascending)
Minor 6th (Desc):       8                 {scale_notes[8]}       ♭6 (descending version)
Major 7th (Asc):        11                {scale_notes[11]}      7th (ascending)
Minor 7th (Desc):       10                {scale_notes[10]}      ♭7 (descending)
Octave:                 12                {scale_notes[12]}      1 + 8va

--- Extensions ---
Major 9th:              14                {scale_notes[2]}       2nd + octave
Perfect 11th:           17                {scale_notes[5]}       4th + octave
Major 13th (Asc):       21                {scale_notes[9]}       6th + octave
Minor 13th (Desc):      20                {scale_notes[8]}       ♭6 + octave


""")

def Double_Harmonic_Major_table (scale_notes):
        
        print(f"""
Interval         Semitones From Tonic    NOTE        Explanation
---------------  --------------------   --------    -------------------------
Tonic:                  0                {scale_notes[0]}      Root note
Minor 2nd:              1                {scale_notes[1]}      ♭2
Major 3rd:              4                {scale_notes[4]}      3rd
Perfect 4th:            5                {scale_notes[5]}      4th
Perfect 5th:            7                {scale_notes[7]}      5th
Minor 6th:              8                {scale_notes[8]}      ♭6
Major 7th:              11               {scale_notes[11]}     7th
Octave:                 12               {scale_notes[12]}     Same as tonic (1 + 8va)

--- Extensions ---
Minor 9th:              13               {scale_notes[1]}      ♭2 + octave
Perfect 11th:           17               {scale_notes[5]}      4th + octave
Minor 13th:             20               {scale_notes[8]}      ♭6 + octave


""")

def Phrygian_Dominant_table (scale_notes):
        
        print(f"""

Interval         Semitones From Tonic    NOTE        Explanation
---------------  --------------------   --------    -------------------------
Tonic:                  0                {scale_notes[0]}      Root note
Minor 2nd:              1                {scale_notes[1]}      ♭2
Major 3rd:              4                {scale_notes[4]}      3rd
Perfect 4th:            5                {scale_notes[5]}      4th
Perfect 5th:            7                {scale_notes[7]}      5th
Minor 6th:              8                {scale_notes[8]}      ♭6
Minor 7th:              10               {scale_notes[10]}     ♭7
Octave:                 12               {scale_notes[12]}     Same as tonic (1 + 8va)

--- Extensions ---
Minor 9th:              13               {scale_notes[1]}      ♭2 + octave
Perfect 11th:           17               {scale_notes[5]}      4th + octave
Minor 13th:             20               {scale_notes[8]}      ♭6 + octave




    """)

def Whole_Tone_table (scale_notes):
        
        print(f"""

Interval         Semitones From Tonic    NOTE        Explanation
---------------  --------------------   --------    -------------------------
Tonic:                  0                {scale_notes[0]}      Root note
Major 2nd:              2                {scale_notes[2]}      2nd
Major 3rd:              4                {scale_notes[4]}      3rd
Augmented 4th:          6                {scale_notes[6]}      #4 / Tritone
Augmented 5th:          8                {scale_notes[8]}      #5
Minor 7th:              10               {scale_notes[10]}     ♭7
Octave:                 12               {scale_notes[12]}     Same as tonic (1 + 8va)

--- Extensions ---
Major 9th:              14               {scale_notes[2]}      2nd + octave
Augmented 11th:         18               {scale_notes[6]}      #4 + octave
Augmented 13th:         20               {scale_notes[8]}      #5 + octave

    """)

def Diminished_Scale_table (scale_notes):
        
        print(f"""

Interval           Semitones From Tonic    NOTE             Explanation
-----------------  ---------------------   ---------        -----------------------------
Tonic:                   0                {scale_notes[0]}       Root note
Minor 2nd:               1                {scale_notes[1]}       ♭2
Major 2nd:               2                {scale_notes[2]}       2nd
Minor 3rd:               3                {scale_notes[3]}       ♭3
Perfect 4th:             5                {scale_notes[5]}       4th
Diminished 5th (Tritone):6                {scale_notes[6]}       ♭5 / #11
Perfect 5th:             7                {scale_notes[7]}       5th
Minor 6th:               8                {scale_notes[8]}       ♭6
Minor 7th:               10               {scale_notes[10]}      ♭7
Octave:                  12               {scale_notes[12]}      1 + 8va

--- Extensions (following the symmetrical pattern) ---
Minor 9th:               13               {scale_notes[1]}       ♭2 + octave
Major 9th:               14               {scale_notes[2]}       2nd + octave
Minor 10th:              15               {scale_notes[3]}       ♭3 + octave
Perfect 11th:            17               {scale_notes[5]}       4th + octave
Diminished 11th:         18               {scale_notes[6]}       ♭5 + octave
Perfect 12th:            19               {scale_notes[7]}       5th + octave
Minor 13th:              20               {scale_notes[8]}       ♭6 + octave
Minor 14th:              22               {scale_notes[10]}      ♭7 + octave


    """)

def Major_Pentatonic_table (scale_notes):
        
        print(f"""

Interval           Semitones From Tonic    NOTE             Explanation
-----------------  ---------------------   ---------        -----------------------------
Tonic:                   0                {scale_notes[0]}       Root note
Major 2nd:               2                {scale_notes[2]}       2nd
Major 3rd:               4                {scale_notes[4]}       3rd
Perfect 5th:             7                {scale_notes[7]}       5th
Major 6th:               9                {scale_notes[9]}       6th
Octave:                  12               {scale_notes[12]}      1 + 8va

--- Extensions ---
Major 9th:               14               {scale_notes[2]}       2nd + octave
Major 13th:              21               {scale_notes[9]}       6th + octave

    """)

def Minor_Pentatonic_table (scale_notes):
        
        print(f"""

Interval           Semitones From Tonic    NOTE             Explanation
-----------------  ---------------------   ---------        -----------------------------
Tonic:                   0                {scale_notes[0]}       Root note
Minor 3rd:               3                {scale_notes[3]}       ♭3
Perfect 4th:             5                {scale_notes[5]}       4th
Perfect 5th:             7                {scale_notes[7]}       5th
Minor 7th:               10               {scale_notes[10]}      ♭7
Octave:                  12               {scale_notes[12]}      1 + 8va

--- Extensions ---
Minor 9th:               13               {scale_notes[1]}       ♭2 + octave
Perfect 11th:            17               {scale_notes[5]}       4th + octave
Minor 13th:              20               {scale_notes[8]}       ♭6 + octave


    """)

def Major_Pentatonic_Blues_table (scale_notes):
        
        print(f"""
              
Interval           Semitones From Tonic    NOTE             Explanation
-----------------  ---------------------   ---------        -----------------------------
Tonic:                   0                {scale_notes[0]}       Root note
Major 2nd:               2                {scale_notes[2]}       2nd
Minor 3rd (blue note):   3                {scale_notes[3]}       ♭3 (blue note)
Major 3rd:               4                {scale_notes[4]}       3rd
Perfect 5th:             7                {scale_notes[7]}       5th
Major 6th:               9                {scale_notes[9]}       6th
Octave:                  12               {scale_notes[12]}      1 + 8va


    """)

def Minor_Pentatonic_Blues_table (scale_notes):
    
    print(f"""
Interval           Semitones From Tonic    NOTE             Explanation
-----------------  ---------------------   ---------        -----------------------------
Tonic:                   0                {scale_notes[0]}       Root note
Minor 3rd:               3                {scale_notes[3]}       ♭3
Perfect 4th:             5                {scale_notes[5]}       4th
Diminished 5th (blue note):6               {scale_notes[6]}       ♭5 (blue note)
Perfect 5th:             7                {scale_notes[7]}       5th
Minor 7th:               10               {scale_notes[10]}      ♭7
Octave:                  12               {scale_notes[12]}      1 + 8va


    """)
    
def scale_sel(scale_selection, scale_notes):
    if scale_selection == 0:
        Chromatic_table(scale_notes)
    
    elif scale_selection == 1:
        Major_table(scale_notes)
    
    elif scale_selection == 2:
        Dorian_table(scale_notes)
    
    elif scale_selection == 3:
        Phrygian_table(scale_notes)
    
    elif scale_selection == 4:
        Lydian_table(scale_notes)
    
    elif scale_selection == 5:
        Mixolydian_table(scale_notes)
    
    elif scale_selection == 6:
        Aeolian_table(scale_notes)
    
    elif scale_selection == 7:
        Locrian_table(scale_notes)
    
    elif scale_selection == 8:
        Harmonic_Minor_table(scale_notes)
    
    elif scale_selection == 9:
        Melodic_Minor_table(scale_notes)
    
    elif scale_selection == 10:
        Double_Harmonic_Major_table(scale_notes)
    
    elif scale_selection == 11:
        Phrygian_Dominant_table(scale_notes)
    
    elif scale_selection == 12:
        Whole_Tone_table(scale_notes)
    
    elif scale_selection == 13:
        Diminished_Scale_table(scale_notes)
    
    elif scale_selection == 14:
        Major_Pentatonic_table(scale_notes)
    
    elif scale_selection == 15:
        Minor_Pentatonic_table(scale_notes)
    
    elif scale_selection == 16:
        Major_Pentatonic_Blues_table(scale_notes)
    
    elif scale_selection == 17:
        Minor_Pentatonic_Blues_table(scale_notes)
    
    else:
        print("Scale not found, please input a valid selection number.")

note_map = {
    "C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11,
    "C#":1,"D#":3,"E#":5,"F#":6,"G#":8,"A#":10,"B#":0,
}

flat_notes_map = {
    "Cb":11,"Db":1,"Eb":3,"Fb":4,"Gb":6,"Ab":8,"Bb":10,
}

sharp_notes_chromatic = [
    "C","C#","D","D#","E","F","F#","G","G#","A","A#","B",
    "C","C#","D","D#","E","F","F#","G","G#","A","A#","B"
]

flat_notes_chromatic = [
    "C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B",
    "C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"
]

while True:
    root_selection = input("Select the root of your scale: ").strip().capitalize()

    if root_selection in note_map:
        
        root_semitones = note_map[root_selection]
        
        scale_notes = sharp_notes_chromatic[root_semitones : root_semitones + 13]

    elif root_selection in flat_notes_map:
        
        root_semitones = flat_notes_map[root_selection]
        
        scale_notes = flat_notes_chromatic[root_semitones : root_semitones + 13]

    else:
        print("Invalid input")
        continue

    try:
        scale_selection = int(input("""
         Select the type of scale: 
|------------------------------------------------|
|           0) Chromatic                         |
|           1) Ionian/ Major                     |
|           2) Dorian                            |
|           3) Phrygian                          |
|           4) Lydian                            |
|           5) Mixolydian                        |
|           6) Aeolian/ Natural Minor            |
|           7) Locrian                           |
|           8) Harmonic Minor                    |
|           9) Melodic Minor                     |
|          10) Double Harmonic Major             |
|          11) Phrygian Dominant                 |
|          12) Whole Tone                        | 
|          13) Octatonic Scale/ Diminished Scale |
|          14) Major Pentatonic                  |
|          15) Minor Pentatonic                  |
|          16) Major Pentatonic Blues            |  
|          17) Minor Pentatonic Blues            |
|________________________________________________|
    : """))
    except ValueError:
        print("Please enter a valid number for the scale selection.")
        continue

    scale_sel(scale_selection, scale_notes)

    ynsel = input("Type (y) to create new scale, type anything else to exit: ").lower()
    if ynsel != "y":
        break
