# sssnakeevader 🐍
> "Evade the snakes like the happy dog you are!" – _Dog van de bark 2024_

A small fun project to try out the pygame engine and learn about software design patterns.

A **playable prototype** based on an older code base is available at itch.io:
- https://man00ka.itch.io/sssnake-evader
- Via python WASM using [pygbag](https://pypi.org/project/pygbag/)


## Dependencies
- numpy==2.0.0
- pygame==2.5.2
- pygame_ce==2.4.1
- pygame_menu==4.4.3  # Will probably resort to custom menus later 
- pyglet==1.5.27  # For future audio stuff. Might be replaced by fmod :-)

## Short-term todos
- Fix difficulty management (more snakes, faster pace)
- Hitboxes and collision detection
- Death screen

## Mid-term todos
- Attack + enemy damage
- HUD / health bar
- Powerups
- Music + SFX (fmod integration)

## Long-term todos
- Different levels

## Attributions
### Assets
  - Characters: [32rogues](https://sethbb.itch.io/32rogues) by _Seth_
  - Background tiles: [Pixel ground package](https://arexxuru.itch.io/pixel-floor-texture-pack-ground-tile) by _GNDLF the Maker_ 
  - Other: https://miguelnero.itch.io/hearth
