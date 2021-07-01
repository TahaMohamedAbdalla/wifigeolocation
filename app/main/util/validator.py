from marshmallow import Schema, fields, validate

class AccessPoints(Schema):
    band = fields.Str()
    bssid = fields.Str(required=True )
    channel = fields.Str()
    frequency = fields.Int()
    rates = fields.Str( )
    rssi = fields.Int( )
    security = fields.Str( )
    ssid = fields.Str( )
    timestamp = fields.Decimal( )
    vendor = fields.Str( )
    width = fields.Str( )

class ScanDataValidator(Schema):
    apscan_data = fields.Nested(
        AccessPoints,
        many=True,
        
    )
