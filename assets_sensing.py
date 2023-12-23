class AssetsSensing:
    def __init__(self):
        self.assets_location = {}
        self.supply_routes_checklist = []
        self.standard_operation_time = 0

    def update_assets_location(self, asset_id, location):
        self.assets_location[asset_id] = location

    def add_supply_route_checklist(self, route):
        self.supply_routes_checklist.append(route)

    def set_standard_operation_time(self, time):
        self.standard_operation_time = time
