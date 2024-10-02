
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

---