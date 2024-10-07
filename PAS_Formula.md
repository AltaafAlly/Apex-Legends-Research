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


The **Playstyle Aggressiveness Score (PAS)** is a metric that aims to quantify how aggressive a player or legend is based on their in-game statistics, specifically focusing on **kills**, **damage**, and **wins**. The score is intended to reflect how actively a player engages in combat, prioritizing damage and eliminations over passive gameplay.

### **Initial PAS Formula**:
The original formula for **PAS** is defined as follows:

PAS = α × (BR Kills / (BR Wins + 1)) + β × (BR Damage / (BR Wins + 1))

#### **Rationale for the Original PAS Formula**:
- **BR Kills** and **BR Damage** are indicators of a player's engagement in combat:
  - High **BR Kills** indicates frequent elimination of opponents.
  - High **BR Damage** indicates that a player consistently inflicts damage during matches.
- **BR Wins** is included in the denominator to normalize the aggression relative to success:
  - The **+1** prevents division by zero when **BR Wins** is zero.
  - A higher **BR Wins** count means the aggression (kills and damage) is spread across more successful matches, which should theoretically result in a lower **PAS** value.

#### **Challenges with the Original PAS Formula**:
- **Impact of High Win Counts**: Legends with high win counts (like Skirmishers) tend to have their kills and damage "diluted" due to being divided by a large number (**BR Wins + 1**). As a result:
  - Even if these legends have high kills and damage, their **PAS** could be lower than that of legends with fewer wins.
  - This might give an inaccurate representation of their aggressive playstyle, as it prioritizes win consistency over pure aggression in combat.

### **Modified PAS Formula**:
To address this, we introduced a modified formula:

PAS =  (BR Kills / (BR Wins + 1)) * 0.5 +  (BR Damage / (BR Wins + 1)) * 0.5

#### **Rationale for the Modified PAS Formula**:
- **Square Root Adjustment**: By taking the square root of **BR Wins + 1**, we reduce the impact that high win counts have on the PAS score:
  - The square root function grows more slowly compared to a linear relationship, meaning that higher values of **BR Wins** do not lower the **PAS** as drastically.
  - This adjustment allows the **BR Kills** and **BR Damage** to retain more influence over the score even when **BR Wins** is high.
- **Better Balance Between Aggression and Wins**:
  - The formula still takes into account **BR Wins** to ensure that players with a history of winning aren't unfairly given high **PAS** values.
  - However, it gives more weight to aggressive play (high kills and damage), offering a more balanced measure of aggression across different legend types.


**Playstyle Aggressiveness Score (PAS) Calculation**:
To quantify player aggressiveness, we developed the Playstyle Aggressiveness Score (**PAS**), which takes into account a player's **BR Kills** and **BR Damage**, normalized by their **BR Wins** to balance aggressive actions against match success. Initially, the PAS was calculated as:

PAS = α × (BR Kills / (BR Wins + 1)) + β × (BR Damage / (BR Wins + 1))

This formulation ensures that kills and damage are contextualized against the player's success in winning matches. However, we observed that this approach overly penalizes players with high win counts, such as Skirmishers, by reducing their PAS despite high engagement in combat.

To address this, we introduced a modified version of the score, **PAS_Modified**:

PAS = (BR Kills / (BR Wins + 1)) * 0.5 +  (BR Damage / (BR Wins + 1)) * 0.5

The square root adjustment reduces the impact of **BR Wins**, allowing **BR Kills** and **BR Damage** to play a more significant role in determining PAS. This adjustment provided a more balanced measure of playstyle aggressiveness, particularly for players with high win counts who also exhibit high combat engagement.

**Justification for PAS_Modified**:
The calculation of **PAS** initially involved normalizing **BR Kills** and **BR Damage** by **BR Wins** to contextualize aggressive actions relative to match outcomes. However, this approach overly penalized legends with high win counts. To address this, we applied a square root transformation to **BR Wins**, creating the **PAS_Modified** metric:

PAS = (BR Kills / (BR Wins + 1)) * 0.5 +  (BR Damage / (BR Wins + 1)) * 0.5

Square root transformations are a common method in statistical analysis to manage non-linear relationships and reduce the influence of extreme values (Draper & Smith, 1998; Ott & Longnecker, 2010). By applying this adjustment, we reduced the disproportionate impact of high win counts, allowing for a more balanced measure of aggressiveness across different legend types.

---
