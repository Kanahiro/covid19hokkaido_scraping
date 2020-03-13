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
                        "No",
                        "リリース日",
                        "曜日",
                        "居住地",
                        "年代",
                        "性別",
                        "属性",
                        "備考",
                        "補足",
                        "退院",
                        "周囲の状況",
                        "濃厚接触者の状況"
                    ],
                    "properties": {
                        "No": {
                            "type": "string",
                            "default": ""
                        },
                        "リリース日": {
                            "type": "string",
                            "default": ""
                        },
                        "曜日": {
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
                        },
                        "属性": {
                            "type": "string",
                            "default": ""
                        },
                        "備考": {
                            "type": "string",
                            "default": ""
                        },
                        "補足": {
                            "type": "string",
                            "default": ""
                        },
                        "退院": {
                            "type": "string",
                            "default": ""
                        },
                        "周囲の状況": {
                            "type": "string",
                            "default": ""
                        },
                        "濃厚接触者の状況": {
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
            }
}