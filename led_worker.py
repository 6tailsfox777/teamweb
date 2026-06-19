import time
import paho.mqtt.client as mqtt
import gpiod  # 樹莓派 5 專用

LED_PIN = 17 
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
led_line.request(consumer="LED_Control", type=gpiod.LINE_REQ_DIR_OUT)

# 💡 這裡記得對齊 Django 的設定
MQTT_BROKER = "broker.emqx.io"  
MQTT_PORT = 1883
MQTT_TOPIC = "pi5/led"

def on_message(client, userdata, msg):
    command = msg.payload.decode('utf-8')
    print(f"收到控制指令: {command}")
    if command == "ON":
        led_line.set_value(1)
        print("💡 實體 LED 已開啟")
    elif command == "OFF":
        led_line.set_value(0)
        print("💤 實體 LED 已關閉")

# 💡 這裡也一樣要加上 VERSION2 宣告喔！
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

print("正在連線至 EMQX Broker...")
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)

print("Pi 5 LED 控制後台已啟動...")
client.loop_forever()