<!-- 
### **Current Progress**

1. **Data Collection:**

   - **Player Statistics:**
     - Gathered data for **900 top players** from each platform (PC, PlayStation, and Xbox), totaling **2,700 players**.
     - Collected overall **career stats**: kills, revives, and wins.
   - **Legend Statistics:**
     - Acquired stats for the different Legends used by each player.
     - Categorized Legends into five classes:
       - **Assault**: Bangalore, Fuse, Ash, Mad Maggie, Ballistic
       - **Skirmisher**: Pathfinder, Wraith, Octane, Revenant, Horizon, Valkyrie, Alter
       - **Recon**: Bloodhound, Crypto, Seer, Vantage
       - **Support**: Gibraltar, Lifeline, Mirage, Loba, Newcastle, Conduit
       - **Controller**: Caustic, Wattson, Rampart, Catalyst
   - **Data Sources:**
     - Used public leaderboards for accessible usernames.
     - Employed a third-party API to obtain player stats.
     - Scraped UIDs to retrieve stats via the API.

2. **Data Imputation:**

   - **Objective:**
     - Addressed missing values in player stats to improve data quality for analysis.
   - **Methodology:**
     - Implemented **Multiple Imputation by Chained Equations (MICE)** to fill in missing data.
     - Tested various models to determine the best dataset, focusing on improving data correlation rather than solely on model accuracy.
   - **Results:**
     - Achieved stronger correlations between key variables:
       - **Career Kills and Wins**: Correlation coefficient of **0.80**.
       - **Career Wins and Revives**: Correlation coefficient of **0.72**.
       - **Career Kills and Revives**: Correlation coefficient of **0.64**.
   - **Interpretation:**
     - The improved correlations suggest that the imputed data is coherent and suitable for further analysis.

3. **Legend Stats Handling:**

   - **Decision:**
     - Chose **not to perform data imputation** on the Legend stats dataset.
   - **Reasoning:**
     - Zero values in Legend stats represent Legends not used by players.
     - Treating zeros as missing values maintains the integrity of the data, avoiding false representation of player activity.
     - Visualized Legend stats now need to interpret them.
     - Explain each legend abilities.
     - Explain why these legends are the most picked with repect to their abilities.

---

### **Focus Areas for Next Steps**

1. **Finalize Data Preparation:**

   - **Data Cleaning:**
     - Ensure all datasets are clean, consistent, and ready for analysis.
     - Document any assumptions made during data preparation.
   - **Data Validation:**
     - Verify the accuracy of imputed data through additional correlation checks or by comparing with known benchmarks.

2. **Begin Statistical Analysis:**

   - **Hypothesis Testing:**
     - For **Research Question 1**:
       - Analyze how Legend abilities impact player aggressiveness and success rate.
       - Use ANOVA tests to determine differences between Legend categories.
     - For **Research Question 2**:
       - Examine the relationship between high kill counts and win rates using correlation and regression analyses.
   - **Cluster Analysis:**
     - Identify player archetypes based on performance metrics.

3. **Incorporate Weapon Usage Data:**

   - **Data Collection:**
     - Gather data on the most commonly used weapons from reliable sources.
   - **Analysis Integration:**
     - Investigate how weapon choice correlates with aggressiveness and win rates.
     - Consider whether certain weapons are preferred by more successful or aggressive players.

4. **Platform Performance Comparison:**

   - **Data Analysis:**
     - Compare key performance metrics across PC, PlayStation, and Xbox platforms.
     - Use statistical tests to identify significant differences.
   - **Interpretation:**
     - Explore possible reasons for performance variations, such as control interfaces or player demographics.

5. **Prepare for Limitations Discussion:**

   - **Data Imputation Implications:**
     - Discuss the impact of data imputation on your analysis.
     - Explain any potential biases or distortions introduced.
   - **Representation and Generalizability:**
     - Address how focusing on top players may affect the applicability of your conclusions to the broader player population.

--- -->

# Apex Legends Data Analysis Checklist

## 1. **Data Collection**

### 1.1 **Player Statistics**
- [x] Gathered data for **900 top players** from each platform (PC, PlayStation, and Xbox), totaling **2,700 players**.
- [x] Collected overall **career stats**: kills, revives, and wins.

### 1.2 **Legend Statistics**
- [x] Acquired stats for the different Legends used by each player.
- [x] Categorized Legends into five classes:
  - **Assault**: Bangalore, Fuse, Ash, Mad Maggie, Ballistic
  - **Skirmisher**: Pathfinder, Wraith, Octane, Revenant, Horizon, Valkyrie, Alter
  - **Recon**: Bloodhound, Crypto, Seer, Vantage
  - **Support**: Gibraltar, Lifeline, Mirage, Loba, Newcastle, Conduit
  - **Controller**: Caustic, Wattson, Rampart, Catalyst

### 1.3 **Data Sources**
- [x] Used public leaderboards for accessible usernames.
- [x] Employed a third-party API to obtain player stats.
- [x] Scraped UIDs to retrieve stats via the API.

---

## 2. **Data Visualization**
- [x] Created bar graphs to visualize trends.
- [ ] Interpret the data from the bar graphs for both career stats and legend stats.
- [ ] Conduct further data analysis to support or refute the hypothesis.

---
# ANALYSIS ANALYSIS ANALYSIS WE NEED TO DO ANALYSIS

## 3. **Additional Data Needed**
- [ ] Gather data on weapons to analyze which weapons players use most frequently.
- [ ] Analyze different maps to determine popular drop locations.
- [ ] Check survival rates in high-population areas to see if they impact player success.
- [ ] Investigate aggressive player tendencies related to landing in populated areas for more kills.
- [ ] PLEASE ADDRESS LIMITATIONS WHETHER IT BE WITH THE DATA OR WHATEVER ADDRESS IT they include:
  - [ ] Data Limitations:
  - No Games Played Data: Without total games played, win rates are estimations.
  - Sample Bias: Data from top players may not reflect the general player base.
  - [ ] External Factors:
  - Meta Changes: Game updates can affect Legend effectiveness.
  - Team Dynamics: Performance may depend on team composition and coordination


Since the *time alive* data is unavailable, we can adjust our approach to measuring aggressiveness. Instead, we will focus on the data we do have—*kills*, *damage dealt*, and *wins*—and create a revised formula to capture the essence of aggressiveness based on combat performance alone. Here's a possible approach:

### Revised Playstyle Aggressiveness Score (PAS)
We can define aggressiveness based on two key combat indicators:
1. **BR Kills**: Players with more kills are likely to engage in combat more frequently.
2. **BR Damage**: Higher damage numbers suggest more active combat participation, regardless of the kills secured.

To capture both aspects, we can use a weighted formula like this:

\[
\text{PAS} = \alpha \times \left( \frac{\text{BR Kills}}{\text{BR Wins} + 1} \right) + \beta \times \left( \frac{\text{BR Damage}}{\text{BR Wins} + 1} \right)
\]

- **BR Kills** / **BR Wins** ratio: This shows how aggressive a player is relative to their wins, where a high number of kills per win is a marker of an aggressive playstyle.
- **BR Damage** / **BR Wins** ratio: This indicates how much damage a player is dealing relative to their wins, again emphasizing active combat engagement.
- The weights \( \alpha \) and \( \beta \) can be tuned depending on whether you want kills or damage to have a stronger influence on the score (you can set these both to 1 for simplicity).

Would you like to calculate this **Playstyle Aggressiveness Score (PAS)** using this formula for your data? If so, I can apply this across all the Legends and players in your datasets to see how different players and Legends rank in terms of aggressiveness.

To justify the components of the **Playstyle Aggressiveness Score (PAS)** and its relevance to measuring aggressiveness, I drew from several principles used in player performance evaluation, as seen in research on multiplayer games and battle royales. Here’s how each part of the formula connects to established literature:

### 1. **Kills as an Indicator of Aggression**
   - **Justification**: High kills are often associated with aggressive playstyles. Players who actively seek out and eliminate opponents are considered to be more aggressive than those who avoid combat.
   - **Supporting Literature**: Shim et al. (2011) link high kill rates to aggressive playstyles in multiplayer shooters【15†source】. Dehpanah et al. (2022) also emphasize kills as a key metric in competitive shooter games【15†source】.

### 2. **Damage as an Indicator of Combat Engagement**
   - **Justification**: Even if a player doesn’t always secure kills, dealing a high amount of damage shows frequent engagement in combat. High damage output suggests a player is actively contributing to fights, which is another mark of aggressive play.
   - **Supporting Literature**: Dehpanah et al. (2022) include damage dealt as a primary factor in assessing player aggression and engagement in battle royale games【15†source】. This metric is particularly emphasized in battle royales, where strategic play and engagement matter as much as outright kills.

### 3. **Adjusting for Wins**
   - **Justification**: Including wins in the denominator helps balance the formula, preventing players with a high number of kills or damage from being overly favored if they don’t win frequently. It’s a way to ensure that combat effectiveness (in the form of wins) is taken into account while still highlighting aggressiveness.
   - **Supporting Literature**: The ratio of kills or damage to wins has been used in previous research as a way to normalize aggressiveness relative to success, particularly in team-based games where pure combat metrics can sometimes overshadow strategic play【15†source】【15†source】.

### 4. **Combining Kills and Damage**
   - **Justification**: The combination of both kills and damage ensures that we account for the full spectrum of aggressive playstyles. Some players might consistently deal damage without always securing kills, while others might have lower damage but more kill efficiency. By combining both, we capture a broader view of aggression.
   - **Supporting Literature**: Visti et al. (2017) argue for using multiple metrics (such as kills and damage) to evaluate player performance comprehensively, noting that any single metric may overlook important aspects of a player’s style【15†source】.

This formula is an extension of these ideas, applying them specifically to the available stats in *Apex Legends*. If you'd like, I can proceed to implement this for your data and help identify which Legends and players are classified as more aggressive based on this model.


---

# Playstyle Aggressiveness Score (PAS)

## Overview

The **Playstyle Aggressiveness Score (PAS)** is a custom metric designed to measure the aggressiveness of players in *Apex Legends*, based on their in-game performance statistics. The PAS score evaluates how frequently a player engages in combat and deals damage relative to their success in winning matches. It accounts for both the number of kills and the total damage dealt by the player, adjusted by their win count to prevent skewing the score towards players who only focus on combat without translating it into victories.

## Formula

The **Playstyle Aggressiveness Score (PAS)** is calculated as follows:

\[
  \text{PAS} = \alpha \times \left( \frac{\text{BR Kills}}{\text{BR Wins} + 1} \right) + \beta \times \left( \frac{\text{BR Damage}}{\text{BR Wins} + 1} \right)
\]

### Variables:
- **BR Kills**: The number of kills a player has secured in *Battle Royale* mode.
- **BR Wins**: The number of wins a player has in *Battle Royale* mode.
- **BR Damage**: The total damage a player has dealt in *Battle Royale* mode.

### Weights:
- **\(\alpha\)**: Weight assigned to the kills per win ratio (default value = 1).
- **\(\beta\)**: Weight assigned to the damage per win ratio (default value = 1).

### Purpose of Weights:
- **\(\alpha\)** and **\(\beta\)** can be adjusted based on the specific research focus. If you want to emphasize the importance of kills over damage, increase \(\alpha\). If damage dealt is considered more reflective of aggressiveness, increase \(\beta\). For most balanced cases, both weights can be set to 1.

## Explanation

- **Kills per Win**: This term reflects how often a player is securing kills relative to the number of games won. A higher ratio indicates that the player tends to be aggressive and successful in combat even if they do not win every match.
- **Damage per Win**: This term reflects how much damage a player deals relative to their win count, capturing their active participation in fights, regardless of securing kills. High damage suggests that the player engages more frequently in combat.
- **+1 in the denominator**: This is used to avoid division by zero in cases where players have no wins, ensuring that all players receive a valid score.

## Application

The **PAS** score helps in:
1. **Identifying Aggressive Players**: Players with high scores are those who frequently engage in combat, either by securing kills or dealing significant damage, even if they don’t always secure wins.
2. **Comparing Legends**: This score can be applied across different Legends to evaluate how each Legend facilitates aggressive playstyles based on player performance.
3. **Tracking Playstyle Trends**: It enables researchers to analyze and categorize players based on their in-game behavior, distinguishing between aggressive and passive strategies.

## Example

For a player with the following stats:
- **BR Kills**: 1000
- **BR Wins**: 50
- **BR Damage**: 500,000

With \(\alpha = 1\) and \(\beta = 1\), the PAS score would be:

\[
\text{PAS} = 1 \times \left( \frac{1000}{50 + 1} \right) + 1 \times \left( \frac{500000}{50 + 1} \right) = 19.61 + 9803.92 = 9823.53
\]

This indicates that the player is quite aggressive in combat, frequently dealing significant damage and securing kills relative to their wins.

---