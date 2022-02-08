# ttn3mqtt

Demo MQTT Client for The Things Network v3 MQTT integration.

Tested with BNDLG CO2 Ampeln (2x).

To run the program ...

* Install Paho-MQTT Python package (https://pypi.org/project/paho-mqtt)
e.g. with  "pip install paho-mqtt"

* Set environment variable `TTN_API_KEY`. On Linux run `. env.sh`.

* Run program `python client.py`. The output looks like

```json
(base) hhoegl@msi:~/GITHUB/ttn3mqtt$ python client.py 
==== subscribing to v3/co2ampeln@ttn/devices/eui-70b3d57ed004c034/up
==== subscribing to v3/co2ampeln@ttn/devices/eui-70b3d57ed004c45b/up

++++ topic: v3/co2ampeln@ttn/devices/eui-70b3d57ed004c034/up
{"end_device_ids":{"device_id":"eui-70b3d57ed004c034","application_ids":{"application_id":"co2ampeln"},"dev_eui":"70B3D57ED004C034","join_eui":"0000000000000000","dev_addr":"260B43E4"},"correlation_ids":["as:up:01FVD5WFH60HJMZNW83ZDTMH21","gs:conn:01FVAVYMZNHTENMK7ZGYMNV066","gs:up:host:01FVAVYN03J5HDJYK7HA2GW0DY","gs:uplink:01FVD5WFANCKC2VZ6CRKEJ4A9F","ns:uplink:01FVD5WFAPNK6W7APDS7DEV1X5","rpc:/ttn.lorawan.v3.GsNs/HandleUplink:01FVD5WFAPV1EYKQ9KJDCSXR9S","rpc:/ttn.lorawan.v3.NsAs/HandleUplink:01FVD5WFH5W2PKSJ13SZRCANMM"],"received_at":"2022-02-08T17:25:16.454557278Z","uplink_message":{"session_key_id":"AX7I8yDX39zoVcSjED6BXg==","f_port":1,"f_cnt":4183,"frm_payload":"IY1G","decoded_payload":{"co2":660,"rh":35,"temp":18.2},"rx_metadata":[{"gateway_ids":{"gateway_id":"eui-58a0cbfffe80130d","eui":"58A0CBFFFE80130D"},"time":"2022-02-08T17:25:16.194729089Z","timestamp":212584339,"rssi":-69,"channel_rssi":-69,"snr":9.5,"location":{"latitude":48.514239620106515,"longitude":10.616698265075684,"altitude":456,"source":"SOURCE_REGISTRY"},"uplink_token":"CiIKIAoUZXVpLTU4YTBjYmZmZmU4MDEzMGQSCFigy//+gBMNEJOPr2UaCwj8zoqQBhCxhO90ILisjviX0BEqCwj8zoqQBhCBqe1c"}],"settings":{"data_rate":{"lora":{"bandwidth":125000,"spreading_factor":7}},"coding_rate":"4/5","frequency":"867100000","timestamp":212584339,"time":"2022-02-08T17:25:16.194729089Z"},"received_at":"2022-02-08T17:25:16.246900690Z","consumed_airtime":"0.051456s","version_ids":{"brand_id":"heltec","model_id":"wifi-lora-32-class-a-otaa","hardware_version":"_unknown_hw_version_","firmware_version":"1.0","band_id":"EU_863_870"},"network_ids":{"net_id":"000013","tenant_id":"ttn","cluster_id":"ttn-eu1"}}}

++++ topic: v3/co2ampeln@ttn/devices/eui-70b3d57ed004c45b/up
{"end_device_ids":{"device_id":"eui-70b3d57ed004c45b","application_ids":{"application_id":"co2ampeln"},"dev_eui":"70B3D57ED004C45B","join_eui":"0000000000000000","dev_addr":"260B0FA3"},"correlation_ids":["as:up:01FVD5WWC2M3683BMHRNXYSAZ4","gs:conn:01FVAVYMZNHTENMK7ZGYMNV066","gs:up:host:01FVAVYN03J5HDJYK7HA2GW0DY","gs:uplink:01FVD5WW4R6D1DMD4FMG2B09ZJ","ns:uplink:01FVD5WW4S86QY8QR6GB5MQTZG","rpc:/ttn.lorawan.v3.GsNs/HandleUplink:01FVD5WW4S2FTK4SEKQ7KVP07H","rpc:/ttn.lorawan.v3.NsAs/HandleUplink:01FVD5WWC1CE62Q446YP4Z42A4"],"received_at":"2022-02-08T17:25:29.602885753Z","uplink_message":{"session_key_id":"AX7OdKDYE59H2Yg9TEyZPQ==","f_port":1,"f_cnt":3229,"frm_payload":"IJJD","decoded_payload":{"co2":640,"rh":33.5,"temp":19.2},"rx_metadata":[{"gateway_ids":{"gateway_id":"eui-58a0cbfffe80130d","eui":"58A0CBFFFE80130D"},"time":"2022-02-08T17:25:29.317506074Z","timestamp":225713940,"rssi":-75,"channel_rssi":-75,"snr":9.25,"location":{"latitude":48.514239620106515,"longitude":10.616698265075684,"altitude":456,"source":"SOURCE_REGISTRY"},"uplink_token":"CiIKIAoUZXVpLTU4YTBjYmZmZmU4MDEzMGQSCFigy//+gBMNEJS+0GsaDAiJz4qQBhCRvqyvASCgzOXsyNARKgwIic+KkAYQmoSzlwE="}],"settings":{"data_rate":{"lora":{"bandwidth":125000,"spreading_factor":7}},"coding_rate":"4/5","frequency":"867900000","timestamp":225713940,"time":"2022-02-08T17:25:29.317506074Z"},"received_at":"2022-02-08T17:25:29.369338658Z","consumed_airtime":"0.051456s","version_ids":{"brand_id":"heltec","model_id":"wifi-lora-32-class-a-otaa","hardware_version":"_unknown_hw_version_","firmware_version":"1.0","band_id":"EU_863_870"},"network_ids":{"net_id":"000013","tenant_id":"ttn","cluster_id":"ttn-eu1"}}}

...
```

Hubert.Hoegl@t-online.de, Feb. 2022
