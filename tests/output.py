import pandas as pd


def pretty_output(top_df: pd.DataFrame):
    output_lines =[]

    output_lines.append(
        f'The {top_df.shape[0]} most present users in the timeline are:\n'
    )

    for _, row in top_df.iterrows():
        output_lines.append(
            f"\t- {row['names']}\t({row['count']} tweets)"
        )

    print('\n'.join(output_lines))
