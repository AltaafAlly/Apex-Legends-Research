Here’s a **README format** for the **Playstyle Aggressiveness Score (PAS)** formula, which you can use in your research:

---

# Playstyle Aggressiveness Score (PAS)

## Overview

The **Playstyle Aggressiveness Score (PAS)** is a custom metric designed to measure the aggressiveness of players in *Apex Legends*, based on their in-game performance statistics. The PAS score evaluates how frequently a player engages in combat and deals damage relative to their success in winning matches. It accounts for both the number of kills and the total damage dealt by the player, adjusted by their win count to prevent skewing the score towards players who only focus on combat without translating it into victories.

## Formula

The **Playstyle Aggressiveness Score (PAS)** is calculated as follows:

PAS = α × (BR Kills / (BR Wins + 1)) + β × (BR Damage / (BR Wins + 1))


### Variables:
- **BR Kills**: The number of kills a player has secured in *Battle Royale* mode.
- **BR Wins**: The number of wins a player has in *Battle Royale* mode.
- **BR Damage**: The total damage a player has dealt in *Battle Royale* mode.

### Weights:
- **α**: Weight assigned to the kills per win ratio (default value = 1).
- **β**: Weight assigned to the damage per win ratio (default value = 1).

### Purpose of Weights:
- **α** and **β** can be adjusted based on the specific research focus. If you want to emphasize the importance of kills over damage, increase α. If damage dealt is considered more reflective of aggressiveness, increase  β. For most balanced cases, both weights can be set to 1.

## Explanation

- **Kills per Win**: This term reflects how often a player is securing kills relative to the number of games won. A higher ratio indicates that the player tends to be aggressive and successful in combat even if they do not win every match.
- **Damage per Win**: This term reflects how much damage a player deals relative to their win count, capturing their active participation in fights, regardless of securing kills. High damage suggests that the player engages more frequently in combat.
- **+1 in the denominator**: This is used to avoid division by zero in cases where players have no wins, ensuring that all players receive a valid score.

## Application

The **PAS** score helps in:
1. **Identifying Aggressive Players**: Players with high scores are those who frequently engage in combat, either by securing kills or dealing significant damage, even if they don’t always secure wins.
2. **Comparing Legends**: This score can be applied across different Legends to evaluate how each Legend facilitates aggressive playstyles based on player performance.
3. **Tracking Playstyle Trends**: It enables researchers to analyze and categorize players based on their in-game behavior, distinguishing between aggressive and passive strategies.
