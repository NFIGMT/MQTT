[
    {
        "id": "442e4e09.540b9",
        "type": "tab",
        "label": "MQTT Flow 1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "cd13687b.d63f98",
        "type": "inject",
        "z": "442e4e09.540b9",
        "name": ",,25.5",
        "topic": "",
        "payload": ",,25.5",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 90,
        "y": 160,
        "wires": [
            [
                "82e345e5.9c7ca8"
            ]
        ]
    },
    {
        "id": "7fa4b757.7fe788",
        "type": "inject",
        "z": "442e4e09.540b9",
        "name": ",,30.3",
        "topic": "",
        "payload": ",,30.3",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 90,
        "y": 240,
        "wires": [
            [
                "82e345e5.9c7ca8"
            ]
        ]
    },
    {
        "id": "82e345e5.9c7ca8",
        "type": "mqtt out",
        "z": "442e4e09.540b9",
        "name": "",
        "topic": "mcs/DB0kLp45/3Ut1MudzASdC4L7L/Temperature",
        "qos": "2",
        "retain": "",
        "broker": "8db3ffaf.856e6",
        "x": 590,
        "y": 200,
        "wires": []
    },
    {
        "id": "8db3ffaf.856e6",
        "type": "mqtt-broker",
        "z": "",
        "name": "MCS Cloud",
        "broker": "mqtt.mcs.mediatek.com",
        "port": "1883",
        "clientid": "",
        "usetls": false,
        "compatmode": false,
        "keepalive": "60",
        "cleansession": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "willTopic": "",
        "willQos": "0",
        "willPayload": ""
    }
]
