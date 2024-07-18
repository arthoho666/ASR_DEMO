# Automatic Speech Recognition (ASR) ภาษาไทย


## วัตถุประสงค์
การพัฒนาระบบ ASR ภาษาไทยนี้มีวัตถุประสงค์เพื่อ:
- ปรับปรุงประสิทธิภาพในการรับรู้และแปลงเสียงพูดภาษาไทย
- สนับสนุนการนำไปใช้ในแอปพลิเคชันหรือบริการที่ต้องการการจดจำเสียงหรือแปลงเสียงเป็นข้อความ

## การใช้งาน
### การติดตั้ง

```sh
python -m venv env
```
Windows
```sh
cmd.exe

C:\> <venv>\Scripts\activate.bat

PowerShell

PS C:\> <venv>\Scripts\Activate.ps1
```

POSIX
```sh
bash/zsh

$ source <venv>/bin/activate

fish

$ source <venv>/bin/activate.fish

csh/tcsh

$ source <venv>/bin/activate.csh

PowerShell

$ <venv>/bin/Activate.ps1
```

```sh
python.exe -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```
*** จำเป็นต้องติดตั้ง FFmpeg https://www.ffmpeg.org/download.html***


### วิธีการใช้งาน
Windows Command Prompt:
```sh
set TF_ENABLE_ONEDNN_OPTS=0
python .\app.py
```
Windows PowerShell:
```sh
$env:TF_ENABLE_ONEDNN_OPTS=0
python .\app.py
```

Linux/MacOS Terminal:
```sh
export TF_ENABLE_ONEDNN_OPTS=0
python .\app.py
```



### ตัวอย่าง
เมื่อรันโปรแกรม ASR แล้ว ท่านสามารถใช้งานโปรแกรมผ่าน Link : http://127.0.0.1:8000

![demo01](https://github.com/user-attachments/assets/195282f2-2581-421e-83e9-d70028955a63)
![demo02](https://github.com/user-attachments/assets/8cb144f0-9171-4b52-b2a1-07b7872ece61)



## ข้อกำหนดและเงื่อนไข
โปรเจกต์นี้เป็น Open Source และใช้ในเชิงการศึกษาเท่านั้น ควรใช้งานในเส้นทางที่ถูกต้องตามข้อกำหนดและเงื่อนไขของ OpenAI GPT และ GitHub

## การร่วมมือและสนับสนุน
หากคุณสนใจที่จะร่วมพัฒนาหรือมีข้อเสนอแนะเกี่ยวกับโปรเจกต์นี้ โปรดติดต่อผ่าน GitHub Issues หรือ Pull Requests

## ข้อมูลติดต่อ
- ผู้พัฒนา: [Apirak Ketkeaw]
- GitHub: [https://github.com/arthoho666/ASR_DEMO]
- อีเมล: [apirak.ketkaew.art@gmail.com]

