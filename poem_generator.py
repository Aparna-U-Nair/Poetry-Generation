import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


model = load_model("model.h5")
token = pickle.load(open("token.pkl","rb"))
poem_len = 10
seq_len = 24
out = []

def gen_poem(base_text,n_lines):
    for i in range(n_lines):
        final = []
        for _ in range(poem_len):
            enc = token.texts_to_sequences([base_text])
            enc = pad_sequences(enc,padding="pre",maxlen=seq_len) #here max length = 24 not 25 as we dont need to separate the target from input.
            pred = np.argmax(model.predict(enc),axis=-1) #will give the numeric value of that word
        #   print("PRED :",pred)
            pred_word =""
            for w,idx in token.word_index.items():
                if idx == pred:
                    pred_word = w
                    break
            base_text = base_text + " " + pred_word
            final.append(pred_word) #a sentence of length 10 will be formed.
        base_text = final[-1] #last word from previous line ll go as input to next
        out.append(" ".join(final))
    return out