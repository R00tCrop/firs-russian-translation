from firs import Cargo

cargo = Cargo(id = 'scrap_metal',
              number = '20',
              type_name = 'string(STR_CARGO_NAME_SCRAP_METAL)',
              unit_name = 'string(STR_CARGO_NAME_SCRAP_METAL)',
              type_abbreviation = 'string(STR_CID_SCRAP_METAL)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '106',
              cargo_payment_list_colour = '106',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_BULK, CC_NON_POURABLE)',
              cargo_label = '"SCMT"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '80',
              items_of_cargo = 'string(STR_CARGO_UNIT_SCRAP_METAL)',
              penalty_lowerbound = '30',
              single_penalty_length = '255',
              capacity_multiplier = '1',
              price_factor = '126.846313477')

cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
