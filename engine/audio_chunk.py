from pydub import AudioSegment
from pydub.silence import split_on_silence
# from engine.speech2text import Speech2Text
import os
import shutil
import time

class AudioChunk :
    # def __init__(self):
    #     self.speech2text = Speech2Text()

    def chunks_audio(self, audio: str ):
        # Chunk up the audio file
        sound_file = AudioSegment.from_mp3(audio)
        duration_in_seconds = len(sound_file) / 1000
        print(f"เวลาของไฟล์ : {duration_in_seconds}")

        count = 0
        if duration_in_seconds > 30 :
            audio_chunks = split_on_silence(sound_file, min_silence_len=500, silence_thresh=-40)
            for chunk in audio_chunks :
                duration_in_seconds = len(chunk) / 1000
                if duration_in_seconds > 30 :
                    new_chunk = check_duration_in_seconds(chunk)
                    export_chunk(new_chunk,count)
                    count += 1
                else :
                    export_chunk(chunk,count)
                    count += 1
        
        else :
            export_chunk(sound_file,count)
            count += 1
        
    
    def remove_chunk(self,output_dir: str =  "chunk_file") :
        # ใช้ os.listdir() เพื่อดึงรายการไฟล์ทั้งหมดในโฟลเดอร์
        file_list = os.listdir(output_dir)

        for file_name in file_list:
            file_path = os.path.join(output_dir, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"ไม่สามารถลบ {file_path}. เกิดข้อผิดพลาด: {e}")


def check_duration_in_seconds(chunk):
    audio_chunks = split_on_silence(chunk, min_silence_len=500, silence_thresh=-34)
    for chunk in audio_chunks:
        duration_in_seconds = len(chunk) / 1000
        print(f"เวลาของ chunk : {duration_in_seconds} วินาที")
        return chunk

def export_chunk(chunk ,count ,output_dir: str =  "chunk_file" ):
    # print("Audio split into " + str(count) + " audio chunks \n")
    out_file = f"{output_dir}/chunk{count}.wav"
    # print("\nExporting >>", out_file)
    print(len(chunk) / 1000)
    chunk.export(out_file, format="wav")
    return out_file

