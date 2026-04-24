# %% [markdown]
# # Artificial Intelligence - Exercise 1
# ## Football Analysis Exercise
# ### Kaggle Dataset: International Football Results(1872-2024)

# %% [markdown]
# #### Step 1: Load the CSV

# %%
import pandas as pd #import the pandas library for data manipulation

# %%
df = pd.read_csv("results.csv")
df.head(10)

# %% [markdown]
# ### Basic Dataset Exploration

# %% [markdown]
# ####  Q1: How many matches are in the dataset?

# %%
df.shape

# %% [markdown]
# #### A1: 49071 rows, 9 columns.Thus there 49,071 matches in the dataset

# %% [markdown]
# #### Q2: What is the earliest and latest year in the dataset?

# %%
print(df["date"].min())
print(df["date"].max())

# %% [markdown]
# #### A2: The earliest date is 1872-11-30 and the latest date is 2026-01-26

# %% [markdown]
# ##### Q3: How many unique countries are there?

# %%
df["home_team"].nunique()

# %% [markdown]
# #### A3: There are 325 unique countries in the dataset

# %% [markdown]
# #### Q4: Which team appears most frequently as home team?

# %%
df["home_team"].value_counts().head()

# %% [markdown]
# #### A4: Brazil is the most frequently appearing home team(610 times).

# %% [markdown]
# ### Goals Analysis

# %%
df["total_goals"] = df["home_score"] + df["away_score"]

# %% [markdown]
# #### Q5: What is the average number of goals per match?

# %%
avg_goals_per_match = df["total_goals"].sum() / df.shape[0]
print(f"Average goals per match is : {round(avg_goals_per_match)}")

# %% [markdown]
# #### Q6: What is the highest scoring match?

# %%
max_goals = df["total_goals"].max()
max_index = df['total_goals'].idxmax()
highest_scoring_match_home_team = df.loc[max_index, "home_team"]
highest_scoring_match_away_team = df.loc[max_index, "away_team"]
highest_scoring_match_date = df.loc[max_index,"date"]
print(f"The highest scoring match was between {highest_scoring_match_home_team} and {highest_scoring_match_away_team} whose total goals were {max_goals} and was held on {highest_scoring_match_date}.")


# %% [markdown]
# #### Q7: Are more goals scored home or away?

# %%
home_total_goals = df["home_score"].sum()
away_total_goals = df["away_score"].sum()
print(home_total_goals)
print(away_total_goals)
if home_total_goals > away_total_goals :
    print("More goals are scored at home.")
else:
    print("More goals are scored away.")

# %% [markdown]
# ##### Q8: What is the most common total goals value?

# %%
print(f"The most common total goals value is {df["total_goals"].value_counts().idxmax()} with a total of {df["total_goals"].value_counts().iloc[0]} games.")

# %% [markdown]
# ### Match Results

# %%
def match_result(row):
    if row["home_score"] > row["away_score"]:
        return "Home Win"
    elif row["home_score"] < row["away_score"]:
        return "Away Win"
    else:
        return "Draw"

df["result"] = df.apply(match_result, axis=1)


# %% [markdown]
# ##### Q9: What percentage of matches are home wins?

# %%
results_groups = df["result"].value_counts()
print(results_groups)
home_wins = results_groups.iloc[0]
print(home_wins)
Total_match_results = df["result"].count()
print(Total_match_results)
home_wins_percentage = (home_wins/Total_match_results) * 100
print(home_wins_percentage)
print(f"Percentage of matches with home wins is {round(home_wins_percentage,2)}%")

# %% [markdown]
# #### Q10: Does home advantage exist?

# %%
home_wins = results_groups.iloc[0]
print(f"Number of home wins:{home_wins}.")
home_wins_percentage = round((home_wins/Total_match_results) * 100, 2)
print(f"Away wins percentage: {home_wins_percentage}%.")
away_wins = results_groups.iloc[1]
print(f"Number of away wins:{away_wins}.")
away_wins_percentage = round((away_wins/Total_match_results) * 100, 2)
print(f"Away wins percentage: {away_wins_percentage}%.")
draws = results_groups.iloc[2]
print(f"Number of draws :{draws}.")
draws_percentage = round((draws/Total_match_results) * 100, 2)
print(f"Away wins percentage: {draws_percentage}%.")
print("\n")
print(f"Home wins with {home_wins_percentage}%, which is almost half of the total results, indicate that home advantage exists.")

# %% [markdown]
# #### Q11. Which Country has the most wins historically?

# %%
df.head(3)

# %%
def won_team(row):
    if row["home_score"] > row["away_score"]:
        return row["home_team"]
    elif row["home_score"] < row["away_score"]:
        return row["away_team"]
    else:
        return "Draw"

df["Won Team"] = df.apply(won_team,axis = 1)
df.head(3)
Winners = df["Won Team"].value_counts().head(10)
print(Winners)
print("\n")
print(f"{Winners.index[1]} is the country with the most wins historically with a total of {Winners.iloc[1]} wins.")

# %%
def lost_team(row):
    if row["home_score"] < row["away_score"]:
        return row["home_team"]
    elif row["home_score"] > row["away_score"]:
        return row["away_team"]
    else:
        return "Draw"

df["Lost Team"] = df.apply(lost_team,axis = 1)
df.head(3)
Loosers = df["Lost Team"].value_counts().head()
print(Loosers)
print("\n")
print(f"{Loosers.index[1]} is the country with the most losses historically with a total of {Loosers.iloc[1]} losses.")

# %% [markdown]
# ### Visualization

# %%
import matplotlib.pyplot as plt

# %% [markdown]
# #### Histogram of goals

# %%
df["total_goals"].hist(bins = 15,color = "green",edgecolor = "black", alpha = 0.7)
plt.title("Distribution of Goals Per Match")
plt.xlabel("No.of goals")
plt.ylabel("No.of matches")
plt.show()

# %% [markdown]
# #### Bar Chart of Match Outcomes

# %%
match_outcomes = df["result"].value_counts() 
match_outcomes.plot(kind = "bar", color = "green", edgecolor = "black", alpha=0.7)
plt.title("Distribution of Match Outcomes")
plt.ylabel("No. of matches")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# %% [markdown]
# #### Top 10 teams by total wins

# %%
No_draw_only_winners = Winners.iloc[1:]
No_draw_only_winners.plot(kind = "barh",color = "green", edgecolor = "black", alpha = 0.7)
plt.gca().invert_yaxis() 
plt.title("Top 10 Teams by Total Wins")
plt.xlabel("Wins")
plt.show()

# %%



