print("""
  ____            _        ____        _ _     _            
 / ___|  ___ __ _| | ___  | __ ) _   _(_) | __| | ___ _ __  
 \___ \ / __/ _` | |/ _ \ |  _ \| | | | | |/ _` |/ _ \ '__| 
  ___) | (_| (_| | |  __/ | |_) | |_| | | | (_| |  __/ |    
 |____/ \___\__,_|_|\___| |____/ \__,_|_|_|\__,_|\___|_|    
                                                            
      """)

def chromatic_table (scale_notes):
    
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
    

while True:

  flat_notes_map={ "Cb":11,"Db":1,"Eb":3,"Fb":4,"Gb":6,"Ab":8,"Bb":10, }


  note_map={

  "C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11,

  "C#":1,"D#":3,"E#":5,"F#":6,"G#":8,"A#":10,"B#":0,

}

  sharp_notes_chromatic = [
    "C","C#","D","D#","E","F","F#","G","G#","A","A#","B",
    "C","C#","D","D#","E","F","F#","G","G#","A","A#","B"
]

  root_selection = input("Select the root of your scale : ").capitalize()

  
  
  if root_selection in note_map:
    
    root_semitones = note_map[root_selection]
    
    scale_notes = sharp_notes_chromatic[root_semitones : root_semitones + 13]

    chromatic_table(scale_notes)


    
   
    
    ynsel=input("""Type (y) to create new scale\nType anything else to exit: """).lower()
    if ynsel=="y":
     continue
    else:
      break

    
  
  
  
  
  
  
  
  elif root_selection in flat_notes_map:
    
    root_semitones = flat_notes_map[root_selection]

    flat_notes_chromatic = [
    "C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B",
    "C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"
]
    
    scale_notes = flat_notes_chromatic[root_semitones : root_semitones + 13]

    chromatic_table(scale_notes)

   
   
    ynsel=input("""Type (y) to create new scale\nType anything else to exit: """).lower()
    if ynsel=="y":
     continue
    else:
      break
    

else:
  print("Invalid input")
