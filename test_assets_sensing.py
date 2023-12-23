from assets_sensing import AssetsSensing
import pytest

@pytest.fixture
def assets_sensing_instance():
    return AssetsSensing()

def test_update_assets_location(assets_sensing_instance):
    assets_sensing_instance.update_assets_location('asset1', 'location1')
    assert assets_sensing_instance.assets_location['asset1'] == 'location1'

def test_add_supply_route_checklist(assets_sensing_instance):
    assets_sensing_instance.add_supply_route_checklist('route1')
    assert 'route1' in assets_sensing_instance.supply_routes_checklist

def test_set_standard_operation_time(assets_sensing_instance):
    assets_sensing_instance.set_standard_operation_time(10)
    assert assets_sensing_instance.standard_operation_time == 10
