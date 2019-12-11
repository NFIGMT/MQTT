[
    {
        "id": "a10e675d.a4ec78",
        "type": "tab",
        "label": "MQTT Flow 2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "5bb1fab4.d53a74",
        "type": "mqtt in",
        "z": "a10e675d.a4ec78",
        "name": "",
        "topic": "mcs/DB0kLp45/3Ut1MudzASdC4L7L/+",
        "qos": "2",
        "datatype": "auto",
        "broker": "8db3ffaf.856e6",
        "x": 210,
        "y": 140,
        "wires": [
            [
                "bca3a35d.f331d"
            ]
        ]
    },
    {
        "id": "8bfbd339.36434",
        "type": "change",
        "z": "a10e675d.a4ec78",
        "name": "Get Data",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "payload.Data",
                "tot": "msg"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 220,
        "y": 300,
        "wires": [
            [
                "a3f0f015.9fa7a"
            ]
        ]
    },
    {
        "id": "4151740b.3dfacc",
        "type": "function",
        "z": "a10e675d.a4ec78",
        "name": "",
        "func": "\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 150,
        "y": 460,
        "wires": [
            []
        ]
    },
    {
        "id": "a3f0f015.9fa7a",
        "type": "ui_gauge",
        "z": "a10e675d.a4ec78",
        "name": "",
        "group": "89538d6f.a5d01",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "gauge",
        "label": "units",
        "format": "{{value}}",
        "min": 0,
        "max": "50",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "x": 280,
        "y": 380,
        "wires": []
    },
    {
        "id": "bca3a35d.f331d",
        "type": "csv",
        "z": "a10e675d.a4ec78",
        "name": "",
        "sep": ",",
        "hdrin": "",
        "hdrout": "",
        "multi": "one",
        "ret": "\\n",
        "temp": ",,Data",
        "skip": "0",
        "strings": true,
        "x": 230,
        "y": 220,
        "wires": [
            [
                "8bfbd339.36434"
            ]
        ]
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
    },
    {
        "id": "89538d6f.a5d01",
        "type": "ui_group",
        "z": "",
        "name": "Status",
        "tab": "8af59f85.b51e3",
        "order": 1,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "8af59f85.b51e3",
        "type": "ui_tab",
        "z": "",
        "name": "Tab 1",
        "icon": "dashboard",
        "order": 1,
        "disabled": false,
        "hidden": false
    }
]
