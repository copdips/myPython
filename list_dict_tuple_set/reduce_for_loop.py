import itertools

nested_dict = {
    "emea": {
        "dev": {"fr": "parisdev", "uk": "londondev"},
        "prd": {"fr": "parisprd", "uk": "londonprd"},
    },
    "apac": {
        "dev": {"cn": "beijingdev", "jp": "tokyodev"},
        "prd": {"cn": "beijingprd", "jp": "tokyoprd"},
    },
    "amer": {
        "dev": {"us": "washingtondev", "br": "riodev"},
        "prd": {"us": "washingtonprd", "br": "rioprd"},
    },
}


def worst_loop_on_nested_object():
    print("\nWorst loop:")
    for region, envs in nested_dict.items():
        for env, countries in envs.items():
            for country, capital in countries.items():
                print(f"   {region}-{env}-{country}-{capital}")


def better_loop_on_nested_object():
    print("\nBetter loop:")
    [
        print(f"   {region}-{env}-{country}-{capital}")
        for region, envs in nested_dict.items()
        for env, countries in envs.items()
        for country, capital in countries.items()
    ]


if __name__ == "__main__":
    worst_loop_on_nested_object()
    better_loop_on_nested_object()
