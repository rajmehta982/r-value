import numpy as np
import pandas as pd


initial_asset_class_weights = {
    'Equity': 0.4,         # 40% allocation to Equity
    'Cryptocurrency': 0.1, # 10% allocation to Cryptocurrency
    'Gold': 0.15,          # 15% allocation to Gold
    'Bonds': 0.25,         # 25% allocation to Bonds
}

def allocate_asset_level(initial_asset_class_weights, initial_weights):
    """
    Allocate weights at the asset level based on initial weights.
    """
    asset_weights = {}
    for asset in asset_classes.keys():
        # Get the weight for each top-level asset class
        asset_weight = initial_weights.get(asset, 0)
        asset_weights[asset] = asset_weight
    return asset_weights



