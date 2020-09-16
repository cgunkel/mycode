#!/usr/bin/env python3
# List of farms
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
		 
# Loop across the farms listing the animals
for farm in farms:
    print(f"The {farm['name']} raises {', '.join(farm['agriculture'])}.")
    for animal in farm['agriculture']:
        print(animal)
        # animal=="sheep"
