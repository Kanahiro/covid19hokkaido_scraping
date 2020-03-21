SCHEMAS = {
    "patients": {
        "type": "object",
        "required": [
            "data",
            "last_update"
        ],
        "properties": {
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "リリース日",
                        "居住地",
                        "年代",
                        "性別"
                    ],
                    "properties": {
                        "リリース日": {
                            "type": "string",
                            "default": ""
                        },
                        "居住地": {
                            "type": "string",
                            "default": ""
                        },
                        "年代": {
                            "type": "string",
                            "default": ""
                        },
                        "性別": {
                            "type": "string",
                            "default": ""
                        }
                    }
                }
            },
            "last_update": {
                "type": "string",
                "default": ""
            }
        }
    },
    "contacts": {
        "type": "object",
        "required": [
            "data",
            "last_update"
        ],
        "properties": {
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "日付",
                        "小計"
                    ],
                    "properties": {
                        "日付": {
                            "type": "string",
                            "default": ""
                        },
                        "小計": {
                            "type": "integer",
                            "default": 0
                        }
                    }
                }
            },
            "last_update": {
                "type": "string",
                "default": ""
            }
        }
    },
    "querents": {
        "type": "object",
        "required": [
            "data",
            "last_update"
        ],
        "properties": {
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "日付",
                        "小計"
                    ],
                    "properties": {
                        "日付": {
                            "type": "string",
                            "default": ""
                        },
                        "小計": {
                            "type": "integer",
                            "default": 0
                        }
                    }
                }
            },
            "last_update": {
                "type": "string",
                "default": ""
            }
        }
    },
    "current_patients": {
        "type": "object",
        "required": [
            "data",
            "last_update"
        ],
        "properties": {
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "日付",
                        "患者数"
                    ],
                    "properties": {
                        "日付": {
                            "type": "string",
                            "default": ""
                        },
                        "患者数": {
                            "type": "integer",
                            "default": 0
                        }
                    }
                }
            },
            "last_update": {
                "type": "string",
                "default": ""
            }
        }
    },
    "discharges_summary": {
        "type": "object",
        "required": [
            "data",
            "last_update"
        ],
        "properties": {
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "日付",
                        "日治療終了数"
                    ],
                    "properties": {
                        "日付": {
                            "type": "string",
                            "default": ""
                        },
                        "日治療終了数": {
                            "type": "integer",
                            "default": 0
                        }
                    }
                }
            },
            "last_update": {
                "type": "string",
                "default": ""
            }
        }
    },
    "inspections": {
        "type": "object",
        "required": [
            "data",
            "last_update"
        ],
        "properties": {
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "日付",
                        "日検査数"
                    ],
                    "properties": {
                        "日付": {
                            "type": "string",
                            "default": ""
                        },
                        "日検査数": {
                            "type": "integer",
                            "default": 0
                        }
                    }
                }
            },
            "last_update": {
                "type": "string",
                "default": ""
            }
        }
    },
    "patients_summary": {
        "type": "object",
        "required": [
            "data",
            "last_update"
        ],
        "properties": {
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "日付",
                        "日陽性数"
                    ],
                    "properties": {
                        "日付": {
                            "type": "string",
                            "default": ""
                        },
                        "日陽性数": {
                            "type": "integer",
                            "default": 0
                        }
                    }
                }
            },
            "last_update": {
                "type": "string",
                "default": ""
            }
        }
    },
    "last_update":{
                "type": "string",
                "default": ""
    },
    "main_summary":{
        "type": "object",
        "required": [
            "検査人数",
            "陽性者数",
            "患者数",
            "軽症・中等症者数",
            "重傷者数",
            "死亡者数",
            "陰性確認数"
        ],
        "properties": {
            "検査人数": {
                "type": "integer",
                "default": 0
            },
            "陽性者数": {
                "type": "integer",
                "default": 0
            },
            "患者数": {
                "type": "integer",
                "default": 0
            },
            "軽症・中等症者数": {
                "type": "integer",
                "default": 0
            },
            "重傷者数": {
                "type": "integer",
                "default": 0
            },
            "死亡者数": {
                "type": "integer",
                "default": 0
            },
            "陰性確認数": {
                "type": "integer",
                "default": 0
            }
        }
    }
}