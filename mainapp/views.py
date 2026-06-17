from django.shortcuts import render
from django.http import JsonResponse
import paho.mqtt.client as mqtt

# 填入你們 Pi 5 的 Mosquitto 設定
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "pi5/led"


def index(request):
    # 渲染首頁
    return render(request, 'mainapp/index.html')


def control_led(request):
    if request.method == "POST":
        status = request.POST.get('status', 'OFF').upper()  # 接收前端傳來的 ON 或 OFF

        # 透過 MQTT 發送指令
        try:
            client = mqtt.Client()
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            client.publish(MQTT_TOPIC, status)
            client.disconnect()
            return JsonResponse({"result": "success", "status": status})
        except Exception as e:
            return JsonResponse({"result": "error", "message": str(e)}, status=500)

    return JsonResponse({"result": "invalid_method"}, status=400)