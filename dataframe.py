
import pandas as pd

# Step 1: Create some data to put into the DataFrame.
ipa_dict = {
    'IPA Symbol': ['p', 'b', 't', 'd', 'k', 'g', 'm', 'n', 'ŋ', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'ʧ', 'ʤ', 'r', 'ʋ', 'j', 'l', 'w', 'i', 'u', 'e', 'o', 'a'],
    'Sound': ['voiceless bilabial stop', 'voiced bilabial stop', 'voiceless alveolar stop', 'voiced alveolar stop', 'voiceless velar stop', 'voiced velar stop',
              'bilabial nasal', 'alveolar nasal', 'velar nasal', 'voiceless labiodental fricative', 'voiced labiodental fricative', 'voiceless dental fricative',
              'voiced dental fricative', 'voiceless alveolar fricative', 'voiced alveolar fricative',
              'voiceless postalveolar fricative', 'voiced postalveolar fricative', 'voiceless postalveolar affricate', 'voiced postalveolar affricate', 'alveolar trill',
              'labiodental approximant', 'palatal approximant', 'alveolar lateral approximant', 'labio-velar approximant', 'close front unrounded vowel', 'close back rounded vowel',
              'close-mid front unrounded vowel', 'close-mid back rounded vowel',
              'open front unrounded vowel']
}


# Step 2: Create a DataFrame from the data.
df = pd.DataFrame(ipa_dict)