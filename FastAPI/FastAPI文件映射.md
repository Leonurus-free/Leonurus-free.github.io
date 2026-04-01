# FastAPI文件映射

```
# 将静态文件目录挂载到 /static 路径
app.mount("/static", StaticFiles(directory="/home/audio_transcription"), name="static")
```
