from transformers import pipeline
import glob
import torch


class Speech2Text:
    def __init__(self):
        self.pipe = self._load_model()


    def _load_model(self):
        pipe = pipeline(
            task="automatic-speech-recognition",
            model="arthoho66/model_005_2000",
            device=0 if torch.cuda.is_available() else -1,  # Use GPU if available, else CPU
        )
        return pipe

    def process_voice(self,audio_file):
        text_result = self.pipe(audio_file)
        print(text_result)
        return text_result
        
    
# Example usage:
if __name__ == "__main__":
    speech2text = Speech2Text()
    speech2text.process()
