import pandas as pd


def mean_temperature(data):
    """
    Get the mean temperature

    Args:
        data (pandas.DataFrame): A pandas dataframe with air temperature measurements.

    Returns:
        The mean air temperature (float)
    """
    temperatures = data['Air temperature (degC)']
    return float(sum(temperatures) / len(temperatures))


def get_spreadsheet_columns(file_loc, print_columns=False):
    """Gets and prints the spreadsheet's header columns

    Args:
        file_loc (str): The file location of the spreadsheet
        print_columns (bool, optional) : A flag used to print the columns to the console (default is False)

    Returns:
        a list of strings used that are the header columns
    """

    file_data = pd.read_excel(file_loc)
    column_headers = list(file_data.columns.values)

    if print_columns:
        print("\n".join(column_headers))

    return column_headers

def main():
    """Analyse a spreadsheet file with temperatures.

    Prompt the user for the file name, print the columns in the spreadsheet, and print the mean
    temperature.
    """
    file_loc = input('Provide the name of the excel file you want to analyse:')
    get_spreadsheet_columns(file_loc, print_columns=True)

    data = pd.read_excel(file_loc)
    mean_temp = mean_temperature(data)
    print(f'Mean temperature is: {mean_temp}')


if __name__ == '__main__':
    main()
