# Importing necessary libraries
import pandas as pd
from apyori import apriori

# Replicating the code structure from the uploaded file to generate the output
transactions = [
    ['beer', 'nuts'],
    ['beer', 'cheese'],
]

# Run Apriori algorithm
results = list(apriori(transactions))

# Parse the RelationRecord object and put the results into a pandas DataFrame
def parse_results_to_dataframe(results):
    # Prepare the DataFrame columns
    columns = ["antecedent -> consequent", "support", "confidence", "lift"]
    # Initialize a list to hold our parsed data
    parsed_data = []

    # Loop over each RelationRecord object in the results
    for result in results:
        # Loop over each OrderedStatistic object in the ordered_statistics
        for ordered_statistic in result.ordered_statistics:
            # Prepare the record for this OrderedStatistic
            record = {
                "antecedent -> consequent": f"{set(ordered_statistic.items_base)} -> {set(ordered_statistic.items_add)}",
                "support": result.support,
                "confidence": ordered_statistic.confidence,
                "lift": ordered_statistic.lift
            }
            parsed_data.append(record)

    # Convert the list of records into a DataFrame
    return pd.DataFrame(parsed_data, columns=columns)

# Creating DataFrame from the results
df_results = parse_results_to_dataframe(results)
print(df_results)
