ollama镜像启动

~~~
docker run -d --gpus=all -v F:/.ollama:/root/.ollama -p 11434:11434 -e OLLAMA_NUM_PARALLEL=20 -e OLLAMA_MAX_LOADED_MODELS=20 --name ollama ollama/ollama
~~~



~~~
docker run -d --gpus=all -v F:/.ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
~~~





运行容器，模型

~~~
docker exec -it ollama ollama run qwen2
~~~

