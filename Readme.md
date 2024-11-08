# Exploring the Relationship Between Legend Categories and Player Success in Apex Legends

## Author
- **Altaaf Ally**  
  School of Computer Science & Applied Mathematics  
  University of the Witwatersrand, Johannesburg, South Africa  

- **Supervisors**  
  Dr. Branden Ingram and Dr. Pravesh Ranchod  

---

## Project Description
This research explores the role-specific contributions of different Legend categories in *Apex Legends*, focusing on their impact on player performance and success. The study investigates two hypotheses:
1. Offensive Legends achieve higher kills per win and kills per match compared to defensive or support-oriented Legends.
2. A strong positive correlation exists between a player's kill count and their overall wins.

The study uses clustering and statistical analysis to examine performance trends across Legend categories and to quantify the relationships between key performance metrics. The findings provide actionable insights into player strategies, game balance, and Legend effectiveness.

---

## Key Features
- **Hypothesis 1**: Clustering techniques and statistical tests to analyze Legend category performance based on kills per match and kills per win.
- **Hypothesis 2**: Correlation and regression analyses to evaluate the relationship between Career Kills and Career Wins.

---

## Methodology
### Data Collection
- Legend-specific statistics collected for top 500 players per Legend.
- Career statistics obtained for top 900 players across platforms (PlayStation, PC, Xbox).

### Data Preprocessing
- Multiple Imputation by Chained Equations (MICE) for missing values.
- Outlier removal using Z-scores.
- Feature scaling and dimensionality reduction with PCA.

### Analysis Techniques
- **Clustering**: K-Means, Gaussian Mixture Models, and Hierarchical Clustering.
- **Statistical Analysis**: Kruskal-Wallis test, Dunn’s post-hoc test, and effect size measures like Cliff’s Delta.
- **Regression and Correlation**: Simple linear regression and correlation analyses using Pearson, Spearman, and Kendall metrics.

---

## Results
### Hypothesis 1
- Offensive Legends (Assault category) dominate in kills per match and kills per win, reinforcing their aggressive roles.
- Clustering revealed three distinct performance groups, aligning with Legend roles.

### Hypothesis 2
- Strong positive correlation between Career Kills and Career Wins (Pearson r = 0.7997), emphasizing offensive performance's critical role in player success.
- Regression analysis accounted for 63.9% of the variability in Career Wins based on Career Kills.

---

## Implications
- Insights for players on optimal Legend selection based on desired performance goals.
- Recommendations for game developers to refine matchmaking and balance Legend abilities.

---

## Limitations and Future Directions
- Data was sourced from third-party APIs, limiting access to comprehensive statistics.
- Future work could expand the dataset to include lower-ranking players and additional metrics like assists and win streaks.
- Exploring team composition dynamics and longitudinal performance trends to capture the evolving gameplay.

---

## Citation
If you use this work, please cite:  
**Altaaf Ally, "Exploring the Relationship Between Legend Categories and Player Success in Apex Legends," University of the Witwatersrand, 2024.**

---
