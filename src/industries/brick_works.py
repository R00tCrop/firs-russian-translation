"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='brick_works',
                    processed_cargos_and_output_ratios=[('COAL', 2), ('SAND', 2), ('CLAY', 4)],
                    combined_cargos_boost_prod=True,
                    prod_cargo_types=['BDMT'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    map_colour='184',
                    spec_flags='bitmask(IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE)',
                    name='string(STR_IND_BRICK_WORKS)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MILL))',
                    fund_cost_multiplier='120')

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='brick_works_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_control={'macro':'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'brick_works_spriteset_ground',
    type='cobble',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'brick_works_spriteset_ground_overlay',
    type='empty',
)

spriteset_1 = industry.add_spriteset(
    id = 'brick_works_spriteset_1',
    sprites = [(10, 10, 64, 101, -31, -64)],
)
spriteset_2 = industry.add_spriteset(
    id = 'brick_works_spriteset_2',
    sprites = [(80, 10, 64, 101, -31, -59)],
)
spriteset_3 = industry.add_spriteset(
    id = 'brick_works_spriteset_3',
    sprites = [(150, 10, 64, 101, -31, -71)],
)
spriteset_4 = industry.add_spriteset(
    id = 'brick_works_spriteset_4',
    sprites = [(220, 10, 64, 101, -31, -69)],
)
spriteset_sand_staithe = industry.add_spriteset(
    id = 'brick_works_spriteset_sand_staithe',
    sprites = [(290, 10, 64, 31, -31, 0)],
)
spriteset_clay_staithe = industry.add_spriteset(
    id = 'brick_works_spriteset_clay_staithe',
    sprites = [(360, 10, 64, 31, -31, 0)],
)
sprite_smoke_boilerhouse = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 8,
    yoffset= 0,
    zoffset= 70,
)
sprite_smoke_kiln = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 0,
    yoffset= 8,
    zoffset= 58,
)

industry.add_spritelayout(
    id = 'brick_works_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    smoke_sprites = [sprite_smoke_boilerhouse],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'brick_works_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'brick_works_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    smoke_sprites = [sprite_smoke_kiln],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'brick_works_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'brick_works_spritelayout_sand_staithe',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_sand_staithe],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'brick_works_spritelayout_clay_staithe',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_clay_staithe],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'brick_works_industry_layout_1',
    layout = [(0, 0, 'brick_works_tile_1', 'brick_works_spritelayout_4'),
              (0, 1, 'brick_works_tile_1', 'brick_works_spritelayout_4'),
              (1, 0, 'brick_works_tile_1', 'brick_works_spritelayout_3'),
              (1, 1, 'brick_works_tile_1', 'brick_works_spritelayout_3'),
              (2, 0, 'brick_works_tile_1', 'brick_works_spritelayout_2'),
              (2, 1, 'brick_works_tile_1', 'brick_works_spritelayout_1'),
              (3, 0, 'brick_works_tile_1', 'brick_works_spritelayout_clay_staithe'),
              (3, 1, 'brick_works_tile_1', 'brick_works_spritelayout_sand_staithe'),
    ]
)
industry.add_industry_layout(
    id = 'brick_works_industry_layout_2',
    layout = [(0, 0, 'brick_works_tile_1', 'brick_works_spritelayout_4'),
              (0, 1, 'brick_works_tile_1', 'brick_works_spritelayout_4'),
              (1, 0, 'brick_works_tile_1', 'brick_works_spritelayout_3'),
              (1, 1, 'brick_works_tile_1', 'brick_works_spritelayout_3'),
              (2, 0, 'brick_works_tile_1', 'brick_works_spritelayout_2'),
              (2, 1, 'brick_works_tile_1', 'brick_works_spritelayout_clay_staithe'),
              (3, 0, 'brick_works_tile_1', 'brick_works_spritelayout_1'),
              (3, 1, 'brick_works_tile_1', 'brick_works_spritelayout_sand_staithe'),
    ]
)
industry.add_industry_layout(
    id = 'brick_works_industry_layout_3',
    layout = [(0, 0, 'brick_works_tile_1', 'brick_works_spritelayout_4'),
              (0, 1, 'brick_works_tile_1', 'brick_works_spritelayout_4'),
              (0, 2, 'brick_works_tile_1', 'brick_works_spritelayout_1'),
              (0, 3, 'brick_works_tile_1', 'brick_works_spritelayout_clay_staithe'),
              (1, 0, 'brick_works_tile_1', 'brick_works_spritelayout_3'),
              (1, 1, 'brick_works_tile_1', 'brick_works_spritelayout_3'),
              (1, 2, 'brick_works_tile_1', 'brick_works_spritelayout_2'),
              (1, 3, 'brick_works_tile_1', 'brick_works_spritelayout_sand_staithe'),
    ]
)
