
# Hubert Högl, 2022-02-08, <Hubert.Hoegl@t-online.de>

import os, time
import paho.mqtt.client as mqtt


# Application ID
co2_user = "co2ampeln@ttn"

# End Device IDs
co2_device_id1 = "eui-70b3d57ed004c034"
co2_device_id2 = "eui-70b3d57ed004c45b"

# Set environment variable TTN_API_KEY
co2_password = os.environ["TTN_API_KEY"]

co2_topic1 = "v3/{}/devices/{}/up".format(co2_user, co2_device_id1)
co2_topic2 = "v3/{}/devices/{}/up".format(co2_user, co2_device_id2)

clientname = "co2-ampel-client"

def on_connect(client, userdata, flags, rc):
    print("==== subscribing to", co2_topic1)
    client.subscribe(co2_topic1, qos=0)
    print("==== subscribing to", co2_topic2)
    client.subscribe(co2_topic2, qos=0)


def on_message(client, userdata, msg):
    print("\n++++ topic:", msg.topic)
    ps = msg.payload.decode('ascii')
    print(ps)


if __name__ == "__main__":
    client = mqtt.Client(clientname)
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(co2_user, co2_password)
    client.connect("eu1.cloud.thethings.network", port=1883)
    client.loop_start()   # event loop

    # end of main program would terminate event loop
    while True:
        time.sleep(10)

